+++
slug = "tuples"
title = "Tuples"
section = "Collections"
summary = "Tuples group a fixed number of positional values."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
+++

Tuples are ordered, immutable sequences. They exist for small fixed groups where position has meaning: coordinates, RGB colors, database rows, and multiple return values.

Use lists for variable-length collections of similar items. Use tuples when the number of positions is part of the data shape and unpacking can give each position a useful name.

Because tuples are immutable, you cannot append or replace positions in place. If the shape needs to grow or change, a list or dataclass is usually a better fit.

:::program
```python
point = (3, 4)
x, y = point
print(x + y)

red = (255, 0, 0)
print(red[0])
print(len(red))

record = ("Ada", 10)
name, score = record
print(f"{name}: {score}")

scores = [10, 9, 8]
scores.append(7)
print(scores)

student = ("Ada", 2024, "math")
name, year, subject = student
print(name, year, subject)
```
:::

:::cell
Use a tuple for a fixed-size record where each position has a known meaning. Unpacking turns those positions into names at the point of use.

```python
point = (3, 4)
x, y = point
print(x + y)
```

```output
7
```
:::

:::cell
Tuples are sequences, so indexing and `len()` work. They are different from lists because their length and item references are fixed after creation.

```python
red = (255, 0, 0)
print(red[0])
print(len(red))
```

```output
255
3
```
:::

:::cell
Tuples pair naturally with multiple return values and unpacking. If the fields need names everywhere, graduate to a dataclass or named tuple.

```python
record = ("Ada", 10)
name, score = record
print(f"{name}: {score}")
```

```output
Ada: 10
```
:::

:::cell
Lists and tuples carry different intent. A list holds a variable number of similar items and grows with `append`; a tuple has a fixed shape where each position has its own meaning, and unpacking gives those positions names.

```python
scores = [10, 9, 8]
scores.append(7)
print(scores)

student = ("Ada", 2024, "math")
name, year, subject = student
print(name, year, subject)
```

```output
[10, 9, 8, 7]
Ada 2024 math
```
:::

:::note
- Tuples are immutable sequences with fixed length.
- Use tuples for small records where position has meaning.
- Use lists for variable-length collections of similar items.
- Reach for a dataclass or `NamedTuple` when fields deserve names everywhere they're used.
:::
