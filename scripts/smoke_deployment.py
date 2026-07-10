#!/usr/bin/env python3
"""Smoke-test a deployed Python By Example origin.

Usage:
    scripts/smoke_deployment.py https://www.pythonbyexample.dev
"""
from __future__ import annotations

import argparse
import html
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
        headers["x-pythonbyexample-smoke-secret"] = smoke_bypass_secret
    request = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


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
        except Exception as exc:  # pragma: no cover - diagnostic path
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
            except Exception as exc:  # pragma: no cover - diagnostic path
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

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    post_count = 0 if args.skip_post else len(POST_SMOKES)
    print(f"Deployment smoke OK ({len(paths)} GETs, {post_count} POSTs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
