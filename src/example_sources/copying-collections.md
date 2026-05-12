+++
slug = "copying-collections"
title = "Copying Collections"
section = "Collections"
summary = "Copies can duplicate a container while still sharing nested objects."
doc_path = "/library/copy.html"
see_also = [
  "mutability",
  "lists",
  "dicts",
]
+++

Copies can duplicate a container while still sharing nested objects. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
import copy

rows = [["Ada"], ["Grace"]]
shallow = rows.copy()
deep = copy.deepcopy(rows)

rows[0].append("Lovelace")

print(shallow)
print(deep)
print(rows[0] is shallow[0])
print(rows[0] is deep[0])
```
:::

:::cell
A shallow copy makes a new outer container.

```python
import copy

rows = [["Ada"], ["Grace"]]
shallow = rows.copy()
deep = copy.deepcopy(rows)

rows[0].append("Lovelace")

print(shallow)
print(deep)
print(rows[0] is shallow[0])
print(rows[0] is deep[0])
```

```output
[['Ada', 'Lovelace'], ['Grace']]
[['Ada'], ['Grace']]
True
False
```
:::

:::note
- A shallow copy makes a new outer container.
- Nested objects are still shared by a shallow copy.
- Use `copy.deepcopy()` only when nested independence is required.
:::
