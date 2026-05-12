+++
slug = "mutability"
title = "Mutability"
section = "Data Model"
summary = "Some objects change in place, while others return new values."
doc_path = "/reference/datamodel.html#objects-values-and-types"
see_also = [
  "variables",
  "object-lifecycle",
  "copying-collections",
  "lists",
]
+++

Objects in Python can be mutable or immutable. Mutable objects such as lists and dictionaries can change in place, while immutable objects such as strings and tuples produce new values instead.

Names can share one mutable object, so a change through one name is visible through another. This is powerful, but it is also the source of many beginner surprises.

The boundary matters across Python: `append()` mutates a list, string methods return new strings, and `sorted()` returns a new list while `list.sort()` mutates an existing one.

:::program
```python
first = ["python"]
second = first
second.append("workers")
print(first)
print(second)

text = "python"
upper_text = text.upper()
print(text)
print(upper_text)

numbers = [3, 1, 2]
ordered = sorted(numbers)
print(ordered)
print(numbers)
```
:::

:::cell
Mutable objects can change in place. `first` and `second` point to the same list, so appending through one name changes the object seen through both names.

```python
first = ["python"]
second = first
second.append("workers")
print(first)
print(second)
```

```output
['python', 'workers']
['python', 'workers']
```
:::

:::cell
Immutable objects do not change in place. String methods such as `upper()` return a new string, leaving the original string unchanged.

```python
text = "python"
upper_text = text.upper()
print(text)
print(upper_text)
```

```output
python
PYTHON
```
:::

:::cell
Some APIs make the boundary explicit. `sorted()` returns a new list, while methods such as `append()` and `list.sort()` mutate an existing list.

```python
numbers = [3, 1, 2]
ordered = sorted(numbers)
print(ordered)
print(numbers)
```

```output
[1, 2, 3]
[3, 1, 2]
```
:::

:::note
- Lists and dictionaries are mutable; strings and tuples are immutable.
- Aliasing is useful, but copy mutable containers when independent changes are needed.
- Pay attention to whether an operation mutates in place or returns a new value.
:::
