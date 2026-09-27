"""Behavioral tests for the Turnstile clearance and cache-key logic.

These exercise the real signing/verification/cookie code in src/main.py
(with only the Workers runtime module stubbed), unlike the source-text
change detectors in test_app.py — a regression in HMAC comparison,
cookie scope, expiry handling, or fail-open mode selection fails here.
"""
from __future__ import annotations

import asyncio
import json
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

from fastapi import Request
from fastapi.responses import HTMLResponse


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
        env = session_env(PBE_SMOKE_BYPASS_SECRET="smoke-secret")
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
        response = self._run(post_request(b"code=print%28%27%E2%82%AC%27%29", env=session_env(TURNSTILE_CHALLENGE_MODE="off")))
        self.assertEqual(self._ran_code, "print('€')")
        self.assertEqual(response.status_code, 200)

    def test_verified_token_sets_clearance_cookie(self):
        self._ran_code = None
        self._stub_run(output="verified-run")

        async def _fake_verify(request, token):
            return True, "", {"outcome": "pass"}

        main._verify_turnstile = _fake_verify
        env = session_env(TURNSTILE_SITE_KEY="site-key")
        request = post_request(b"code=print(1)&cf-turnstile-response=tok", env=env)
        request.state.wide_event = {"path": "/examples/values"}
        response = self._run(request)
        self.assertEqual(self._ran_code, "print(1)")
        set_cookie = response.headers.get("set-cookie", "")
        self.assertIn(f"{main.TURNSTILE_CLEARANCE_COOKIE}=", set_cookie)
        self.assertEqual(request.state.wide_event["turnstile"], {"outcome": "pass"})

    def test_issued_challenge_is_recorded_apart_from_failures(self):
        # A challenge is the normal first run of a session; recording it as
        # "fail" hid real rejections among ordinary first runs.
        self._stub_run()
        request = post_request(b"code=print(1)", env=session_env(TURNSTILE_SITE_KEY="site-key"))
        request.state.wide_event = {"path": "/examples/values"}
        self._run(request)
        self.assertEqual(request.state.wide_event["turnstile"], {"outcome": "challenged"})

        misconfigured = post_request(b"code=print(1)", env=session_env())
        misconfigured.state.wide_event = {"path": "/examples/values"}
        self._run(misconfigured)
        self.assertEqual(
            misconfigured.state.wide_event["turnstile"], {"outcome": "fail", "reason": "site_key_missing"}
        )

    def test_rejected_token_records_reason_and_does_not_run_code(self):
        self._ran_code = None
        self._stub_run()

        async def _rejecting_verify(request, token):
            return main._turnstile_failure("rejected", ["invalid-input-secret"])

        main._verify_turnstile = _rejecting_verify
        request = post_request(
            b"code=print(1)&cf-turnstile-response=tok", env=session_env(TURNSTILE_SITE_KEY="site-key")
        )
        request.state.wide_event = {"path": "/examples/values"}
        response = self._run(request)
        body = response.body.decode()
        self.assertIsNone(self._ran_code)
        self.assertIn(main.TURNSTILE_FAILED_MESSAGE, body)
        self.assertIn('data-turnstile-required="true"', body)
        self.assertNotIn("set-cookie", response.headers)
        self.assertEqual(
            request.state.wide_event["turnstile"],
            {"outcome": "fail", "reason": "rejected", "error_codes": ["invalid-input-secret"]},
        )


class _SiteverifyResponse:
    def __init__(self, status, body):
        self.status, self.body = status, body

    async def text(self):
        return self.body


class TurnstileSiteverifyTests(unittest.TestCase):
    def setUp(self):
        self.saved = {name: getattr(main, name) for name in ("js_fetch", "JsRequest", "AbortSignal")}
        main.JsRequest = type("Request", (), {"new": staticmethod(lambda url, options: (url, options))})
        self.sent = []

    def tearDown(self):
        for name, value in self.saved.items():
            setattr(main, name, value)

    def _respond(self, body, status=200):
        async def fetch(request):
            self.sent.append(request)
            return _SiteverifyResponse(status, body)

        main.js_fetch = fetch

    def _verify(self, token="token"):
        return asyncio.run(main._verify_turnstile(make_request(env=session_env()), token))

    def test_transport_status_and_payload_failures_fail_closed(self):
        async def failing(_request):
            raise RuntimeError("network down")

        for fetch in (
            failing,
            lambda _request: _awaitable(_SiteverifyResponse(500, '{"success": true}')),
            lambda _request: _awaitable(_SiteverifyResponse(503, "<html>upstream down</html>")),
            lambda _request: _awaitable(_SiteverifyResponse(200, "not json")),
            lambda _request: _awaitable(_SiteverifyResponse(200, "[]")),
        ):
            with self.subTest(fetch=fetch):
                main.js_fetch = fetch
                ok, message, details = self._verify()
                self.assertFalse(ok)
                self.assertIn("verification failed", message)
                self.assertEqual(details, {"outcome": "fail", "reason": "siteverify_unavailable"})

    def test_siteverify_request_carries_a_timeout_signal(self):
        main.AbortSignal = type("AbortSignal", (), {"timeout": staticmethod(lambda ms: ("timeout", ms))})
        self._respond('{"success": true, "hostname": "www.pythonbyexample.dev", "action": "run-example"}')
        self._verify()
        url, options = self.sent[0]
        self.assertEqual(url, main.TURNSTILE_VERIFY_URL)
        self.assertEqual(options["signal"], ("timeout", main.SITEVERIFY_TIMEOUT_MS))
        self.assertEqual(main.SITEVERIFY_TIMEOUT_MS, 10_000)

    def test_overlong_token_is_rejected_without_calling_siteverify(self):
        self._respond('{"success": true, "hostname": "www.pythonbyexample.dev", "action": "run-example"}')
        ok, _, details = self._verify("x" * (main.MAX_TURNSTILE_TOKEN_CHARS + 1))
        self.assertFalse(ok)
        self.assertEqual(details, {"outcome": "fail", "reason": "token_too_long"})
        self.assertEqual(self.sent, [])

        ok, _, _ = self._verify("x" * main.MAX_TURNSTILE_TOKEN_CHARS)
        self.assertTrue(ok)
        self.assertEqual(len(self.sent), 1)

    def test_successful_siteverify_requires_matching_hostname_and_action(self):
        self._respond('{"success": true, "hostname": "www.pythonbyexample.dev", "action": "run-example"}')
        ok, message, details = self._verify()
        self.assertTrue(ok)
        self.assertEqual(message, "")
        self.assertEqual(details, {"outcome": "pass"})

    def test_siteverify_rejects_wrong_missing_or_non_string_hostname_and_action(self):
        cases = [
            ('{"success": true}', "hostname_mismatch"),
            ('{"success": true, "hostname": null, "action": "run-example"}', "hostname_mismatch"),
            ('{"success": true, "hostname": 7, "action": "run-example"}', "hostname_mismatch"),
            ('{"success": true, "hostname": "other.example", "action": "run-example"}', "hostname_mismatch"),
            ('{"success": true, "hostname": "www.pythonbyexample.dev", "action": "other-action"}', "action_mismatch"),
            ('{"success": true, "hostname": "www.pythonbyexample.dev"}', "action_mismatch"),
        ]
        for payload, reason in cases:
            with self.subTest(payload=payload):
                self._respond(payload)
                ok, message, details = self._verify()
                self.assertFalse(ok)
                self.assertIn("verification failed", message)
                self.assertEqual(details, {"outcome": "fail", "reason": reason})

    def test_rejection_records_only_documented_error_codes(self):
        cases = [
            ('{"success": false}', {"outcome": "fail", "reason": "rejected"}),
            (
                '{"success": false, "error-codes": ["invalid-input-secret"]}',
                {"outcome": "fail", "reason": "rejected", "error_codes": ["invalid-input-secret"]},
            ),
            (
                '{"success": false, "error-codes": ["timeout-or-duplicate", "x-new-code", 5, {"a": 1}]}',
                {"outcome": "fail", "reason": "rejected", "error_codes": ["other", "timeout-or-duplicate"]},
            ),
            ('{"success": "true", "error-codes": "bad-request"}', {"outcome": "fail", "reason": "rejected"}),
        ]
        for payload, expected in cases:
            with self.subTest(payload=payload):
                self._respond(payload)
                ok, _, details = self._verify()
                self.assertFalse(ok)
                self.assertEqual(details, expected)

    def test_http_400_secret_errors_are_configuration_codes_not_outages(self):
        # Live Siteverify returns these exact bodies with HTTP 400. Treating
        # every non-2xx as "unavailable" hid invalid-input-secret entirely.
        cases = [
            ('{"error-codes":["invalid-input-secret"],"success":false,"messages":[]}', "invalid-input-secret"),
            ('{"error-codes":["missing-input-secret"],"success":false,"messages":[]}', "missing-input-secret"),
        ]
        for payload, code in cases:
            with self.subTest(code=code):
                self._respond(payload, status=400)
                ok, _, details = self._verify()
                self.assertFalse(ok)
                self.assertEqual(details, {"outcome": "fail", "reason": "rejected", "error_codes": [code]})

    def test_non_2xx_never_passes_even_when_the_body_claims_success(self):
        self._respond(
            '{"success": true, "hostname": "www.pythonbyexample.dev", "action": "run-example", "error-codes": ["internal-error"]}',
            status=500,
        )
        ok, _, details = self._verify()
        self.assertFalse(ok)
        self.assertEqual(details, {"outcome": "fail", "reason": "rejected", "error_codes": ["internal-error"]})


# Replies live Siteverify gave to the dummy token, per secret.
PRODUCTION_SECRET_REPLY = (200, '{"success": false, "error-codes": ["invalid-input-response"]}')
BAD_SECRET_REPLY = (400, '{"error-codes":["invalid-input-secret"],"success":false,"messages":[]}')
TEST_SECRET_REPLIES = {
    "always-pass": (
        200,
        (
            '{"challenge_ts":"2026-09-25T22:08:06.790Z","error-codes":[],"hostname":"example.com",'
            '"metadata":{"result_with_testing_key":true},"success":true}'
        ),
    ),
    "always-fail": (
        200,
        (
            '{"error-codes":["invalid-input-response"],"success":false,"messages":[],'
            '"metadata":{"result_with_testing_key":true}}'
        ),
    ),
    "token-spent": (
        200,
        (
            '{"error-codes":["timeout-or-duplicate"],"success":false,"messages":[],'
            '"metadata":{"result_with_testing_key":true}}'
        ),
    ),
}


class TurnstileProbeTests(unittest.TestCase):
    """The smoke-gated probe proves the deployed secret with the dummy token.

    Response bodies are the ones live Siteverify returned for the dummy token.
    """

    def setUp(self):
        self.saved = {name: getattr(main, name) for name in ("js_fetch", "JsRequest", "AbortSignal")}
        main.JsRequest = type("Request", (), {"new": staticmethod(lambda url, options: (url, options))})
        main.AbortSignal = None
        self.sent = []

    def tearDown(self):
        for name, value in self.saved.items():
            setattr(main, name, value)

    def _respond(self, status, body):
        async def fetch(request):
            self.sent.append(request)
            return _SiteverifyResponse(status, body)

        main.js_fetch = fetch

    def _smoke_request(self, header="smoke-secret", **env):
        values = {"PBE_SMOKE_BYPASS_SECRET": "smoke-secret", "TURNSTILE_SITE_KEY": "site-key"}
        values.update(env)
        headers = {main.SMOKE_BYPASS_HEADER: header} if header else {}
        return make_request(headers=headers, env=session_env(**values))

    def _probe(self, request):
        return asyncio.run(main._probe_turnstile(request))

    def test_working_production_secret_is_ok(self):
        self._respond(*PRODUCTION_SECRET_REPLY)
        report = self._probe(self._smoke_request())
        self.assertEqual(
            report,
            {"challenge_mode": "session", "site_key_configured": True, "secret": "valid", "ok": True},
        )
        _, options = self.sent[0]
        self.assertIn(f"response={main.TURNSTILE_PROBE_TOKEN}", options["body"])
        self.assertIn("secret=server-secret", options["body"])
        self.assertNotIn("remoteip", options["body"])

    def test_bad_secret_fails_with_its_error_code(self):
        self._respond(*BAD_SECRET_REPLY)
        report = self._probe(self._smoke_request())
        self.assertEqual(report["secret"], "invalid")
        self.assertEqual(report["error_codes"], ["invalid-input-secret"])
        self.assertFalse(report["ok"])

    def test_every_test_secret_fails_including_the_one_that_mimics_production(self):
        for name, response in TEST_SECRET_REPLIES.items():
            with self.subTest(secret=name):
                self._respond(*response)
                report = self._probe(self._smoke_request())
                self.assertEqual(report["secret"], "testing_key")
                self.assertFalse(report["ok"])

    def test_valid_secret_without_site_key_is_not_ok(self):
        self._respond(*PRODUCTION_SECRET_REPLY)
        report = self._probe(self._smoke_request(TURNSTILE_SITE_KEY=""))
        self.assertEqual(report["secret"], "valid")
        self.assertFalse(report["site_key_configured"])
        self.assertFalse(report["ok"])

    def test_absent_secret_reports_turnstile_off_without_calling_siteverify(self):
        self._respond(*PRODUCTION_SECRET_REPLY)
        report = self._probe(self._smoke_request(TURNSTILE_SECRET_KEY=""))
        self.assertEqual(report["secret"], "absent")
        self.assertTrue(report["ok"])
        self.assertEqual(self.sent, [])

    def test_unreachable_or_unexpected_siteverify_is_not_ok(self):
        async def failing(_request):
            raise RuntimeError("network down")

        main.js_fetch = failing
        self.assertEqual(self._probe(self._smoke_request())["secret"], "unverified")
        for status, body in (
            (200, '{"success": false, "error-codes": ["internal-error"]}'),
            (200, '{"success": false}'),
            (503, '{"success": false, "error-codes": ["invalid-input-response"]}'),
        ):
            with self.subTest(status=status, body=body):
                self._respond(status, body)
                report = self._probe(self._smoke_request())
                self.assertEqual(report["secret"], "unexpected")
                self.assertFalse(report["ok"])

    def test_route_requires_the_smoke_header_and_returns_json(self):
        self._respond(*BAD_SECRET_REPLY)
        for header in ("", "wrong-secret"):
            with self.subTest(header=header):
                response = asyncio.run(main.turnstile_probe(self._smoke_request(header=header)))
                self.assertEqual(response.status_code, 404)
                self.assertEqual(self.sent, [], "an unauthenticated probe must not reach Siteverify")

        request = self._smoke_request()
        request.state.wide_event = {"path": main.TURNSTILE_PROBE_PATH}
        response = asyncio.run(main.turnstile_probe(request))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.media_type, "application/json")
        report = json.loads(response.body)
        self.assertEqual(report["secret"], "invalid")
        self.assertFalse(report["ok"])
        self.assertEqual(request.state.wide_event["turnstile_probe"], {"secret": "invalid", "ok": False})
        self.assertNotIn("server-secret", response.body.decode())


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
        from app import (
            DYNAMIC_OUTPUT_LIMIT_MESSAGE,
            MAX_DYNAMIC_OUTPUT_BYTES,
            build_dynamic_worker_code,
        )

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
            exec(  # noqa: S102 - test executes the generated worker module
                build_dynamic_worker_code(f"print('€' * {(MAX_DYNAMIC_OUTPUT_BYTES - 1) // 3})"),
                namespace,
            )
            under = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(under.status, 200)
            self.assertLessEqual(len(under.body.encode()), MAX_DYNAMIC_OUTPUT_BYTES)
            namespace = {}
            exec(  # noqa: S102 - test executes the generated worker module
                build_dynamic_worker_code(f"print('x' * {MAX_DYNAMIC_OUTPUT_BYTES + 1})"), namespace
            )
            over = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(over.status, 413)
            self.assertEqual(over.body, DYNAMIC_OUTPUT_LIMIT_MESSAGE)
            namespace = {}
            exec(  # noqa: S102 - test executes the generated worker module
                build_dynamic_worker_code(f"raise ValueError('x' * {MAX_DYNAMIC_OUTPUT_BYTES + 1})"),
                namespace,
            )
            huge_error = asyncio.run(namespace["Default"]().fetch(None))
            self.assertEqual(huge_error.status, 413)
            self.assertEqual(huge_error.body, DYNAMIC_OUTPUT_LIMIT_MESSAGE)
            self.assertLessEqual(len(huge_error.body.encode()), MAX_DYNAMIC_OUTPUT_BYTES)
            namespace = {}
            exec(  # noqa: S102 - test executes the generated worker module
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
