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

        js.URL = URL
        sys.modules["js"] = js
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

    def test_bridge_has_pre_asgi_body_cap_hook(self):
        bridge_source = (ROOT / "src" / "worker_asgi_bridge.py").read_text()
        main_source = (ROOT / "src" / "main.py").read_text()

        self.assertIn("max_body_bytes", bridge_source)
        self.assertIn("body_bytes > max_body_bytes", bridge_source)
        self.assertIn("max_body_bytes=MAX_SUBMITTED_BODY_BYTES", main_source)


if __name__ == "__main__":
    unittest.main()
