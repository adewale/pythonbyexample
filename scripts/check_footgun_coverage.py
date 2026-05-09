#!/usr/bin/env python3
"""Verify each canonical Python footgun has a page that shows broken+fixed.

Reads `docs/quality-registries.toml`. The owning page must contain at
least one token from each of `broken_tokens` and `fixed_tokens`. Token
matching is permissive on purpose: this gate checks that the lesson is
present, not that it is phrased in any particular way.
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
    footguns = data.get("footguns", [])
    errors: list[str] = []
    for entry in footguns:
        name = entry["name"]
        owner = entry["owner"]
        broken = entry.get("broken_tokens", [])
        fixed = entry.get("fixed_tokens", [])
        page = EXAMPLES_DIR / f"{owner}.md"
        if not page.exists():
            errors.append(f"{REGISTRY_PATH}: footgun owner page missing: {owner}.md")
            continue
        text = page.read_text()
        if not any(token in text for token in broken):
            errors.append(
                f"{page}: footgun {name!r} missing broken-form token; "
                f"expected one of {broken}"
            )
        if not any(token in text for token in fixed):
            errors.append(
                f"{page}: footgun {name!r} missing fixed-form token; "
                f"expected one of {fixed}"
            )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Footgun coverage OK ({len(footguns)} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
