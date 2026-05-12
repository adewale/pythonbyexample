"""Tests for the four quality-check scripts.

Each test runs the script as a subprocess against a temporary registry
or example directory so the script's command-line behavior is what is
validated, not just its internals.
"""
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(script: str, *, env_overrides: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class CheckScriptSmokeTests(unittest.TestCase):
    """The shipped catalog must pass every gate."""

    def test_registry_integrity_passes(self):
        result = run("check_registry_integrity.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Registry integrity OK", result.stdout)

    def test_confusable_pairs_pass(self):
        result = run("check_confusable_pairs.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Confusable-pair coverage OK", result.stdout)

    def test_broad_surface_tours_pass(self):
        result = run("check_broad_surface_tours.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Broad-surface tour coverage OK", result.stdout)

    def test_footgun_coverage_passes(self):
        result = run("check_footgun_coverage.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Footgun coverage OK", result.stdout)

    def test_notes_supported_passes(self):
        result = run("check_notes_supported.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Notes-supported check OK", result.stdout)

    def test_quality_scores_pass(self):
        result = run("check_quality_scores.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Quality score gate OK", result.stdout)

    def test_no_figure_rationales_pass(self):
        result = run("check_no_figure_rationales.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("No-figure rationale registry OK", result.stdout)

    def test_journey_outcomes_pass(self):
        result = run("check_journey_outcomes.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Journey outcomes OK", result.stdout)


class RegistryIntegrityTests(unittest.TestCase):
    """The integrity script catches typos before they reach the coverage checks."""

    def _write_and_run(self, registry_text: str) -> subprocess.CompletedProcess:
        # Patch the script in-memory by overriding REGISTRY_PATH via a
        # generated wrapper. Simpler: write the registry to a temp file and
        # patch the script's module-level constant by invoking it through a
        # small Python program.
        with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False) as fh:
            fh.write(registry_text)
            registry_path = Path(fh.name)
        program = textwrap.dedent(f"""
            import sys
            from pathlib import Path
            sys.path.insert(0, {str(SCRIPTS)!r})
            import check_registry_integrity as mod
            mod.REGISTRY_PATH = Path({str(registry_path)!r})
            sys.exit(mod.main())
        """)
        return subprocess.run(
            [sys.executable, "-c", program],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )

    def test_unknown_owner_in_confusable_pair_fails(self):
        result = self._write_and_run(
            textwrap.dedent("""
                [[confusable_pairs]]
                name = "fake pair"
                owner = "no-such-page"
                tokens = ["a", "b"]
            """)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown owner", result.stderr)
        self.assertIn("no-such-page", result.stderr)

    def test_missing_tokens_in_confusable_pair_fails(self):
        result = self._write_and_run(
            textwrap.dedent("""
                [[confusable_pairs]]
                name = "empty"
                owner = "hello-world"
                tokens = []
            """)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("no tokens", result.stderr)

    def test_unknown_footgun_owner_fails(self):
        result = self._write_and_run(
            textwrap.dedent("""
                [[footguns]]
                name = "fake"
                owner = "no-such-page"
                broken_tokens = ["x"]
                fixed_tokens = ["y"]
            """)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown owner", result.stderr)

    def test_unknown_broad_tour_slug_fails(self):
        result = self._write_and_run(
            textwrap.dedent("""
                [broad_surface_tours.no-such-page]
                required_tokens = ["x"]
            """)
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown slug", result.stderr)


class NotesSupportedHeuristicTests(unittest.TestCase):
    """The notes check should accept grounded bullets and reject ungrounded ones."""

    def test_token_extraction_drops_stopwords(self):
        sys.path.insert(0, str(SCRIPTS))
        try:
            import check_notes_supported as mod
        finally:
            sys.path.pop(0)
        extracted = mod.tokens("The quick fox uses functions and methods.")
        self.assertNotIn("the", extracted)
        self.assertNotIn("functions", extracted)  # filtered
        self.assertIn("quick", extracted)
        self.assertIn("fox", extracted)


if __name__ == "__main__":
    unittest.main()
