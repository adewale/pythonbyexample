import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "example-source-format-spec.md"


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


if __name__ == "__main__":
    unittest.main()
