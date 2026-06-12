+++
slug = "bytes-and-bytearray"
title = "Bytes and Bytearray"
section = "Text"
summary = "bytes and bytearray store binary data, not Unicode text."
doc_path = "/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview"
see_also = [
  "strings",
  "literals",
  "networking",
]
+++

`str` stores Unicode text. `bytes` stores raw byte values. The boundary matters whenever text leaves Python for a file, network protocol, subprocess, or binary format.

Encoding turns text into bytes with a named encoding such as UTF-8. Decoding turns bytes back into text. The lengths can differ because one Unicode character may require several bytes.

Use immutable `bytes` for stable binary data and `bytearray` when the bytes must be changed in place.

:::program
```python
text = "café"
data = text.encode("utf-8")

print(data)
print(len(text), len(data))
print(data.decode("utf-8"))
print(data[0])

packet = bytearray(b"py")
packet[0] = ord("P")
print(packet)
```
:::

:::cell
Encode text when an external boundary needs bytes. UTF-8 uses one byte for ASCII characters and more than one byte for many other characters.

```python
text = "café"
data = text.encode("utf-8")
print(data)
print(len(text), len(data))
```

```output
b'caf\xc3\xa9'
4 5
```
:::

:::cell
Decode bytes when the program needs text again. The decoder must match the encoding used at the boundary.

```python
print(data.decode("utf-8"))
```

```output
café
```
:::

:::cell
Indexing a `bytes` object returns an integer byte value, not a one-character `bytes` object.

```python
print(data[0])
```

```output
99
```
:::

:::cell
`bytes` is immutable. Use `bytearray` when binary data must be changed in place.

```python
packet = bytearray(b"py")
packet[0] = ord("P")
print(packet)
```

```output
bytearray(b'Py')
```
:::

:::note
- Encode text when an external boundary needs bytes.
- Decode bytes when you want text again.
- Indexing `bytes` returns integers from 0 to 255.
- Use `bytearray` when binary data must be changed in place.
:::
