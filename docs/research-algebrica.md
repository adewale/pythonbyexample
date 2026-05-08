# Research note: Algebrica

Sources:

- <https://github.com/antoniolupetti/algebrica>
- <https://algebrica.org>

Algebrica is a free, ad-free mathematics knowledge base whose repository publishes source Markdown and editable SVG diagrams. Its README describes an editorial goal that is directly relevant to Python By Example: **reduce without distorting**. Pages are written from multiple university-level sources, reconciled into a coherent exposition, and revised as adjacent pages expose gaps or inconsistencies.

## What we can learn

### 1. Strong pages have a deliberate progression

Algebrica pages do not read like disconnected fact lists. A page such as `definite-integrals` moves through a clear learning arc:

```text
geometric intuition
→ approximation
→ formal definition
→ computation rule
→ properties
→ worked examples
→ edge cases
→ links to deeper pages
```

For Python By Example, broad examples should have a comparable editorial progression:

```text
why this exists
→ smallest concrete form
→ runtime/protocol model
→ common operations
→ boundary or edge case
→ worked output
→ neighboring concepts
```

The former `Operators and Literals` page failed this test: it sampled useful syntax but did not provide a coherent map. Splitting it into `Operators` and `Literals` improved the title-to-content contract.

### 2. Reduce without distorting

Small examples are valuable only when they preserve the concept. If an example compresses too much into one cell, it can become technically correct but educationally shallow.

Example risk:

```text
Bytes and Bytearray: encode, length contrast, decode, and mutation all in one cell.
```

Better progression:

```text
text → UTF-8 bytes
bytes → text
bytes indexing / immutability
bytearray mutation
```

### 3. Broad concepts need maps, not sample trays

Algebrica handles broad topics by organizing subtopics. It does not merely sample a few facts and hope the title carries the rest.

For us, broad pages should either:

1. be scoped explicitly as a first pass / surface map, with links to focused neighbors; or
2. be split into narrower examples.

Examples that need this discipline include `Testing`, `Modules`, `Packages`, `Type Hints`, `Operators`, `Literals`, `Bytes and Bytearray`, and the type-system cluster.

### 4. Teaching artifacts should be inspectable

Algebrica releases source Markdown and editable SVGs. The lesson is not that Python By Example needs more diagrams; it is that core teaching artifacts should be inspectable, reusable, and versioned.

For Python By Example, the inspectable artifacts are:

- Markdown examples
- `:::program` complete runner source
- `:::cell` teaching fragments
- expected output
- official docs links
- generated embedded source
- tests and golden parity fixtures
- rubric and lessons learned docs

### 5. Cross-links should express prerequisites and next depth

Algebrica links to prerequisite concepts and deeper topics as part of the explanation, not as decorative tags.

For us, `See also` links should keep behaving like a conceptual graph:

```text
operators → assignment-expressions, operator-overloading
literals → strings, bytes-and-bytearray, dicts
bytes-and-bytearray → strings, networking
 type-aliases → type-hints, newtype
```

### 6. Edge cases belong near the main idea

The definite-integrals page introduces positive/negative area and improper integrals after the main computation story. Edge cases are part of the concept, not trivia hidden at the end.

For Python examples, this suggests adding visible boundary cells for common misunderstandings:

- `json`: non-JSON Python objects or decode errors
- `testing`: failing-test output or what the result object records
- `bytes-and-bytearray`: indexing bytes yields integers; `bytes` is immutable
- `type-hints`: hints inform tools but do not enforce runtime behavior
- `operators`: precedence and parentheses

### 7. Process transparency builds trust

Algebrica documents editorial process, source reuse, licensing, and revision. Python By Example should continue to surface its own trust signals:

- official Python docs links
- deterministic expected output
- verification scripts
- CI
- cache/versioning checks
- public Markdown source
- quality rubric
- lessons learned

## Rubric changes implied

Add or strengthen these rubric checks:

1. **Editorial progression** — broad examples need a visible sequence, not a grab bag.
2. **Scope contract** — title, summary, and first paragraphs must match the breadth of the code.
3. **Reduction without distortion** — examples may be small, but not at the cost of removing a necessary boundary, contrast, or edge case.
4. **Map-or-split rule** — broad pages must either become surface maps with links to focused neighbors or be split into narrower pages.
5. **Edge case placement** — common edge cases should appear in cells or concrete notes near the main idea.
6. **Inspectable artifact quality** — Markdown source should remain clean enough to serve as public educational material, not merely runtime input.
7. **Conceptual links as graph edges** — `See also` should mark prerequisite/neighbor/next-depth relationships.

## Known improvement queue

### Improve existing examples

High priority:

- `bytes-and-bytearray` — split one compressed cell into encode/decode/immutability-mutation cells.
- `type-aliases` — replace generic prose; contrast `type` aliases, assignment-style aliases, and `NewType`.
- `operators` — monitor for sample-tray drift; add precedence/parentheses if readers need it.
- `literals` — keep as source-syntax map; ensure it does not pretend to teach every value type deeply.

Type-system cluster:

- `runtime-type-checks`
- `union-and-optional-types`
- `typed-dicts`
- `callable-types`
- `generics-and-typevar`
- `casts-and-any`
- `newtype`

Each should gain at least one contrast cell showing static-tool meaning versus runtime behavior or misuse boundary.

Medium priority:

- `numbers` — link complex literal syntax to `literals`; consider future `decimal-and-fractions`.
- `modules` — scope as imports/namespaces; consider entry-point/import-system follow-ups.
- `packages` — optionally add an illustrative package tree as `:::unsupported` or prose.
- `regular-expressions` — keep scoped as first pass; consider flags/substitution only as focused follow-ups.
- `testing` — consider failing-test output or fixtures if deterministic output stays readable.
- `json` — consider indentation, decode errors, or non-JSON objects as a boundary cell.
- `decorators` — consider `functools.wraps` metadata preservation.
- `context-managers` — consider a small `__enter__` / `__exit__` protocol cell or stronger link to data model examples.
- `exceptions` — consider `else` / `finally` cleanup if reliability coverage needs it.

### Create new examples

Potential focused pages:

- `decimal-and-fractions`
- `module-entry-points`
- `import-system`
- `regex-substitution`
- `regex-flags`
- `test-fixtures`
- `pytest-style-tests`
- `json-errors`
- `operator-precedence`
- `exception-cleanup`

### Journey changes to consider

- **Runtime** — ensure `Literals` and `Operators` remain placed by prerequisite logic, not catalog convenience.
- **Control Flow** — keep `Operators` before `Conditionals` only while the page covers comparisons and boolean expressions.
- **Types** — add contrast cells before adding more type pages; avoid a long list of shallow type examples.
- **Reliability** — consider whether `Testing`, `Logging`, `Exceptions`, and cleanup examples form a stronger progression if `exception-cleanup` or `test-fixtures` is added.
- **Interfaces** — keep the data-model sequence coherent: `Special Methods` → focused protocol pages → `Descriptors` → `Metaclasses`.

### Remove or avoid

- Avoid restoring a combined `Operators and Literals` page.
- Avoid broad catch-all pages that merely list syntax without a learning progression.
- Avoid adding new examples to journeys unless they strengthen the story rather than lengthen the index.
