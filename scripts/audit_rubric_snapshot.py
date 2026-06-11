#!/usr/bin/env python3
"""Generate a full rubric-audit snapshot for examples, figures, and journeys.

The ordinary quality checks are release gates. This script is a review aid: it
puts the same ledgers beside each other so an editorial pass can see whether
example scores, figure scores, journey outcomes, and graph support still agree.
"""
from __future__ import annotations

import argparse
import datetime
import sys
import tomllib
from collections import Counter
from pathlib import Path
from statistics import mean, median
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs" / "quality-registries.toml"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.score_example_criteria import criterion_scores, weighted_score  # noqa: E402
from src.app import JOURNEYS  # noqa: E402
from src.example_loader import load_examples  # noqa: E402
from src.marginalia import (  # noqa: E402
    ATTACHMENTS,
    EXAMPLE_QUALITY_SCORES,
    SCORES,
    SECTION_FIGURE_SCORES,
    SECTION_FIGURES,
)


Example = dict[str, Any]
Registry = dict[str, Any]


def md(text: object) -> str:
    """Escape a value for a compact Markdown table cell."""
    return str(text).replace("|", "\\|").replace("\n", " ")


def score_summary(scores: list[float]) -> str:
    distribution = ", ".join(
        f"{score:g} × {count}" for score, count in sorted(Counter(scores).items())
    )
    return (
        f"count={len(scores)}, min={min(scores):g}, avg={mean(scores):.2f}, "
        f"median={median(scores):g}, below9={sum(score < 9.0 for score in scores)}, "
        f"distribution={distribution}"
    )


def example_rows(examples: list[Example], registry: Registry) -> list[dict[str, Any]]:
    weights = registry["score_model"]
    rows: list[dict[str, Any]] = []
    for example in examples:
        slug = example["slug"]
        attachments = ATTACHMENTS.get(slug, [])
        if len(attachments) != 1:
            figure = "missing" if not attachments else f"{len(attachments)} figures"
            anchor = "—"
            figure_score = "—"
        else:
            anchor, figure, _caption = attachments[0]
            figure_score = SCORES[slug][0]
        criteria = criterion_scores(example)
        weakest = sorted(criteria.items(), key=lambda item: item[1])[:3]
        rows.append(
            {
                "slug": slug,
                "score": EXAMPLE_QUALITY_SCORES[slug][0],
                "heuristic": weighted_score(criteria, weights),
                "cells": sum(1 for cell in example["cells"] if cell["kind"] == "cell"),
                "notes": len(example["notes"]),
                "see_also": len(example["see_also"]),
                "figure": figure,
                "anchor": anchor,
                "figure_score": figure_score,
                "weakest": ", ".join(f"{name}={score:.2f}" for name, score in weakest),
            }
        )
    return rows


def graph_stats(examples: list[Example]) -> dict[str, int]:
    slugs = {example["slug"] for example in examples}
    linked = set()
    edges = 0
    for example in examples:
        see_also = example["see_also"]
        edges += len(see_also)
        if see_also:
            linked.add(example["slug"])
        linked.update(slug for slug in see_also if slug in slugs)
    return {
        "linked_sources": len(linked),
        "edges": edges,
        "orphaned": len(slugs - linked),
    }


def reused_section_figures() -> list[dict[str, str]]:
    example_figures: dict[str, list[str]] = {}
    for slug, attachments in ATTACHMENTS.items():
        for _anchor, figure, _caption in attachments:
            example_figures.setdefault(figure, []).append(slug)

    rows: list[dict[str, str]] = []
    for title, (figure, _caption) in SECTION_FIGURES.items():
        if figure in example_figures:
            rows.append(
                {
                    "section": title,
                    "figure": figure,
                    "example_slugs": ", ".join(sorted(example_figures[figure])),
                }
            )
    return rows


def journey_rows(registry: Registry) -> list[dict[str, Any]]:
    outcome_registry = registry["journey_outcomes"]
    rows: list[dict[str, Any]] = []
    for journey in JOURNEYS:
        journey_slug = journey["slug"]
        for section in journey["sections"]:
            title = section["title"]
            key = f"{journey_slug}::{title}"
            support = [item[1] for item in section["items"] if item[0] == "example"]
            figure, caption = SECTION_FIGURES[title]
            rows.append(
                {
                    "journey": journey_slug,
                    "section": title,
                    "support": len(support),
                    "outcomes": len(outcome_registry[key]["outcomes"]),
                    "figure": figure,
                    "score": SECTION_FIGURE_SCORES[title][0],
                    "caption": caption,
                }
            )
    return rows


def dimension_ledgers(
    reused_sections: list[dict[str, str]],
) -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Each dimension's Result names HOW it is assured, not a bare PASS.

    GATED means a named script or test fails the build when the
    dimension regresses — this report does not re-run those gates, so a
    GATED row is only as current as the last `make verify`. CURATED
    means the dimension rests on editorial judgement recorded in the
    score registries; an audit pass must re-affirm those by review
    rather than trusting this snapshot.
    """
    examples = [
        ("Conceptual payoff", "Curated score registry + criterion search", "CURATED (re-affirm by review)"),
        ("Rationale", "Criterion search + notes-supported gate", "GATED by check_notes_supported"),
        ("Alternatives and boundaries", "Confusable pairs, footguns, broad tours, graph edges", "GATED by quality-checks"),
        ("Executable determinism", "`verify_examples.py` over every program and cell", "GATED by verify-examples"),
        ("Python idiom and accuracy", "Python 3.13 verification, docs links, Ruff", "GATED by verify-examples + lint"),
        ("Literate fit", "Markdown parser requires prose beside every cell", "GATED by the loader"),
        ("Source/result pairing", "Every runnable cell carries expected output", "GATED by verify-examples"),
        ("Concept decomposition", "Criterion search + curated score floor", "CURATED (re-affirm by review)"),
        ("Progressive walkthrough", "Cell sequence review + criterion search", "CURATED (re-affirm by review)"),
        ("Representative coverage", "Broad-surface and syntax-surface gates", "GATED by check_broad_surface_tours"),
        ("Practical usefulness", "Criterion search + editorial score comments", "CURATED (re-affirm by review)"),
        ("Editorial progression", "Quality registry + graph audit", "GATED by audit_example_graph"),
    ]
    figures = [
        ("Cell fidelity", "Attachment anchor resolves to a real rendered cell", "GATED by FigureAnchorContract"),
        ("Earns its place", "Curated figure scores", "CURATED (re-affirm by review)"),
        ("One conceptual move", "Figure score rationale + emphasis-scarcity contract", "CURATED + accent contract"),
        ("Mechanism over metaphor", "Canvas grammar uses bindings, arrows, cells, lanes, boundaries", "CURATED (re-affirm by review)"),
        ("Caption quality", "Unique, complete-sentence figcaptions", "GATED by FigureCaptionContract"),
        ("Grammar conformance", "Palette, font, and stroke contracts", "GATED by geometry contracts"),
        ("Emphasis scarcity", "At most one accent mark per figure", "GATED by FigureEmphasisScarcityContract"),
        ("Restraint", "Locked primitive grammar; no bespoke SVG", "GATED by the grammar's surface"),
        ("Banner-row fit", "Intrinsic-width contract", "GATED by FigureSizeContract"),
        ("Pairs with surrounding cell", "Caption/figure agreement on the marginalia gestalt", "CURATED (re-affirm by review)"),
    ]
    independence_result = (
        "computed: no reuse" if not reused_sections else f"WATCH ({len(reused_sections)} reused paint functions)"
    )
    journeys = [
        ("Section fidelity", "Section figure keyed by journey section title", "GATED by SectionFigureContract"),
        ("Pedagogical scope", "Section-level captions and score rationales", "CURATED (re-affirm by review)"),
        ("One conceptual move", "One figure per section and one emphasis mark", "GATED + CURATED"),
        ("Mechanism over metaphor", "Canvas primitives show protocols, boundaries, lanes, or flows", "CURATED (re-affirm by review)"),
        ("Caption alignment", "Section figure captions unique and declarative", "GATED by FigureCaptionContract"),
        ("Grammar conformance", "Shared geometry contracts", "GATED by geometry contracts"),
        (
            "Independence from lesson figures",
            "Section figures compared with example attachments",
            independence_result,
        ),
        ("Layout fit", "Journey figure dimensions within production column", "GATED by FigureSizeContract"),
        ("Outcome support", "`check_journey_outcomes.py` over all journey sections", "GATED by check_journey_outcomes"),
        ("Prerequisite order", "Journey order reviewed against lesson dependencies", "CURATED (re-affirm by review)"),
    ]
    return examples, figures, journeys


def render_table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        lines.append("| " + " | ".join(md(value) for value in row) + " |")
    return lines


def render_report(date: str) -> str:
    registry = tomllib.loads(REGISTRY_PATH.read_text())
    _catalog, examples = load_examples()
    example_scores = [score for score, _comment in EXAMPLE_QUALITY_SCORES.values()]
    figure_scores = [score for score, _comment in SCORES.values()]
    journey_scores = [score for score, _comment in SECTION_FIGURE_SCORES.values()]
    reused_sections = reused_section_figures()
    examples_ledger, figures_ledger, journeys_ledger = dimension_ledgers(reused_sections)
    graph = graph_stats(examples)
    rows = example_rows(examples, registry)
    section_rows = journey_rows(registry)

    waivers = registry.get("quality_waivers", {})
    waiver_lines = [
        f"- Accepted waiver: `{slug}` at "
        f"{EXAMPLE_QUALITY_SCORES.get(slug, (0.0, ''))[0]:g} "
        f"(floor {entry.get('accepted_min', '?')}, expires {entry.get('expires', '?')})."
        for slug, entry in sorted(waivers.items())
    ] or ["- Accepted waivers: none."]

    lines = [
        f"# Rubric audit snapshot — {date}",
        "",
        "This snapshot puts the catalog's quality ledgers beside each other for an "
        "editorial pass. Every number is computed from the live registries at "
        "generation time; rows marked CURATED are editorial judgements that the "
        "audit pass must re-affirm by review — this report does not validate them.",
        "",
        "## Scoreboard",
        "",
        f"- Examples: {score_summary(example_scores)}",
        f"- Example diagrams: {score_summary(figure_scores)}",
        f"- Journey diagrams: {score_summary(journey_scores)}",
        *waiver_lines,
        "- Graph health: "
        f"{graph['linked_sources']} linked sources, {graph['edges']} edges, "
        f"{graph['orphaned']} orphaned examples.",
        "",
        "## Example rubric dimensions",
        "",
    ]
    lines.extend(render_table(["Dimension", "Evidence", "Result"], examples_ledger))
    lines.extend([
        "",
        "## Example-figure rubric dimensions",
        "",
    ])
    lines.extend(render_table(["Dimension", "Evidence", "Result"], figures_ledger))
    lines.extend([
        "",
        "## Journey-visualisation rubric dimensions",
        "",
    ])
    lines.extend(render_table(["Dimension", "Evidence", "Result"], journeys_ledger))
    lines.extend([
        "",
        "## Example and diagram inventory",
        "",
    ])
    lines.extend(
        render_table(
            ["Slug", "Quality", "Heuristic", "Cells", "Notes", "Edges", "Figure", "Anchor", "Fig score", "Weakest heuristic axes"],
            [
                [
                    row["slug"],
                    row["score"],
                    row["heuristic"],
                    row["cells"],
                    row["notes"],
                    row["see_also"],
                    row["figure"],
                    row["anchor"],
                    row["figure_score"],
                    row["weakest"],
                ]
                for row in rows
            ],
        )
    )
    lines.extend([
        "",
        "## Journey section inventory",
        "",
    ])
    lines.extend(
        render_table(
            ["Journey", "Section", "Support examples", "Outcomes", "Figure", "Score", "Caption"],
            [
                [
                    row["journey"],
                    row["section"],
                    row["support"],
                    row["outcomes"],
                    row["figure"],
                    row["score"],
                    row["caption"],
                ]
                for row in section_rows
            ],
        )
    )
    lines.extend([
        "",
        "## Journey figure independence watchlist",
        "",
    ])
    if reused_sections:
        lines.extend([
            f"{len(reused_sections)} section figures still reuse production example paint functions. They "
            "remain above the project gate, but the journey rubric's independence "
            "criterion should be the next visual-design frontier.",
            "",
        ])
        lines.extend(
            render_table(
                ["Section", "Shared figure", "Also attached to example"],
                [
                    [row["section"], row["figure"], row["example_slugs"]]
                    for row in reused_sections
                ],
            )
        )
    else:
        lines.append("No journey section figures reuse production example paint functions.")
    target = float(registry.get("quality_gates", {}).get("example_target", 9.0))
    below_target = sorted(
        slug for slug, (score, _comment) in EXAMPLE_QUALITY_SCORES.items()
        if score < target and slug not in waivers
    )
    findings: list[str] = []
    if below_target:
        findings.append(
            f"{len(below_target)} example(s) below target {target:g} without a waiver: "
            + ", ".join(f"`{slug}`" for slug in below_target) + "."
        )
    if graph["orphaned"]:
        findings.append(f"{graph['orphaned']} orphaned example(s) in the see_also graph.")
    if reused_sections:
        findings.append(
            f"{len(reused_sections)} journey section(s) reuse example paint functions."
        )
    weakest_diagram = min(figure_scores) if figure_scores else 0.0
    weakest_journey = min(journey_scores) if journey_scores else 0.0
    lines.extend([
        "",
        "## Computed findings",
        "",
        *(
            [f"- {finding}" for finding in findings]
            or ["- No gate-blocking conditions detected in the computed ledgers."]
        ),
        f"- Weakest example diagram score: {weakest_diagram:g}; "
        f"weakest journey diagram score: {weakest_journey:g}.",
        "",
        "CURATED dimensions above are not validated by this report; the audit "
        "pass owns re-affirming them (the marginalia gestalt page shows every "
        "figure with its production caption for exactly that review).",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.date.today().isoformat())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = render_report(args.date)
    if args.output:
        args.output.write_text(report)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
