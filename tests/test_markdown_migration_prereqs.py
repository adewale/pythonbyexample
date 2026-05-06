import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "example-source-format-spec.md"
INVESTIGATION = ROOT / "docs" / "markdown-cell-migration-investigation.md"


class MarkdownMigrationPrereqTests(unittest.TestCase):
    def test_spec_covers_all_fourteen_migration_prerequisites(self):
        spec = SPEC.read_text()
        required_phrases = [
            "Cloudflare bundling behavior",
            "Golden parity script",
            "Cell model",
            "Generated full code",
            "Verifier correctness",
            "Line-number reporting",
            "Formatter behavior",
            "Build step",
            "Cache busting",
            "Worker runtime startup",
            "POST execution",
            "Browser layout",
            "Production smoke test",
            "Python version migration command",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, spec)

    def test_spec_defines_red_green_refactor_order(self):
        spec = SPEC.read_text()
        self.assertIn("Red", spec)
        self.assertIn("Green", spec)
        self.assertIn("Refactor", spec)
        self.assertLess(spec.index("Red"), spec.index("Green"))
        self.assertLess(spec.index("Green"), spec.index("Refactor"))

    def test_spec_blocks_deploy_without_full_teaching_parity(self):
        spec = SPEC.read_text()
        self.assertIn("100% golden parity", spec)
        self.assertIn("100% parity", spec)
        self.assertIn("Do not deploy Markdown-backed examples unless Phase 3 has 100% parity", spec)
        self.assertIn("No allowlist is permitted for the app switch", spec)
        self.assertIn("teaching-structure difference", spec)

    def test_spec_names_examples_that_lost_fine_grained_cells(self):
        spec = SPEC.read_text()
        for slug in [
            "match-statements",
            "recursion",
            "classes",
            "properties",
            "special-methods",
            "type-hints",
        ]:
            with self.subTest(slug=slug):
                self.assertIn(slug, spec)

    def test_investigation_documents_program_and_cell_solution(self):
        investigation = INVESTIGATION.read_text()
        self.assertIn(":::program", investigation)
        self.assertIn("cells are not concatenated", investigation)
        self.assertIn("restate earlier definitions", investigation)
        for slug in [
            "match-statements",
            "recursion",
            "classes",
            "properties",
            "special-methods",
            "type-hints",
        ]:
            with self.subTest(slug=slug):
                self.assertIn(f"`{slug}`", investigation)


if __name__ == "__main__":
    unittest.main()
