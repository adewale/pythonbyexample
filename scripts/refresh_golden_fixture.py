#!/usr/bin/env python3
"""Regenerate tests/fixtures/golden_examples.py from the current loader.

The fixture is a reviewed structural snapshot of the parsed catalog —
the teaching structure readers actually get. check_example_migration_parity.py
fails whenever loader output stops matching it, which catches pipeline
regressions: a loader or parser change that silently rewrites parsed
structure shows up as fixture drift across many files, while a content
edit shows up only for the file you touched.

Refreshes are deliberate: run this script in its own commit, review the
structural summary it prints, and keep content changes and fixture
refreshes in the same change so the diff explains itself.
"""
from __future__ import annotations

import importlib.util
import pprint
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import load_examples  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "golden_examples.py"

# The canonical snapshot fields. `walkthrough` (the pre-migration
# prose-grouping) is deliberately absent: the rendered teaching
# structure is `cells`, and snapshotting both would keep the legacy
# grouping alive for no reader-visible reason.
EXAMPLE_FIELDS = [
    "slug",
    "title",
    "section",
    "summary",
    "doc_path",
    "doc_url",
    "explanation",
    "notes",
    "see_also",
    "cells",
    "code",
    "expected_output",
]
CELL_FIELDS = ["kind", "prose", "code", "output"]

HEADER = '''"""Structural snapshot of the example catalog (generated).

Regenerate with scripts/refresh_golden_fixture.py after intentional
content changes; review the printed structural summary before
committing. check_example_migration_parity.py fails the build whenever
the loader's output stops matching this snapshot, so an accidental
loader/parser change cannot silently rewrite the teaching structure.
"""
'''


def snapshot_cell(cell: dict) -> dict:
    return {field: cell[field] for field in CELL_FIELDS}


def snapshot_example(example: dict) -> dict:
    row = {}
    for field in EXAMPLE_FIELDS:
        value = example[field]
        if field == "cells":
            value = [snapshot_cell(cell) for cell in value]
        row[field] = value
    return row


def load_previous() -> list[dict] | None:
    if not FIXTURE.exists():
        return None
    spec = importlib.util.spec_from_file_location("golden_examples_previous", FIXTURE)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.EXAMPLES


def structural_summary(previous: list[dict] | None, current: list[dict]) -> list[str]:
    if previous is None:
        return [f"new fixture: {len(current)} examples"]
    old_by_slug = {example["slug"]: example for example in previous}
    new_by_slug = {example["slug"]: example for example in current}
    lines: list[str] = []
    for slug in sorted(set(new_by_slug) - set(old_by_slug)):
        lines.append(f"added: {slug} ({len(new_by_slug[slug]['cells'])} cells)")
    for slug in sorted(set(old_by_slug) - set(new_by_slug)):
        lines.append(f"removed: {slug}")
    changed = 0
    for slug in sorted(set(old_by_slug) & set(new_by_slug)):
        old, new = old_by_slug[slug], new_by_slug[slug]
        fields = [
            field
            for field in EXAMPLE_FIELDS
            if field != "cells" and old.get(field) != new.get(field)
        ]
        old_cells = [snapshot_cell(c) for c in old.get("cells", [])]
        if old_cells != new["cells"]:
            fields.append(f"cells {len(old_cells)}→{len(new['cells'])}")
        if fields:
            changed += 1
            lines.append(f"changed: {slug}: {', '.join(fields)}")
    lines.append(
        f"summary: {len(current)} examples, {changed} changed, "
        f"{len(set(new_by_slug) - set(old_by_slug))} added, "
        f"{len(set(old_by_slug) - set(new_by_slug))} removed"
    )
    return lines


def main() -> int:
    catalog, examples = load_examples()
    previous = load_previous()
    rows = [snapshot_example(example) for example in examples]
    body = pprint.pformat(rows, width=100, sort_dicts=False)
    FIXTURE.write_text(
        HEADER
        + f"\nPYTHON_VERSION = {catalog.python_version!r}\n"
        + f"REFERENCE_URL = {catalog.docs_base_url + '/'!r}\n\n"
        + f"EXAMPLES = {body}\n"
    )
    for line in structural_summary(previous, rows):
        print(line)
    print(f"wrote {FIXTURE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
