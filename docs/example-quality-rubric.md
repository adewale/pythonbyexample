# Python By Example quality rubric

The target is to beat Go By Example and Rust By Example on Python teaching craft: each page should feel like a compact literate program that leaves the reader understanding the idea, not just recognizing the syntax.

Score each example on a 10 point scale:

1. **Conceptual payoff (0-1.0)** — the page teaches a real Python idea, not merely a doc fragment; the reader leaves with a durable mental model, not just syntax recognition.
2. **Rationale (0-0.75)** — the example explains why the feature exists, what problem shape calls for it, and what pressure made the syntax or API worth having.
3. **Alternatives and boundaries (0-0.75)** — the page names nearby choices and shows when to prefer this feature instead: `while` vs `for`, tuple vs list, `None` vs exception, property vs method, eager collection vs lazy stream, and similar alternatives.
4. **Executable determinism (0-1.0)** — the sample runs as-is, has stable output, avoids network/time/randomness unless that is the lesson, and demonstrates cause and effect.
5. **Python idiom and accuracy (0-1.0)** — code uses current Python 3.13 idioms, names reflect the concept, and prose is technically precise without distracting caveats.
6. **Literate programming fit (0-1.0)** — prose and source read as one continuous article; each paragraph explains the adjacent fragment; comments are used only when they clarify the program itself.
7. **Source/result pairing (0-1.0)** — each important source fragment has nearby output that proves the semantic point, not merely that the code ran.
8. **Concept decomposition (0-1.0)** — the example breaks the concept into meaningful parts instead of presenting one compressed trick.
9. **Progressive walkthrough (0-0.75)** — each cell introduces one new idea, and the sequence builds toward the complete concept. Single-cell examples are acceptable only for intentionally atomic concepts.
10. **Representative coverage (0-0.75)** — the code covers the forms promised by the title, summary, and prose, and the catalog has an explicit home for every common Python syntax form. Do not claim lists, dictionaries, and sets while showing only two of them; do not let syntax such as `break`, `continue`, `assert`, `nonlocal`, `yield from`, `async for`, or `:=` exist only as untested assumptions.
11. **Practical usefulness (0-1.0)** — names, data, and outputs resemble simplified real code rather than toy placeholders; the example gives the feature a reason to exist.
12. **Editorial progression (0-1.0)** — broad examples move through a deliberate sequence: motivation, smallest concrete form, model/protocol, common operations, boundary or edge case, and neighboring concepts. The page should feel like a guided exposition rather than a sample tray.

Topic-specific gates:

- **Text and strings** — examples must distinguish text from bytes, explain Unicode/code-point behavior when relevant, and show the boundary where encoding such as UTF-8 appears. A string page that only demonstrates ASCII operations is incomplete. When using non-English text to show that code points and bytes differ, include an English/ASCII baseline with the same kind of phrase so the contrast is visible rather than implied.
- **Broad surface tours** — if a title names a broad surface area (`Testing`, `Packages`, `Regular Expressions`, `Type Hints`, `Async Await`, `Special Methods`, `Operators`, `Literals`), the page must either cover the reader's reasonable expectations or clearly frame itself as a first pass and link to focused neighbors. A broad title with one narrow demonstration is a scope bug, not just a content gap.
- **Reduce without distorting** — small examples are good only when the necessary boundary, contrast, or edge case remains visible. If compression removes the part that makes the concept understandable, split the example or add another cell.
- **Map-or-split rule** — broad pages must either be surface maps with explicit categories and `See also` links, or be split into narrower pages. Do not ship a broad page that merely samples unrelated forms.
- **Runtime-boundary examples** — when standard Python code cannot run in Dynamic Workers, teach the standard form first, state the runtime constraint once, and avoid repeated apology or caveat-heavy prose.

Release gates outside the score:

- official Python documentation is linked through `doc_path`
- expected output is visible before a run
- page layout remains restrained and readable
- examples verify under the configured Python version
- generated embedded source and asset manifests are up to date
- syntax-surface tests prove that each major statement, expression marker, loop-control form, function-signature marker, pattern form, import form, and async form has a runnable example
- iteration examples identify what produces values, what consumes values, whether values are stored or streamed, and whether the stream is reusable or one-pass

Quality bands:

- **9.0-10.0**: Better-than-reference quality; concise, literate, memorable, and useful as both tutorial and reference.
- **8.0-8.9**: strong; may need hand-authored prose/code alignment or a sharper demonstration.
- **7.0-7.9**: serviceable tutorial material, not yet reference-grade.
- **below 7.0**: rewrite before publishing.

Project gate: every shipped example should score at least **8.5**, and the catalog average should exceed sampled Go By Example and Rust By Example pages on craft and understandability. The score is a guide, not a substitute for reading the page.

## Weak-example smells

Flag these during review even when the code is correct:

- A multi-part concept has only one cell.
- The title or prose promises forms not shown by code.
- A Python syntax form appears in the language-tour checklist but has no runnable example.
- Output is a single scalar for a collection transformation, so the reader cannot see the shape of the result.
- A concept with a common confusion has no contrast, boundary, or alternative-choice example.
- More than half of nonblank code lines are `print(...)` calls.
- Data is purely toy-shaped when realistic small data would clarify the purpose.
- Notes repeat the prose instead of adding practical guidance.
- The program shows valid syntax but not when or why to use it.
- The rationale is missing: the page does not explain the pressure that made the feature useful.
- Alternatives are missing: the page does not say what a reader might use instead or when this feature is the wrong choice.
- The page teaches an operation but not the problem shape that made the feature worth having.
- The page does not connect the feature to a nearby alternative, such as `while` vs `for`, slice vs index, tuple vs list, text `str` vs binary `bytes`, or f-string expression vs display formatting.
- An iteration example uses a lazy object but does not show when values are consumed.
- An iteration example blurs eager containers with one-pass streams.
- A broad title hides a narrow example: the page sounds like a tour of a surface area but demonstrates only one isolated technique.
- A syntax form has a focused example but is missing from a natural umbrella page where learners would expect to see it.
- The journey order follows implementation/catalog history instead of prerequisites: conditionals before booleans, closures before scope, networking before bytes, or process boundaries before environment boundaries.
- Runtime constraints are repeated in the intro, code block, notes, and runner area until the limitation overwhelms the Python lesson.
- The page has no editorial progression: examples are technically related but ordered like a checklist rather than a learning path.
- The page reduces so aggressively that a necessary edge case or contrast disappears.
- `See also` links behave like tags instead of prerequisite, neighbor, or next-depth graph edges.

## Strengthening checklist

Before publishing or substantially editing an example, ask:

1. What are the 2-4 parts of the concept a reader must understand?
2. Does each cell add exactly one of those parts?
3. Does the output prove the specific semantic point of the adjacent source?
4. Does the example use small realistic data?
5. Is there a contrast readers commonly need to avoid misuse?
6. Would an explicit loop, named function, or mutation-vs-copy contrast make the idiom clearer?
7. For iteration examples, what produces values, what consumes them, and are they stored eagerly or streamed lazily?
8. What neighboring feature would a learner confuse this with, and does the page explain the boundary?
9. Does the data shape explain why this feature exists?
10. What syntax form would disappear from the catalog if this page were removed, and is that covered somewhere else?
11. For text examples, does the page make Unicode and encoding boundaries visible instead of assuming ASCII-only strings? If non-English text is used, is it compared with an English/ASCII baseline?
12. If the title names a broad surface area, what would a learner reasonably expect to see, and is that expectation met or explicitly scoped down?
13. Is any important syntax form covered only in a focused page even though an umbrella page should point to it?
14. Does the journey sequence respect prerequisites rather than merely mirroring catalog order?
15. If the page mentions a runtime limitation, is the constraint stated once without becoming the main story?
16. Does the page reduce the concept without distorting it, or did compression remove an essential boundary?
17. For broad pages, is this a map with categories and links, or should it be split?
18. Do edge cases appear close enough to the main idea that readers understand the boundary?
19. Do `See also` links express prerequisite, neighbor, or next-depth relationships rather than tags?
