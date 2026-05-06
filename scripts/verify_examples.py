#!/usr/bin/env python3
"""Verify Markdown example source files using the website loader."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import EXAMPLES_DIR, load_examples, verify_example_output  # noqa: E402
from src.example_sources_data import EXAMPLE_SOURCE_FILES  # noqa: E402


def version_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slugs", nargs="*", help="Optional example slugs to verify")
    parser.add_argument("--python-version", help="Expected manifest Python version")
    args = parser.parse_args()

    catalog, examples = load_examples()
    selected = set(args.slugs)
    errors: list[str] = []

    if args.python_version and catalog.python_version != args.python_version:
        errors.append(f"manifest python_version is {catalog.python_version!r}, expected {args.python_version!r}")
    expected_docs_base = f"https://docs.python.org/{catalog.python_version}"
    if catalog.docs_base_url != expected_docs_base:
        errors.append(f"docs_base_url must be {expected_docs_base!r}, got {catalog.docs_base_url!r}")

    for source_path in [EXAMPLES_DIR / "manifest.toml", *sorted(EXAMPLES_DIR.glob("*.md"))]:
        if EXAMPLE_SOURCE_FILES.get(source_path.name) != source_path.read_text():
            errors.append(f"{source_path}: embedded source is stale; run scripts/embed_example_sources.py")

    md_paths = sorted(path for path in EXAMPLES_DIR.glob("*.md"))
    manifest_slugs = set(catalog.order)
    file_slugs = {path.stem for path in md_paths}
    if manifest_slugs != file_slugs:
        errors.append(f"manifest/file slug mismatch: missing={sorted(file_slugs - manifest_slugs)}, extra={sorted(manifest_slugs - file_slugs)}")
    if len(catalog.order) != len(manifest_slugs):
        errors.append("manifest contains duplicate slugs")

    titles: set[str] = set()
    version_sensitive: list[str] = []
    hardcoded_docs_pattern = re.compile(r"docs\.python\.org/3\.\d+")

    for example in examples:
        slug = example["slug"]
        if selected and slug not in selected:
            continue
        path = EXAMPLES_DIR / f"{slug}.md"
        text = path.read_text()
        if slug != path.stem:
            errors.append(f"{path}: slug must match filename")
        if hardcoded_docs_pattern.search(text):
            errors.append(f"{path}: use doc_path instead of hardcoded docs.python.org/3.x URLs")
        if not example["doc_path"].startswith("/"):
            errors.append(f"{path}: doc_path must start with /")
        if not example["doc_url"].startswith(catalog.docs_base_url + "/"):
            errors.append(f"{path}: generated doc_url has wrong docs base")
        if not example["summary"].strip():
            errors.append(f"{path}: summary is required")
        if example["title"] in titles:
            errors.append(f"{path}: duplicate title {example['title']!r}")
        titles.add(example["title"])
        if example.get("min_python") and version_tuple(example["min_python"]) > version_tuple(catalog.python_version):
            errors.append(f"{path}: min_python exceeds manifest python_version")
        if example.get("version_sensitive"):
            version_sensitive.append(slug)
            if not example.get("version_notes"):
                errors.append(f"{path}: version_sensitive examples require version_notes")
        for index, cell in enumerate(example["cells"], 1):
            if not cell["prose"]:
                errors.append(f"{path}: cell {index} prose is required")
            if not cell["code"].strip():
                errors.append(f"{path}: cell {index} source is required")
        errors.extend(verify_example_output(example))

    unknown = selected - manifest_slugs
    if unknown:
        errors.append(f"unknown slugs: {sorted(unknown)}")

    if version_sensitive:
        print("Version-sensitive examples:", ", ".join(version_sensitive))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Verified {len([e for e in examples if not selected or e['slug'] in selected])} example(s) for Python {catalog.python_version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
