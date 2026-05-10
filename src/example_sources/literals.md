+++
slug = "literals"
title = "Literals"
section = "Basics"
summary = "Literals write values directly in Python source code."
doc_path = "/reference/lexical_analysis.html#literals"
see_also = [
  "values",
  "strings",
  "numbers",
  "string-formatting",
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

flags = 0xFF
mask = 0b1010
million = 1_000_000
print(flags, mask, million)

text = "python"
raw_pattern = r"\d+"
data = b"py"
score = 98
formatted = f"score={score}"
print(text)
print(raw_pattern)
print(data)
print(formatted)

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

print(type({}).__name__)
print(type(set()).__name__)
print(type({1, 2}).__name__)
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
Integer literals also accept hexadecimal (`0x`), binary (`0b`), and octal (`0o`) prefixes. Underscores group digits visually without changing the value.

```python
flags = 0xFF
mask = 0b1010
million = 1_000_000
print(flags, mask, million)
```

```output
255 10 1000000
```
:::

:::cell
String literals write Unicode text. Raw strings keep backslashes literal, bytes literals write binary data rather than text, and f-strings (`f"..."`) embed expressions inline.

```python
text = "python"
raw_pattern = r"\d+"
data = b"py"
score = 98
formatted = f"score={score}"
print(text)
print(raw_pattern)
print(data)
print(formatted)
```

```output
python
\d+
b'py'
score=98
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

:::cell
Curly-brace literals are dictionaries by default. The empty form `{}` is an empty dictionary, not an empty set; use `set()` for that. A non-empty `{1, 2}` is a set because keyless items can only be a set.

```python
print(type({}).__name__)
print(type(set()).__name__)
print(type({1, 2}).__name__)
```

```output
dict
set
set
```
:::

:::note
- Literals are good for small local values; constants are better for repeated values with meaning.
- `{}` is an empty dictionary. Use `set()` for an empty set.
- Bytes literals are binary data; string literals are Unicode text.
- `...` evaluates to the `Ellipsis` object.
:::
