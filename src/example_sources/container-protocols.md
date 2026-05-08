+++
slug = "container-protocols"
title = "Container Protocols"
section = "Data Model"
summary = "Container methods connect objects to indexing, membership, and item assignment."
doc_path = "/reference/datamodel.html#emulating-container-types"
see_also = [
  "lists",
  "dicts",
  "special-methods",
]
+++

Container protocols let a class behave like the collection it represents. Instead of inventing method names such as `has()` or `lookup()`, the object can support `in`, indexing, and assignment.

The key methods are small and familiar: `__contains__` powers `in`, `__getitem__` powers `obj[key]`, and `__setitem__` powers `obj[key] = value`. Add only the operations the object can honestly support.

This keeps the public interface aligned with Python's built-in containers. Callers can use the same syntax for custom records, caches, tables, and sequence-like objects.

:::program
```python
class Scores:
    def __init__(self):
        self._scores = {}

    def __contains__(self, name):
        return name in self._scores

    def __getitem__(self, name):
        return self._scores[name]

    def __setitem__(self, name, score):
        self._scores[name] = score

scores = Scores()
scores["Ada"] = 98
print("Ada" in scores)
print(scores["Ada"])
```
:::

:::cell
`__setitem__` gives assignment syntax to a custom container.

```python
class Scores:
    def __init__(self):
        self._scores = {}

    def __setitem__(self, name, score):
        self._scores[name] = score

scores = Scores()
scores["Ada"] = 98
print(scores._scores)
```

```output
{'Ada': 98}
```
:::

:::cell
`__contains__` answers membership tests written with `in`.

```python
class Scores:
    def __init__(self):
        self._scores = {"Ada": 98}

    def __contains__(self, name):
        return name in self._scores

scores = Scores()
print("Ada" in scores)
```

```output
True
```
:::

:::cell
`__getitem__` connects bracket lookup to your internal storage.

```python
class Scores:
    def __init__(self):
        self._scores = {"Ada": 98}

    def __getitem__(self, name):
        return self._scores[name]

scores = Scores()
print(scores["Ada"])
```

```output
98
```
:::

:::note
- Implement the narrowest container protocol your object needs.
- Use `KeyError` and `IndexError` consistently with built-in containers.
- If a plain `dict` or `list` is enough, prefer it over a custom container.
:::
