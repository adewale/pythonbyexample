# Python By Example quality rubric

The target is to beat Go By Example and Rust By Example on Python teaching craft: each page should feel like a compact literate program that leaves the reader understanding the idea, not just recognizing the syntax.

Score each example on a 10 point scale:

1. **Conceptual payoff (0-1.25)** — the page teaches a real Python idea, not merely a doc fragment; the reader learns when and why the feature matters.
2. **Executable determinism (0-1.0)** — the sample runs as-is, has stable output, avoids network/time/randomness unless that is the lesson, and demonstrates cause and effect.
3. **Python idiom and accuracy (0-1.25)** — code uses current Python 3.13 idioms, names reflect the concept, and prose is technically precise without distracting caveats.
4. **Literate programming fit (0-1.0)** — prose and source read as one continuous article; each paragraph explains the adjacent fragment; comments are used only when they clarify the program itself.
5. **Source/result pairing (0-1.25)** — each important source fragment has nearby output that proves the semantic point, not merely that the code ran.
6. **Concept decomposition (0-1.0)** — the example breaks the concept into meaningful parts instead of presenting one compressed trick.
7. **Progressive walkthrough (0-0.75)** — each cell introduces one new idea, and the sequence builds toward the complete concept. Single-cell examples are acceptable only for intentionally atomic concepts.
8. **Representative coverage (0-0.75)** — the code covers the forms promised by the title, summary, and prose. Do not claim lists, dictionaries, and sets while showing only two of them.
9. **Contrast and boundary clarity (0-0.75)** — when a feature is commonly confused with another feature, the example shows the distinction: comprehension vs loop, `sorted()` vs `list.sort()`, `lambda` vs `def`, `==` vs `is`, generator vs list, property vs method, and similar boundaries.
10. **Practical usefulness (0-1.0)** — names, data, and outputs resemble simplified real code rather than toy placeholders; the example gives the feature a reason to exist.

Release gates outside the score:

- official Python documentation is linked through `doc_path`
- expected output is visible before a run
- page layout remains restrained and readable
- examples verify under the configured Python version
- generated embedded source and asset manifests are up to date

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
- Output is a single scalar for a collection transformation, so the reader cannot see the shape of the result.
- A concept with a common confusion has no contrast or boundary example.
- More than half of nonblank code lines are `print(...)` calls.
- Data is purely toy-shaped when realistic small data would clarify the purpose.
- Notes repeat the prose instead of adding practical guidance.
- The program shows valid syntax but not when or why to use it.

## Strengthening checklist

Before publishing or substantially editing an example, ask:

1. What are the 2-4 parts of the concept a reader must understand?
2. Does each cell add exactly one of those parts?
3. Does the output prove the specific semantic point of the adjacent source?
4. Does the example use small realistic data?
5. Is there a contrast readers commonly need to avoid misuse?
6. Would an explicit loop, named function, or mutation-vs-copy contrast make the idiom clearer?
