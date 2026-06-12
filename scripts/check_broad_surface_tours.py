#!/usr/bin/env python3
"""Verify that each broad-surface tour page covers its required tokens.

Reads `docs/quality-registries.toml`. A page may opt out of the strict
check by adding `scope_first_pass = true` to its frontmatter, in which
case the registry must name `focused_neighbors` and the page must link to
all of them via `see_also`.
"""
from __future__ import annotations

import sys
from pathlib import Path

from _common import EXAMPLES_DIR, REGISTRY_PATH, frontmatter, load_registry


def scope_first_pass_errors(page: Path, see_also: list[str], focused_neighbors: list[str]) -> list[str]:
    errors: list[str] = []
    if not focused_neighbors:
        errors.append(
            f"{page}: scope_first_pass=true requires focused_neighbors in broad_surface_tours"
        )
        return errors
    missing = [slug for slug in focused_neighbors if slug not in see_also]
    if missing:
        errors.append(
            f"{page}: scope_first_pass=true missing focused see_also neighbors: {missing}"
        )
    return errors


def main() -> int:
    data = load_registry()
    tours = data.get("broad_surface_tours", {})
    errors: list[str] = []
    for slug, spec in tours.items():
        page = EXAMPLES_DIR / f"{slug}.md"
        if not page.exists():
            errors.append(f"{REGISTRY_PATH}: broad-tour page missing: {slug}.md")
            continue
        text = page.read_text()
        page_frontmatter = frontmatter(page)
        required = spec.get("required_tokens", [])
        missing = [token for token in required if token not in text]
        if page_frontmatter.get("scope_first_pass"):
            errors.extend(
                scope_first_pass_errors(
                    page,
                    page_frontmatter.get("see_also") or [],
                    spec.get("focused_neighbors") or [],
                )
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
