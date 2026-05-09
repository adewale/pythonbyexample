#!/usr/bin/env python3
"""Verify that each confusable pair appears on its owning page.

Reads `docs/quality-registries.toml` and fails if the owning page's source
text is missing any token from the pair. Tokens are matched as substrings,
so they should be specific enough to avoid false positives.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"


def main() -> int:
    data = tomllib.loads(REGISTRY_PATH.read_text())
    pairs = data.get("confusable_pairs", [])
    errors: list[str] = []
    for entry in pairs:
        name = entry["name"]
        owner = entry["owner"]
        tokens = entry["tokens"]
        page = EXAMPLES_DIR / f"{owner}.md"
        if not page.exists():
            errors.append(f"{REGISTRY_PATH}: owner page missing for {name!r}: {owner}.md")
            continue
        text = page.read_text()
        missing = [token for token in tokens if token not in text]
        if missing:
            errors.append(f"{page}: confusable pair {name!r} missing tokens: {missing}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Confusable-pair coverage OK ({len(pairs)} pairs).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
