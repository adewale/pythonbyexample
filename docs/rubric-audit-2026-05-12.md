# Rubric audit snapshot — 2026-05-12

> **Superseded.** This is a point-in-time snapshot. The catalog has since dropped the Workers journey (journey sections went from 24 to 21) and the figure registry grew past a one-per-slug count. The journey-section counts below have been corrected to the current 21; regenerate a fresh snapshot with `make rubric-audit` rather than trusting the rest of these frozen numbers.

This snapshot audits the shipped catalog against the example, example-figure, and journey-visualisation rubrics. It records the green baseline and the accepted exception so future passes can hunt for semantic drift instead of rediscovering the same ledgers.

## Scoreboard

- Examples: count=109, min=7.1, avg=8.98, median=9, below9=1, distribution=7.1 × 1, 9 × 108
- Example diagrams: count=109, min=9, avg=9.01, median=9, below9=0, distribution=9 × 106, 9.5 × 3
- Journey diagrams: count=21, min=9, avg=9.02, median=9, below9=0, distribution=9 × 20, 9.5 × 1
- Accepted waiver: `hello-world` remains intentionally tiny at 7.1.
- Graph health: 109 linked sources, 361 edges, 0 orphaned examples.

## Example rubric dimensions

| Dimension | Evidence | Result |
| --- | --- | --- |
| Conceptual payoff | Curated score registry + criterion search | PASS |
| Rationale | Criterion search + notes-supported gate | PASS |
| Alternatives and boundaries | Confusable pairs, footguns, broad tours, graph edges | PASS |
| Executable determinism | `verify_examples.py` over every program and cell | PASS |
| Python idiom and accuracy | Python 3.13 verification, docs links, Ruff | PASS |
| Literate fit | Markdown parser requires prose beside every cell | PASS |
| Source/result pairing | Every runnable cell carries expected output | PASS |
| Concept decomposition | Criterion search + curated score floor | PASS |
| Progressive walkthrough | Cell sequence review + criterion search | PASS |
| Representative coverage | Broad-surface and syntax-surface gates | PASS |
| Practical usefulness | Criterion search + editorial score comments | PASS |
| Editorial progression | Quality registry + graph audit | PASS |

## Example-figure rubric dimensions

| Dimension | Evidence | Result |
| --- | --- | --- |
| Cell fidelity | Attachment anchor resolves to a real teaching cell | PASS |
| Earns its place | Curated figure scores; all example figures >= 9.0 | PASS |
| One conceptual move | Figure score rationale + emphasis-scarcity contract | PASS |
| Mechanism over metaphor | Canvas grammar uses bindings, arrows, cells, lanes, boundaries | PASS |
| Caption quality | Unique declarative figcaptions | PASS |
| Grammar conformance | Palette, font, and stroke contracts | PASS |
| Emphasis scarcity | At most one accent mark per figure | PASS |
| Restraint | Locked primitive grammar; no bespoke SVG | PASS |
| Banner-row fit | Intrinsic-width contract | PASS |
| Pairs with surrounding cell | Anchor/cell semantic pass + score registry | PASS |

## Journey-visualisation rubric dimensions

| Dimension | Evidence | Result |
| --- | --- | --- |
| Section fidelity | Section figure keyed by journey section title | PASS |
| Pedagogical scope | Section-level captions and score rationales | PASS |
| One conceptual move | One figure per section and one emphasis mark | PASS |
| Mechanism over metaphor | Canvas primitives show protocols, boundaries, lanes, or flows | PASS |
| Caption alignment | Section figure captions unique and declarative | PASS |
| Grammar conformance | Shared geometry contracts | PASS |
| Independence from lesson figures | Section figures compared with example attachments | PASS |
| Layout fit | Journey figure dimensions within production column | PASS |
| Outcome support | `check_journey_outcomes.py` over all 21 sections | PASS |
| Prerequisite order | Journey order reviewed against lesson dependencies | PASS |

## Example and diagram inventory

| Slug | Quality | Heuristic | Cells | Notes | Edges | Figure | Anchor | Fig score | Weakest heuristic axes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hello-world | 7.1 | 8.3 | 1 | 2 | 2 | program-output | cell-0 | 9.0 | alternatives_and_boundaries=0.25, concept_decomposition=0.58, representative_coverage=0.65 |
| values | 9.0 | 9.3 | 3 | 3 | 4 | value-types | cell-0 | 9.0 | alternatives_and_boundaries=0.25, practical_usefulness=0.80, conceptual_payoff=1.00 |
| literals | 9.0 | 9.6 | 6 | 4 | 4 | literal-forms | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.97, rationale=1.00 |
| numbers | 9.0 | 9.4 | 4 | 4 | 2 | number-lines | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| booleans | 9.0 | 9.8 | 3 | 4 | 3 | boolean-truth-table | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=1.00, rationale=1.00 |
| operators | 9.0 | 9.4 | 6 | 4 | 4 | expression-tree | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.80, rationale=1.00 |
| none | 9.0 | 9.6 | 3 | 3 | 4 | none-singleton | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.97, rationale=1.00 |
| variables | 9.0 | 9.3 | 3 | 3 | 4 | variables-bind | cell-0 | 9.5 | alternatives_and_boundaries=0.50, conceptual_payoff=0.80, practical_usefulness=0.80 |
| constants | 9.0 | 9.4 | 3 | 3 | 3 | variables-bind | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.97 |
| truthiness | 9.0 | 9.5 | 3 | 2 | 4 | truthy-check | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.87, rationale=1.00 |
| equality-and-identity | 9.0 | 9.4 | 4 | 4 | 4 | identity-and-equality | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| mutability | 9.0 | 9.4 | 3 | 3 | 4 | aliasing-mutation | cell-0 | 9.5 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| object-lifecycle | 9.0 | 8.7 | 2 | 3 | 3 | object-lifecycle | cell-0 | 9.0 | alternatives_and_boundaries=0.25, rationale=0.65, concept_decomposition=0.80 |
| strings | 9.0 | 9.5 | 3 | 5 | 4 | codepoints-bytes | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| bytes-and-bytearray | 9.0 | 9.5 | 4 | 4 | 3 | bytes-vs-bytearray | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| string-formatting | 9.0 | 9.2 | 3 | 3 | 4 | format-spec | cell-1 | 9.0 | alternatives_and_boundaries=0.25, conceptual_payoff=0.80, rationale=1.00 |
| conditionals | 9.0 | 9.3 | 3 | 3 | 4 | branch-fork | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.87 |
| guard-clauses | 9.0 | 9.2 | 2 | 3 | 3 | guard-clauses | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| assignment-expressions | 9.0 | 9.2 | 2 | 3 | 3 | naming-decisions | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| for-loops | 9.0 | 9.5 | 3 | 3 | 3 | iterator-unroll | cell-1 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.90, rationale=1.00 |
| break-and-continue | 9.0 | 9.4 | 2 | 3 | 3 | early-exit | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| loop-else | 9.0 | 9.3 | 2 | 3 | 3 | loop-else-gate | cell-0 | 9.0 | alternatives_and_boundaries=0.50, representative_coverage=0.75, concept_decomposition=0.80 |
| iterating-over-iterables | 9.0 | 9.7 | 3 | 3 | 3 | iter-protocol | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.93, rationale=1.00 |
| iterators | 9.0 | 9.6 | 3 | 3 | 3 | iter-protocol | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| iterator-vs-iterable | 9.0 | 9.6 | 4 | 3 | 3 | iter-protocol | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.97, rationale=1.00 |
| sentinel-iteration | 9.0 | 9.1 | 2 | 3 | 3 | sentinel-iteration | cell-0 | 9.0 | alternatives_and_boundaries=0.50, representative_coverage=0.75, concept_decomposition=0.80 |
| match-statements | 9.0 | 9.4 | 3 | 3 | 4 | match-dispatch-ladder | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.93 |
| advanced-match-patterns | 9.0 | 9.4 | 3 | 3 | 3 | match-pattern-variants | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| while-loops | 9.0 | 9.2 | 2 | 3 | 3 | loop-repetition | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| lists | 9.0 | 9.3 | 3 | 3 | 4 | list-append | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.87 |
| tuples | 9.0 | 9.5 | 4 | 4 | 3 | tuple-frozen | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.87, rationale=1.00 |
| unpacking | 9.0 | 9.7 | 3 | 3 | 4 | unpacking-bind | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.90, rationale=1.00 |
| dicts | 9.0 | 9.6 | 4 | 4 | 4 | dict-buckets | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=1.00, rationale=1.00 |
| sets | 9.0 | 9.5 | 3 | 4 | 3 | set-buckets | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=0.87 |
| slices | 9.0 | 9.0 | 2 | 3 | 3 | slice-ruler | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.80, concept_decomposition=0.80 |
| comprehensions | 9.0 | 9.5 | 3 | 4 | 4 | comprehension-equivalence | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.90, rationale=1.00 |
| comprehension-patterns | 9.0 | 9.1 | 2 | 3 | 3 | comprehension-equivalence | cell-0 | 9.0 | alternatives_and_boundaries=0.70, representative_coverage=0.75, concept_decomposition=0.80 |
| sorting | 9.0 | 9.6 | 3 | 3 | 3 | sort-stability | cell-1 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=1.00, rationale=1.00 |
| collections-module | 9.0 | 9.8 | 3 | 3 | 4 | collections-containers | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=1.00, rationale=1.00 |
| copying-collections | 9.0 | 9.6 | 3 | 3 | 3 | aliasing-mutation | cell-0 | 9.5 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| functions | 9.0 | 9.4 | 4 | 4 | 4 | function-with-body | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.97 |
| keyword-only-arguments | 9.0 | 9.2 | 3 | 3 | 4 | kw-only-separator | cell-0 | 9.0 | alternatives_and_boundaries=0.25, practical_usefulness=0.80, conceptual_payoff=0.87 |
| positional-only-parameters | 9.0 | 9.0 | 2 | 3 | 3 | positional-only-separator | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.80, concept_decomposition=0.80 |
| args-and-kwargs | 9.0 | 9.6 | 3 | 3 | 4 | args-kwargs | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.80, rationale=1.00 |
| multiple-return-values | 9.0 | 9.0 | 2 | 3 | 3 | multiple-return | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| closures | 9.0 | 9.2 | 3 | 4 | 4 | closure-cell | cell-0 | 9.0 | alternatives_and_boundaries=0.25, practical_usefulness=0.80, conceptual_payoff=0.93 |
| partial-functions | 9.0 | 9.6 | 3 | 3 | 3 | partial-functions | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| scope-global-nonlocal | 9.0 | 9.2 | 2 | 3 | 3 | scope-rings | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| recursion | 9.0 | 9.0 | 2 | 3 | 3 | call-stack | cell-1 | 9.0 | alternatives_and_boundaries=0.50, representative_coverage=0.75, concept_decomposition=0.80 |
| lambdas | 9.0 | 9.7 | 3 | 3 | 3 | lambda-expression | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.90, rationale=1.00 |
| generators | 9.0 | 9.6 | 4 | 4 | 3 | generator-ribbon | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=1.00 |
| yield-from | 9.0 | 9.0 | 2 | 3 | 3 | yield-delegation | cell-0 | 9.0 | alternatives_and_boundaries=0.50, representative_coverage=0.75, concept_decomposition=0.80 |
| generator-expressions | 9.0 | 9.4 | 3 | 3 | 4 | lazy-stream | cell-1 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| itertools | 9.0 | 9.6 | 3 | 4 | 4 | itertools-chain | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| decorators | 9.0 | 9.2 | 3 | 3 | 4 | decorator-rebind | cell-0 | 9.0 | alternatives_and_boundaries=0.25, practical_usefulness=0.80, conceptual_payoff=0.93 |
| classes | 9.0 | 9.4 | 4 | 5 | 4 | class-triangle | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| inheritance-and-super | 9.0 | 9.2 | 2 | 3 | 4 | mro-chain | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| classmethods-and-staticmethods | 9.0 | 9.5 | 4 | 4 | 3 | method-kinds | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| dataclasses | 9.0 | 9.4 | 3 | 3 | 3 | dataclass-fields | cell-0 | 9.0 | alternatives_and_boundaries=0.25, conceptual_payoff=0.93, rationale=1.00 |
| properties | 9.0 | 9.5 | 3 | 3 | 4 | property-fork | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| special-methods | 9.0 | 9.5 | 8 | 6 | 4 | operator-dispatch | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| truth-and-size | 9.0 | 9.6 | 3 | 3 | 3 | truth-and-size | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=1.00 |
| container-protocols | 9.0 | 9.7 | 3 | 3 | 3 | container-methods | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.93, rationale=1.00 |
| callable-objects | 9.0 | 9.5 | 3 | 3 | 4 | callable-objects | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=0.87 |
| operator-overloading | 9.0 | 9.4 | 3 | 3 | 3 | operator-dispatch | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| attribute-access | 9.0 | 9.4 | 3 | 3 | 4 | attribute-lookup | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.93 |
| bound-and-unbound-methods | 9.0 | 9.4 | 4 | 4 | 4 | bound-unbound | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.93 |
| descriptors | 9.0 | 9.3 | 2 | 3 | 3 | descriptor-protocol | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| metaclasses | 9.0 | 9.2 | 2 | 3 | 3 | metaclass-triangle | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| context-managers | 9.0 | 9.5 | 3 | 4 | 3 | context-bowtie | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| delete-statements | 9.0 | 9.6 | 3 | 3 | 3 | delete-name-erased | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| exceptions | 9.0 | 9.5 | 3 | 4 | 4 | exception-lanes | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| assertions | 9.0 | 9.2 | 2 | 3 | 3 | assertion-check | cell-0 | 9.0 | alternatives_and_boundaries=0.50, representative_coverage=0.75, concept_decomposition=0.80 |
| exception-chaining | 9.0 | 9.1 | 2 | 3 | 3 | exception-cause-context | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| exception-groups | 9.0 | 9.1 | 2 | 3 | 3 | exception-group-peel | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| warnings | 9.0 | 9.1 | 2 | 3 | 3 | warning-signal | cell-0 | 9.0 | alternatives_and_boundaries=0.50, concept_decomposition=0.80, representative_coverage=0.80 |
| modules | 9.0 | 9.8 | 4 | 4 | 2 | sys-path-resolution | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=1.00, rationale=1.00 |
| import-aliases | 9.0 | 9.3 | 2 | 4 | 2 | import-alias | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| packages | 9.0 | 9.8 | 4 | 4 | 3 | package-tree | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=1.00, rationale=1.00 |
| virtual-environments | 9.0 | 8.9 | 1 | 3 | 3 | venv-boundary | cell-0 | 9.0 | concept_decomposition=0.58, alternatives_and_boundaries=0.70, representative_coverage=0.75 |
| type-hints | 9.0 | 9.6 | 5 | 5 | 4 | annotation-ghost | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.97, rationale=1.00 |
| runtime-type-checks | 9.0 | 9.6 | 3 | 3 | 4 | isinstance-check | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=0.93 |
| union-and-optional-types | 9.0 | 9.6 | 3 | 3 | 3 | union-types | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.93, rationale=1.00 |
| type-aliases | 9.0 | 9.5 | 3 | 3 | 3 | type-alias-name | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.83, rationale=1.00 |
| typed-dicts | 9.0 | 9.6 | 3 | 3 | 4 | typed-dict-shape | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=1.00, rationale=1.00 |
| structured-data-shapes | 9.0 | 9.8 | 4 | 4 | 4 | structured-shapes | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=1.00, rationale=1.00 |
| literal-and-final | 9.0 | 9.4 | 3 | 3 | 4 | literal-constrained | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.93 |
| callable-types | 9.0 | 9.4 | 3 | 3 | 3 | callable-type | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.90 |
| generics-and-typevar | 9.0 | 9.5 | 3 | 3 | 3 | generic-preservation | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=0.87, rationale=1.00 |
| paramspec | 9.0 | 9.5 | 3 | 3 | 3 | paramspec-preserve | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| overloads | 9.0 | 9.5 | 3 | 3 | 3 | overload-signatures | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| casts-and-any | 9.0 | 9.7 | 3 | 3 | 3 | cast-escape | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.90, rationale=1.00 |
| newtype | 9.0 | 9.4 | 3 | 3 | 3 | newtype-phantom | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.97 |
| protocols | 9.0 | 9.7 | 3 | 3 | 4 | protocol-check | cell-0 | 9.0 | alternatives_and_boundaries=0.70, conceptual_payoff=0.93, rationale=1.00 |
| abstract-base-classes | 9.0 | 9.6 | 4 | 4 | 3 | class-triangle | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=1.00 |
| enums | 9.0 | 9.2 | 2 | 4 | 3 | enum-members | cell-0 | 9.0 | alternatives_and_boundaries=0.70, concept_decomposition=0.80, representative_coverage=0.80 |
| regular-expressions | 9.0 | 9.6 | 6 | 6 | 2 | regex-anchors | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=1.00, rationale=1.00 |
| number-parsing | 9.0 | 9.4 | 3 | 3 | 3 | number-parse | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.97 |
| custom-exceptions | 9.0 | 9.1 | 3 | 3 | 4 | custom-exception-chain | cell-0 | 9.0 | alternatives_and_boundaries=0.50, rationale=0.65, practical_usefulness=0.80 |
| json | 9.0 | 9.5 | 4 | 4 | 3 | json-python-mapping | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=1.00 |
| logging | 9.0 | 9.0 | 2 | 3 | 3 | logging-levels | cell-0 | 9.0 | alternatives_and_boundaries=0.25, concept_decomposition=0.80, representative_coverage=0.80 |
| testing | 9.0 | 9.4 | 3 | 3 | 3 | aaa-pattern | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.97 |
| subprocesses | 9.0 | 8.9 | 1 | 3 | 3 | subprocess-spawn | cell-0 | 9.0 | concept_decomposition=0.58, alternatives_and_boundaries=0.70, representative_coverage=0.75 |
| threads-and-processes | 9.0 | 9.3 | 2 | 3 | 3 | gil-lanes | cell-0 | 9.0 | representative_coverage=0.75, concept_decomposition=0.80, practical_usefulness=0.80 |
| networking | 9.0 | 8.8 | 1 | 3 | 3 | socket-byte-boundary | cell-0 | 9.0 | concept_decomposition=0.58, alternatives_and_boundaries=0.70, representative_coverage=0.75 |
| datetime | 9.0 | 9.6 | 3 | 3 | 3 | datetime-instant | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=1.00 |
| csv-data | 9.0 | 9.6 | 3 | 3 | 3 | csv-records | cell-0 | 9.0 | alternatives_and_boundaries=0.50, conceptual_payoff=1.00, rationale=1.00 |
| async-await | 9.0 | 9.6 | 4 | 4 | 3 | async-swimlane | cell-0 | 9.0 | alternatives_and_boundaries=0.70, practical_usefulness=0.80, conceptual_payoff=1.00 |
| async-iteration-and-context | 9.0 | 9.4 | 3 | 3 | 3 | async-swimlane | cell-0 | 9.0 | alternatives_and_boundaries=0.50, practical_usefulness=0.80, conceptual_payoff=0.93 |

## Journey section inventory

| Journey | Section | Support examples | Outcomes | Figure | Score | Caption |
| --- | --- | --- | --- | --- | --- | --- |
| runtime | Start with executable evidence. | 5 | 4 | runtime-evidence-loop | 9.0 | Examples are evidence loops: source, a run step, and visible output stay together. |
| runtime | Separate value, identity, and absence. | 6 | 4 | runtime-object-axes | 9.0 | Runtime objects answer separate questions: equal value, same identity, or the singleton that marks absence. |
| runtime | Read expressions as object operations. | 5 | 4 | runtime-expression-model | 9.0 | Expression syntax enters the data model; object methods produce the result. |
| control-flow | Choose between paths. | 4 | 4 | control-decision-map | 9.0 | Facts flow into one decision point; exactly one branch owns the next step. |
| control-flow | Name and shape decisions. | 3 | 3 | control-fact-shape | 9.0 | Name a fact when a condition needs it; match shape when the data structure is the decision. |
| control-flow | Stop as soon as the answer is known. | 3 | 3 | control-stop-boundary | 9.0 | Early exits draw a boundary: once the answer is found, the tail stays unread. |
| iteration | Choose the right loop shape. | 5 | 4 | iteration-loop-selector | 9.0 | Choose the loop from its stopping rule: exhaustion, condition, or sentinel marker. |
| iteration | See the protocol behind `for`. | 3 | 3 | iteration-protocol-map | 9.5 | for is surface syntax; iter() creates an iterator and next() pulls values until StopIteration. |
| iteration | Compose lazy value streams. | 3 | 3 | iteration-lazy-pull | 9.0 | Lazy pipelines run from the consumer's pull: next() requests one value through each stage. |
| shapes | Pick the container that matches the question. | 5 | 4 | container-questions | 9.0 | Each container answers a different question: ordered, fixed, lookup, unique. |
| shapes | Move between shapes deliberately. | 6 | 4 | reshape-pipeline | 9.0 | Most everyday code reshapes data: one input, one transform, one new value. |
| shapes | Cross text and data boundaries. | 5 | 4 | text-data-boundary | 9.0 | Programs receive text and produce structured data; parsing makes the boundary explicit. |
| interfaces | Start with functions as named behavior. | 5 | 4 | function-signature | 9.0 | A function is the first abstraction boundary: arguments in, body, return value out. |
| interfaces | Use functions as values. | 6 | 4 | function-as-value | 9.0 | Functions are first-class values. A second name binds to the same function object. |
| interfaces | Bundle behavior with state. | 12 | 4 | class-with-state | 9.0 | Classes group fields and methods so data and behavior move together behind one interface. |
| types | Keep runtime and static analysis separate. | 4 | 4 | type-runtime-static-split | 9.0 | Runtime values run the program; static tools inspect separate annotations and report before execution. |
| types | Describe realistic data shapes. | 5 | 4 | type-shape-catalog | 9.0 | Real data contracts combine fields, variants, and expected absence instead of one scalar type. |
| types | Scale annotations for reusable libraries. | 5 | 4 | type-library-contract | 9.0 | Reusable APIs carry caller contracts through the library boundary with generics, parameters, and overloads. |
| reliability | Make failure explicit. | 6 | 4 | reliability-signal-map | 9.0 | Different failure shapes need explicit signals: assertions, recovery, chained causes, or warnings. |
| reliability | Control resource and module boundaries. | 6 | 4 | reliability-boundary-map | 9.0 | Reliable programs name their boundaries: resources clean up, modules import, environments constrain runtime. |
| reliability | Handle operations that outlive one expression. | 7 | 4 | reliability-operation-boundary | 9.0 | Async, threaded, test, and logging work cross an operation boundary before evidence comes back. |
| workers | Replace unavailable process boundaries with portable evidence. | 3 | 3 | workers-portable-evidence | 9.0 | Worker isolation breaks the usual cross-process pathways; the lesson preserves a captured value as portable evidence instead. |
| workers | Keep network lessons local to the protocol boundary. | 3 | 3 | workers-protocol-local | 9.0 | Demonstrate the protocol shape (request and response) rather than calling out over the network. |
| workers | Preserve the lesson while respecting the runtime. | 3 | 3 | workers-lesson-runtime | 9.0 | The lesson's evidence survives across the boundary that the worker runtime enforces. |

## Journey figure independence watchlist

No journey section figures reuse production example paint functions.

## Audit conclusion

No gate-blocking edits are required by this pass. The only below-target example is the standing `hello-world` waiver; all example diagrams and journey figures are at or above 9.0; every journey section has declared outcomes; the example graph has no orphaned sources; and every journey section now uses a journey-native figure rather than a lesson attachment.
