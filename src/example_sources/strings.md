+++
slug = "strings"
title = "Strings"
section = "Text"
summary = "Strings are immutable Unicode text sequences."
doc_path = "/library/stdtypes.html#text-sequence-type-str"
+++

Python strings are immutable Unicode text sequences. A `str` stores text as Unicode code points, so it can represent Thai, accented letters, emoji, and ordinary ASCII with the same type.

This is different from bytes. Use `str` when you mean text, and encode to `bytes` only at boundaries such as files, network protocols, and binary APIs.

String operations such as `upper()` and `strip()` return new strings instead of changing the original. Use indexing and iteration for code points, and `encode()` when you need the underlying UTF-8 bytes.

:::program
```python
word = "สวัสดี"
print(len(word))
print(len(word.encode("utf-8")))
print(word[0])
print([hex(ord(char)) for char in word[:2]])

text = "  café  "
clean = text.strip()
print(clean)
print(clean.upper())
print(clean.encode("utf-8"))
```
:::

:::cell
A Python `str` is text, not raw bytes. `len()` counts Unicode code points, while UTF-8 encoding shows how many bytes are needed at a byte boundary.

```python
word = "สวัสดี"
print(len(word))
print(len(word.encode("utf-8")))
```

```output
6
18
```
:::

:::cell
Indexing and iteration work with Unicode code points. `ord()` returns the integer code point, which is often displayed in hexadecimal when teaching text encoding.

```python
print(word[0])
print([hex(ord(char)) for char in word[:2]])
```

```output
ส
['0xe2a', '0xe27']
```
:::

:::cell
String methods return new strings because strings are immutable. Encoding turns text into bytes when another system needs a byte representation.

```python
text = "  café  "
clean = text.strip()
print(clean)
print(clean.upper())
print(clean.encode("utf-8"))
```

```output
café
CAFÉ
b'caf\xc3\xa9'
```
:::

:::note
- Use `str` for text and `bytes` for binary data.
- `len(text)` counts Unicode code points; `len(text.encode("utf-8"))` counts encoded bytes.
- String methods return new strings because strings are immutable.
- User-visible “characters” can be more subtle than code points; combining marks and emoji sequences may need specialized text handling.
:::
