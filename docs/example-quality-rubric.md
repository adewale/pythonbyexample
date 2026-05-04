# Python By Example quality rubric

The target is to beat Go By Example and Rust By Example on Python teaching craft: each page should feel like a compact literate program that leaves the reader understanding the idea, not just recognizing the syntax.

Score each example on a 10 point scale:

1. **Conceptual payoff (0-2)** — the page teaches a real Python idea, not merely a doc fragment; the reader learns when and why the feature matters.
2. **Executable determinism (0-1.25)** — the sample runs as-is, has stable output, avoids network/time/randomness unless that is the lesson, and demonstrates cause and effect.
3. **Python idiom and accuracy (0-1.75)** — code uses current Python 3.13 idioms, names reflect the concept, and prose is technically precise without distracting caveats.
4. **Literate programming fit (0-2)** — prose and source read as one continuous article; each paragraph explains the adjacent fragment; comments are used only when they clarify the program itself.
5. **Output as evidence (0-1)** — expected output is visible without a run, aligned with the code, wraps long text, and proves the lesson.
6. **Navigation and reference context (0-1)** — previous/next links preserve learning flow, and official Python documentation is available without distracting from the lesson.
7. **Chrome restraint and layout utility (0-1)** — links look like links; controls, cards, borders, and labels are used only when they clarify structure.

Quality bands:

- **9.0-10.0**: Better-than-reference quality; concise, literate, memorable, and useful as both tutorial and reference.
- **8.0-8.9**: strong; may need hand-authored prose/code alignment or a sharper demonstration.
- **7.0-7.9**: serviceable tutorial material, not yet reference-grade.
- **below 7.0**: rewrite before publishing.

Project gate: every shipped example should score at least **8.5**, and the catalog average should exceed sampled Go By Example and Rust By Example pages on craft and understandability. The score is a guide, not a substitute for reading the page.
