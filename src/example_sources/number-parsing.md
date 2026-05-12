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

Parsing turns text from files, forms, command lines, or network messages into numeric objects. `int()` parses whole-number text, and `float()` parses decimal or scientific-notation text.

Invalid numeric text raises `ValueError`. Catch that specific exception when bad user input is expected and recoverable; let it fail loudly when the string is supposed to be trusted program data.

`int()` also accepts a base, which is useful at protocol boundaries where numbers are written in hexadecimal, binary, or another explicit notation.

:::program
```python
print(int("42"))
print(float("3.5"))
print(int("ff", 16))

texts = ["10", "python", "20"]
for text in texts:
    try:
        print(int(text) * 2)
    except ValueError:
        print(f"skip {text!r}")
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
Pass a base when the text format says the number is not decimal.

```python
print(int("ff", 16))
```

```output
255
```
:::

:::cell
Catch `ValueError` at the input boundary when invalid text is normal and recoverable.

```python
texts = ["10", "python", "20"]
for text in texts:
    try:
        print(int(text) * 2)
    except ValueError:
        print(f"skip {text!r}")
```

```output
20
skip 'python'
40
```
:::

:::note
- `int()` and `float()` are constructors that also parse strings.
- `int(text, base)` makes non-decimal input explicit.
- Catch `ValueError` for recoverable user input; do not hide unexpected data corruption.
:::
