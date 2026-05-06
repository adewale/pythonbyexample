# Python By Example quality rubric

The target is to beat Go By Example and Rust By Example on Python teaching craft: each page should feel like a compact literate program that leaves the reader understanding the idea, not just recognizing the syntax.

Score each example on a 10 point scale:

1. **Conceptual payoff (0-1.5)** — the page teaches a real Python idea, not merely a doc fragment; the reader learns when and why the feature matters.
2. **Executable determinism (0-1.25)** — the sample runs as-is, has stable output, avoids network/time/randomness unless that is the lesson, and demonstrates cause and effect.
3. **Python idiom and accuracy (0-1.5)** — code uses current Python 3.13 idioms, names reflect the concept, and prose is technically precise without distracting caveats.
4. **Literate programming fit (0-1.5)** — prose and source read as one continuous article; each paragraph explains the adjacent fragment; comments are used only when they clarify the program itself.
5. **Source/result pairing (0-1.5)** — each important source fragment has nearby output that proves the point; the reader can see exactly which code produced which result.
6. **Example compactness (0-1)** — the page teaches one focused idea without unrelated syntax, extra APIs, filler prose, or code that does not support the lesson.
7. **Learning-sequence clarity (0-0.75)** — the title, summary, examples, and previous/next position make the page easy to place in the broader language tour.
8. **Language-tour clarity (0-0.75)** — the example teaches a Python language feature, syntax pattern, object model behavior, or core standard-library concept without drifting into task-cookbook documentation.
9. **Practical usefulness (0-0.75)** — names, data, and outputs resemble simplified real code rather than toy placeholders; the example gives the feature a reason to exist.
10. **Reference context and layout restraint (0-1.5)** — official Python documentation is available, expected output is visible without a run, and controls, cards, borders, and labels are used only when they clarify structure.

Quality bands:

- **9.0-10.0**: Better-than-reference quality; concise, literate, memorable, and useful as both tutorial and reference.
- **8.0-8.9**: strong; may need hand-authored prose/code alignment or a sharper demonstration.
- **7.0-7.9**: serviceable tutorial material, not yet reference-grade.
- **below 7.0**: rewrite before publishing.

Project gate: every shipped example should score at least **8.5**, and the catalog average should exceed sampled Go By Example and Rust By Example pages on craft and understandability. The score is a guide, not a substitute for reading the page.
