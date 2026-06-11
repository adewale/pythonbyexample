#!/usr/bin/env python3
"""Heuristic criterion-level scoring for example quality hill-climbing.

This is not the editorial source of truth. It is a search aid: it breaks the
rubric into observable criteria so the next rewrite can target the weakest
axis instead of arguing about one opaque number.

It is also the one bound on the hand-curated score registry: a curated
score more than --max-delta above the heuristic fails the build, so the
registry cannot drift upward without the page itself changing in ways
the observable criteria can see.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.example_loader import load_examples  # noqa: E402
from src.marginalia import EXAMPLE_QUALITY_SCORES  # noqa: E402

REGISTRY = ROOT / "docs" / "quality-registries.toml"
GENERIC_PHRASES = [
    "it exists to make a common boundary explicit",
    "the example is small, deterministic",
    "prefer simpler neighboring tools",
]
BOUNDARY_WORDS = re.compile(r"\b(prefer|instead|boundary|when|unless|except|error|raises?|static|runtime|unsupported|footgun|warning)\b", re.I)
RATIONALE_WORDS = re.compile(r"\b(use|prefer|reach for|when|because|useful|right tool|fit|shape)\b", re.I)
TOY_WORDS = re.compile(r"\b(foo|bar|baz|spam|eggs)\b", re.I)


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def tokenise(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[a-zA-Z_]{3,}", text)}


def criterion_scores(example: dict) -> dict[str, float]:
    prose = "\n".join(example.get("explanation", []))
    notes = "\n".join(example.get("notes", []))
    code = example.get("code", "")
    cells = example.get("cells", [])
    normal_cells = [cell for cell in cells if cell.get("kind") == "cell"]
    unsupported_cells = [cell for cell in cells if cell.get("kind") == "unsupported"]
    outputs = [cell.get("output", "") for cell in normal_cells]
    all_text = "\n".join([example.get("summary", ""), prose, notes])
    cell_prose = [" ".join(cell.get("prose", [])) for cell in normal_cells]
    distinct_cell_starts = len({text[:60] for text in cell_prose})
    output_lines = sum(len(output.splitlines()) for output in outputs if output)
    code_tokens = tokenise(code)
    prose_tokens = tokenise(all_text)
    overlap = len(code_tokens & prose_tokens)
    generic_penalty = 0.2 * sum(phrase in all_text.lower() for phrase in GENERIC_PHRASES)

    return {
        "conceptual_payoff": clamp(0.45 + min(len(prose) / 900, 0.35) + min(overlap / 30, 0.2) - generic_penalty),
        "rationale": clamp(0.35 + 0.35 * bool(RATIONALE_WORDS.search(all_text)) + min(len(example.get("notes", [])) / 6, 0.3) - generic_penalty),
        "alternatives_and_boundaries": clamp(0.25 + 0.25 * bool(BOUNDARY_WORDS.search(all_text)) + 0.2 * bool(unsupported_cells) + min(notes.lower().count("prefer") / 2, 0.2)),
        "executable_determinism": clamp(0.75 + 0.25 * bool(example.get("expected_output")) - 0.25 * bool(example.get("version_sensitive"))),
        "python_idiom_and_accuracy": clamp(0.75 + 0.15 * bool(example.get("doc_url")) + 0.1 * ("print(" in code) - 0.25 * bool(TOY_WORDS.search(code))),
        "literate_fit": clamp(0.35 + min(len(normal_cells) / 4, 0.35) + 0.3 * all(cell.get("prose") for cell in normal_cells)),
        "source_result_pairing": clamp(0.35 + 0.45 * all(outputs) + min(output_lines / 8, 0.2)),
        "concept_decomposition": clamp(0.25 + min(len(normal_cells) / 3, 0.55) + 0.2 * (len(normal_cells) >= 3)),
        "progressive_walkthrough": clamp(0.35 + min(distinct_cell_starts / max(len(normal_cells), 1), 0.45) + 0.2 * (len(normal_cells) >= 2)),
        "representative_coverage": clamp(0.3 + min(output_lines / 10, 0.25) + min(len(example.get("see_also", [])) / 4, 0.25) + 0.2 * (len(normal_cells) >= 3)),
        "practical_usefulness": clamp(0.55 + 0.25 * (not bool(TOY_WORDS.search(code))) + 0.2 * bool(re.search(r"Ada|Grace|project|config|score|price|request|path|file|service|team", code))),
        "editorial_progression": clamp(0.35 + min(len(example.get("explanation", [])) / 3, 0.25) + min(len(example.get("notes", [])) / 4, 0.25) + 0.15 * bool(example.get("see_also"))),
    }


def weighted_score(scores: dict[str, float], weights: dict[str, float]) -> float:
    return round(sum(scores[name] * float(weight) for name, weight in weights.items()), 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--below", type=float, default=9.0)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument(
        "--max-delta",
        type=float,
        default=1.5,
        help="fail when a curated score exceeds the heuristic by more than this",
    )
    args = parser.parse_args()

    weights = tomllib.loads(REGISTRY.read_text())["score_model"]
    _, examples = load_examples()
    rows = []
    for example in examples:
        criteria = criterion_scores(example)
        heuristic = weighted_score(criteria, weights)
        curated, comment = EXAMPLE_QUALITY_SCORES[example["slug"]]
        weakest = sorted(criteria.items(), key=lambda item: item[1])[:3]
        rows.append({
            "slug": example["slug"],
            "curated": curated,
            "heuristic": heuristic,
            "delta": round(curated - heuristic, 1),
            "comment": comment,
            "weakest": weakest,
            "criteria": criteria,
        })

    if args.json:
        print(json.dumps(rows, indent=2, sort_keys=True))
        return 0

    selected = [row for row in rows if row["curated"] < args.below]
    selected.sort(key=lambda row: (row["curated"], row["heuristic"]))
    for row in selected[: args.limit]:
        weak = ", ".join(f"{name}={score:.2f}" for name, score in row["weakest"])
        print(f"{row['curated']:>3.1f} h={row['heuristic']:>3.1f} {row['slug']:<30} {weak}")
    print(
        f"criterion heuristic: examples={len(rows)} "
        f"curated_avg={mean(row['curated'] for row in rows):.2f} "
        f"heuristic_avg={mean(row['heuristic'] for row in rows):.2f}"
    )

    inflated = [row for row in rows if row["curated"] - row["heuristic"] > args.max_delta]
    if inflated:
        for row in sorted(inflated, key=lambda r: r["heuristic"] - r["curated"]):
            print(
                f"{row['slug']}: curated {row['curated']:.1f} exceeds heuristic "
                f"{row['heuristic']:.1f} by more than {args.max_delta:.1f}; "
                f"re-grade or improve the page",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
