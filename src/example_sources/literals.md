+++
slug = "literals"
title = "Literals"
section = "Basics"
summary = "Literals write values directly in Python source code."
doc_path = "/reference/lexical_analysis.html#literals"
scope_first_pass = true
see_also = [
  "values",
  "strings",
  "bytes-and-bytearray",
  "dicts",
  "string-formatting",
  "numbers",
]
+++

Literals are source-code forms for values: numbers, text, bytes, containers, booleans, `None`, and a few specialized markers. They are how a program writes small values directly.

The literal form is only the beginning. Later examples explain each value family in depth: strings are Unicode text, bytes are binary data, lists and dicts are containers, and `None` represents intentional absence.

Use literals when the value is small and local. Give repeated or meaningful values a name so the program explains why that value matters.

:::program
```python
whole = 42
fraction = 3.5
complex_number = 2 + 3j
print(whole, fraction, complex_number.imag)

text = "python"
raw_pattern = r"\d+"
data = b"py"
print(text)
print(raw_pattern)
print(data)

point = (2, 3)
names = ["Ada", "Grace"]
scores = {"Ada": 98}
unique = {"py", "go"}
print(point)
print(names[0])
print(scores["Ada"])
print(sorted(unique))

print(True, False, None)
print(...)
```
:::

:::cell
Numeric literals write numbers directly. Complex literals use `j` for the imaginary part.

```python
whole = 42
fraction = 3.5
complex_number = 2 + 3j
print(whole, fraction, complex_number.imag)
```

```output
42 3.5 3.0
```
:::

:::cell
String literals write Unicode text. Raw strings keep backslashes literal, and bytes literals write binary data rather than text.

```python
text = "python"
raw_pattern = r"\d+"
data = b"py"
print(text)
print(raw_pattern)
print(data)
```

```output
python
\d+
b'py'
```
:::

:::cell
Container literals create tuples, lists, dictionaries, and sets. Each container answers a different question about order, position, lookup, or uniqueness.

```python
point = (2, 3)
names = ["Ada", "Grace"]
scores = {"Ada": 98}
unique = {"py", "go"}
print(point)
print(names[0])
print(scores["Ada"])
print(sorted(unique))
```

```output
(2, 3)
Ada
98
['go', 'py']
```
:::

:::cell
`True`, `False`, `None`, and `...` are singleton literal-like constants used for truth values, absence, and placeholders.

```python
print(True, False, None)
print(...)
```

```output
True False None
Ellipsis
```
:::

:::note
- Literals are good for small local values; constants are better for repeated values with meaning.
- `{}` is an empty dictionary. Use `set()` for an empty set.
- Bytes literals are binary data; string literals are Unicode text.
- `...` evaluates to the `Ellipsis` object.
:::
