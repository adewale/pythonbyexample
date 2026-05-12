#!/usr/bin/env python3
"""Check rubric score registries and tracked quality debt.

The score dictionaries are curated editorial data. This check does not
pretend to grade prose automatically; it makes the gate explicit:
examples below the hard minimum must either have a narrow waiver or be
tracked in the improvement backlog with a concrete next action.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"
sys.path.insert(0, str(ROOT))

from src.examples import EXAMPLES  # noqa: E402
from src.marginalia import EXAMPLE_QUALITY_SCORES, SECTION_FIGURE_SCORES  # noqa: E402


def _load_registry() -> dict:
    return tomllib.loads(REGISTRY_PATH.read_text())


def _entry_has_text(entry: dict, *keys: str) -> bool:
    return all(isinstance(entry.get(key), str) and bool(entry[key].strip()) for key in keys)


def main() -> int:
    registry = _load_registry()
    gates = registry.get("quality_gates", {})
    target = float(gates.get("example_target", 9.0))
    hard_min = float(gates.get("example_hard_min", 8.5))
    section_min = float(gates.get("journey_section_min", 8.5))

    score_model = registry.get("score_model", {})
    model_total = sum(value for value in score_model.values() if isinstance(value, (int, float)))
    if round(model_total, 2) != 10.0:
        errors = [f"score_model weights must sum to 10.0, got {model_total:.2f}"]
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    slugs = {example["slug"] for example in EXAMPLES}
    waivers = registry.get("quality_waivers", {})
    backlog = registry.get("quality_improvement_backlog", {})
    section_backlog = registry.get("journey_section_improvement_backlog", {})
    errors: list[str] = []

    missing_scores = slugs - set(EXAMPLE_QUALITY_SCORES)
    ghost_scores = set(EXAMPLE_QUALITY_SCORES) - slugs
    if missing_scores:
        errors.append(f"missing example quality scores: {sorted(missing_scores)}")
    if ghost_scores:
        errors.append(f"quality scores for unknown examples: {sorted(ghost_scores)}")

    for slug in sorted(waivers):
        if slug not in slugs:
            errors.append(f"quality waiver for unknown example: {slug}")
            continue
        entry = waivers[slug]
        if not _entry_has_text(entry, "reason", "expires") or not isinstance(entry.get("accepted_min"), (int, float)):
            errors.append(f"quality waiver {slug} must include accepted_min, reason, and expires")

    for slug in sorted(backlog):
        if slug not in slugs:
            errors.append(f"quality backlog entry for unknown example: {slug}")
            continue
        if slug in waivers:
            errors.append(f"{slug} cannot be both waiver and improvement backlog")
        score = EXAMPLE_QUALITY_SCORES.get(slug, (0.0, ""))[0]
        if score >= hard_min:
            errors.append(f"quality backlog {slug} is stale because score is now {score:.1f}")
        if not _entry_has_text(backlog[slug], "cause", "next_action"):
            errors.append(f"quality backlog {slug} must include cause and next_action")

    below_target: list[str] = []
    below_hard_min: list[str] = []
    for slug, (score, _comment) in sorted(EXAMPLE_QUALITY_SCORES.items()):
        if score < target:
            below_target.append(slug)
            if slug in waivers:
                accepted = float(waivers[slug].get("accepted_min", hard_min))
                if score < accepted:
                    errors.append(f"{slug}: score {score:.1f} below waiver floor {accepted:.1f}")
            elif score < hard_min:
                if slug in backlog:
                    below_hard_min.append(slug)
                else:
                    errors.append(f"{slug}: score {score:.1f} below hard minimum {hard_min:.1f} without backlog entry")
            else:
                errors.append(f"{slug}: score {score:.1f} below target {target:.1f} without waiver")

    for title in sorted(section_backlog):
        if title not in SECTION_FIGURE_SCORES:
            errors.append(f"journey section backlog for unknown section: {title}")
            continue
        if not _entry_has_text(section_backlog[title], "cause", "next_action"):
            errors.append(f"journey section backlog {title} must include cause and next_action")

    weak_sections = [title for title, (score, _comment) in SECTION_FIGURE_SCORES.items() if score < section_min]
    if weak_sections:
        for title in weak_sections:
            if title not in section_backlog:
                errors.append(f"journey section figure below {section_min:.1f}: {title}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(
        "Quality score gate OK "
        f"(target={target:.1f}, hard_min={hard_min:.1f}, "
        f"below_target={len(below_target)}, tracked_below_min={len(below_hard_min)}, "
        f"tracked_weak_sections={len(weak_sections)}, waivers={len(waivers)})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
