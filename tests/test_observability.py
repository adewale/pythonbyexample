import asyncio
import contextlib
import io
import json
import unittest
from pathlib import Path
from types import SimpleNamespace

import src.observability as observability

ROOT = Path(__file__).resolve().parents[1]


class FakeConsole:
    def __init__(self):
        self.log_calls = []
        self.error_calls = []

    def log(self, payload):
        self.log_calls.append(payload)

    def error(self, payload):
        self.error_calls.append(payload)


class FakeObject:
    @staticmethod
    def fromEntries(entries):
        return dict(entries)


class ObservabilityEmitterTests(unittest.TestCase):
    def setUp(self):
        self.original_console = observability.console
        self.original_object = observability.Object
        self.original_to_js = observability.to_js

    def tearDown(self):
        observability.console = self.original_console
        observability.Object = self.original_object
        observability.to_js = self.original_to_js

    def install_structured_console(self):
        console = FakeConsole()
        conversions = []

        def fake_to_js(payload, *, dict_converter):
            conversions.append((payload, dict_converter))
            return payload

        observability.console = console
        observability.Object = FakeObject
        observability.to_js = fake_to_js
        return console, conversions

    def test_emit_uses_structured_console_object_with_deploy_context(self):
        console, conversions = self.install_structured_console()
        env = SimpleNamespace(
            CF_VERSION_METADATA=SimpleNamespace(
                id="version-1",
                tag="release-2026-05-13",
                timestamp="2026-05-13T12:34:56Z",
            ),
        )

        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            observability.emit(
                {"request_id": "req-1", "status_code": 200, "outcome": "success"},
                env=env,
            )

        self.assertEqual(len(console.log_calls), 1)
        self.assertEqual(console.error_calls, [])
        self.assertEqual(len(conversions), 1)
        payload = console.log_calls[0]
        self.assertIsInstance(payload, dict)
        self.assertNotIsInstance(payload, str)
        self.assertEqual(payload["service"], "pythonbyexample")
        self.assertNotIn("commit_hash", payload)
        self.assertEqual(payload["worker_version"], {"id": "version-1"})
        self.assertEqual(payload["request_id"], "req-1")
        self.assertEqual(payload["level"], "info")
        self.assertIsInstance(payload["timestamp"], float)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_error_events_use_console_log_and_truncate_exception_messages(self):
        console, _ = self.install_structured_console()
        exc = RuntimeError("x" * 700)
        error = observability.error_dict(exc)

        observability.emit({"outcome": "error", "error": error}, env=None)

        self.assertEqual(console.error_calls, [])
        self.assertEqual(len(console.log_calls), 1)
        payload = console.log_calls[0]
        self.assertEqual(payload["level"], "error")
        self.assertEqual(payload["error"]["type"], "RuntimeError")
        self.assertLessEqual(len(payload["error"]["message"]), 513)
        self.assertTrue(payload["error"]["message"].endswith("…"))
        self.assertNotIn("commit_hash", payload)
        self.assertEqual(payload["worker_version"], {"id": ""})

    def test_error_dict_redacts_obvious_user_supplied_values(self):
        exc = RuntimeError(
            "failed https://example.test/run?token=turnstile-token-marker&ok=1 "
            "code=raw-code-marker&cf-turnstile-response=challenge-marker"
        )

        error = observability.error_dict(exc)

        self.assertEqual(error["type"], "RuntimeError")
        self.assertIn("https://example.test/run?<redacted>", error["message"])
        self.assertIn("code=<redacted>", error["message"])
        self.assertIn("cf-turnstile-response=<redacted>", error["message"])
        self.assertNotIn("turnstile-token-marker", error["message"])
        self.assertNotIn("raw-code-marker", error["message"])
        self.assertNotIn("challenge-marker", error["message"])

    def test_emit_falls_back_to_json_lines_when_console_is_unavailable(self):
        observability.console = None
        observability.Object = None
        observability.to_js = None

        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            observability.emit({"request_id": "ok", "outcome": "success"})
            observability.emit({"request_id": "bad", "outcome": "error"})

        info_payload = json.loads(stdout.getvalue())
        error_payload = json.loads(stderr.getvalue())
        self.assertEqual(info_payload["request_id"], "ok")
        self.assertEqual(info_payload["level"], "info")
        self.assertEqual(error_payload["request_id"], "bad")
        self.assertEqual(error_payload["level"], "error")
        self.assertIn("python_version", info_payload)
        self.assertEqual(error_payload["worker_version"], {"id": ""})

    def test_safe_exception_helpers_strip_large_or_user_derived_details(self):
        class FakeValidationError:
            def errors(self):
                return [
                    {
                        "type": "value_error",
                        "loc": ("body", "code"),
                        "msg": "bad code=raw-code-marker",
                        "input": "raw-code-marker",
                        "ctx": {"error": "raw-code-marker"},
                    },
                    *({"type": "extra", "loc": ("body", str(i)), "input": i} for i in range(25)),
                ]

        details = observability.safe_validation_errors(FakeValidationError())

        self.assertEqual(len(details), 21)
        self.assertEqual(
            details[0],
            {"type": "value_error", "loc": ["body", "code"], "msg": "bad code=<redacted>"},
        )
        self.assertEqual(details[-1], {"type": "truncated", "omitted": 6})
        self.assertNotIn("input", details[0])
        self.assertNotIn("ctx", details[0])
        self.assertNotIn("raw-code-marker", json.dumps(details))
        self.assertEqual(observability.safe_http_detail("Not Found"), "Not Found")
        self.assertEqual(
            observability.safe_http_detail("token=secret-token and code=raw-code"),
            {"type": "str", "length": len("token=secret-token and code=raw-code")},
        )
        self.assertEqual(observability.safe_http_detail({"token": "secret"}), {"type": "dict"})

    def test_emit_does_not_raise_when_deploy_metadata_is_broken(self):
        class BrokenEnv:
            @property
            def CF_VERSION_METADATA(self):
                raise RuntimeError("metadata unavailable")

        console, _ = self.install_structured_console()

        observability.emit({"request_id": "ok", "outcome": "success"}, env=BrokenEnv())

        self.assertEqual(console.log_calls[0]["worker_version"], {"id": ""})

    def test_emit_does_not_raise_when_fallback_stream_write_fails(self):
        class BrokenStream:
            def write(self, text):
                raise OSError("closed")

            def flush(self):
                pass

        observability.console = None
        observability.Object = None
        observability.to_js = None

        with contextlib.redirect_stdout(BrokenStream()):
            observability.emit({"request_id": "ok", "outcome": "success"})


class RequestEventBuilderTests(unittest.TestCase):
    def test_worker_request_event_uses_sanitized_request_id_and_cloudflare_context(self):
        request = SimpleNamespace(
            method="POST",
            url="https://www.pythonbyexample.dev/examples/hello-world?token=secret",
            headers={
                "x-request-id": "trace-123",
                "cf-ray": "abc123",
                "cf-ipcountry": "GB",
                "cf-connecting-ip": "203.0.113.10",
            },
            cf={"colo": "SJC", "country": "US"},
        )

        event = observability.event_from_worker_request(
            request,
            cache="bypass",
            html_cache_version=7,
        )

        self.assertEqual(event["request_id"], "trace-123")
        self.assertEqual(event["method"], "POST")
        self.assertEqual(event["path"], "/examples/hello-world")
        self.assertEqual(event["cf"], {"ray": "abc123", "colo": "SJC", "country": "US"})
        self.assertEqual(event["cache"], "bypass")
        self.assertEqual(event["html_cache_version"], 7)
        self.assertNotIn("token=secret", json.dumps(event))
        self.assertNotIn("203.0.113.10", json.dumps(event))
        self.assertNotIn("url", event)

    def test_worker_request_event_rejects_untrusted_request_ids(self):
        request = SimpleNamespace(
            method="GET",
            url="https://www.pythonbyexample.dev/",
            headers={"x-request-id": "bad\nheader", "cf-ray": "ray789-LHR"},
        )

        event = observability.event_from_worker_request(
            request,
            cache="miss",
            html_cache_version=3,
        )

        self.assertEqual(event["request_id"], "ray789-LHR")
        self.assertEqual(event["cf"]["ray"], "ray789-LHR")
        self.assertEqual(event["cf"]["colo"], "LHR")
        self.assertIsNone(event["cf"]["country"])
        self.assertEqual(event["path"], "/")
        self.assertEqual(event["cache"], "miss")

    def test_worker_request_event_falls_back_to_ray_suffix_for_colo(self):
        request = SimpleNamespace(
            method="GET",
            url="https://www.pythonbyexample.dev/",
            headers={"cf-ray": "ray789-LHR", "cf-ipcountry": "GB"},
        )

        event = observability.event_from_worker_request(
            request,
            cache="miss",
            html_cache_version=3,
        )

        self.assertEqual(event["cf"], {"ray": "ray789-LHR", "colo": "LHR", "country": "GB"})

    def test_worker_request_event_caps_allowed_cloudflare_headers(self):
        huge_ray = f"ray-{'x' * 300}"
        request = SimpleNamespace(
            method="GET",
            url="https://www.pythonbyexample.dev/",
            headers={
                "x-request-id": "trace-123",
                "cf-ray": huge_ray,
                "cf-ipcountry": "GB\nspoofed",
            },
        )

        event = observability.event_from_worker_request(
            request,
            cache="miss",
            html_cache_version=3,
        )

        self.assertEqual(event["request_id"], "trace-123")
        self.assertEqual(event["cf"], {"ray": None, "colo": None, "country": None})
        self.assertNotIn(huge_ray, json.dumps(event))
        self.assertNotIn("spoofed", json.dumps(event))

    def test_record_status_maps_http_status_to_outcome_and_level(self):
        success = {}
        client_error = {}
        server_error = {}
        worker_error_with_http_200 = {"level": "error", "worker": {"outcome": "error"}}

        observability.record_status(success, 399)
        observability.record_status(client_error, 404)
        observability.record_status(server_error, 503)
        observability.record_status(worker_error_with_http_200, 200)

        self.assertEqual(success, {"status_code": 399, "outcome": "success", "level": "info"})
        self.assertEqual(
            client_error,
            {"status_code": 404, "outcome": "client_error", "level": "info"},
        )
        self.assertEqual(
            server_error,
            {"status_code": 503, "outcome": "error", "level": "error"},
        )
        self.assertEqual(
            worker_error_with_http_200,
            {
                "status_code": 200,
                "outcome": "error",
                "level": "error",
                "worker": {"outcome": "error"},
            },
        )


class WranglerObservabilityConfigTests(unittest.TestCase):
    def test_invocation_logs_are_disabled_for_single_custom_event_per_request(self):
        config = json.loads((ROOT / "wrangler.jsonc").read_text())

        self.assertTrue(config["observability"]["enabled"])
        self.assertEqual(config["observability"]["head_sampling_rate"], 1)
        self.assertEqual(config["observability"]["logs"], {"invocation_logs": False})
        self.assertEqual(config["version_metadata"], {"binding": "CF_VERSION_METADATA"})
        self.assertEqual(
            config.get("vars"),
            {
                "TURNSTILE_CHALLENGE_MODE": "session",
                "TURNSTILE_CLEARANCE_SECONDS": "28800",
            },
        )
        self.assertNotIn("TURNSTILE_SITE_KEY", config.get("vars", {}))
        self.assertNotIn("TURNSTILE_SECRET_KEY", config.get("vars", {}))
        self.assertNotIn("TURNSTILE_CLEARANCE_SECRET", config.get("vars", {}))
        self.assertNotIn("PBE_SMOKE_BYPASS_SECRET", config.get("vars", {}))


class WideEventMiddlewareTests(unittest.TestCase):
    def setUp(self):
        self.original_emit = observability.emit

    def tearDown(self):
        observability.emit = self.original_emit

    def run_asgi(self, app, scope):
        messages = []

        async def receive():
            return {"type": "http.request", "body": b"", "more_body": False}

        async def send(message):
            messages.append(message)

        asyncio.run(app(scope, receive, send))
        return messages

    def test_middleware_enriches_supplied_event_without_emitting_it(self):
        emitted = []
        observability.emit = lambda *args, **kwargs: emitted.append((args, kwargs))
        event = {"request_id": "outer", "cache": "miss"}

        async def app(scope, receive, send):
            self.assertIs(scope["state"]["wide_event"], event)
            scope["state"]["wide_event"]["example"] = {"slug": "hello-world"}
            await send({"type": "http.response.start", "status": 201, "headers": []})
            await send({"type": "http.response.body", "body": b""})

        scope = {"type": "http", "method": "GET", "path": "/", "headers": [], "state": {"wide_event": event}}
        messages = self.run_asgi(observability.WideEventMiddleware(app), scope)

        self.assertEqual(emitted, [])
        self.assertEqual(messages[0]["status"], 201)
        self.assertEqual(event["status_code"], 201)
        self.assertEqual(event["outcome"], "success")
        self.assertEqual(event["level"], "info")
        self.assertEqual(event["example"], {"slug": "hello-world"})
        self.assertIsInstance(event["app_duration_ms"], float)

    def test_middleware_creates_and_emits_fallback_event_for_asgi_only_calls(self):
        emitted = []

        def fake_emit(event, *, env=None):
            emitted.append((event, env))

        observability.emit = fake_emit
        env = SimpleNamespace(CF_VERSION_METADATA=SimpleNamespace(id="version-1"))

        async def app(scope, receive, send):
            scope["state"]["wide_event"]["handler_seen"] = True
            await send({"type": "http.response.start", "status": 404, "headers": []})
            await send({"type": "http.response.body", "body": b"not found"})

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/missing",
            "headers": [(b"cf-ray", b"ray-SFO"), (b"cf-ipcountry", b"US")],
            "env": env,
        }
        self.run_asgi(observability.WideEventMiddleware(app), scope)

        self.assertEqual(len(emitted), 1)
        event, emitted_env = emitted[0]
        self.assertIs(emitted_env, env)
        self.assertIs(scope["state"]["wide_event"], event)
        self.assertEqual(event["request_id"], "ray-SFO")
        self.assertEqual(event["path"], "/missing")
        self.assertEqual(event["cf"], {"ray": "ray-SFO", "colo": "SFO", "country": "US"})
        self.assertEqual(event["status_code"], 404)
        self.assertEqual(event["outcome"], "client_error")
        self.assertEqual(event["level"], "info")
        self.assertTrue(event["handler_seen"])
        self.assertEqual(event["duration_ms"], event["app_duration_ms"])


if __name__ == "__main__":
    unittest.main()
