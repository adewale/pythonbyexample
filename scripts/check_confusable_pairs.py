#!/usr/bin/env python3
"""Verify that each confusable pair appears on its owning page.

Reads `docs/quality-registries.toml` and fails if the owning page's
source text is missing any token from the pair.

Matching defends against substring shadowing: before checking a token,
every LONGER sibling token in the same entry is stripped from the text,
so "def " cannot be satisfied by the "async def" that another token
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


def missing_tokens(text: str, tokens: list[str]) -> list[str]:
    missing = []
    for token in tokens:
        longer_siblings = [other for other in tokens if other != token and token in other]
        stripped = text
        for sibling in longer_siblings:
            stripped = stripped.replace(sibling, "")
        if token not in stripped:
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
