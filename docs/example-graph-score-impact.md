# See also graph score impact

The `see_also` implementation adds subtle graph behavior on top of the linear previous/next tour:

- edge labels such as `contrast`, `prerequisite`, `alternative`, `builds on`, `shared mechanism`, and `next depth`
- validation with `scripts/audit_example_graph.py --check`
- lightweight recommendations on unknown `/examples/{slug}` pages
- a graph-aware score component in `scripts/score_examples.py`

The score comparison below uses the same loaded catalog and the graph-aware scorer. “Before” subtracts the new graph component; “After” includes it.

| Cohort | Count | Before avg | After avg | Delta |
|---|---:|---:|---:|---:|
| All examples | 69 | 9.37 | 9.44 | +0.07 |
| Examples with `see_also` | 17 | 9.31 | 9.61 | +0.30 |

Lowest linked examples before/after:

| Example | Before | After | Delta |
|---|---:|---:|---:|
| `import-aliases` | 8.56 | 8.86 | +0.30 |
| `metaclasses` | 8.89 | 9.19 | +0.30 |
| `async-iteration-and-context` | 9.08 | 9.38 | +0.30 |
| `assignment-expressions` | 9.34 | 9.64 | +0.30 |
| `break-and-continue` | 9.34 | 9.64 | +0.30 |
| `loop-else` | 9.34 | 9.64 | +0.30 |
| `positional-only-parameters` | 9.34 | 9.64 | +0.30 |
| `inheritance-and-super` | 9.34 | 9.64 | +0.30 |
| `exception-chaining` | 9.34 | 9.64 | +0.30 |
| `exception-groups` | 9.34 | 9.64 | +0.30 |

Interpretation: the graph does not make weak prose strong by itself. It gives a modest rubric gain where links clarify alternatives, prerequisites, or next-depth concepts. The main catalog average moves only slightly because most examples intentionally remain unlinked unless there is a meaningful conceptual edge.
