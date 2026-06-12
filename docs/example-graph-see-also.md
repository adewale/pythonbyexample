# See also links and the example graph

The catalog should stay readable as a linear tour, but Python concepts are not purely linear. `See also` links turn the examples into a small concept graph without adding visual noise to every paragraph.

## Why add them

- **Boundaries become explicit.** A page can point to the neighboring feature learners often confuse it with: `break` vs loop `else`, comprehensions vs generator expressions, `assert` vs exceptions, property vs method.
- **Prerequisites and follow-ups are visible.** A syntax page can stay compact while sending readers to the examples that explain the underlying model.
- **Coverage becomes auditable.** If every edge points to a real slug, tests can catch broken conceptual links and make missing syntax harder to overlook.
- **The site becomes a graph, not just a list.** Previous/next remains the recommended path; See also links expose cross-cutting concepts.

## Risks

- **Too many links can dilute the page.** Use two to four links, not a tag cloud.
- **Circular links can feel arbitrary.** Cycles are fine when concepts truly reinforce each other, but every edge should answer “why should I read this next?”
- **Maintenance cost increases.** Renaming or deleting a slug must update graph edges. Automated tests should validate every `see_also` slug.
- **SEO and crawl shape changes.** Internal links help discovery, but repeated boilerplate links should not crowd the main lesson.

## Design rule

`See also` should be reserved for conceptual edges:

- prerequisite: `yield-from` → `generators`
- contrast: `assignment-expressions` → `conditionals`
- continuation: `async-iteration-and-context` → `async-await`
- shared mechanism: `delete-statements` → `mutability`

Do not use it as a category list. The home page and previous/next navigation already provide the linear table of contents.

## Current implementation

Example Markdown frontmatter may include:

```toml
see_also = [
  "for-loops",
  "while-loops",
]
```

The loader exposes `see_also`, the example renderer displays a compact `See also` section, and tests verify that every linked slug exists and does not point to itself.

## Graph audit

`scripts/audit_example_graph.py` reports orphan pages, high in-degree pages, and reciprocal links. Its `--check` mode runs in `make quality-checks` and fails the build on broken targets, self-links, out-degree above 4, or orphaned examples.

## Future improvements

- Show short edge labels later, e.g. `contrast`, `prerequisite`, `next depth`.
- Use graph data to recommend examples on 404 pages or search results.
- Keep the first version minimal until we know the links improve reading rather than distracting from the code.
