# Shallow example audit

This audit looks for examples that may surprise readers by being narrower than their title, summary, or journey placement suggests. The main smell is the **broad surface tour problem**: a page title sounds like a tour of a feature family, but the example demonstrates one small slice without enough scoping, contrast, or links to neighbors.

## Method

Signals used:

- broad titles such as `Operators`, `Literals`, `Testing`, `Packages`, `Regular Expressions`, `Type Hints`, `Async Await`, `Special Methods`, `Modules`, `JSON`, `Numbers`
- one-cell or two-cell examples for multi-part concepts
- very short programs under broad titles
- prose that scopes the page poorly or uses generic boilerplate
- missing nearby syntax that a learner would reasonably expect on the page
- journey order that hides prerequisites

This is a qualitative audit. Passing verification proves examples run; it does not prove they are comprehensive enough for their title.

## Recently fixed broad-surface issue

### Former combined `Operators and Literals`

Status: **split into `Operators` and `Literals`**.

Why it surprised:

- The title promised a large surface: operators plus literals.
- The page sampled raw strings, bytes, complex numbers, bit operators, set symmetric difference, `@`, `...`, and `:=`.
- That was useful surface coverage, but it read like a grab bag rather than a coherent map of Python's operator/literal families.

What changed:

- `Operators` now focuses on expression syntax that combines, compares, and tests values.
- `Literals` now focuses on source-code forms that create values directly.
- Runtime and Control Flow journeys now point to the narrower pages.
- `Operators` links to `Assignment Expressions`; `Literals` links to focused value/container/text pages.

Expected rubric impact:

- `Operators`: approximately **8.8-9.2** if it keeps its surface-map framing and avoids becoming an all-operators reference page.
- `Literals`: approximately **8.7-9.1** if it remains a value-syntax map and keeps links to focused pages.

Remaining watch point:

- `Operators` still covers a lot of syntax. If it starts to feel like a table of punctuation, split out `operator-precedence` or keep precedence as a note only.

## Recently fixed shallow examples

### `bytes-and-bytearray`

Status: **fixed**.

What changed:

- Split one compressed cell into encode, decode, byte indexing, and `bytearray` mutation cells.
- Added the important boundary that indexing `bytes` returns integers.
- Linked the page to `strings`, `literals`, and `networking`.

### `type-aliases`

Status: **fixed**.

What changed:

- Replaced generic boilerplate with a sharper static-shape explanation.
- Added separate cells for the `type` statement, runtime alias names, and assignment-style aliases.
- Explicitly contrasted aliases with `NewType`.

### Type-system cluster single-cell examples

Affected pages:

- `runtime-type-checks`
- `union-and-optional-types`
- `typed-dicts`
- `callable-types`
- `generics-and-typevar`
- `casts-and-any`
- `newtype`

Status: **fixed for the first pass**.

What changed:

- Added static-vs-runtime or boundary contrast cells across the cluster.
- `runtime-type-checks` now separates exact type, inheritance-aware checks, and class relationships.
- `union-and-optional-types` now shows narrowing and visible runtime annotations.
- `typed-dicts` now shows ordinary dict runtime behavior and optional keys.
- `callable-types` now contrasts functions with callable objects.
- `generics-and-typevar` now shows input/output type relationships and runtime annotations.
- `casts-and-any` now shows that `cast()` returns the same object and contrasts with runtime narrowing.
- `newtype` now contrasts static identity with runtime integer behavior.

## Medium-priority findings

### `numbers`

Status: **improved, still introductory**.

What was fixed:

- Added complex numbers to the numeric story instead of leaving them only in `Literals`.
- Added visible floating-point approximation output.
- Linked to `Literals` and `Operators`.

Remaining gap:

- Decimal and fraction arithmetic remain separate future topics.

### `modules`

Status: **improved, still introductory**.

What was fixed:

- Added explicit scoping: this page is about import forms and namespaces.
- Added `sys.modules` cache evidence.
- Linked to `Import Aliases` and `Packages`.

Remaining gap:

- Module search paths, side effects, entry points, reloads, and relative imports remain separate future topics.

### `packages`

Status: **improved, still introductory**.

What was fixed:

- Replaced generic boilerplate.
- Split package-as-module, dotted imports, and dynamic import into separate cells.

Remaining gap:

- Does not show real on-disk package layout because examples cannot create a project tree naturally in the runner.

Recommendation:

- Add an unsupported/illustrative layout snippet if needed:
  `project/pkg/__init__.py`, `project/pkg/models.py`.

### `regular-expressions`

Status: **improved, still first-pass**.

What was fixed:

- Split repeated extraction, first-match groups, and string-method alternative.

Remaining gap:

- No substitution, flags, compiled patterns, anchors, or greedy/non-greedy behavior.

Recommendation:

- Keep current page scoped as first pass.
- Add future `regex-substitution` or `regex-flags` only if the catalog needs deeper text coverage.

### `testing`

Status: **improved, still minimal**.

What was fixed:

- Replaced generic boilerplate.
- Shows named test methods, assertions, suite, runner result.

Remaining gap:

- No failure output, fixtures, parameterization, mocks, or pytest comparison.

Recommendation:

- Add a deliberate failing-test cell only if the page can keep deterministic output readable.
- Consider future `test-fixtures` or `pytest-style-tests` example.

### `json`

Status: **improved, mostly acceptable**.

What was fixed:

- Added `indent=2` formatting evidence.
- Added invalid JSON boundary with `JSONDecodeError`.
- Linked to dictionaries, `TypedDict`, and strings.

Remaining gap:

- File helpers (`dump`/`load`) and custom encoders remain separate advanced topics.

## Lower-priority findings

### `decorators`

Status: **improved**.

What was fixed:

- Added `functools.wraps` to the example and showed preserved metadata.
- Linked to closures, functions, and callable types.

### `context-managers`

Status: **improved**.

What was fixed:

- Added a class-based `__enter__` / `__exit__` cell.
- Kept `contextlib.contextmanager` as the concise neighboring form.
- Added the exception propagation/suppression boundary.

### `exceptions`

Status: **adequate first pass**.

Gap:

- Does not show `else`/`finally`; those may be expected under exceptions.

Recommendation:

- Consider an `exception-cleanup` example if reliability coverage needs it.

### `async-await`

Status: **acceptable because scoped**.

Why acceptable:

- It clearly focuses on coroutine creation, `await`, and `gather`.
- `async-iteration-and-context` covers neighboring async protocols.

Gap:

- No cancellation, tasks, timeouts, or task groups.

Recommendation:

- Do not expand this page into all async. Add focused pages if needed.

### `type-hints`

Status: **acceptable because scoped and journey-supported**.

Why acceptable:

- It draws the important static-vs-runtime boundary.
- The Types journey has focused neighbors for unions, aliases, protocols, callables, generics, `Any`, and `NewType`.

Gap:

- Could link more explicitly to those neighbors.

## Action list

Completed:

- Split `Operators and Literals` into `Operators` and `Literals`.
- Expanded `bytes-and-bytearray` into multiple boundary cells.
- Rewrote `type-aliases` with contrast and multiple cells.
- Added static-vs-runtime contrast cells to the shallow type-system cluster.

Remaining:

1. Consider focused follow-up examples such as `decimal-and-fractions`, `module-entry-points`, `import-system`, `operator-precedence`, and `exception-cleanup`.
2. Continue auditing broad pages after each new journey change; broadness can return when examples are moved or renamed.
