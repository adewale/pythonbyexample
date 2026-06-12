#!/usr/bin/env python3
"""Validate the no-figure rationale registry.

Some lessons are constraint-shaped or infrastructure-shaped and should not be
forced into weak diagrams. The registry lets those pages opt out explicitly
while preventing silent holes or stale entries.
"""
from __future__ import annotations

import datetime
import sys

from _common import load_catalog, load_registry
from src.marginalia import ATTACHMENTS


def main() -> int:
    registry = load_registry()
    rationales = registry.get("no_figure_rationales", {})
    _catalog, examples = load_catalog()
    slugs = {example["slug"] for example in examples}
    errors: list[str] = []

    for slug, entry in sorted(rationales.items()):
        if slug not in slugs:
            errors.append(f"no-figure rationale for unknown example: {slug}")
            continue
        if slug in ATTACHMENTS:
            errors.append(f"{slug}: has both a no-figure rationale and production ATTACHMENTS")
        if not isinstance(entry, dict):
            errors.append(f"{slug}: rationale must be a table")
            continue
        reason = entry.get("reason")
        review_after = entry.get("review_after")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{slug}: missing no-figure reason")
        if not isinstance(review_after, str) or not review_after.strip():
            errors.append(f"{slug}: missing review_after")
        else:
            try:
                due = datetime.date.fromisoformat(review_after)
            except ValueError:
                errors.append(f"{slug}: review_after must be an ISO date, got {review_after!r}")
            else:
                if due <= datetime.date.today():
                    errors.append(
                        f"{slug}: review_after {review_after} has passed; "
                        f"re-review the no-figure decision and move the date or draw the figure"
                    )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"No-figure rationale registry OK ({len(rationales)} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
