"""Behavioral tests for the Turnstile clearance and cache-key logic.

These exercise the real signing/verification/cookie code in src/main.py
(with only the Workers runtime module stubbed), unlike the source-text
change detectors in test_app.py — a regression in HMAC comparison,
cookie scope, expiry handling, or fail-open mode selection fails here.
"""
from __future__ import annotations

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
        token = main._sign_clearance("clearance-secret", int(time.time()) + 600)
        request = make_request(cookie=token, env=env)
        self.assertTrue(main._clearance_valid(request))
        self.assertFalse(main._requires_turnstile(request))

    def test_tampered_signature_is_rejected(self):
        env = session_env()
        token = main._sign_clearance("clearance-secret", int(time.time()) + 600)
        tampered = token[:-2] + ("aa" if not token.endswith("aa") else "bb")
        request = make_request(cookie=tampered, env=env)
        self.assertFalse(main._clearance_valid(request))
        self.assertTrue(main._requires_turnstile(request))

    def test_expired_clearance_is_rejected(self):
        env = session_env()
        token = main._sign_clearance("clearance-secret", int(time.time()) - 1)
        request = make_request(cookie=token, env=env)
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
    def test_appends_version_with_query_separator(self):
        key = main.html_cache_key_url("https://example.dev/examples/values")
        self.assertIn(f"?__html_v={main.HTML_CACHE_VERSION}", key)
        keyed = main.html_cache_key_url("https://example.dev/examples/values?a=1")
        self.assertIn(f"&__html_v={main.HTML_CACHE_VERSION}", keyed)
        self.assertTrue(keyed.startswith("https://example.dev/examples/values?a=1"))

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


if __name__ == "__main__":
    unittest.main()
