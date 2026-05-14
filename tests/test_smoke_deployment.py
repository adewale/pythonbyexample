import importlib.util
import pathlib
import unittest

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


if __name__ == "__main__":
    unittest.main()
