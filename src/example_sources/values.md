+++
slug = "values"
title = "Values"
section = "Basics"
summary = "Python programs evaluate expressions into objects such as text, numbers, booleans, and None."
doc_path = "/library/stdtypes.html"
+++

A Python program works by evaluating expressions into values. Values are objects: text, integers, floats, booleans, `None`, and many richer types introduced later.

Names point to values; they are not declarations that permanently fix a type. Operations usually produce new values, which you can print, store, compare, or pass to functions.

This page is a map, not the whole territory. Later pages explain the boundaries: equality vs identity, mutable vs immutable values, truthiness vs literal booleans, and `None` vs a missing key or an exception.

:::program
```python
text = "python"
count = 3
ratio = 2.5
ready = True
missing = None

print(type(text).__name__)
print(text.upper())
print(count + 4)
print(ratio * 2)

print(ready and count > 0)
print(missing is None)
```
:::

:::cell
Start with several built-in values. Python does not require declarations before binding these names, and each value is still an object with a type.

```python
text = "python"
count = 3
ratio = 2.5
ready = True
missing = None

print(type(text).__name__)
```

```output
str
```
:::

:::cell
Methods and operators evaluate to new values. The original `text`, `count`, and `ratio` bindings remain ordinary objects you can reuse.

```python
print(text.upper())
print(count + 4)
print(ratio * 2)
```

```output
PYTHON
7
5.0
```
:::

:::cell
Boolean expressions combine facts, and `None` is checked by identity because it is a singleton absence marker.

```python
print(ready and count > 0)
print(missing is None)
```

```output
True
True
```
:::

:::note
- Values are objects; names point to them and operations usually create new values.
- Use `is None` for the absence marker, not `== None`.
- This overview introduces boundaries that later pages explain in detail.
:::
