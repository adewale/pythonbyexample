#!/usr/bin/env python3
"""Verify Markdown examples using the canonical website loader."""
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
    parser.add_argument("slugs", nargs="*")
    parser.add_argument("--python-version")
    args = parser.parse_args()
    selected = set(args.slugs)
    errors: list[str] = []
    catalog, examples = load_examples()

    if args.python_version and catalog.python_version != args.python_version:
        errors.append(f"src/example_sources/manifest.toml:1: python_version is {catalog.python_version!r}, expected {args.python_version!r}")
    expected_base = f"https://docs.python.org/{catalog.python_version}"
    if catalog.docs_base_url != expected_base:
        errors.append(f"src/example_sources/manifest.toml:2: docs_base_url must be {expected_base!r}")

    for path in [EXAMPLES_DIR / "manifest.toml", *sorted(EXAMPLES_DIR.glob("*.md"))]:
        if EXAMPLE_SOURCE_FILES.get(path.name) != path.read_text():
            errors.append(f"{path}:1: embedded source is stale; run scripts/embed_example_sources.py")
    manifest_slugs = set(catalog.order)
    file_slugs = {path.stem for path in EXAMPLES_DIR.glob("*.md")}
    if manifest_slugs != file_slugs:
        errors.append(f"src/example_sources/manifest.toml:1: manifest/file slug mismatch missing={sorted(file_slugs - manifest_slugs)} extra={sorted(manifest_slugs - file_slugs)}")
    if len(catalog.order) != len(manifest_slugs):
        errors.append("src/example_sources/manifest.toml:1: duplicate slug in order")

    hardcoded_docs = re.compile(r"docs\.python\.org/3\.\d+")
    titles: set[str] = set()
    version_sensitive: list[str] = []
    count = 0
    for order_slug, example in zip(catalog.order, examples):
        slug = example["slug"]
        if slug != order_slug:
            errors.append(
                f"{EXAMPLES_DIR / f'{order_slug}.md'}:1: frontmatter slug {slug!r} "
                f"does not match the filename"
            )
            continue
        if selected and slug not in selected:
            continue
        count += 1
        path = EXAMPLES_DIR / f"{slug}.md"
        text = path.read_text()
        if hardcoded_docs.search(text):
            errors.append(f"{path}:1: use doc_path instead of hardcoded docs.python.org/3.x URLs")
        if not example["doc_path"].startswith("/"):
            errors.append(f"{path}:1: doc_path must start with /")
        if not example["doc_url"].startswith(catalog.docs_base_url + "/"):
            errors.append(f"{path}:1: generated doc_url has wrong base")
        if not example["summary"].strip():
            errors.append(f"{path}:1: summary is required")
        if example["title"] in titles:
            errors.append(f"{path}:1: duplicate title {example['title']!r}")
        titles.add(example["title"])
        if example.get("min_python") and version_tuple(example["min_python"]) > version_tuple(catalog.python_version):
            errors.append(f"{path}:1: min_python exceeds manifest python_version")
        if example.get("version_sensitive"):
            version_sensitive.append(slug)
            if not example.get("version_notes"):
                errors.append(f"{path}:1: version_sensitive examples require version_notes")
        for error in verify_example_output(example):
            errors.append(f"{path.parent / error}" if error.startswith(f"{slug}.md:") else error)

    unknown = selected - manifest_slugs
    if unknown:
        errors.append(f"unknown slugs: {sorted(unknown)}")
    if version_sensitive:
        print("Version-sensitive examples:", ", ".join(version_sensitive))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Verified {count} example(s) for Python {catalog.python_version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
