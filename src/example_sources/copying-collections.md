+++
slug = "copying-collections"
title = "Copying Collections"
section = "Collections"
summary = "Copies can duplicate the outer container while nested objects may still be shared."
doc_path = "/library/copy.html"
see_also = [
  "mutability",
  "lists",
  "dicts",
]
+++

Copying answers two different questions: do you need a new outer container, or do you also need independent nested objects? A plain assignment gives another name for the same object. A shallow copy duplicates only the outer container. `copy.deepcopy()` recursively copies contained objects.

Most Python code wants a shallow copy or a deliberate rebuild. Use a deep copy only when shared nested state would be wrong and the objects involved are safe to duplicate.

The outputs below show the footgun directly: a shallow copy has a different outer list, but its inner lists are still the same objects.

:::program
```python
import copy

rows = [["Ada"], ["Grace"]]
alias = rows
shallow = rows.copy()
deep = copy.deepcopy(rows)

rows[0].append("Lovelace")

print(alias is rows)
print(shallow is rows)
print(rows[0] is shallow[0])
print(rows[0] is deep[0])
print(shallow)
print(deep)
```
:::

:::cell
Assignment does not copy a collection. It gives the same list another name.

```python
rows = [["Ada"], ["Grace"]]
alias = rows

print(alias is rows)
```

```output
True
```
:::

:::cell
A shallow copy creates a new outer list, but nested lists are still shared.

```python
shallow = rows.copy()
rows[0].append("Lovelace")

print(shallow is rows)
print(rows[0] is shallow[0])
print(shallow)
```

```output
False
True
[['Ada', 'Lovelace'], ['Grace']]
```
:::

:::cell
A deep copy is independent at the nested level, so later mutation of `rows[0]` does not appear in `deep`.

```python
import copy

rows = [["Ada"], ["Grace"]]
deep = copy.deepcopy(rows)
rows[0].append("Lovelace")

print(rows[0] is deep[0])
print(deep)
```

```output
False
[['Ada'], ['Grace']]
```
:::

:::note
- Assignment aliases; it does not copy.
- Shallow copies duplicate the outer container only.
- Deep copies are useful for nested independence, but they can be expensive and surprising for objects with external resources.
:::
