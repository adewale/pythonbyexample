#!/usr/bin/env python3
"""Normalize Markdown example source files without changing prose or code."""
from __future__ import annotations

import argparse
import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "example_sources"
FRONTMATTER_ORDER = ["slug", "title", "section", "summary", "doc_path", "see_also", "min_python", "version_sensitive", "version_notes"]


def toml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
    if isinstance(value, list):
        if all(isinstance(item, str) for item in value):
            if len(value) == 0:
                return "[]"
            inner = "\n".join(f"  {toml_value(item)}," for item in value)
            return "[\n" + inner + "\n]"
    raise TypeError(f"Unsupported TOML value: {value!r}")


def ordered_keys(data: dict[str, Any]) -> list[str]:
    known = [key for key in FRONTMATTER_ORDER if key in data]
    unknown = sorted(key for key in data if key not in FRONTMATTER_ORDER)
    return known + unknown


def dump_toml(data: dict[str, Any]) -> str:
    return "\n".join(f"{key} = {toml_value(data[key])}" for key in ordered_keys(data)) + "\n"


def normalize_body(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    out: list[str] = []
    blank = False
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            if line == "```py":
                line = "```python"
            in_fence = not in_fence
        if not in_fence and line == "":
            if blank:
                continue
            blank = True
        else:
            blank = False
        out.append(line)
    return "\n".join(out).strip()


def split_frontmatter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("+++\n"):
        raise ValueError(f"{path}: expected +++ frontmatter")
    marker = "\n+++\n"
    end = normalized.find(marker, 4)
    if end < 0:
        raise ValueError(f"{path}: missing closing +++")
    frontmatter = tomllib.loads(normalized[4:end])
    return frontmatter, normalized[end + len(marker) :]


def format_markdown(path: Path) -> str:
    frontmatter, body = split_frontmatter(path.read_text(), path)
    return "+++\n" + dump_toml(frontmatter) + "+++\n\n" + normalize_body(body) + "\n"


def format_manifest(path: Path) -> str:
    data = tomllib.loads(path.read_text())
    sections = [
        f"python_version = {toml_value(data['python_version'])}",
        f"docs_base_url = {toml_value(data['docs_base_url'])}",
        "",
        f"order = {toml_value(data['order'])}",
    ]
    return "\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed: list[Path] = []
    paths = [SOURCE_DIR / "manifest.toml", *sorted(SOURCE_DIR.glob("*.md"))]
    for path in paths:
        original = path.read_text()
        formatted = format_manifest(path) if path.name == "manifest.toml" else format_markdown(path)
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
