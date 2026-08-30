"""Structured properties for the Markdown example source boundary."""

import json
import unittest

from hypothesis import given
from hypothesis import strategies as st
from src.example_loader import _split_frontmatter

TOML_TEXT = st.text(
    alphabet=st.characters(blacklist_categories=("Cc", "Cs")),
    max_size=200,
)
MARKDOWN_BODY = st.text(max_size=1_000)


class ExampleSourceParserProperties(unittest.TestCase):
    @given(slug=TOML_TEXT, title=TOML_TEXT, body=MARKDOWN_BODY)
    def test_toml_frontmatter_round_trips_without_changing_markdown(
        self,
        slug,
        title,
        body,
    ):
        """Generated TOML metadata and arbitrary Markdown stay separated."""
        source = (
            "+++\n"
            f"slug = {json.dumps(slug, ensure_ascii=False)}\n"
            f"title = {json.dumps(title, ensure_ascii=False)}\n"
            "+++\n"
            f"{body}"
        )

        metadata, parsed_body, body_line = _split_frontmatter(
            source,
            "generated.md",
        )

        self.assertEqual(metadata, {"slug": slug, "title": title})
        self.assertEqual(parsed_body, body)
        self.assertEqual(body_line, 5)


if __name__ == "__main__":
    unittest.main()
