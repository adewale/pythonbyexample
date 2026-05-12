+++
slug = "slices"
title = "Slices"
section = "Collections"
summary = "Slices copy meaningful ranges from ordered sequences."
doc_path = "/tutorial/introduction.html#lists"
see_also = [
  "lists",
  "tuples",
  "strings",
]
+++

Slicing reads a range from an ordered sequence with `start:stop:step`. It exists because Python code often needs a meaningful piece of a sequence: a page, a prefix, a tail, a stride, or a reversed view.

The stop index is excluded. That convention makes lengths and adjacent ranges line up: `items[:3]` and `items[3:]` split a sequence without overlap.

Slices return new sequence objects for built-in lists and strings. Use indexing for one item; use slicing when the result should still be a sequence.

:::program
```python
letters = ["a", "b", "c", "d", "e", "f"]
first_page = letters[:3]
rest = letters[3:]
print(first_page)
print(rest)

middle = letters[1:5]
every_other = letters[::2]
reversed_letters = letters[::-1]
print(middle)
print(every_other)
print(reversed_letters)
print(letters)
```
:::

:::cell
Omitted bounds mean “from the beginning” or “through the end.” Because the stop index is excluded, adjacent slices split a sequence cleanly.

```python
letters = ["a", "b", "c", "d", "e", "f"]
first_page = letters[:3]
rest = letters[3:]
print(first_page)
print(rest)
```

```output
['a', 'b', 'c']
['d', 'e', 'f']
```
:::

:::cell
Use `start:stop` for a middle range and `step` when you want to skip or walk backward. These operations return new lists; the original list is unchanged.

```python
middle = letters[1:5]
every_other = letters[::2]
reversed_letters = letters[::-1]
print(middle)
print(every_other)
print(reversed_letters)
print(letters)
```

```output
['b', 'c', 'd', 'e']
['a', 'c', 'e']
['f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f']
```
:::

:::note
- Slice stop indexes are excluded, so adjacent ranges compose cleanly.
- Omitted bounds mean the beginning or end of the sequence.
- A negative step walks backward; `[::-1]` is a common reversed-copy idiom.
:::
