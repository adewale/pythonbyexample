#!/usr/bin/env python3
"""Run every example's complete program in the real sandbox.

`verify_examples.py` executes the catalog under host CPython. This check
posts each program to a running Worker (the local dev Worker by default),
so it exercises what a learner gets when they press Run: the Pyodide
runtime, the Dynamic Worker harness, and the page that renders the output.

Pages whose frontmatter sets `sandbox_limit` teach something the sandbox
cannot do (child processes, threads, sockets). For those the check asserts
that Run explains the limit instead of expecting the CPython output.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from _common import load_catalog

OUTPUT_RE = re.compile(r'<section class="runner-panel output-panel"[^>]*>.*?<pre><code>(.*?)</code></pre>', re.DOTALL)


def run_in_worker(base_url: str, slug: str, code: str) -> str:
    request = urllib.request.Request(
        f"{base_url}/examples/{slug}",
        data=urllib.parse.urlencode({"code": code}).encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        page = response.read().decode("utf-8")
    match = OUTPUT_RE.search(page)
    if match is None:
        raise RuntimeError("response has no output panel")
    return html.unescape(match.group(1))


def check(base_url: str, example: dict) -> str | None:
    slug = example["slug"]
    try:
        actual = run_in_worker(base_url, slug, example["code"])
    except Exception as error:  # noqa: BLE001 - report every transport failure per page
        return f"{slug}: request failed: {error.__class__.__name__}: {error}"
    limit = example.get("sandbox_limit")
    if limit:
        if limit not in actual or "sandbox" not in actual:
            return f"{slug}: sandbox_limit page did not explain the limit ({limit!r}); got {actual[:200]!r}"
        return None
    if actual.rstrip("\n") != example["expected_output"].rstrip("\n"):
        return f"{slug}: sandbox output differs from expected_output\n  expected: {example['expected_output'][:300]!r}\n  actual:   {actual[:300]!r}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url", nargs="?", default="http://127.0.0.1:9696")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("slugs", nargs="*")
    args = parser.parse_args()
    _, examples = load_catalog()
    if args.slugs:
        examples = [example for example in examples if example["slug"] in set(args.slugs)]
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        failures = [failure for failure in pool.map(lambda example: check(args.base_url.rstrip("/"), example), examples) if failure]
    for failure in failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    if failures:
        return 1
    print(f"All {len(examples)} example programs ran in the sandbox and matched their expected output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
