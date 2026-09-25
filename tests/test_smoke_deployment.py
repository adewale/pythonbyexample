import contextlib
import importlib.util
import io
import os
import pathlib
import sys
import unittest
import urllib.error
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_smoke_module():
    spec = importlib.util.spec_from_file_location("smoke_deployment", ROOT / "scripts" / "smoke_deployment.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class SmokeDeploymentTests(unittest.TestCase):
    def test_post_expectation_checks_output_panel_not_textarea(self):
        smoke = load_smoke_module()
        body = """
        <textarea>print('runtime-smoke-values')</textarea>
        <section class="runner-panel output-panel"><h3>Output</h3><pre><code>Verification required before running edited code.</code></pre></section>
        """

        self.assertNotIn("runtime-smoke-values", smoke.output_panel_text(body))
        self.assertIn("Verification required", smoke.output_panel_text(body))

    def test_output_panel_text_unescapes_runtime_output(self):
        smoke = load_smoke_module()
        body = '<section class="runner-panel output-panel"><pre><code>&lt;ok&gt;\n</code></pre></section>'

        self.assertEqual(smoke.output_panel_text(body), "<ok>\n")

    def test_smoke_bypass_secret_requires_https_origin(self):
        smoke = load_smoke_module()

        self.assertIsNone(smoke.validate_smoke_bypass_origin("http://localhost:9696", ""))
        self.assertIsNone(smoke.validate_smoke_bypass_origin("https://example.dev", "secret"))
        self.assertIn(
            "https://",
            smoke.validate_smoke_bypass_origin("http://example.dev", "secret"),
        )


OK_PROBE_REPORT = {"challenge_mode": "session", "ok": True, "secret": "valid", "site_key_configured": True}


class TurnstileProbeSmokeTests(unittest.TestCase):
    """Bypass-authenticated smoke must still prove the deployed Turnstile secret."""

    def setUp(self):
        self.smoke = load_smoke_module()
        self.probes = []

    def run_smoke(self, report=None, *, secret="smoke-secret", probe_error=None):
        smoke = self.smoke

        def fake_probe(base_url, smoke_bypass_secret):
            self.probes.append((base_url, smoke_bypass_secret))
            if probe_error is not None:
                raise probe_error
            return report

        def fake_post(url, code, smoke_bypass_secret=""):
            expected = next(marker for _, source, marker in smoke.POST_SMOKES if source == code)
            return 200, f'<section class="output-panel"><pre><code>{expected}</code></pre></section>'

        stdout, stderr = io.StringIO(), io.StringIO()
        env = {"PBE_SMOKE_BYPASS_SECRET": secret} if secret else {}
        with (
            mock.patch.object(smoke, "fetch", lambda url: (200, "<html>ok</html>")),
            mock.patch.object(smoke, "post_code", fake_post),
            mock.patch.object(smoke, "probe_turnstile", fake_probe),
            mock.patch.object(sys, "argv", ["smoke_deployment.py", "https://www.pythonbyexample.dev"]),
            mock.patch.dict(os.environ, env, clear=True),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            code = smoke.main()
        return code, stdout.getvalue(), stderr.getvalue()

    def test_working_secret_passes_and_is_reported(self):
        code, stdout, _ = self.run_smoke(OK_PROBE_REPORT)
        self.assertEqual(code, 0)
        self.assertEqual(self.probes, [("https://www.pythonbyexample.dev/", "smoke-secret")])
        self.assertIn("Turnstile secret valid, mode session", stdout)
        self.assertIn("Deployment smoke OK", stdout)

    def test_bad_secret_fails_smoke_even_though_bypassed_runs_pass(self):
        report = {**OK_PROBE_REPORT, "ok": False, "secret": "invalid", "error_codes": ["invalid-input-secret"]}
        code, _, stderr = self.run_smoke(report)
        self.assertEqual(code, 1)
        self.assertIn("Siteverify rejects TURNSTILE_SECRET_KEY", stderr)
        self.assertIn("invalid-input-secret", stderr)

    def test_missing_probe_route_or_wrong_bypass_secret_fails(self):
        error = urllib.error.HTTPError("https://www.pythonbyexample.dev/__smoke/turnstile", 404, "Not Found", {}, None)
        code, _, stderr = self.run_smoke(probe_error=error)
        self.assertEqual(code, 1)
        self.assertIn("HTTP 404", stderr)

    def test_without_bypass_secret_the_probe_is_skipped_not_failed(self):
        code, stdout, _ = self.run_smoke(secret="")
        self.assertEqual(self.probes, [])
        self.assertIn("SKIP", stdout)
        self.assertEqual(code, 0)

    def test_probe_problems_name_the_misconfiguration(self):
        problem = self.smoke.turnstile_probe_problem
        self.assertIsNone(problem(OK_PROBE_REPORT))
        self.assertIsNone(problem({"ok": True, "secret": "absent", "site_key_configured": False}))
        self.assertIn("test secret", problem({"ok": False, "secret": "testing_key"}))
        self.assertIn(
            "TURNSTILE_SITE_KEY", problem({"ok": False, "secret": "valid", "site_key_configured": False})
        )
        self.assertIn("could not reach Siteverify", problem({"ok": False, "secret": "unverified"}))
        self.assertIn("internal-error", problem({"ok": False, "secret": "unexpected", "error_codes": ["internal-error"]}))
        self.assertIn("unrecognized", problem({"ok": False, "secret": "new-state"}))


if __name__ == "__main__":
    unittest.main()
