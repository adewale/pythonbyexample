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

`None` represents the absence of a value. It is the usual sentinel when a function has no result to return but the absence itself is meaningful.

Because `None` is a singleton, idiomatic Python checks it with `is None` or `is not None`. This avoids confusing identity with value equality.

Absence has several nearby shapes in Python. A function can return `None`, a dictionary lookup can supply a default for a missing key, and an invalid operation can raise an exception.

:::program
```python
result = None
print(result is None)

def find_score(name):
    if name == "Ada":
        return 10
    return None

score = find_score("Grace")
print(score is None)

profile = {"name": "Ada"}
print(profile.get("timezone", "UTC"))

try:
    int("python")
except ValueError:
    print("invalid number")
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
Functions often return `None` when absence is expected and callers can continue. The function name and surrounding code should make that possibility clear.

```python
def find_score(name):
    if name == "Ada":
        return 10
    return None

score = find_score("Grace")
print(score is None)
```

```output
True
```
:::

:::cell
A missing dictionary key is another absence boundary. Use `get()` when the mapping can supply a default, and use exceptions for invalid operations that cannot produce a value.

```python
profile = {"name": "Ada"}
print(profile.get("timezone", "UTC"))

try:
    int("python")
except ValueError:
    print("invalid number")
```

```output
UTC
invalid number
```
:::

:::note
- Use `is None` rather than `== None`; `None` is a singleton identity value.
- Use `None` for expected absence that callers can test.
- Use dictionary defaults for missing mapping keys and exceptions for invalid operations.
:::
