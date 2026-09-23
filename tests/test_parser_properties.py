"""Structured properties for the Markdown example source boundary."""

import json
import unittest

from hypothesis import example, given
from hypothesis import strategies as st
from src.example_loader import _split_frontmatter

TOML_TEXT = st.text(
    alphabet=st.characters(blacklist_categories=("Cc", "Cs")),
    max_size=200,
)
MARKDOWN_BODY = st.text(max_size=1_000)


class ExampleSourceParserProperties(unittest.TestCase):
    @example(
        slug="frontmatter +++ marker",
        title='quote " and backslash \\',
        extra_values=["metadata +++ delimiter"],
        body="before\n+++\nafter",
    )
    @given(
        slug=TOML_TEXT,
        title=TOML_TEXT,
        extra_values=st.lists(TOML_TEXT, max_size=6),
        body=MARKDOWN_BODY,
    )
    def test_toml_frontmatter_round_trips_without_changing_markdown(
        self,
        slug,
        title,
        extra_values,
        body,
    ):
        """Generated TOML metadata and arbitrary Markdown stay separated."""
        expected_metadata = {"slug": slug, "title": title}
        expected_metadata.update(
            {f"extra_{index}": value for index, value in enumerate(extra_values)}
        )
        frontmatter_lines = [
            f"{key} = {json.dumps(value, ensure_ascii=False)}"
            for key, value in expected_metadata.items()
        ]
        source = "+++\n" + "\n".join(frontmatter_lines) + "\n+++\n" + body

        metadata, parsed_body, body_line = _split_frontmatter(
            source,
            "generated.md",
        )

        self.assertEqual(metadata, expected_metadata)
        self.assertEqual(parsed_body, body)
        self.assertEqual(body_line, len(frontmatter_lines) + 3)


if __name__ == "__main__":
    unittest.main()
