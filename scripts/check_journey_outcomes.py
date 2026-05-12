#!/usr/bin/env python3
"""Check that journey sections have explicit learner outcomes.

Journey order is supposed to follow prerequisite thinking, not catalog order.
This registry makes each section state what it wants the learner to be able to
explain, and ties those outcomes back to examples in that section.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"
sys.path.insert(0, str(ROOT))

from src.app import JOURNEYS  # noqa: E402
from src.examples import EXAMPLES  # noqa: E402


def main() -> int:
    registry = tomllib.loads(REGISTRY_PATH.read_text())
    outcomes = registry.get("journey_outcomes", {})
    example_slugs = {example["slug"] for example in EXAMPLES}
    expected: dict[str, tuple[str, str, set[str]]] = {}
    errors: list[str] = []

    for journey in JOURNEYS:
        for section in journey["sections"]:
            key = f'{journey["slug"]}::{section["title"]}'
            support = {item[1] for item in section["items"] if item[0] == "example"}
            expected[key] = (journey["slug"], section["title"], support)

    missing = set(expected) - set(outcomes)
    extra = set(outcomes) - set(expected)
    if missing:
        errors.append(f"missing journey outcomes: {sorted(missing)}")
    if extra:
        errors.append(f"outcomes for unknown journey sections: {sorted(extra)}")

    for key, entry in sorted(outcomes.items()):
        if key not in expected:
            continue
        journey_slug, section_title, section_slugs = expected[key]
        if entry.get("journey") != journey_slug:
            errors.append(f"{key}: journey mismatch {entry.get('journey')!r} != {journey_slug!r}")
        if entry.get("section") != section_title:
            errors.append(f"{key}: section mismatch {entry.get('section')!r} != {section_title!r}")
        support = entry.get("support", [])
        section_outcomes = entry.get("outcomes", [])
        if not isinstance(support, list) or not support:
            errors.append(f"{key}: support must list examples in the section")
            support = []
        if not isinstance(section_outcomes, list) or len(section_outcomes) < 2:
            errors.append(f"{key}: outcomes must list at least two learner outcomes")
            section_outcomes = []
        unknown_support = set(support) - example_slugs
        outside_section = set(support) - section_slugs
        if unknown_support:
            errors.append(f"{key}: support references unknown examples {sorted(unknown_support)}")
        if outside_section:
            errors.append(f"{key}: support examples are not in the section {sorted(outside_section)}")
        for outcome in section_outcomes:
            if not isinstance(outcome, str) or len(outcome.strip()) < 12:
                errors.append(f"{key}: weak outcome {outcome!r}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Journey outcomes OK ({len(outcomes)} sections).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
