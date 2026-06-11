#!/usr/bin/env python3
"""Validate that the quality registries reference real example slugs.

A typo in `docs/quality-registries.toml` would otherwise surface as a
confusing "page missing" error from one of the coverage checks. This
script runs first and fails fast with a clear message instead.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "src" / "example_sources"
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"
MANIFEST_PATH = EXAMPLES_DIR / "manifest.toml"


def _frontmatter_see_also(path: Path) -> set[str]:
    text = path.read_text()
    end = text.find("\n+++\n", 4)
    if not text.startswith("+++\n") or end < 0:
        return set()
    return set(tomllib.loads(text[4:end]).get("see_also", []))


def main() -> int:
    registries = tomllib.loads(REGISTRY_PATH.read_text())
    manifest = tomllib.loads(MANIFEST_PATH.read_text())
    known: set[str] = set(manifest.get("order", []))
    errors: list[str] = []

    for entry in registries.get("confusable_pairs", []):
        owner = entry.get("owner")
        if owner not in known:
            errors.append(
                f"confusable_pairs: {entry.get('name')!r} has unknown owner {owner!r}"
            )
        if not entry.get("tokens"):
            errors.append(
                f"confusable_pairs: {entry.get('name')!r} has no tokens"
            )

    for slug, spec in registries.get("broad_surface_tours", {}).items():
        if slug not in known:
            errors.append(f"broad_surface_tours: unknown slug {slug!r}")
        if not spec.get("required_tokens"):
            errors.append(f"broad_surface_tours: {slug!r} has no required_tokens")

    for entry in registries.get("footguns", []):
        owner = entry.get("owner")
        if owner not in known:
            errors.append(
                f"footguns: {entry.get('name')!r} has unknown owner {owner!r}"
            )
        if not entry.get("broken_tokens"):
            errors.append(f"footguns: {entry.get('name')!r} has no broken_tokens")
        if not entry.get("fixed_tokens"):
            errors.append(f"footguns: {entry.get('name')!r} has no fixed_tokens")

    for pair in registries.get("paired_pages", {}).get("pairs", []):
        for slug in pair:
            if slug not in known:
                errors.append(f"paired_pages: unknown slug {slug!r} in {pair}")
        # The registry's contract: at least one member of each pair must
        # demonstrate the relationship. The checkable form of that is
        # mutual discoverability — one member's see_also names the other.
        if all(slug in known for slug in pair):
            first, second = pair
            see_also = {
                slug: _frontmatter_see_also(EXAMPLES_DIR / f"{slug}.md") for slug in pair
            }
            if second not in see_also[first] and first not in see_also[second]:
                errors.append(
                    f"paired_pages: neither {first!r} nor {second!r} links the other "
                    f"via see_also, so the pair relationship is undiscoverable"
                )

    seen: set[tuple[str, str]] = set()
    for entry in registries.get("confusable_pairs", []):
        key = (entry.get("owner"), entry.get("name"))
        if key in seen:
            errors.append(f"confusable_pairs: duplicate entry {key}")
        seen.add(key)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    total = (
        len(registries.get("confusable_pairs", []))
        + len(registries.get("broad_surface_tours", {}))
        + len(registries.get("footguns", []))
    )
    print(f"Registry integrity OK ({total} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
