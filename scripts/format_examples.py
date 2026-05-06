#!/usr/bin/env python3
"""Normalize Markdown example source files."""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "example_sources"


def normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    out: list[str] = []
    blank = False
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and line == "":
            if blank:
                continue
            blank = True
        else:
            blank = False
        out.append(line)
    return "\n".join(out).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed: list[Path] = []
    for path in [SOURCE_DIR / "manifest.toml", *sorted(SOURCE_DIR.glob("*.md"))]:
        original = path.read_text()
        formatted = normalize_text(original)
        if formatted != original:
            changed.append(path)
            if not args.check:
                path.write_text(formatted)
    if changed:
        for path in changed:
            print(path)
        return 1 if args.check else 0
    print("Example sources already formatted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
