#!/usr/bin/env python3
"""Smoke-test a deployed Python By Example origin.

Usage:
    scripts/smoke_deployment.py https://www.pythonbyexample.dev
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin

SMOKE_PATHS = [
    "/",
    "/examples/values",
    "/examples/async-await",
    "/examples/networking",
    "/examples/subprocesses",
    "/journeys/workers",
    "/prototyping/production-figures-gestalt",
]
ERROR_MARKERS = ["error code: 1101", "PythonError", "Traceback"]


def fetch(url: str) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "pythonbyexample-smoke/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url", help="deployment origin, e.g. https://www.pythonbyexample.dev")
    parser.add_argument("--path", action="append", dest="paths", help="additional path to check")
    args = parser.parse_args()

    base = args.base_url.rstrip("/") + "/"
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
        lowered = body.lower()
        for marker in ERROR_MARKERS:
            if marker.lower() in lowered:
                failures.append(f"{url}: rendered exception marker {marker!r}")
                break
        print(f"{status} {url}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print(f"Deployment smoke OK ({len(paths)} paths).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
