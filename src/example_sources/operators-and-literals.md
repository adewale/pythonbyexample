+++
slug = "operators-and-literals"
title = "Operators and Literals"
section = "Basics"
summary = "Python has specialized operators and literal forms for particular data shapes."
doc_path = "/reference/lexical_analysis.html#literals"
see_also = [
  "numbers",
  "strings",
  "sets",
]
+++

Most examples use everyday operators, but Python also has syntax for specialized domains: bytes, raw strings, complex numbers, bit operations, and custom infix operations.

Use these forms when the data shape calls for them. A raw string is useful for patterns, bytes are useful for binary data, and bit operators are useful for masks and sets.

The `@` operator is reserved for matrix-like multiplication and other types that define `__matmul__`.

:::program
```python
pattern = r"\d+"
data = b"py"
number = 2 + 3j
print(pattern)
print(data)
print(number.real)

flags = 0b0011
print(flags ^ 0b0101)
print(flags << 1)
print(~0)
print(sorted({"python", "go"} ^ {"go", "rust"}))

class Scale:
    def __init__(self, value):
        self.value = value

    def __matmul__(self, other):
        return self.value * other.value

print(Scale(2) @ Scale(3))
print(...)
```
:::

:::cell
Raw strings keep backslashes literal, bytes literals store binary data, and complex literals use `j` for the imaginary part.

```python
pattern = r"\d+"
data = b"py"
number = 2 + 3j
print(pattern)
print(data)
print(number.real)
```

```output
\d+
b'py'
2.0
```
:::

:::cell
Bit operators work on integers and some collection types. For sets, `^` means symmetric difference: values in either set but not both.

```python
flags = 0b0011
print(flags ^ 0b0101)
print(flags << 1)
print(~0)
print(sorted({"python", "go"} ^ {"go", "rust"}))
```

```output
6
6
-1
['python', 'rust']
```
:::

:::cell
The `@` operator calls `__matmul__` on custom objects. `...` is the `Ellipsis` literal, commonly used as a placeholder in stubs and slicing APIs.

```python
class Scale:
    def __init__(self, value):
        self.value = value

    def __matmul__(self, other):
        return self.value * other.value

print(Scale(2) @ Scale(3))
print(...)
```

```output
6
Ellipsis
```
:::

:::note
- Raw strings are useful when backslashes are part of the data, such as regular expressions.
- Bytes literals represent binary data, not text strings.
- Prefer everyday strings, numbers, and operators until the data shape calls for these specialized forms.
- Specialized operators should make the data model clearer, not more mysterious.
:::
