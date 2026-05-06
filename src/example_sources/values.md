+++
slug = "values"
title = "Values"
section = "Basics"
summary = "Python has strings, integers, floats, booleans, and None."
doc_path = "/library/stdtypes.html"
+++

A Python program works by evaluating expressions into values. The most common first values are text, integers, floats, booleans, and `None`.

Operators and method calls produce more values. `text.upper()` returns a new string, arithmetic returns numbers, and comparisons or logical operators return booleans.

`None` is a real singleton value used to mean “no value here.” Checking it with `is None` introduces identity before the later equality and mutability examples.

:::program
```python
text = "python"
count = 3
ratio = 2.5
ready = True
missing = None

print(text.upper())
print(count + 4)
print(ratio * 2)
print(ready and count > 0)
print(missing is None)
```
:::

:::cell
Start with several built-in values. Python does not require declarations before binding these names.

Methods and operators evaluate to new values. The original `text`, `count`, and `ratio` bindings remain ordinary objects you can reuse.

```python
text = "python"
count = 3
ratio = 2.5
ready = True
missing = None

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
- A small value tour should make later pages feel familiar, not replace the dedicated pages for numbers, strings, and booleans.
:::
