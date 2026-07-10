import asyncio
import importlib
import pathlib
import sys
import types
import unittest
from types import SimpleNamespace
from urllib.parse import urlparse


ROOT = pathlib.Path(__file__).resolve().parents[1]


class WorkerAsgiBridgeScopeTests(unittest.TestCase):
    def setUp(self):
        self.saved_workers = sys.modules.get("workers")
        self.saved_js = sys.modules.get("js")
        self.saved_bridge = sys.modules.pop("src.worker_asgi_bridge", None)

        workers = types.ModuleType("workers")

        class Request:
            pass

        workers.Request = Request
        workers.Context = object
        workers.wait_until = lambda task: None
        sys.modules["workers"] = workers
        self.Request = Request

        js = types.ModuleType("js")

        class URL:
            @classmethod
            def new(cls, value):
                parsed = urlparse(value)
                return SimpleNamespace(
                    protocol=f"{parsed.scheme}:",
                    pathname=parsed.path or "/",
                    search=f"?{parsed.query}" if parsed.query else "",
                )

        # Minimal JS-runtime fakes used by HTTP and WebSocket bridge paths.
        class Response:
            def __init__(self, body, headers, status, web_socket=None):
                self.body = body
                self.headers = headers
                self.status = status
                self.webSocket = web_socket

            @classmethod
            def new(cls, body, *, headers=None, status=200, webSocket=None):
                return cls(body, headers, status, webSocket)

        class Object:
            @staticmethod
            def fromEntries(pairs):
                return dict(pairs)

        class WebSocketServer:
            def __init__(self):
                self.accepted = False
                self.onopen = None
                self.onclose = None
                self.onmessage = None
                self.sent = []
                self.closed = None

            def accept(self):
                self.accepted = True

            def send(self, value):
                self.sent.append(value)

            def close(self, code=1000, reason=""):
                self.closed = (code, reason)

        class WebSocketPair:
            @classmethod
            def new(cls):
                client = SimpleNamespace(name="client")
                server = WebSocketServer()
                self.ws_server = server
                return SimpleNamespace(object_values=lambda: (client, server))

        js.URL = URL
        js.Response = Response
        js.Object = Object
        js.TransformStream = object  # only referenced on the streaming path
        js.WebSocketPair = WebSocketPair
        sys.modules["js"] = js

        ffi = types.ModuleType("pyodide.ffi")
        self.released_buffers = 0
        test_case = self

        class _JSBytes:
            def __init__(self, value):
                self.value = value

            def slice(self):
                return self.value

        class _Buffer:
            def __init__(self, value):
                self.data = _JSBytes(value)

            def release(self):
                test_case.released_buffers += 1

        class _Proxy:
            def __init__(self, obj):
                self._obj = obj

            def getBuffer(self):
                return _Buffer(self._obj)

            def destroy(self):
                pass

        ffi.create_proxy = _Proxy
        self.saved_pyodide = sys.modules.get("pyodide")
        self.saved_pyodide_ffi = sys.modules.get("pyodide.ffi")
        pyodide = sys.modules.get("pyodide") or types.ModuleType("pyodide")
        pyodide.ffi = ffi
        sys.modules["pyodide"] = pyodide
        sys.modules["pyodide.ffi"] = ffi

        self.bridge = importlib.import_module("src.worker_asgi_bridge")

    def tearDown(self):
        sys.modules.pop("src.worker_asgi_bridge", None)
        if self.saved_bridge is not None:
            sys.modules["src.worker_asgi_bridge"] = self.saved_bridge
        if self.saved_workers is None:
            sys.modules.pop("workers", None)
        else:
            sys.modules["workers"] = self.saved_workers
        if self.saved_js is None:
            sys.modules.pop("js", None)
        else:
            sys.modules["js"] = self.saved_js
        for name, saved in (("pyodide", self.saved_pyodide), ("pyodide.ffi", self.saved_pyodide_ffi)):
            if saved is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = saved

    def _fake_request(self, *, method="POST", url, headers, body_chunks):
        async def body_iter():
            for chunk in body_chunks:
                yield SimpleNamespace(to_bytes=lambda c=chunk: c)

        class FakeRequest(self.Request):
            pass

        req = FakeRequest()
        req.method = method
        req.url = url
        req.headers = headers
        req.body = body_iter() if body_chunks else None
        return req

    def test_process_request_non_streaming_echoes_body_and_status(self):
        async def app(scope, receive, send):
            body = b""
            while True:
                message = await receive()
                body += message.get("body", b"")
                if not message.get("more_body"):
                    break
            await send(
                {
                    "type": "http.response.start",
                    "status": 201,
                    "headers": [(b"content-type", b"text/plain"), (b"x-trace", b"abc")],
                }
            )
            await send({"type": "http.response.body", "body": b"echo:" + body, "more_body": False})

        req = self._fake_request(
            url="https://x.dev/examples/values",
            headers={"content-type": "text/plain"},
            body_chunks=[b"pi", b"ng"],
        )
        response = asyncio.run(
            self.bridge.process_request(app, req, SimpleNamespace(), None, state={})
        )
        self.assertEqual(response.status, 201)
        self.assertEqual(response.body, b"echo:ping")
        self.assertEqual(response.headers.get("content-type"), "text/plain")
        self.assertEqual(response.headers.get("x-trace"), "abc")
        self.assertEqual(self.released_buffers, 1)

    def test_latin1_headers_round_trip_through_scope_and_response(self):
        async def app(scope, receive, send):
            self.assertIn((b"x-label", b"caf\xe9"), scope["headers"])
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [(b"x-label", b"caf\xe9")],
                }
            )
            await send({"type": "http.response.body", "body": b"ok", "more_body": False})

        req = self._fake_request(
            url="https://x.dev/examples/values",
            headers={"X-Label": "café"},
            body_chunks=[],
        )
        response = asyncio.run(
            self.bridge.process_request(app, req, SimpleNamespace(), None, state={})
        )
        self.assertEqual(response.headers["x-label"], "café")

    def test_process_request_propagates_app_exception(self):
        async def app(scope, receive, send):
            raise RuntimeError("boom in app")

        req = self._fake_request(
            url="https://x.dev/examples/values",
            headers={"content-type": "text/plain"},
            body_chunks=[],
        )
        with self.assertRaises(RuntimeError):
            asyncio.run(self.bridge.process_request(app, req, SimpleNamespace(), None, state={}))

    def test_process_request_rejects_oversize_body_before_running_app(self):
        ran = {"app": False}

        async def app(scope, receive, send):  # pragma: no cover - must not run
            ran["app"] = True

        req = self._fake_request(
            url="https://x.dev/examples/values",
            headers={"content-type": "text/plain"},
            body_chunks=[b"toolong"],
        )
        response = asyncio.run(
            self.bridge.process_request(app, req, SimpleNamespace(), None, state={}, max_body_bytes=3)
        )
        self.assertEqual(response.status, 413)
        self.assertFalse(ran["app"], "oversize body must be rejected before the app runs")

    def test_request_to_scope_accepts_state_without_request_globals_or_extra_scope(self):
        class FakeRequest(self.Request):
            method = "POST"
            url = "https://www.pythonbyexample.dev/examples/hello-world?run=1"
            headers = {"Content-Type": "text/plain", "X-Request-ID": "trace-1"}

        request = FakeRequest()
        env = SimpleNamespace(NAME="env")
        wide_event = {"request_id": "trace-1"}
        state = {"wide_event": wide_event, "cache": "bypass"}

        scope = self.bridge.request_to_scope(request, env, state=state)

        self.assertEqual(scope["type"], "http")
        self.assertEqual(scope["method"], "POST")
        self.assertEqual(scope["scheme"], "https")
        self.assertEqual(scope["path"], "/examples/hello-world")
        self.assertEqual(scope["query_string"], b"run=1")
        self.assertEqual(scope["headers"], [(b"content-type", b"text/plain"), (b"x-request-id", b"trace-1")])
        self.assertIs(scope["env"], env)
        self.assertNotIn("worker_request", scope)
        self.assertNotIn("cache_mode", scope)
        self.assertIsNot(scope["state"], state)
        self.assertIs(scope["state"]["wide_event"], wide_event)
        self.assertEqual(scope["state"]["cache"], "bypass")

    def test_websocket_close_callback_delivers_disconnect_event(self):
        received = []

        async def app(scope, receive, send):
            self.assertEqual(scope["type"], "websocket")
            received.append(await receive())
            received.append(await receive())

        req = self._fake_request(
            method="GET",
            url="https://x.dev/socket",
            headers={},
            body_chunks=[],
        )

        async def scenario():
            response = await self.bridge.process_websocket(app, req)
            await asyncio.sleep(0)
            self.ws_server.onclose(SimpleNamespace(code=1001, reason="leaving"))
            for _ in range(20):
                if len(received) == 2:
                    break
                await asyncio.sleep(0)
            return response

        response = asyncio.run(scenario())
        self.assertEqual(response.status, 101)
        self.assertEqual(received[0], {"type": "websocket.connect"})
        self.assertEqual(
            received[1],
            {"type": "websocket.disconnect", "code": 1001, "reason": "leaving"},
        )

    def test_websocket_application_close_closes_server_socket(self):
        async def app(scope, receive, send):
            await receive()
            await send({"type": "websocket.close", "code": 1008, "reason": "policy"})

        req = self._fake_request(
            method="GET",
            url="https://x.dev/socket",
            headers={},
            body_chunks=[],
        )
        response = asyncio.run(self.bridge.process_websocket(app, req))
        self.assertEqual(response.status, 101)
        self.assertEqual(self.ws_server.closed, (1008, "policy"))

    def test_fetch_starts_lifespan_once_per_application(self):
        calls = {"startup": 0, "request": 0}
        app = object()
        self.bridge._app_lifespans.clear()

        async def start_application(_app):
            self.assertIs(_app, app)
            calls["startup"] += 1

        async def process_request(_app, req, env, ctx, **kwargs):
            self.assertIs(_app, app)
            calls["request"] += 1
            return SimpleNamespace(status=200)

        self.bridge.start_application = start_application
        self.bridge.process_request = process_request
        req = self._fake_request(
            method="GET",
            url="https://x.dev/",
            headers={},
            body_chunks=[],
        )

        async def scenario():
            await self.bridge.fetch(app, req, SimpleNamespace())
            await self.bridge.fetch(app, req, SimpleNamespace())

        asyncio.run(scenario())
        self.assertEqual(calls, {"startup": 1, "request": 2})

    def test_bridge_has_pre_asgi_body_cap_hook(self):
        bridge_source = (ROOT / "src" / "worker_asgi_bridge.py").read_text()
        main_source = (ROOT / "src" / "main.py").read_text()

        self.assertIn("max_body_bytes", bridge_source)
        self.assertIn("body_bytes > max_body_bytes", bridge_source)
        self.assertIn("max_body_bytes=MAX_SUBMITTED_BODY_BYTES", main_source)


if __name__ == "__main__":
    unittest.main()
