#!/usr/bin/env python3
"""Verify Markdown examples against the frozen golden catalog."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import load_examples  # noqa: E402

GOLDEN = ROOT / "tests" / "fixtures" / "golden_examples.py"


def run(code: str) -> str:
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exec(compile(code, "<parity>", "exec", dont_inherit=True), {"__name__": "__main__"})
    return stdout.getvalue()


def load_golden():
    spec = importlib.util.spec_from_file_location("golden_examples", GOLDEN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {GOLDEN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.EXAMPLES


def comparable_cells(example: dict) -> list[tuple[tuple[str, ...], str, str]]:
    # Import lazily so this script compares against the same rendering grouping
    # that the website used before the Markdown switch.
    from src.app import _walkthrough_cells  # noqa: PLC0415

    return [(tuple(cell["prose"]), cell["code"], cell["output"]) for cell in _walkthrough_cells(example)]


def markdown_cells(example: dict) -> list[tuple[tuple[str, ...], str, str]]:
    return [(tuple(cell["prose"]), cell["code"], cell["output"]) for cell in example["cells"]]


def main() -> int:
    golden = load_golden()
    _, markdown = load_examples()
    errors: list[str] = []
    rows: list[str] = []
    if [e["slug"] for e in golden] != [e["slug"] for e in markdown]:
        errors.append("example order differs")
    for old, new in zip(golden, markdown):
        slug = old["slug"]
        for field in ["slug", "title", "section", "summary", "doc_url", "code", "expected_output", "notes"]:
            if old.get(field) != new.get(field):
                errors.append(f"{slug}: field differs: {field}")
        if run(old["code"]) != run(new["code"]):
            errors.append(f"{slug}: stdout differs")
        old_cells = comparable_cells(old)
        new_cells = markdown_cells(new)
        if old_cells != new_cells:
            errors.append(f"{slug}: teaching-structure difference")
        rows.append(f"{slug}: cells={len(new_cells)}")
    print("\n".join(rows))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("100% golden parity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
