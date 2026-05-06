#!/usr/bin/env python3
"""Temporary parity helper retained for future catalog migrations.

The app has switched to Markdown sources. This script now verifies that the
Markdown catalog loads and executes; old-catalog parity is only meaningful when
an old golden catalog file is supplied explicitly.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import load_examples  # noqa: E402


def run(code: str) -> str:
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exec(compile(code, "<parity>", "exec", dont_inherit=True), {"__name__": "__main__"})
    return stdout.getvalue()


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", "", text)


def load_module_examples(path: Path):
    spec = importlib.util.spec_from_file_location("golden_examples", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module.EXAMPLES


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--golden", type=Path, help="Old Python catalog to compare against")
    args = parser.parse_args()
    _, markdown = load_examples()
    if args.golden is None:
        for example in markdown:
            actual = run(example["code"])
            if actual != example["expected_output"]:
                print(f"{example['slug']}: output mismatch", file=sys.stderr)
                return 1
        print(f"Loaded and executed {len(markdown)} Markdown example(s). No golden catalog supplied.")
        return 0

    golden = load_module_examples(args.golden)
    errors: list[str] = []
    rows: list[str] = []
    if [e["slug"] for e in golden] != [e["slug"] for e in markdown]:
        errors.append("example order differs")
    for old, new in zip(golden, markdown):
        slug = old["slug"]
        for field in ["slug", "title", "section", "summary", "doc_url", "expected_output", "notes"]:
            if old.get(field) != new.get(field):
                errors.append(f"{slug}: field differs: {field}")
        old_out = run(old["code"])
        new_out = run(new["code"])
        if old_out != new_out:
            errors.append(f"{slug}: stdout differs")
        if old["code"] == new["code"]:
            code_status = "identical"
        elif normalize_ws(old["code"]) == normalize_ws(new["code"]):
            code_status = "whitespace-only"
        else:
            code_status = "semantic-same-output" if old_out == new_out else "semantic"
            if old_out != new_out:
                errors.append(f"{slug}: semantic code difference")
        rows.append(f"{slug}: {code_status}")
    print("\n".join(rows))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
