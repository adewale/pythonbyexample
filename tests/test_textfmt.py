import unittest

from src.textfmt import render_inline


class RenderInlineTests(unittest.TestCase):
    def test_escapes_plain_code_and_link_text(self):
        rendered = render_inline('<img src=x> `a < b` [<safe>](/examples/values)')
        self.assertIn('&lt;img src=x&gt;', rendered)
        self.assertIn('<code class="syntax-inline">a &lt; b</code>', rendered)
        self.assertIn('<a class="text-link" href="/examples/values">&lt;safe&gt;</a>', rendered)

    def test_only_valid_internal_links_become_anchors(self):
        rendered = render_inline('[outside](https://example.test) [bad](/nope) [journey](/journeys/runtime)')
        self.assertIn('[outside](https://example.test)', rendered)
        self.assertIn('[bad](/nope)', rendered)
        self.assertIn('<a class="text-link" href="/journeys/runtime">journey</a>', rendered)

    def test_unmatched_backtick_remains_escaped_code_boundary(self):
        self.assertEqual(render_inline('before `unterminated'), 'before <code class="syntax-inline">unterminated</code>')


if __name__ == '__main__':
    unittest.main()
