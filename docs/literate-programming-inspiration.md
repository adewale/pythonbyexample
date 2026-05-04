# Literate programming and prose-code layout inspiration

The previous per-chunk boxes made the page feel like a collection of cards. Go By Example works better because prose and code form one continuous reading surface: commentary on the left, source on the right, with minimal chrome.

Useful references:

| Reference | URL | What to borrow |
|---|---|---|
| Literate programming, Donald Knuth | https://www-cs-faculty.stanford.edu/~knuth/lp.html | Treat programs as explanations for humans first; order the exposition by concept, not by compiler convenience. |
| Observable notebooks | https://observablehq.com/ | Immediate feedback near code; code cells are part of a narrative, not isolated widgets. |
| Jupyter Book | https://jupyterbook.org/ | Long-form computational narratives with executable code and output. |
| Quarto | https://quarto.org/ | Clean publishing model for prose, code, and output in one document. |
| R Markdown | https://rmarkdown.rstudio.com/ | Reproducible documents where code chunks support surrounding explanation. |
| Sphinx-Gallery | https://sphinx-gallery.github.io/ | Generates example pages from scripts with prose and code interleaved. |
| Org Babel | https://orgmode.org/worg/org-contrib/babel/ | Literate source blocks that can execute and feed results back into documentation. |
| Pollen | https://docs.racket-lang.org/pollen/ | Programmable publishing with text and code treated as one authored artifact. |
| AMP By Example announcement | https://medium.com/google-developers/introducing-amp-by-example-dc6118794369 | Product framing for learning by modifying real examples rather than reading abstract API docs. |
| AMP By Example: Hello World | https://amp.dev/documentation/examples/introduction/hello_world/ | Separates explanation, source, and live result without making the code feel decorative; useful inspiration for our source plus runnable-output split. |

Design direction adopted here:

- Use a **literate program** section instead of separate mini-cards.
- Keep each explanatory paragraph directly beside its source fragment in a continuous reading flow, like Go By Example's prose/source rhythm.
- Remove dark boxed fragments inside the explanation column; code fragments should feel like part of the document, not nested cards.
- Use a simple spacing scale and larger separation between the literate article and the runnable playground, following the `impeccable/layout` emphasis on rhythm and grouping.
- Keep the full editable source as the execution surface, because learners still need one place to modify and run the complete example.
