"""Contracts that keep the tested Python environment identical to production."""

import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _locked_versions(path: Path) -> dict[str, str]:
    data = tomllib.loads(path.read_text())
    return {package["name"]: package["version"] for package in data.get("package", [])}


class DependencyLockTests(unittest.TestCase):
    def test_uv_lock_tests_exactly_what_pylock_deploys(self):
        """Every package pywrangler vendors is tested at the vendored version."""
        deployed = tomllib.loads((ROOT / "pylock.toml").read_text())["packages"]
        tested = _locked_versions(ROOT / "uv.lock")
        self.assertTrue(deployed)
        drift = {
            package["name"]: (package["version"], tested.get(package["name"]))
            for package in deployed
            if tested.get(package["name"]) != package["version"]
        }
        self.assertEqual(
            drift,
            {},
            "uv.lock differs from pylock.toml as {name: (deployed, tested)}; "
            "run scripts/align_runtime_lock.py",
        )

    def test_deploys_and_ci_use_the_committed_pylock(self):
        makefile = (ROOT / "Makefile").read_text()
        verify_workflow = (ROOT / ".github" / "workflows" / "verify.yml").read_text()
        self.assertIn("git diff --exit-code -- pylock.toml", makefile)
        self.assertIn("git diff --exit-code -- pylock.toml", verify_workflow)


if __name__ == "__main__":
    unittest.main()
