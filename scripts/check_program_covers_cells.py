#!/usr/bin/env python3
"""Check that every executable cell is anchored in the program block.

The site convention is that the editable `:::program` block contains the
code the cells walk through. Cells may restate definitions, vary inputs,
or add inspection lines (`print`, imports), but a cell whose substantive
logic is entirely absent from the program teaches code the editor cannot
reproduce — the drift this gate exists to catch.

A page that deliberately contrasts an approach the program does not use
can opt out with `standalone_cells = true` in frontmatter; the opt-out
is reported so it stays a visible editorial decision.
"""
from __future__ import annotations

from _common import EXAMPLES_DIR, fail, frontmatter, load_catalog

INSPECTION_PREFIXES = ("print(", "import ", "from ", "#")


def substantive_lines(code: str) -> list[str]:
    lines = []
    for raw in code.splitlines():
        line = raw.strip()
        if not line or line.startswith(INSPECTION_PREFIXES):
            continue
        lines.append(line)
    return lines


def main() -> int:
    _, examples = load_catalog()
    errors: list[str] = []
    opted_out: list[str] = []
    for example in examples:
        slug = example["slug"]
        path = EXAMPLES_DIR / f"{slug}.md"
        if frontmatter(path).get("standalone_cells"):
            opted_out.append(slug)
            continue
        program_lines = set(substantive_lines(example["code"]))
        for index, cell in enumerate(example["cells"], 1):
            if cell.get("kind") != "cell":
                continue
            cell_lines = substantive_lines(cell["code"])
            if cell_lines and not set(cell_lines) & program_lines:
                errors.append(
                    f"{path}:{cell.get('line', 1)}: cell {index} shares no substantive line "
                    f"with the :::program block; add the code to the program or set "
                    f"standalone_cells = true with a reason in prose"
                )
    if opted_out:
        print("standalone_cells opt-outs:", ", ".join(sorted(opted_out)))
    return fail(errors, f"Program-covers-cells check OK ({len(examples)} examples).")


if __name__ == "__main__":
    raise SystemExit(main())
