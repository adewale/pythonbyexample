#!/usr/bin/env python3
"""Verify that each broad-surface tour page covers its required tokens.

Reads `docs/quality-registries.toml`. A page may opt out of the strict
check by adding `scope_first_pass = true` to its frontmatter, in which
case it must instead carry `see_also` links pointing at focused
neighbors that the registry expects to exist.
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"


FRONTMATTER_RE = re.compile(r"^\+\+\+\n(.*?)\n\+\+\+\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    return tomllib.loads(match.group(1))


def main() -> int:
    data = tomllib.loads(REGISTRY_PATH.read_text())
    tours = data.get("broad_surface_tours", {})
    errors: list[str] = []
    for slug, spec in tours.items():
        page = EXAMPLES_DIR / f"{slug}.md"
        if not page.exists():
            errors.append(f"{REGISTRY_PATH}: broad-tour page missing: {slug}.md")
            continue
        text = page.read_text()
        frontmatter = parse_frontmatter(text)
        required = spec.get("required_tokens", [])
        missing = [token for token in required if token not in text]
        if frontmatter.get("scope_first_pass"):
            see_also = frontmatter.get("see_also") or []
            if not see_also:
                errors.append(
                    f"{page}: scope_first_pass=true requires see_also links to focused neighbors"
                )
            continue
        if missing:
            errors.append(
                f"{page}: broad-tour {slug!r} missing tokens: {missing}; "
                "either add cells covering them or set scope_first_pass=true with see_also"
            )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Broad-surface tour coverage OK ({len(tours)} pages).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
