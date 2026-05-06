+++
slug = "strings"
title = "Strings"
section = "Text"
summary = "Strings are immutable Unicode text sequences."
doc_path = "/library/stdtypes.html#text-sequence-type-str"
+++

Python strings are immutable Unicode text sequences. That means they behave like sequences for reading, but operations such as `lower()` and `strip()` create new strings instead of changing the original.

Common string work is transformation and composition: normalize case, remove surrounding whitespace, interpolate values, and join pieces with a separator.

Because strings are immutable, you can pass them around safely without worrying that another function will alter the object in place.

:::program
```python
language = "Python"
message = "  Python by Example  "

print(language[0])
print(language.lower())
print(message.strip())
print(f"Hello, {language}!")
print(", ".join(["lists", "dicts", "sets"]))
```
:::

:::cell
Strings store Unicode text and can be indexed like other sequences.

```python
language = "Python"
message = "  Python by Example  "

print(language[0])
```

```output
P
```
:::

:::cell
Methods such as `lower()` and `strip()` return transformed strings. They do not mutate the original value.

```python
print(language.lower())
print(message.strip())
```

```output
python
Python by Example
```
:::

:::cell
Use f-strings for readable interpolation and `join()` when a separator belongs between several pieces.

```python
print(f"Hello, {language}!")
print(", ".join(["lists", "dicts", "sets"]))
```

```output
Hello, Python!
lists, dicts, sets
```
:::

:::note
- Strings are sequences of Unicode characters, so indexing and many sequence operations work.
- String methods return new strings because strings are immutable.
- Use `join()` when building text from many pieces; it makes the separator explicit.
:::
