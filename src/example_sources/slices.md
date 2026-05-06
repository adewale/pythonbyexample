+++
slug = "slices"
title = "Slices"
section = "Collections"
summary = "Slices select ranges from sequences."
doc_path = "/tutorial/introduction.html#lists"
+++

Slicing reads a range from a sequence with `start:stop:step`. It is one of Python's most compact tools for working with ordered data.

The stop index is excluded. This convention makes lengths and adjacent slices easier to reason about.

Omitted bounds default to the beginning or end, and the optional step can skip items or reverse a sequence.

:::program
```python
letters = ["a", "b", "c", "d", "e"]

print(letters[1:4])
print(letters[:2])
print(letters[2:])
print(letters[::2])
print(letters[::-1])
```
:::

:::cell
Start with an ordered sequence. Slices return selected ranges without changing the original list.

The stop index is excluded. Omitting a bound means “from the beginning” or “through the end.”

```python
letters = ["a", "b", "c", "d", "e"]

print(letters[1:4])
print(letters[:2])
print(letters[2:])
```

```output
['b', 'c', 'd']
['a', 'b']
['c', 'd', 'e']
```
:::

:::cell
The step controls how the slice moves. A step of `2` skips, and `-1` walks backward.

```python
print(letters[::2])
print(letters[::-1])
```

```output
['a', 'c', 'e']
['e', 'd', 'c', 'b', 'a']
```
:::

:::note
- Slice stop indexes are excluded, so adjacent ranges compose cleanly.
- Omitted bounds mean the beginning or end of the sequence.
- A negative step walks backward through the sequence.
:::
