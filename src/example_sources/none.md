+++
slug = "none"
title = "None"
section = "Basics"
summary = "None represents expected absence, distinct from missing keys and errors."
doc_path = "/library/constants.html#None"
see_also = [
  "values",
  "truthiness",
  "exceptions",
  "dicts",
]
+++

`None` represents the absence of a value. It is the usual result when a call has nothing to hand back but the absence itself is meaningful.

Because `None` is a singleton, idiomatic Python checks it with `is None` or `is not None`. This avoids confusing identity with value equality.

Absence has several nearby shapes in Python. A call can return `None`, a dictionary lookup can supply a default for a missing key, and an invalid operation can raise an exception instead of returning anything.

:::program
```python
result = None
print(result is None)

names = ["Grace", "Ada"]
result = names.sort()
print(result is None)
print(names)

profile = {"name": "Ada"}
timezone = profile.get("timezone")
print(timezone is None)
print(profile.get("timezone", "UTC"))
```
:::

:::cell
`None` is Python's value for “nothing here.” Check it with `is None` because it is a singleton identity value.

```python
result = None
print(result is None)
```

```output
True
```
:::

:::cell
A call that does its work without producing a result returns `None`. `list.sort()` reorders the list in place, so the value it hands back is `None` and the sorted data is in `names`. Assigning that result to a name is a common slip; the same rule applies to every [function](/examples/functions) that finishes without a `return` value.

```python
names = ["Grace", "Ada"]
result = names.sort()
print(result is None)
print(names)
```

```output
True
['Ada', 'Grace']
```
:::

:::cell
A missing dictionary key is another absence boundary. `get()` returns `None` when the key is missing, or a default when the mapping can supply one. Indexing with `profile["timezone"]` would not return `None`: it raises `KeyError`, because Python reports invalid operations with [exceptions](/examples/exceptions) rather than with a value.

```python
profile = {"name": "Ada"}
timezone = profile.get("timezone")
print(timezone is None)
print(profile.get("timezone", "UTC"))
```

```output
True
UTC
```
:::

:::note
- Use `is None` rather than `== None`; `None` is a singleton identity value.
- Use `None` for expected absence that callers can test.
- Calls that only change something in place, such as `list.sort()`, return `None`.
- Use dictionary defaults for missing mapping keys and exceptions for invalid operations.
:::
