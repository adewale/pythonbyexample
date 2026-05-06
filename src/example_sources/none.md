+++
slug = "none"
title = "None"
section = "Basics"
summary = "None represents the absence of a value."
doc_path = "/library/constants.html#None"
+++

`None` represents the absence of a value. It is the usual sentinel when a function has no result to return but the absence itself is meaningful.

Because `None` is a singleton, idiomatic Python checks it with `is None` or `is not None`. This avoids confusing identity with value equality.

A function that reaches the end without a `return` statement returns `None`, so explicit `None` results should be documented by names and control flow.

:::program
```python
result = None
print(result is None)

def find_score(name):
    if name == "Ada":
        return 10
    return None

score = find_score("Grace")
if score is None:
    print("missing score")
```
:::

:::cell
`None` is Python's value for “nothing here.” It is commonly used as a sentinel when a real result is unavailable.

```python
result = None
print(result is None)
```

```output
True
```
:::

:::cell
Functions often return `None` when lookup or parsing fails without raising an exception.

Check for `None` with `is None`. That tests identity with the singleton object instead of asking for value equality.

```python
def find_score(name):
    if name == "Ada":
        return 10
    return None

score = find_score("Grace")
if score is None:
    print("missing score")
```

```output
missing score
```
:::

:::note
- Use `is None` rather than `== None`; `None` is a singleton identity value.
- A function that reaches the end without `return` also returns `None`.
:::
