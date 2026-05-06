"""Load example catalog entries from Markdown source files."""
from __future__ import annotations

import ast
import contextlib
import io
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = Path(__file__).with_name("example_sources")
MANIFEST_PATH = EXAMPLES_DIR / "manifest.toml"

try:
    from .example_sources_data import EXAMPLE_SOURCE_FILES
except ImportError:  # pragma: no cover - Cloudflare imports src as root.
    try:
        from example_sources_data import EXAMPLE_SOURCE_FILES
    except ImportError:  # pragma: no cover - verifier can still use filesystem source.
        EXAMPLE_SOURCE_FILES = {}


def _source_text(filename: str) -> str:
    path = EXAMPLES_DIR / filename
    if path.exists():
        return path.read_text()
    return EXAMPLE_SOURCE_FILES[filename]


@dataclass(frozen=True)
class Cell:
    prose: list[str]
    source: str
    output: str


@dataclass(frozen=True)
class ExampleCatalog:
    python_version: str
    docs_base_url: str
    order: list[str]


def load_manifest() -> ExampleCatalog:
    data = tomllib.loads(_source_text("manifest.toml"))
    return ExampleCatalog(
        python_version=data["python_version"],
        docs_base_url=data["docs_base_url"].rstrip("/"),
        order=list(data["order"]),
    )


def _split_frontmatter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    if not text.startswith("+++\n"):
        raise ValueError(f"{path}: expected TOML frontmatter delimited by +++")
    try:
        raw_frontmatter, body = text[4:].split("\n+++\n", 1)
    except ValueError as error:
        raise ValueError(f"{path}: missing closing +++ frontmatter delimiter") from error
    return tomllib.loads(raw_frontmatter), body.strip()


def _paragraphs(markdown_text: str) -> list[str]:
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", markdown_text.strip()):
        cleaned = " ".join(line.strip() for line in paragraph.splitlines()).strip()
        if cleaned:
            paragraphs.append(cleaned)
    return paragraphs


def _parse_fence(text: str, language: str, path: Path) -> str:
    pattern = rf"```{re.escape(language)}\n(.*?)\n```"
    matches = re.findall(pattern, text, flags=re.S)
    if len(matches) != 1:
        raise ValueError(f"{path}: expected exactly one {language!r} fence in each cell")
    return matches[0].rstrip("\n")


def _parse_cells(body: str, path: Path) -> tuple[str, list[Cell], list[str]]:
    notes: list[str] = []
    note_pattern = re.compile(r"\n?:::note\n(.*?)\n:::\s*", re.S)

    def collect_note(match: re.Match[str]) -> str:
        for line in match.group(1).splitlines():
            stripped = line.strip()
            if stripped.startswith("- "):
                notes.append(stripped[2:].strip())
            elif stripped:
                notes.append(stripped)
        return "\n"

    body_without_notes = note_pattern.sub(collect_note, body)
    cell_pattern = re.compile(r":::cell\n(.*?)\n:::", re.S)
    matches = list(cell_pattern.finditer(body_without_notes))
    if not matches:
        raise ValueError(f"{path}: expected at least one :::cell block")

    intro = body_without_notes[: matches[0].start()].strip()
    cells: list[Cell] = []
    for match in matches:
        cell_text = match.group(1).strip()
        source = _parse_fence(cell_text, "python", path)
        output = _parse_fence(cell_text, "output", path)
        prose_text = re.sub(r"```python\n.*?\n```", "", cell_text, flags=re.S)
        prose_text = re.sub(r"```output\n.*?\n```", "", prose_text, flags=re.S)
        prose = _paragraphs(prose_text)
        if not prose:
            raise ValueError(f"{path}: cell prose is required")
        cells.append(Cell(prose=prose, source=source, output=output.rstrip("\n")))
    return intro, cells, notes


def _run(code: str, namespace: dict[str, Any] | None = None) -> str:
    stdout = io.StringIO()
    if namespace is None:
        namespace = {"__name__": "__main__"}
    with contextlib.redirect_stdout(stdout):
        exec(compile(code, "<example>", "exec", dont_inherit=True), namespace)
    return stdout.getvalue()


def example_to_dict(path: Path, catalog: ExampleCatalog) -> dict[str, Any]:
    frontmatter, body = _split_frontmatter(_source_text(path.name), path)
    intro, cells, notes = _parse_cells(body, path)
    slug = frontmatter["slug"]
    code = "\n\n".join(cell.source for cell in cells).rstrip() + "\n"
    expected_output = "\n".join(cell.output for cell in cells).rstrip() + "\n"
    doc_path = frontmatter["doc_path"]
    doc_url = f"{catalog.docs_base_url}{doc_path}"
    paragraphs = _paragraphs(intro)
    return {
        "slug": slug,
        "title": frontmatter["title"],
        "section": frontmatter["section"],
        "summary": frontmatter["summary"],
        "doc_path": doc_path,
        "doc_url": doc_url,
        "explanation": paragraphs,
        "notes": notes,
        "walkthrough": [{"prose": prose, "code": cell.source} for cell in cells for prose in cell.prose],
        "cells": [{"prose": cell.prose, "code": cell.source, "output": cell.output} for cell in cells],
        "code": code,
        "expected_output": expected_output,
        "min_python": frontmatter.get("min_python"),
        "version_sensitive": bool(frontmatter.get("version_sensitive", False)),
        "version_notes": frontmatter.get("version_notes"),
    }


def load_examples() -> tuple[ExampleCatalog, list[dict[str, Any]]]:
    catalog = load_manifest()
    examples = [example_to_dict(EXAMPLES_DIR / f"{slug}.md", catalog) for slug in catalog.order]
    return catalog, examples


def verify_example_output(example: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    namespace: dict[str, Any] = {"__name__": "__main__"}
    for index, cell in enumerate(example["cells"], 1):
        try:
            ast.parse(cell["code"])
            actual = _run(cell["code"], namespace).rstrip("\n")
        except Exception as error:  # noqa: BLE001 - report verifier errors with example context.
            errors.append(f"{example['slug']} cell {index}: execution failed: {error.__class__.__name__}: {error}")
            continue
        if actual != cell["output"]:
            errors.append(f"{example['slug']} cell {index}: output mismatch: expected {cell['output']!r}, got {actual!r}")
    try:
        ast.parse(example["code"])
        full_actual = _run(example["code"]).rstrip("\n") + "\n"
    except Exception as error:  # noqa: BLE001
        errors.append(f"{example['slug']} full code: execution failed: {error.__class__.__name__}: {error}")
    else:
        if full_actual != example["expected_output"]:
            errors.append(f"{example['slug']} full code: output mismatch")
    return errors
