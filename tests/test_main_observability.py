import asyncio
import importlib
import sys
import types
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class MainObservabilityTests(unittest.TestCase):
    def setUp(self):
        self.saved_modules = {
            name: sys.modules.get(name)
            for name in ("workers", "main", "worker_asgi_bridge", "observability")
        }
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


if __name__ == "__main__":
    unittest.main()
