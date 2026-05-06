+++
slug = "truthiness"
title = "Truthiness"
section = "Basics"
summary = "Python conditions use truthiness, not only explicit booleans."
doc_path = "/library/stdtypes.html#truth-value-testing"
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
Truthiness is one of Python's most important conveniences: conditions can test objects directly instead of requiring explicit boolean comparisons everywhere.

Empty containers, numeric zero, None, and False are false; most other values are true. This makes common checks such as if items: concise and idiomatic.

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
Use truthiness when it reads naturally, but choose explicit comparisons when the distinction matters, such as checking whether a value is exactly None.

```python
if name:
    print("has a name")
```

```output
has a name
```
:::

:::cell
Use truthiness when it reads naturally, but choose explicit comparisons when the distinction matters, such as checking whether a value is exactly None.

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
