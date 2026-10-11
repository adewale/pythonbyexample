import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CI = ROOT / ".github" / "workflows" / "verify.yml"


class MarkdownMigrationPrereqTests(unittest.TestCase):
    # The Markdown migration shipped (see docs/example-source-format-spec.md).
    # Tests that only checked the spec's wording, including the order of the
    # words "Red", "Green" and "Refactor", were removed: they proved nothing
    # about the process. What remains is the contributor-facing contract.

    def test_readme_and_ci_keep_the_markdown_workflow_commands(self):
        readme = README.read_text()
        workflow = CI.read_text()
        for phrase in ["src/example_sources/", ":::program", ":::cell", "make build", "make verify-examples"]:
            with self.subTest(readme=phrase):
                self.assertIn(phrase, readme)
        for phrase in ["make verify", "format_examples.py --check", "verify-python-version"]:
            with self.subTest(workflow=phrase):
                self.assertIn(phrase, workflow)
        self.assertNotIn("check_example_migration_parity.py", workflow)


if __name__ == "__main__":
    unittest.main()
