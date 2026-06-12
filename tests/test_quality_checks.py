"""Tests for the quality-check scripts in scripts/.

Each smoke test runs the script as a subprocess so the command-line
behavior is what is validated, not just its internals; the negative
tests prove each gate can actually fail.
"""
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), *args],
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

    def test_criterion_scoring_report_passes(self):
        result = run("score_example_criteria.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("criterion heuristic", result.stdout)

    def test_no_figure_rationales_pass(self):
        result = run("check_no_figure_rationales.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("No-figure rationale registry OK", result.stdout)

    def test_journey_outcomes_pass(self):
        result = run("check_journey_outcomes.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Journey outcomes OK", result.stdout)

    def test_rubric_audit_snapshot_passes(self):
        result = run("audit_rubric_snapshot.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Rubric audit snapshot", result.stdout)
        self.assertIn("Example and diagram inventory", result.stdout)
        self.assertIn("Journey section inventory", result.stdout)

    def test_program_covers_cells_passes(self):
        result = run("check_program_covers_cells.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Program-covers-cells check OK", result.stdout)

    def test_prose_duplication_passes(self):
        result = run("check_prose_duplication.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Prose-duplication check OK", result.stdout)

    def test_inline_links_pass(self):
        result = run("check_inline_links.py")
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Inline-link check OK", result.stdout)

    def test_example_graph_passes(self):
        result = run("audit_example_graph.py", "--check")
        self.assertEqual(result.returncode, 0, msg=result.stderr)


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
        self.addCleanup(registry_path.unlink, missing_ok=True)
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


def _scripts_import(name):
    sys.path.insert(0, str(SCRIPTS))
    try:
        return __import__(name)
    finally:
        sys.path.pop(0)


class GateLogicCanFailTests(unittest.TestCase):
    """Each content gate's core predicate must be able to reject bad input —
    a gate that cannot fail is decoration, not enforcement."""

    def test_program_covers_cells_flags_disjoint_cell(self):
        mod = _scripts_import("check_program_covers_cells")
        program = mod.substantive_lines("total = 1\nprint(total)")
        disjoint_cell = mod.substantive_lines("other = 2\nvalue = other * 2")
        self.assertEqual(set(program) & set(disjoint_cell), set())
        overlapping_cell = mod.substantive_lines("total = 1\nextra = total + 1")
        self.assertNotEqual(set(program) & set(overlapping_cell), set())

    def test_confusable_pairs_reject_substring_shadowing(self):
        mod = _scripts_import("check_confusable_pairs")
        async_only_page = "async def fetch(): ...\nawait fetch()"
        self.assertEqual(
            mod.missing_tokens(async_only_page, ["async def", "def "]), ["def "]
        )
        both_forms = "async def fetch(): ...\ndef plain(): ..."
        self.assertEqual(mod.missing_tokens(both_forms, ["async def", "def "]), [])

    def test_inline_link_regex_catches_external_targets(self):
        mod = _scripts_import("check_inline_links")
        match = mod.LINK_RE.search("see [docs](/data-model/container-protocols) here")
        self.assertIsNotNone(match)
        self.assertIsNone(mod.INTERNAL_RE.match(match.group(2)))
        good = mod.LINK_RE.search("see [page](/examples/values)")
        self.assertIsNotNone(mod.INTERNAL_RE.match(good.group(2)))

    def test_waiver_expiry_dates_are_enforced(self):
        import datetime

        mod = _scripts_import("check_quality_scores")
        today = datetime.date(2026, 6, 11)
        self.assertIsNotNone(mod.check_expiry_date("never", today=today))
        self.assertIsNotNone(mod.check_expiry_date("2026-06-11", today=today))
        self.assertIsNotNone(mod.check_expiry_date(None, today=today))
        self.assertIsNone(mod.check_expiry_date("2026-06-12", today=today))

    def test_criterion_scoring_fails_on_inflated_curated_score(self):
        result = run("score_example_criteria.py", "--max-delta", "-11")
        self.assertEqual(result.returncode, 1)
        self.assertIn("exceeds heuristic", result.stderr)


if __name__ == "__main__":
    unittest.main()
