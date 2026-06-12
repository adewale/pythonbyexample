+++
slug = "truthiness"
title = "Truthiness"
section = "Basics"
summary = "Python conditions use truthiness, not only explicit booleans."
doc_path = "/library/stdtypes.html#truth-value-testing"
see_also = [
  "booleans",
  "none",
  "conditionals",
  "special-methods",
]
+++

Truthiness is one of Python's most important conveniences: conditions can test objects directly instead of requiring explicit boolean comparisons everywhere.

Empty containers, numeric zero, None, and False are false; most other values are true. This makes common checks such as if items: concise and idiomatic.

Use truthiness when it reads naturally, but choose explicit comparisons when the distinction matters, such as checking whether a value is exactly None.

:::program
```python
items = []
name = "Ada"

if not items:
    print("no items")

if name:
    print("has a name")

print(bool(0))
print(bool(42))
```
:::

:::cell
An empty list is false, so `not items` reads as "items is empty". The condition tests the object directly — no `len(items) == 0` comparison is needed.

```python
items = []
name = "Ada"

if not items:
    print("no items")
```

```output
no items
```
:::

:::cell
A non-empty string is true, so `if name:` asks "did we get a name?" in one word. Reach for an explicit comparison instead when the distinction matters — `if name is not None:` treats an empty string differently from a missing one.

```python
if name:
    print("has a name")
```

```output
has a name
```
:::

:::cell
`bool()` reveals the truth value any condition would use. Zero-like numbers convert to `False`; other numbers convert to `True`.

```python
print(bool(0))
print(bool(42))
```

```output
False
True
```
:::

:::note
- Empty containers and zero-like numbers are false in conditions.
- Use explicit comparisons when they communicate intent better than truthiness.
:::
