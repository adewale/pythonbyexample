import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "example-source-format-spec.md"
README = ROOT / "README.md"
CI = ROOT / ".github" / "workflows" / "verify.yml"


class MarkdownMigrationPrereqTests(unittest.TestCase):
    def test_spec_covers_all_fourteen_migration_prerequisites(self):
        spec = SPEC.read_text()
        required_phrases = [
            "Cloudflare bundling behavior",
            "Historical golden parity script",
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

    def test_spec_captures_successful_migration_and_rollback_rehearsal(self):
        spec = SPEC.read_text()
        self.assertIn("Lessons from the successful parity migration", spec)
        self.assertIn("100% golden parity", spec)
        self.assertIn("rollback-rehearsed", spec)
        self.assertIn("revert the migration, deploy the rollback", spec)
        self.assertIn("re-apply the migration and repeat verification", spec)

    def test_remaining_operational_lessons_are_documented_and_verified(self):
        spec = SPEC.read_text()
        readme = README.read_text()
        workflow = CI.read_text()
        for phrase in [
            "Golden fixture cleanup policy",
            "CI policy",
            "Contributor documentation policy",
            "Native Markdown bundling remains unproven",
            "reserialize it deterministically",
            "TOML editorial registries",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, spec)
        for phrase in ["src/example_sources/", ":::program", ":::cell", "make build", "make verify-examples"]:
            with self.subTest(readme=phrase):
                self.assertIn(phrase, readme)
        for phrase in ["make verify", "format_examples.py --check", "verify-python-version"]:
            with self.subTest(workflow=phrase):
                self.assertIn(phrase, workflow)
        self.assertNotIn("check_example_migration_parity.py", workflow)


if __name__ == "__main__":
    unittest.main()
