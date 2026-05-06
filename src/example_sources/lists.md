+++
slug = "lists"
title = "Lists"
section = "Collections"
summary = "Lists are ordered, mutable collections."
doc_path = "/tutorial/datastructures.html#more-on-lists"
+++

Lists are Python's general-purpose mutable sequence type. Use them when order matters and the collection may grow, shrink, or be rearranged.

Indexing reads individual positions. `0` is the first item, and negative indexes count backward from the end.

Mutation and copying matter: `append()` changes the list, while `sorted()` returns a new ordered list and leaves the original alone.

:::cell
Create a list with square brackets. Because lists are mutable, `append()` changes this same list object.

```python
numbers = [3, 1, 4]
numbers.append(1)

print(numbers)
```

```output
[3, 1, 4, 1]
```
:::

:::cell
Use indexes to read positions. Negative indexes are convenient for reading from the end.

```python
print(numbers[0])
print(numbers[-1])
```

```output
3
1
```
:::

:::cell
Use `sorted()` when you want an ordered copy and still need the original order afterward.

```python
print(sorted(numbers))
print(numbers)
```

```output
[1, 1, 3, 4]
[3, 1, 4, 1]
```
:::

:::note
- Lists are mutable sequences: methods such as `append()` change the list in place.
- Negative indexes count from the end.
- `sorted()` returns a new list; `list.sort()` sorts the existing list in place.
:::
