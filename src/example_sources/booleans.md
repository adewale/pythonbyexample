+++
slug = "booleans"
title = "Booleans"
section = "Basics"
summary = "Booleans represent truth values and combine with logical operators."
doc_path = "/library/stdtypes.html#boolean-type-bool"
+++

Booleans are the values `True` and `False`. They are produced by comparisons and combined with `and`, `or`, and `not`.

Python's logical operators short-circuit. That means the right side is evaluated only when needed, which keeps guard checks efficient and safe.

Booleans are also connected to truthiness: many objects can be tested in conditions even when they are not literally `True` or `False`.

:::program
```python
logged_in = True
has_permission = False

print(logged_in and has_permission)
print(logged_in or has_permission)
print(not has_permission)

name = "Ada"
print(name == "Ada" and len(name) > 0)
```
:::

:::cell
Use booleans for facts that are either true or false. Python spells the constants `True` and `False`.

Use `and`, `or`, and `not` to combine truth values. These operators read like English and short-circuit when possible.

```python
logged_in = True
has_permission = False

print(logged_in and has_permission)
print(logged_in or has_permission)
print(not has_permission)
```

```output
False
True
True
```
:::

:::cell
Comparisons produce booleans too, so they compose naturally with logical operators in conditions and validation checks.

```python
name = "Ada"
print(name == "Ada" and len(name) > 0)
```

```output
True
```
:::

:::note
- Boolean constants are `True` and `False`, with capital letters.
- `and` and `or` short-circuit: Python does not evaluate the right side if the left side already determines the result.
- Prefer truthiness for containers and explicit comparisons when the exact boolean condition matters.
:::
