"""Behavioral tests for the Turnstile clearance and cache-key logic.

These exercise the real signing/verification/cookie code in src/main.py
(with only the Workers runtime module stubbed), unlike the source-text
change detectors in test_app.py — a regression in HMAC comparison,
cookie scope, expiry handling, or fail-open mode selection fails here.
"""
from __future__ import annotations

import asyncio
import sys
import time
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

_WORKERS_STUB_ATTRS = {
    "WorkerEntrypoint": object,
    "python_from_rpc": staticmethod(lambda value: value),
    "Context": object,
    "Request": object,
    "wait_until": staticmethod(lambda task: None),
}


def _import_main():
    saved = sys.modules.get("workers")
    workers = types.ModuleType("workers")
    for name, value in _WORKERS_STUB_ATTRS.items():
        setattr(workers, name, value)
    sys.modules["workers"] = workers
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    try:
        import main
    finally:
        if saved is not None:
            sys.modules["workers"] = saved
    return main


main = _import_main()

from fastapi import Request  # noqa: E402
from fastapi.responses import HTMLResponse  # noqa: E402


class _Env:
    def __init__(self, **values):
        for key, value in values.items():
            setattr(self, key, value)


def make_request(*, cookie: str = "", headers: dict[str, str] | None = None, env=None) -> Request:
    raw_headers = []
    if cookie:
        raw_headers.append((b"cookie", f"{main.TURNSTILE_CLEARANCE_COOKIE}={cookie}".encode()))
    for key, value in (headers or {}).items():
        raw_headers.append((key.lower().encode(), value.encode()))
    return Request(
        {
            "type": "http",
            "method": "POST",
            "path": "/examples/values",
            "query_string": b"",
            "headers": raw_headers,
            "scheme": "https",
            "server": ("www.pythonbyexample.dev", 443),
            "env": env,
        }
    )


def session_env(**overrides) -> _Env:
    values = {
        "TURNSTILE_SECRET_KEY": "server-secret",
        "TURNSTILE_CLEARANCE_SECRET": "clearance-secret",
        "TURNSTILE_CHALLENGE_MODE": "session",
    }
    values.update(overrides)
    return _Env(**values)


class ClearanceSigningTests(unittest.TestCase):
    def test_signed_clearance_round_trips(self):
        env = session_env()
        clearance_cookie = main._sign_clearance("clearance-secret", int(time.time()) + 600)
        request = make_request(cookie=clearance_cookie, env=env)
        self.assertTrue(main._clearance_valid(request))
        self.assertFalse(main._requires_turnstile(request))

    def test_tampered_signature_is_rejected(self):
        env = session_env()
        clearance_cookie = main._sign_clearance("clearance-secret", int(time.time()) + 600)
        tampered = clearance_cookie[:-2] + ("aa" if not clearance_cookie.endswith("aa") else "bb")
        request = make_request(cookie=tampered, env=env)
        self.assertFalse(main._clearance_valid(request))
        self.assertTrue(main._requires_turnstile(request))

    def test_expired_clearance_is_rejected(self):
        env = session_env()
        clearance_cookie = main._sign_clearance("clearance-secret", int(time.time()) - 1)
        request = make_request(cookie=clearance_cookie, env=env)
        self.assertFalse(main._clearance_valid(request))

    def test_non_integer_expiry_is_rejected(self):
        env = session_env()
        request = make_request(cookie="soon.deadbeef", env=env)
        self.assertFalse(main._clearance_valid(request))

    def test_signature_for_different_expiry_is_rejected(self):
        env = session_env()
        valid = main._sign_clearance("clearance-secret", int(time.time()) + 600)
        _, signature = valid.split(".", 1)
        forged = f"{int(time.time()) + 99999}.{signature}"
        request = make_request(cookie=forged, env=env)
        self.assertFalse(main._clearance_valid(request))


class ChallengeModeTests(unittest.TestCase):
    def test_off_mode_disables_challenge(self):
        request = make_request(env=session_env(TURNSTILE_CHALLENGE_MODE="off"))
        self.assertFalse(main._requires_turnstile(request))

    def test_session_mode_requires_challenge_without_clearance(self):
        request = make_request(env=session_env())
        self.assertTrue(main._requires_turnstile(request))

    def test_unknown_mode_fails_closed(self):
        request = make_request(env=session_env(TURNSTILE_CHALLENGE_MODE="sessoin"))
        self.assertTrue(main._requires_turnstile(request))

    def test_no_secret_disables_challenge(self):
        request = make_request(env=_Env(TURNSTILE_CHALLENGE_MODE="session"))
        self.assertFalse(main._requires_turnstile(request))

    def test_smoke_bypass_header_disables_challenge(self):
        env = session_env(**{"PBE_SMOKE_BYPASS_SECRET": "smoke-secret"})
        request = make_request(headers={main.SMOKE_BYPASS_HEADER: "smoke-secret"}, env=env)
        self.assertFalse(main._requires_turnstile(request))
        wrong = make_request(headers={main.SMOKE_BYPASS_HEADER: "wrong"}, env=env)
        self.assertTrue(main._requires_turnstile(wrong))


class ClearanceCookieTests(unittest.TestCase):
    def _set_cookie_header(self, env) -> str:
        response = HTMLResponse("ok")
        request = make_request(env=env)
        main._set_turnstile_clearance(response, request)
        return response.headers.get("set-cookie", "")

    def test_cookie_attributes(self):
        header = self._set_cookie_header(session_env())
        self.assertIn(f"{main.TURNSTILE_CLEARANCE_COOKIE}=", header)
        self.assertIn("Path=/examples", header)
        self.assertIn("HttpOnly", header)
        self.assertIn("Secure", header)
        self.assertIn("SameSite=lax", header.lower().replace("samesite=lax", "SameSite=lax"))
        self.assertIn(f"Max-Age={main.DEFAULT_TURNSTILE_CLEARANCE_SECONDS}", header)

    def test_clearance_seconds_clamped_to_bounds(self):
        low = make_request(env=session_env(TURNSTILE_CLEARANCE_SECONDS="1"))
        self.assertEqual(main._turnstile_clearance_seconds(low), 60)
        high = make_request(env=session_env(TURNSTILE_CLEARANCE_SECONDS=str(10**9)))
        self.assertEqual(main._turnstile_clearance_seconds(high), 60 * 60 * 24 * 7)
        garbage = make_request(env=session_env(TURNSTILE_CLEARANCE_SECONDS="soon"))
        self.assertEqual(
            main._turnstile_clearance_seconds(garbage), main.DEFAULT_TURNSTILE_CLEARANCE_SECONDS
        )


class HtmlCacheKeyTests(unittest.TestCase):
    def test_normalizes_ignored_query_strings(self):
        key = main.html_cache_key_url("https://example.dev/examples/values")
        self.assertEqual(
            key,
            f"https://example.dev/examples/values?__html_v={main.HTML_CACHE_VERSION}",
        )
        keyed = main.html_cache_key_url("https://example.dev/examples/values?a=1&utm=x#frag")
        self.assertEqual(keyed, key)

    def test_turnstile_site_key_fragments_the_cache(self):
        plain = main.html_cache_key_url("https://example.dev/")
        keyed = main.html_cache_key_url("https://example.dev/", "site-key")
        other = main.html_cache_key_url("https://example.dev/", "other-key")
        self.assertNotEqual(plain, keyed)
        self.assertNotEqual(keyed, other)
        self.assertNotIn("site-key", keyed, "raw site key must not appear in cache keys")

    def test_layout_options_bypass_cache(self):
        self.assertFalse(main.should_cache_get_url("https://example.dev/layout-options/x"))
        self.assertTrue(main.should_cache_get_url("https://example.dev/examples/values"))


def post_request(body: bytes, *, env=None, headers: dict[str, str] | None = None) -> Request:
    raw_headers = [(b"content-type", b"application/x-www-form-urlencoded")]
    for key, value in (headers or {}).items():
        raw_headers.append((key.lower().encode(), value.encode()))

    async def receive():
        return {"type": "http.request", "body": body, "more_body": False}

    return Request(
        {
            "type": "http",
            "method": "POST",
            "path": "/examples/values",
            "query_string": b"",
            "headers": raw_headers,
            "env": env,
        },
        receive,
    )


class RunExampleFlowTests(unittest.TestCase):
    """Behavioral tests of the POST /examples/{slug} handler branches:
    verification-required, missing-site-key, too-large, and
    verify-then-set-clearance. Exercises the real run_example handler with
    a constructed Request; the Dynamic Worker run and Turnstile siteverify
    HTTP call are stubbed so only the handler's control flow is under test.
    """

    def _run(self, request):
        return asyncio.run(main.run_example("values", request))

    def setUp(self):
        self._saved = {name: getattr(main, name) for name in ("_run_example", "_verify_turnstile")}

    def tearDown(self):
        for name, value in self._saved.items():
            setattr(main, name, value)

    def _stub_run(self, output="OUT"):
        async def _fake_run_example(request, slug, code):
            self._ran_code = code
            return output
        main._run_example = _fake_run_example

    def test_verification_required_path_does_not_run_code(self):
        self._ran_code = None
        self._stub_run()
        env = session_env(TURNSTILE_SITE_KEY="site-key")
        response = self._run(post_request(b"code=print(1)", env=env))
        body = response.body.decode()
        # The retriable-challenge marker is rendered as a real attribute
        # (the bare string also lives in the page's static JS selector).
        self.assertIn('data-turnstile-required="true"', body)
        self.assertIn("Verification required", body)
        self.assertIsNone(self._ran_code, "code must not run before verification")

    def test_missing_site_key_message(self):
        self._stub_run()
        env = session_env()  # secret set, but no TURNSTILE_SITE_KEY
        response = self._run(post_request(b"code=print(1)", env=env))
        body = response.body.decode()
        self.assertIn("TURNSTILE_SITE_KEY is not configured", body)
        self.assertNotIn('data-turnstile-required="true"', body)

    def test_oversize_body_rejected_with_413(self):
        self._stub_run()
        big = b"code=" + b"x" * (main.MAX_SUBMITTED_BODY_BYTES + 1)
        response = self._run(post_request(big, env=session_env(TURNSTILE_CHALLENGE_MODE="off")))
        self.assertEqual(response.status_code, 413)
        self.assertIn("too large", response.body.decode().lower())

    def test_off_mode_runs_without_challenge(self):
        self._ran_code = None
        self._stub_run(output="ran-output")
        response = self._run(
            post_request(b"code=print(42)", env=session_env(TURNSTILE_CHALLENGE_MODE="off"))
        )
        self.assertEqual(self._ran_code, "print(42)")
        self.assertIn("ran-output", response.body.decode())

    def test_dynamic_worker_output_rejection_propagates_413(self):
        async def rejected(request, slug, code):
            request.state.dynamic_worker_status = 413
            return main.DYNAMIC_OUTPUT_LIMIT_MESSAGE

        main._run_example = rejected
        response = self._run(
            post_request(b"code=print(42)", env=session_env(TURNSTILE_CHALLENGE_MODE="off"))
        )
        self.assertEqual(response.status_code, 413)
        self.assertIn("output exceeded", response.body.decode())

    def test_invalid_raw_or_percent_encoded_utf8_is_rejected_before_execution(self):
        for body in (b"code=\xff", b"code=%FF"):
            with self.subTest(body=body):
                self._ran_code = None
                self._stub_run()
                response = self._run(post_request(body, env=session_env(TURNSTILE_CHALLENGE_MODE="off")))
                self.assertEqual(response.status_code, 400)
                self.assertIn("valid UTF-8", response.body.decode())
                self.assertIsNone(self._ran_code)

    def test_valid_unicode_form_reaches_runner(self):
        self._stub_run(output="ok")
        response = self._run(post_request("code=print%28%27%E2%82%AC%27%29".encode(), env=session_env(TURNSTILE_CHALLENGE_MODE="off")))
        self.assertEqual(self._ran_code, "print('€')")
        self.assertEqual(response.status_code, 200)

    def test_verified_token_sets_clearance_cookie(self):
        self._ran_code = None
        self._stub_run(output="verified-run")

        async def _fake_verify(request, token):
            return True, "ok", "success"

        main._verify_turnstile = _fake_verify
        env = session_env(TURNSTILE_SITE_KEY="site-key")
        response = self._run(post_request(b"code=print(1)&cf-turnstile-response=tok", env=env))
        self.assertEqual(self._ran_code, "print(1)")
        set_cookie = response.headers.get("set-cookie", "")
        self.assertIn(f"{main.TURNSTILE_CLEARANCE_COOKIE}=", set_cookie)


class TurnstileSiteverifyTests(unittest.TestCase):
    def setUp(self):
        self.saved_fetch = main.js_fetch
        self.saved_request = main.JsRequest
        main.JsRequest = type("Request", (), {"new": staticmethod(lambda url, options: (url, options))})

    def tearDown(self):
        main.js_fetch = self.saved_fetch
        main.JsRequest = self.saved_request

    def test_transport_status_and_payload_failures_fail_closed(self):
        class Response:
            def __init__(self, status, body):
                self.status, self.body = status, body
            async def text(self):
                return self.body

        async def failing(_request):
            raise RuntimeError("network down")

        request = make_request(env=session_env())
        for fetch in (
            failing,
            lambda _request: _awaitable(Response(500, '{"success": true}')),
            lambda _request: _awaitable(Response(200, "not json")),
            lambda _request: _awaitable(Response(200, "[]")),
            lambda _request: _awaitable(Response(200, '{"success": false}')),
        ):
            with self.subTest(fetch=fetch):
                main.js_fetch = fetch
                ok, message, outcome = asyncio.run(main._verify_turnstile(request, "token"))
                self.assertFalse(ok)
                self.assertIn("verification failed", message)
                self.assertEqual(outcome, "fail")

    def test_successful_siteverify_requires_matching_hostname_and_action(self):
        class Response:
            status = 200
            async def text(self):
                return '{"success": true, "hostname": "www.pythonbyexample.dev", "action": "run-example"}'

        main.js_fetch = lambda _request: _awaitable(Response())
        ok, message, outcome = asyncio.run(main._verify_turnstile(make_request(env=session_env()), "token"))
        self.assertTrue(ok)
        self.assertEqual(message, "")
        self.assertEqual(outcome, "pass")

    def test_siteverify_rejects_wrong_or_missing_hostname_and_action(self):
        payloads = [
            '{"success": true}',
            '{"success": true, "hostname": "other.example", "action": "run-example"}',
            '{"success": true, "hostname": "www.pythonbyexample.dev", "action": "other-action"}',
        ]
        for payload in payloads:
            with self.subTest(payload=payload):
                class Response:
                    status = 200

                    async def text(self):
                        return payload

                main.js_fetch = lambda _request: _awaitable(Response())
                ok, message, outcome = asyncio.run(main._verify_turnstile(make_request(env=session_env()), "token"))
                self.assertFalse(ok)
                self.assertIn("verification failed", message)
                self.assertEqual(outcome, "fail")


async def _awaitable(value):
    return value


class DynamicWorkerCodeTests(unittest.TestCase):
    """Behavioral coverage of build_dynamic_worker_code: the generated
    module embeds the submitted code as a string literal (so a
    closing-quote injection cannot break out) and defines the entrypoint.
    """

    def test_generated_module_embeds_code_and_entrypoint(self):
        from app import build_dynamic_worker_code

        module = build_dynamic_worker_code("print('hi <b>')")
        self.assertIn(repr("print('hi <b>')"), module)
        self.assertIn("class Default(WorkerEntrypoint)", module)
        self.assertIn("async def fetch", module)
        tricky = build_dynamic_worker_code("x = '''end'''")
        self.assertIn(repr("x = '''end'''"), tricky)

    def test_generated_worker_enforces_utf8_output_cap(self):
        from app import DYNAMIC_OUTPUT_LIMIT_MESSAGE, MAX_DYNAMIC_OUTPUT_BYTES, build_dynamic_worker_code

        saved_workers = sys.modules.get("workers")
        fake_workers = types.ModuleType("workers")

        class Response:
            def __init__(self, body, status=200, headers=None):
                self.body, self.status, self.headers = body, status, headers or {}

        fake_workers.Response = Response
        fake_workers.WorkerEntrypoint = object
        sys.modules["workers"] = fake_workers
        try:
            namespace = {}
            exec(build_dynamic_worker_code(f"print('€' * {(MAX_DYNAMIC_OUTPUT_BYTES - 1) // 3})"), namespace)
            under = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(under.status, 200)
            self.assertLessEqual(len(under.body.encode()), MAX_DYNAMIC_OUTPUT_BYTES)
            namespace = {}
            exec(build_dynamic_worker_code(f"print('x' * {MAX_DYNAMIC_OUTPUT_BYTES + 1})"), namespace)
            over = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(over.status, 413)
            self.assertEqual(over.body, DYNAMIC_OUTPUT_LIMIT_MESSAGE)
            namespace = {}
            exec(build_dynamic_worker_code(f"raise ValueError('x' * {MAX_DYNAMIC_OUTPUT_BYTES + 1})"), namespace)
            huge_error = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(huge_error.status, 413)
            self.assertEqual(huge_error.body, DYNAMIC_OUTPUT_LIMIT_MESSAGE)
            self.assertLessEqual(len(huge_error.body.encode()), MAX_DYNAMIC_OUTPUT_BYTES)
            namespace = {}
            exec(
                build_dynamic_worker_code(
                    f"import sys; sys.stdout.parts.append('x' * {MAX_DYNAMIC_OUTPUT_BYTES + 1})"
                ),
                namespace,
            )
            mutated_sink = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(mutated_sink.status, 413)
            self.assertEqual(mutated_sink.body, DYNAMIC_OUTPUT_LIMIT_MESSAGE)
        finally:
            if saved_workers is None:
                sys.modules.pop("workers", None)
            else:
                sys.modules["workers"] = saved_workers


if __name__ == "__main__":
    unittest.main()
