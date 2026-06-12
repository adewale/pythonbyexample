#!/usr/bin/env python3
"""Verify the loader's parsed catalog against the reviewed snapshot.

tests/fixtures/golden_examples.py is a structural snapshot of the
teaching structure readers get: every example's metadata, program,
expected output, and cell sequence (prose, code, output, kind). This
gate fails whenever the live loader's output stops matching it.

What that buys: an accidental loader/parser/renderer change cannot
silently rewrite the parsed structure — it surfaces here as drift
across many examples, while a deliberate content edit surfaces only for
the files actually touched. Refreshes are explicit and reviewed:
scripts/refresh_golden_fixture.py regenerates the snapshot and prints a
structural summary; commit it alongside the content change it reflects.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import load_examples  # noqa: E402
from scripts.refresh_golden_fixture import (  # noqa: E402
    EXAMPLE_FIELDS,
    snapshot_example,
)

GOLDEN = ROOT / "tests" / "fixtures" / "golden_examples.py"


def load_golden():
    spec = importlib.util.spec_from_file_location("golden_examples", GOLDEN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {GOLDEN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.EXAMPLES


def main() -> int:
    golden = load_golden()
    _, examples = load_examples()
    current = [snapshot_example(example) for example in examples]
    errors: list[str] = []
    if [row["slug"] for row in golden] != [row["slug"] for row in current]:
        errors.append("example order differs from the snapshot")
    by_slug = {row["slug"]: row for row in golden}
    for row in current:
        slug = row["slug"]
        old = by_slug.get(slug)
        if old is None:
            errors.append(f"{slug}: not in the snapshot")
            continue
        for field in EXAMPLE_FIELDS:
            if old.get(field) != row[field]:
                errors.append(f"{slug}: field differs from snapshot: {field}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(
            "If these differences are intentional content edits, regenerate the "
            "snapshot with scripts/refresh_golden_fixture.py and review its summary. "
            "If you changed the loader or parser, the drift above is the regression.",
            file=sys.stderr,
        )
        return 1
    print(f"{len(current)} examples match the structural snapshot")
    print("100% golden parity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
