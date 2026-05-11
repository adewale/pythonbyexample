"""Content contracts for example markdown sources.

These contracts check pedagogical correctness rather than geometry:
does each cell's prose explain the code in that cell? Does the
unsupported-cell prose lead with the lesson or with a runtime
caveat?

The contracts complement tests/test_marginalia_geometry.py
(geometry, palette, registration) by catching content-shaped bugs
that geometry contracts can't see.
"""
from __future__ import annotations

import re
import unittest

from src.example_loader import load_examples


_, EXAMPLES = load_examples()


def _code_identifiers(code: str) -> set[str]:
    """Return identifier-like tokens from a code block.

    Strips Python keywords and the common stdlib names that appear
    in nearly every example (`print`, `import`) so the audit
    measures the lesson-specific vocabulary, not the language.
    """
    keywords = {
        "def", "return", "import", "from", "as", "if", "else",
        "elif", "try", "except", "finally", "with", "for", "in",
        "and", "or", "not", "is", "true", "false", "none",
        "print", "pass", "raise", "while", "break", "continue",
        "class", "lambda", "yield", "global", "nonlocal",
    }
    return {w for w in re.findall(r"\b[a-z_][a-z_0-9]+\b", code.lower())
            if w not in keywords and len(w) > 1}


class UnsupportedCellProseContract(unittest.TestCase):
    """Contract 11: every :::unsupported cell's prose explains the
    code, not just the runtime constraint.

    The :::unsupported block is rendered on production pages as a
    walkthrough cell with prose + code. When the prose only says
    'Dynamic Workers do not provide X', the reader sees the
    constraint but no pedagogical content. The fix is to lead with
    what the code does and move the runtime caveat to a closing
    parenthetical (or to the Notes section).

    Heuristic: each unsupported cell's prose must mention at least
    two code identifiers — variable names, function calls, or
    method names from the code block. Two is the minimum that
    proves the prose discusses *this specific code* rather than
    a generic note about Workers.
    """

    MIN_IDENT_OVERLAP = 2

    def test_unsupported_prose_mentions_code(self):
        failures: list[str] = []
        for ex in EXAMPLES:
            for cell in ex.get("cells", []):
                if cell.get("kind") != "unsupported":
                    continue
                prose = " ".join(cell.get("prose", [])).lower()
                idents = _code_identifiers(cell.get("code", ""))
                hits = sum(1 for ident in idents if ident in prose)
                if hits < self.MIN_IDENT_OVERLAP:
                    failures.append(
                        f"{ex['slug']}: unsupported cell prose references "
                        f"{hits} code identifier(s) (need ≥ {self.MIN_IDENT_OVERLAP}); "
                        f"prose looks generic. idents: {sorted(idents)[:5]}…"
                    )
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


if __name__ == "__main__":
    unittest.main()
