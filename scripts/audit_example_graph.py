#!/usr/bin/env python3
"""Audit see_also links as a lightweight example graph."""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.examples import EXAMPLES  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="additionally fail on orphaned examples (invalid links, self-links, "
        "and out-degree violations always fail)",
    )
    parser.add_argument("--max-out-degree", type=int, default=4)
    args = parser.parse_args()

    slugs = {example["slug"] for example in EXAMPLES}
    incoming: Counter[str] = Counter()
    outgoing: dict[str, list[str]] = {}
    errors: list[str] = []

    for example in EXAMPLES:
        slug = example["slug"]
        links = list(example.get("see_also", []))
        outgoing[slug] = links
        if len(links) > args.max_out_degree:
            errors.append(f"{slug}: too many see_also links ({len(links)} > {args.max_out_degree})")
        if slug in links:
            errors.append(f"{slug}: self-link")
        for target in links:
            if target not in slugs:
                errors.append(f"{slug}: missing target {target}")
            else:
                incoming[target] += 1

    linked = [slug for slug, links in outgoing.items() if links]
    orphaned = sorted(slug for slug in slugs if not outgoing[slug] and incoming[slug] == 0)
    high_in_degree = incoming.most_common(10)
    reciprocal = []
    for source, links in outgoing.items():
        for target in links:
            if source in outgoing.get(target, []):
                reciprocal.append(tuple(sorted((source, target))))
    reciprocal = sorted(set(reciprocal))

    print(f"examples={len(EXAMPLES)}")
    print(f"linked_sources={len(linked)}")
    print(f"edges={sum(len(links) for links in outgoing.values())}")
    print(f"orphaned={len(orphaned)}")
    if orphaned:
        print("orphaned_slugs=" + ", ".join(orphaned[:25]) + (" ..." if len(orphaned) > 25 else ""))
    if high_in_degree:
        print("top_in_degree=" + ", ".join(f"{slug}:{count}" for slug, count in high_in_degree))
    if reciprocal:
        print("reciprocal_edges=" + ", ".join(f"{a}<->{b}" for a, b in reciprocal[:20]))

    if args.check and orphaned:
        errors.append("orphaned examples: " + ", ".join(orphaned))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
