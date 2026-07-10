import asyncio
import importlib
import sys
import types
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class MainModuleHarness(unittest.TestCase):
    """Imports src/main.py with stubbed FastAPI/Workers modules.

    Subclass this to test main.py handlers directly; the stub Response
    classes record content, status, and headers for assertions.
    """

    def setUp(self):
        self.saved_modules = {
            name: sys.modules.get(name)
            for name in (
                "fastapi",
                "fastapi.exception_handlers",
                "fastapi.exceptions",
                "fastapi.responses",
                "main",
                "observability",
                "starlette.exceptions",
                "worker_asgi_bridge",
                "workers",
            )
        }
        fastapi = types.ModuleType("fastapi")

        class FastAPI:
            def __init__(self, *args, **kwargs):
                pass

            def add_middleware(self, *args, **kwargs):
                pass

            def exception_handler(self, *args, **kwargs):
                def decorator(func):
                    return func

                return decorator

            def get(self, *args, **kwargs):
                def decorator(func):
                    return func

                return decorator

            def post(self, *args, **kwargs):
                def decorator(func):
                    return func

                return decorator

        class Request:
            pass

        fastapi.FastAPI = FastAPI
        fastapi.Request = Request
        sys.modules["fastapi"] = fastapi

        exception_handlers = types.ModuleType("fastapi.exception_handlers")

        async def http_exception_handler(request, exc):
            return None

        async def request_validation_exception_handler(request, exc):
            return None

        exception_handlers.http_exception_handler = http_exception_handler
        exception_handlers.request_validation_exception_handler = request_validation_exception_handler
        sys.modules["fastapi.exception_handlers"] = exception_handlers

        fastapi_exceptions = types.ModuleType("fastapi.exceptions")

        class RequestValidationError(Exception):
            pass

        fastapi_exceptions.RequestValidationError = RequestValidationError
        sys.modules["fastapi.exceptions"] = fastapi_exceptions

        fastapi_responses = types.ModuleType("fastapi.responses")

        class Response:
            def __init__(self, content=None, status_code=200, headers=None, media_type=None, **kwargs):
                self.content = content
                self.status_code = status_code
                self.headers = headers or {}
                self.media_type = media_type

        class HTMLResponse(Response):
            pass

        fastapi_responses.HTMLResponse = HTMLResponse
        fastapi_responses.Response = Response
        sys.modules["fastapi.responses"] = fastapi_responses

        starlette_exceptions = types.ModuleType("starlette.exceptions")

        class HTTPException(Exception):
            pass

        starlette_exceptions.HTTPException = HTTPException
        sys.modules["starlette.exceptions"] = starlette_exceptions

        workers = types.ModuleType("workers")

        class WorkerEntrypoint:
            pass

        class Request:
            pass

        workers.WorkerEntrypoint = WorkerEntrypoint
        workers.Request = Request
        workers.Context = object
        workers.wait_until = lambda task: None
        workers.python_from_rpc = lambda response: response
        sys.modules["workers"] = workers
        sys.path.insert(0, str(SRC))

    def tearDown(self):
        if str(SRC) in sys.path:
            sys.path.remove(str(SRC))
        for name, module in self.saved_modules.items():
            sys.modules.pop(name, None)
            if module is not None:
                sys.modules[name] = module

    def import_main(self):
        sys.modules.pop("main", None)
        return importlib.import_module("main")


class _Headers(dict):
    def set(self, name, value):
        self[name] = value


class MainDefaultFetchTests(MainModuleHarness):
    def test_post_and_bridge_rejections_get_security_no_store_and_status_observability(self):
        main = self.import_main()
        emitted = []
        event = {"cache": "bypass"}
        response = SimpleNamespace(status=413, headers=_Headers())

        async def asgi_fetch(*args, **kwargs):
            return response

        main.caches = None
        main.asgi.fetch = asgi_fetch
        main.observability.event_from_worker_request = lambda *args, **kwargs: event
        main.observability.emit = lambda value, env=None: emitted.append(value.copy())
        worker = main.Default()
        worker.env = SimpleNamespace()
        request = SimpleNamespace(
            method="POST",
            url="https://www.pythonbyexample.dev/examples/values",
            js_object=SimpleNamespace(),
        )

        returned = asyncio.run(worker.fetch(request))

        self.assertIs(returned, response)
        self.assertEqual(response.headers["Cache-Control"], "no-store")
        for name, value in main.SECURITY_HEADERS.items():
            self.assertEqual(response.headers[name], value)
        self.assertEqual(emitted[-1]["status_code"], 413)
        self.assertEqual(emitted[-1]["outcome"], "client_error")

    def test_dynamic_response_reader_cancels_stream_above_output_cap(self):
        main = self.import_main()
        cancelled = []

        class Chunk:
            def __init__(self, value):
                self.value = value

            def to_bytes(self):
                return self.value

        class Reader:
            def __init__(self):
                self.results = [
                    SimpleNamespace(done=False, value=Chunk(b"x" * 40_000)),
                    SimpleNamespace(done=False, value=Chunk(b"y" * 40_000)),
                ]

            async def read(self):
                return self.results.pop(0)

            async def cancel(self, reason):
                cancelled.append(reason)

        reader = Reader()
        response = SimpleNamespace(body=SimpleNamespace(getReader=lambda: reader))
        text, exceeded = asyncio.run(main._read_dynamic_response_text(response))

        self.assertTrue(exceeded)
        self.assertEqual(text, main.DYNAMIC_OUTPUT_LIMIT_MESSAGE)
        self.assertEqual(len(cancelled), 1)


class MainObservabilityTests(MainModuleHarness):
    def test_run_example_marks_dynamic_worker_http_500_as_worker_error(self):
        main = self.import_main()
        destroyed = []
        captured_request = {}

        class CodeCallback:
            def destroy(self):
                destroyed.append(True)

        class FakeJsRequest:
            @staticmethod
            def new(url, options):
                request = SimpleNamespace(url=url, options=options)
                captured_request["request"] = request
                return request

        class FakeResponse:
            status = 500

            async def text(self):
                return "Traceback from the Dynamic Worker"

        class FakeEntrypoint:
            async def fetch(self, request):
                return FakeResponse()

        class FakeWorker:
            def getEntrypoint(self):
                return FakeEntrypoint()

        main.JsRequest = FakeJsRequest
        main.create_once_callable = lambda callback: CodeCallback()
        main.python_from_rpc = lambda response: response
        env = SimpleNamespace(LOADER=SimpleNamespace(get=lambda worker_id, callback: FakeWorker()))
        event = {"request_id": "req-123"}
        request = SimpleNamespace(
            state=SimpleNamespace(wide_event=event),
            scope={"env": env},
            url="https://www.pythonbyexample.dev/examples/hello-world",
        )

        output = asyncio.run(main._run_example(request, "hello-world", "raise RuntimeError('boom')"))

        self.assertEqual(output, "Traceback from the Dynamic Worker")
        main.observability.record_status(event, 200)

        self.assertEqual(event["level"], "error")
        self.assertEqual(event["outcome"], "error")
        self.assertEqual(event["worker"]["outcome"], "error")
        self.assertEqual(event["worker"]["status_code"], 500)
        self.assertEqual(event["worker"]["error"]["type"], "DynamicWorkerHTTPError")
        self.assertIn("HTTP 500", event["worker"]["error"]["message"])
        self.assertEqual(
            captured_request["request"].options["headers"],
            {"x-request-id": "req-123"},
        )
        self.assertEqual(destroyed, [True])

    def test_run_example_marks_dynamic_worker_output_limit_as_rejected(self):
        main = self.import_main()

        class FakeJsRequest:
            @staticmethod
            def new(url, options):
                return SimpleNamespace(url=url, options=options)

        class Response:
            status = 413
            async def text(self):
                return "Program output exceeded the 64 kB limit. Reduce output and try again."

        class Worker:
            def getEntrypoint(self):
                return SimpleNamespace(fetch=lambda request: _response(Response()))

        main.JsRequest = FakeJsRequest
        main.create_once_callable = lambda callback: SimpleNamespace(destroy=lambda: None)
        main.python_from_rpc = lambda response: response
        event = {"request_id": "req-413"}
        request = SimpleNamespace(
            state=SimpleNamespace(wide_event=event),
            scope={"env": SimpleNamespace(LOADER=SimpleNamespace(get=lambda *_: Worker()))},
            url="https://www.pythonbyexample.dev/examples/values",
        )
        output = asyncio.run(main._run_example(request, "values", "print('x')"))
        self.assertIn("output exceeded", output)
        self.assertEqual(event["worker"]["status_code"], 413)
        self.assertEqual(event["worker"]["outcome"], "rejected")
        self.assertEqual(event["worker"]["rejected"], "output_too_large")


async def _response(value):
    return value


if __name__ == "__main__":
    unittest.main()
