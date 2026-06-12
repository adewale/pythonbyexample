+++
slug = "hello-world"
title = "Hello World"
section = "Basics"
summary = "The first Python program prints a line of text."
doc_path = "/tutorial/introduction.html"
see_also = [
  "values",
  "variables",
]
+++

Every Python program starts by executing statements from top to bottom. Calling `print()` is the smallest useful program because it shows how Python evaluates an expression and sends text to standard output.

Strings are ordinary values, so the message passed to `print()` can be changed, stored in a variable, or produced by a function. This example keeps the first program intentionally small.

Run the program and compare what you see with the source: the text appears on standard output followed by a newline, which is why successive `print()` calls land on separate lines.

:::program
```python
print("hello world")
```
:::

:::cell
The whole program is one statement. Python evaluates the string literal `"hello world"` and passes that value to `print()`, which writes it to standard output — the output panel shows exactly that line.

```python
print("hello world")
```

```output
hello world
```
:::

:::note
- `print()` writes text followed by a newline.
- Strings can be delimited with single or double quotes.
:::
