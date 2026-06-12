#!/usr/bin/env python3
"""Validate that the quality registries reference real example slugs.

A typo in `docs/quality-registries.toml` would otherwise surface as a
confusing "page missing" error from one of the coverage checks. This
script runs first and fails fast with a clear message instead.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _common import EXAMPLES_DIR, frontmatter, load_catalog, load_registry

CELL_BLOCK_RE = re.compile(r":::(?:cell|unsupported)\n(.*?)\n:::", re.S)


def _frontmatter_see_also(path: Path) -> set[str]:
    return set(frontmatter(path).get("see_also", []))


def _cell_text(path: Path) -> str:
    return "\n\n".join(match.group(1) for match in CELL_BLOCK_RE.finditer(path.read_text()))


def _pair_key(first: str, second: str) -> str:
    return f"{first}|{second}"


def main() -> int:
    registries = load_registry()
    catalog, _examples = load_catalog()
    known: set[str] = set(catalog.order)
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

    paired_pages = registries.get("paired_pages", {})
    cell_tokens_by_pair = paired_pages.get("cell_tokens", {})
    for pair in paired_pages.get("pairs", []):
        if len(pair) != 2:
            errors.append(f"paired_pages: expected two slugs, got {pair!r}")
            continue
        for slug in pair:
            if slug not in known:
                errors.append(f"paired_pages: unknown slug {slug!r} in {pair}")
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
            tokens = cell_tokens_by_pair.get(_pair_key(first, second)) or cell_tokens_by_pair.get(
                _pair_key(second, first)
            )
            if not tokens:
                errors.append(
                    f"paired_pages: {pair!r} needs cell_tokens proving the relationship "
                    "inside at least one teaching cell"
                )
                continue
            page_cell_text = {
                slug: _cell_text(EXAMPLES_DIR / f"{slug}.md").lower() for slug in pair
            }
            lowered_tokens = [token.lower() for token in tokens]
            if not any(
                all(token in text for token in lowered_tokens)
                for text in page_cell_text.values()
            ):
                errors.append(
                    f"paired_pages: {pair!r} cell_tokens {tokens!r} do not all appear "
                    "inside a cell on either paired page"
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
