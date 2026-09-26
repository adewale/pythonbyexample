#!/usr/bin/env python3
"""Smoke-test a deployed Python By Example origin.

Usage:
    scripts/smoke_deployment.py https://www.pythonbyexample.dev
    PBE_SMOKE_BYPASS_SECRET=... scripts/smoke_deployment.py https://www.pythonbyexample.dev

With PBE_SMOKE_BYPASS_SECRET, POST runs skip Turnstile, so the script also
asks the Worker to prove its Turnstile secret against Siteverify.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from urllib.parse import urljoin

SMOKE_PATHS = [
    "/",
    "/about",
    "/privacy",
    "/examples/values",
    "/examples/async-await",
    "/examples/networking",
    "/examples/subprocesses",
    "/journeys/reliability",
    "/prototyping/production-figures-gestalt",
]
POST_SMOKES = [
    ("values", "print('runtime-smoke-values')\n", "runtime-smoke-values"),
    ("values", "print('runtime-smoke-values-edited')\n", "runtime-smoke-values-edited"),
    ("async-await", "import asyncio\n\nasync def main():\n    return 'runtime-smoke-async'\n\nprint(asyncio.run(main()))\n", "runtime-smoke-async"),
    ("networking", "print('runtime-smoke-networking-boundary')\n", "runtime-smoke-networking-boundary"),
    ("subprocesses", "print('runtime-smoke-subprocess-boundary')\n", "runtime-smoke-subprocess-boundary"),
]
ERROR_MARKERS = ["error code: 1101", "PythonError", "Traceback"]
SMOKE_BYPASS_HEADER = "x-pythonbyexample-smoke-secret"
TURNSTILE_PROBE_PATH = "/__smoke/turnstile"
TURNSTILE_PROBE_PROBLEMS = {
    "invalid": "Siteverify rejects TURNSTILE_SECRET_KEY, so every challenged run fails",
    "testing_key": "TURNSTILE_SECRET_KEY is a Cloudflare test secret, which ignores the visitor",
    "unverified": "the Worker could not reach Siteverify; re-run smoke before trusting the secret",
    "unexpected": "Siteverify answered the dummy token unexpectedly",
}


def fetch(url: str) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "pythonbyexample-smoke/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def post_code(url: str, code: str, smoke_bypass_secret: str = "") -> tuple[int, str]:
    data = urllib.parse.urlencode({"code": code}).encode()
    headers = {
        "User-Agent": "pythonbyexample-smoke/1.0",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    if smoke_bypass_secret:
        headers[SMOKE_BYPASS_HEADER] = smoke_bypass_secret
    request = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def probe_turnstile(base_url: str, smoke_bypass_secret: str) -> dict:
    request = urllib.request.Request(
        urljoin(base_url, TURNSTILE_PROBE_PATH.lstrip("/")),
        data=b"",
        headers={"User-Agent": "pythonbyexample-smoke/1.0", SMOKE_BYPASS_HEADER: smoke_bypass_secret},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def turnstile_probe_problem(report: dict) -> str | None:
    """Explain why the Worker's Turnstile configuration cannot verify browsers."""
    if report.get("ok") is True:
        return None
    secret = report.get("secret")
    if secret == "valid" and not report.get("site_key_configured"):
        return "TURNSTILE_SITE_KEY is not configured, so challenges cannot render"
    problem = TURNSTILE_PROBE_PROBLEMS.get(secret, f"unrecognized probe report {report!r}")
    if codes := report.get("error_codes"):
        problem += f" ({', '.join(codes)})"
    return problem


def has_exception_marker(body: str) -> str | None:
    lowered = body.lower()
    for marker in ERROR_MARKERS:
        if marker.lower() in lowered:
            return marker
    return None


def validate_smoke_bypass_origin(base_url: str, smoke_bypass_secret: str) -> str | None:
    if smoke_bypass_secret and urllib.parse.urlparse(base_url).scheme != "https":
        return "PBE_SMOKE_BYPASS_SECRET may only be sent to an https:// deployment origin"
    return None


def output_panel_text(body: str) -> str:
    match = re.search(
        r'<section[^>]*class="[^"]*output-panel[^"]*"[^>]*>.*?<pre><code>(.*?)</code></pre>',
        body,
        flags=re.DOTALL,
    )
    return html.unescape(match.group(1)) if match else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url", help="deployment origin, e.g. https://www.pythonbyexample.dev")
    parser.add_argument("--path", action="append", dest="paths", help="additional path to check")
    parser.add_argument("--skip-post", action="store_true", help="check rendered pages only")
    args = parser.parse_args()

    base = args.base_url.rstrip("/") + "/"
    smoke_bypass_value = os.environ.get("PBE_SMOKE_BYPASS_SECRET", "")
    if origin_error := validate_smoke_bypass_origin(base, smoke_bypass_value):
        print(origin_error, file=sys.stderr)
        return 1
    paths = SMOKE_PATHS + (args.paths or [])
    failures: list[str] = []

    for path in paths:
        url = urljoin(base, path.lstrip("/"))
        try:
            status, body = fetch(url)
        except urllib.error.HTTPError as exc:
            failures.append(f"{url}: HTTP {exc.code}")
            continue
        except Exception as exc:  # noqa: BLE001  # pragma: no cover - report any transport failure
            failures.append(f"{url}: {exc!r}")
            continue
        if status != 200:
            failures.append(f"{url}: HTTP {status}")
        marker = has_exception_marker(body)
        if marker:
            failures.append(f"{url}: rendered exception marker {marker!r}")
        print(f"GET {status} {url}")

    if not args.skip_post:
        for slug, code, expected in POST_SMOKES:
            url = urljoin(base, f"examples/{slug}")
            try:
                status, body = post_code(url, code, smoke_bypass_value)
            except urllib.error.HTTPError as exc:
                failures.append(f"POST {url}: HTTP {exc.code}")
                continue
            except Exception as exc:  # noqa: BLE001  # pragma: no cover - report any transport failure
                failures.append(f"POST {url}: {exc!r}")
                continue
            if status != 200:
                failures.append(f"POST {url}: HTTP {status}")
            marker = has_exception_marker(body)
            if marker:
                failures.append(f"POST {url}: rendered exception marker {marker!r}")
            rendered_output = output_panel_text(body)
            if expected not in rendered_output:
                failures.append(f"POST {url}: missing edited-code output {expected!r}")
            print(f"POST {status} {url} -> {expected}")

        url = urljoin(base, TURNSTILE_PROBE_PATH.lstrip("/"))
        if not smoke_bypass_value:
            print(f"SKIP {url}: set PBE_SMOKE_BYPASS_SECRET to verify the deployed Turnstile secret")
        else:
            try:
                report = probe_turnstile(base, smoke_bypass_value)
            except urllib.error.HTTPError as exc:
                failures.append(f"POST {url}: HTTP {exc.code} (deploy the probe route, or check PBE_SMOKE_BYPASS_SECRET)")
            except Exception as exc:  # noqa: BLE001  # pragma: no cover - report any transport failure
                failures.append(f"POST {url}: {exc!r}")
            else:
                if problem := turnstile_probe_problem(report):
                    failures.append(f"POST {url}: {problem}")
                print(f"POST {url} -> Turnstile secret {report.get('secret')}, mode {report.get('challenge_mode')}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    post_count = 0 if args.skip_post else len(POST_SMOKES)
    print(f"Deployment smoke OK ({len(paths)} GETs, {post_count} POSTs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
