#!/usr/bin/env python3
"""Check rubric score registries and tracked quality debt.

The score dictionaries are curated editorial data. This check does not
pretend to grade prose automatically; it makes the gate explicit:
examples below the hard minimum must either have a narrow waiver or be
tracked in the improvement backlog with a concrete next action.

Waivers are time-boxed: `expires` must be an ISO date in the future,
and a waiver whose example has recovered to target is flagged as stale
so the registry only ever describes live editorial debt.

A waiver that expires within WAIVER_WARNING_DAYS prints a warning. The
weekly scheduled workflow runs `--fail-within-days 30`, so an approaching
expiry turns that run red a month before it would fail every pull request.
"""
from __future__ import annotations

import argparse
import datetime
import sys

from _common import load_catalog, load_registry
from src.marginalia import EXAMPLE_QUALITY_SCORES, SECTION_FIGURE_SCORES


def _entry_has_text(entry: dict, *keys: str) -> bool:
    return all(isinstance(entry.get(key), str) and bool(entry[key].strip()) for key in keys)


WAIVER_WARNING_DAYS = 30


def check_expiry_date(value, *, today: datetime.date | None = None) -> str | None:
    """Return an error string when `value` is not a future ISO date."""
    today = today or datetime.datetime.now(datetime.UTC).date()
    if not isinstance(value, str):
        return f"expires must be an ISO date string, got {value!r}"
    try:
        expires = datetime.date.fromisoformat(value)
    except ValueError:
        return f"expires must be an ISO date (YYYY-MM-DD), got {value!r}"
    if expires <= today:
        return f"expired on {value}; re-review and extend or fix the example"
    return None


def expiry_warning(
    value, *, today: datetime.date | None = None, within_days: int = WAIVER_WARNING_DAYS
) -> str | None:
    """Return a warning when a still-valid waiver expires within `within_days`."""
    today = today or datetime.datetime.now(datetime.UTC).date()
    if check_expiry_date(value, today=today) is not None:
        return None  # invalid or already expired: check_expiry_date reports it
    days_left = (datetime.date.fromisoformat(value) - today).days
    if days_left > within_days:
        return None
    return f"expires on {value} ({days_left} days left); re-review and extend or fix the example"


def waiver_expiry_findings(
    waivers: dict, *, today: datetime.date, fail_within_days: int | None = None
) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for waiver expiry dates.

    Expired or malformed dates are errors. Dates inside the warning window
    are warnings, or errors when `fail_within_days` is set.
    """
    errors: list[str] = []
    warnings: list[str] = []
    window = WAIVER_WARNING_DAYS if fail_within_days is None else fail_within_days
    for slug in sorted(waivers):
        expires = waivers[slug].get("expires")
        if expiry_error := check_expiry_date(expires, today=today):
            errors.append(f"quality waiver {slug}: {expiry_error}")
        elif warning := expiry_warning(expires, today=today, within_days=window):
            (warnings if fail_within_days is None else errors).append(f"quality waiver {slug}: {warning}")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "--fail-within-days",
        type=int,
        default=None,
        help="treat waivers expiring within N days as errors (the scheduled run uses 30)",
    )
    parser.add_argument("--as-of", help="evaluate expiry as of this ISO date instead of today (UTC)")
    args = parser.parse_args(argv)
    today = (
        datetime.date.fromisoformat(args.as_of)
        if args.as_of
        else datetime.datetime.now(datetime.UTC).date()
    )

    registry = load_registry()
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

    _catalog, examples = load_catalog()
    slugs = {example["slug"] for example in examples}
    waivers = registry.get("quality_waivers", {})
    backlog = registry.get("quality_improvement_backlog", {})
    section_backlog = registry.get("journey_section_improvement_backlog", {})
    errors: list[str] = []
    expiry_errors, warnings = waiver_expiry_findings(
        {slug: entry for slug, entry in waivers.items() if slug in slugs},
        today=today,
        fail_within_days=args.fail_within_days,
    )
    errors.extend(expiry_errors)

    missing_scores = slugs - set(EXAMPLE_QUALITY_SCORES)
    ghost_scores = set(EXAMPLE_QUALITY_SCORES) - slugs
    if missing_scores:
        errors.append(f"missing example quality scores: {sorted(missing_scores)}")
    if ghost_scores:
        errors.append(f"quality scores for unknown examples: {sorted(ghost_scores)}")

    for label, registry_scores in (
        ("example", EXAMPLE_QUALITY_SCORES),
        ("journey section", SECTION_FIGURE_SCORES),
    ):
        for key, entry in registry_scores.items():
            if not isinstance(entry, tuple) or len(entry) != 2:
                errors.append(f"{label} score {key}: not a (score, commentary) tuple")
                continue
            score, commentary = entry
            if not isinstance(score, (int, float)) or not 0 <= score <= 10:
                errors.append(f"{label} score {key}: {score!r} outside the rubric's [0, 10]")
            if not isinstance(commentary, str) or not commentary.strip():
                errors.append(f"{label} score {key}: empty commentary")

    for slug in sorted(waivers):
        if slug not in slugs:
            errors.append(f"quality waiver for unknown example: {slug}")
            continue
        entry = waivers[slug]
        if not _entry_has_text(entry, "reason") or not isinstance(entry.get("accepted_min"), (int, float)):
            errors.append(f"quality waiver {slug} must include accepted_min, reason, and expires")
        waived_score = EXAMPLE_QUALITY_SCORES.get(slug, (0.0, ""))[0]
        if waived_score >= target:
            errors.append(f"quality waiver {slug} is stale because score is now {waived_score:.1f}")

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
        score = SECTION_FIGURE_SCORES[title][0]
        if score >= section_min:
            errors.append(f"journey section backlog {title} is stale because score is now {score:.1f}")
        if not _entry_has_text(section_backlog[title], "cause", "next_action"):
            errors.append(f"journey section backlog {title} must include cause and next_action")

    weak_sections = [title for title, (score, _comment) in SECTION_FIGURE_SCORES.items() if score < section_min]
    if weak_sections:
        for title in weak_sections:
            if title not in section_backlog:
                errors.append(f"journey section figure below {section_min:.1f}: {title}")

    journey_average_min = gates.get("journey_average_min")
    if journey_average_min is not None and SECTION_FIGURE_SCORES:
        average = sum(score for score, _ in SECTION_FIGURE_SCORES.values()) / len(SECTION_FIGURE_SCORES)
        if average < float(journey_average_min):
            errors.append(
                f"journey section figure average {average:.2f} below "
                f"journey_average_min {float(journey_average_min):.1f}"
            )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
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
