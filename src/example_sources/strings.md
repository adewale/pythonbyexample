+++
slug = "strings"
title = "Strings"
section = "Text"
summary = "Strings are immutable Unicode text sequences."
doc_path = "/library/stdtypes.html#text-sequence-type-str"
see_also = [
  "values",
  "string-formatting",
  "bytes-and-bytearray",
  "regular-expressions",
]
+++

Python strings are immutable Unicode text sequences. A `str` stores text as Unicode code points, so it can represent English, Thai, accented letters, emoji, and ordinary ASCII with the same type.

Unicode matters because text length and byte length are different questions. The English word `"hello"` uses five code points and five UTF-8 bytes because ASCII characters encode as one byte each. The Thai greeting `"สวัสดี"` has six code points but needs eighteen UTF-8 bytes.

Use `str` when you mean text, and encode to `bytes` only at boundaries such as files, network protocols, and binary APIs. String operations such as `upper()` and `strip()` return new strings instead of changing the original.

:::program
```python
english = "hello"
french = "café"
thai = "สวัสดี"

for label, word in [("English", english), ("French", french), ("Thai", thai)]:
    print(label, word, len(word), len(word.encode("utf-8")))

print(thai[0])
print([hex(ord(char)) for char in thai[:2]])

text = "  café  "
clean = text.strip()
print(clean)
print(clean.upper())
print(clean.encode("utf-8"))
```
:::

:::cell
Compare three words by code-point count and UTF-8 byte count. ASCII characters take one byte each (`hello` → 5 bytes); the `é` in `café` is one code point but two UTF-8 bytes; each Thai character takes three. The `str` type abstracts over all three.

```python
english = "hello"
french = "café"
thai = "สวัสดี"

for label, word in [("English", english), ("French", french), ("Thai", thai)]:
    print(label, word, len(word), len(word.encode("utf-8")))
```

```output
English hello 5 5
French café 4 5
Thai สวัสดี 6 18
```
:::

:::cell
Indexing and iteration work with Unicode code points, not encoded bytes. `ord()` returns the integer code point, which is often displayed in hexadecimal when teaching text encoding.

```python
print(thai[0])
print([hex(ord(char)) for char in thai[:2]])
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
- ASCII text is a useful baseline because each ASCII code point is one UTF-8 byte.
- String methods return new strings because strings are immutable.
- User-visible “characters” can be more subtle than code points; combining marks and emoji sequences may need specialized text handling.
:::
