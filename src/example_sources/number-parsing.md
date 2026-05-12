+++
slug = "number-parsing"
title = "Number Parsing"
section = "Standard Library"
summary = "int() and float() parse text into numbers and raise ValueError on bad input."
doc_path = "/library/functions.html#int"
see_also = [
  "exceptions",
  "strings",
  "numbers",
]
+++

Parsing turns text into numeric values. `int()` parses whole-number text and `float()` parses decimal or scientific-notation text.

Invalid numeric text raises `ValueError`. Catching that specific exception makes it clear that bad input is expected and recoverable.

After parsing, the result is a number and can participate in arithmetic; before parsing, it is just text.

:::program
```python
print(int("42"))
print(float("3.5"))

try:
    int("python")
except ValueError as error:
    print(type(error).__name__)
```
:::

:::cell
Use `int()` for whole numbers and `float()` for decimal text. Parsed values are real numbers, not strings.

```python
print(int("42"))
print(float("3.5"))
```

```output
42
3.5
```
:::

:::cell
Bad numeric text raises `ValueError`. Catch that specific exception when invalid input is part of the normal flow.

```python
try:
    int("python")
except ValueError as error:
    print(type(error).__name__)
```

```output
ValueError
```
:::

:::note
- `int()` and `float()` are constructors that also parse strings.
- Catch `ValueError` when bad user input is expected and recoverable.
:::
