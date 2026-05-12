+++
slug = "object-lifecycle"
title = "Object Lifecycle"
section = "Basics"
summary = "References keep objects alive until Python can reclaim them."
doc_path = "/reference/datamodel.html#objects-values-and-types"
see_also = [
  "variables",
  "mutability",
  "classes",
]
+++

References keep objects alive until Python can reclaim them. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
import gc

names = []
alias = names
alias.append("Ada")

print(names is alias)
print(names)

object_id = id(names)
del alias
print(id(names) == object_id)

del names
print("object can be reclaimed")
gc.collect()
```
:::

:::cell
Use `is` and `id()` to observe identity while two names refer to the same object.

```python
import gc

names = []
alias = names
alias.append("Ada")

print(names is alias)
print(names)

object_id = id(names)
del alias
print(id(names) == object_id)

del names
print("object can be reclaimed")
gc.collect()
```

```output
True
['Ada']
True
object can be reclaimed
```
:::

:::note
- Use `is` and `id()` to observe identity while two names refer to the same object.
- Deleting a name removes one reference; it does not directly destroy the object if another reference still exists.
- Python reclaims unreachable objects automatically, so programs usually manage ownership by controlling references.
:::
