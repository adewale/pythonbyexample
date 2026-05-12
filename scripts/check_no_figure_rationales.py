#!/usr/bin/env python3
"""Validate the no-figure rationale registry.

Some lessons are constraint-shaped or infrastructure-shaped and should not be
forced into weak diagrams. The registry lets those pages opt out explicitly
while preventing silent holes or stale entries.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"
sys.path.insert(0, str(ROOT))

from src.examples import EXAMPLES  # noqa: E402
from src.marginalia import ATTACHMENTS  # noqa: E402


def main() -> int:
    registry = tomllib.loads(REGISTRY_PATH.read_text())
    rationales = registry.get("no_figure_rationales", {})
    slugs = {example["slug"] for example in EXAMPLES}
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

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"No-figure rationale registry OK ({len(rationales)} entries).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
