#!/usr/bin/env python3
"""Verify that each confusable pair appears on its owning page.

Reads `docs/quality-registries.toml` and fails if the owning page's
source text is missing any token from the pair.

Matching defends against substring shadowing: a token occurrence that
sits inside a longer sibling token's occurrence does not count, so
"def " cannot be satisfied by the "async def " that another token
already requires — the page must contain a plain function definition of
its own. Entries may also supply `patterns` (regular expressions) when
substring tokens are not precise enough.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"


def _spans(text: str, token: str) -> list[tuple[int, int]]:
    spans = []
    start = 0
    while (found := text.find(token, start)) != -1:
        spans.append((found, found + len(token)))
        start = found + 1
    return spans


def missing_tokens(text: str, tokens: list[str]) -> list[str]:
    missing = []
    for token in tokens:
        shadow_spans = [
            span
            for other in tokens
            if other != token and len(other) > len(token)
            for span in _spans(text, other)
        ]
        unshadowed = [
            (start, end)
            for start, end in _spans(text, token)
            if not any(start < o_end and o_start < end for o_start, o_end in shadow_spans)
        ]
        if not unshadowed:
            missing.append(token)
    return missing


def main() -> int:
    data = tomllib.loads(REGISTRY_PATH.read_text())
    pairs = data.get("confusable_pairs", [])
    errors: list[str] = []
    for entry in pairs:
        name = entry["name"]
        owner = entry["owner"]
        page = EXAMPLES_DIR / f"{owner}.md"
        if not page.exists():
            errors.append(f"{REGISTRY_PATH}: owner page missing for {name!r}: {owner}.md")
            continue
        text = page.read_text()
        missing = missing_tokens(text, entry.get("tokens", []))
        if missing:
            errors.append(f"{page}: confusable pair {name!r} missing tokens: {missing}")
        for pattern in entry.get("patterns", []):
            if not re.search(pattern, text):
                errors.append(f"{page}: confusable pair {name!r} missing pattern: {pattern!r}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Confusable-pair coverage OK ({len(pairs)} pairs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
