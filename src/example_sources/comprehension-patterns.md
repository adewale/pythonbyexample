+++
slug = "comprehension-patterns"
title = "Comprehension Patterns"
section = "Collections"
summary = "Comprehensions can use multiple for clauses and filters when the shape stays clear."
doc_path = "/tutorial/datastructures.html#list-comprehensions"
see_also = [
  "comprehensions",
  "generator-expressions",
  "for-loops",
]
+++

Comprehensions can contain more than one `for` clause and more than one `if` filter. The clauses are read in the same order as nested loops.

Use these forms only while the shape remains easy to scan. If a comprehension starts needing several names, comments, or branches, an explicit loop is usually better.

Nested comprehensions build concrete collections immediately, just like simpler list, dict, and set comprehensions.

:::program
```python
colors = ["red", "blue"]
sizes = ["S", "M"]
variants = [(color, size) for color in colors for size in sizes]
print(variants)

numbers = range(10)
filtered = [n for n in numbers if n % 2 == 0 if n > 2]
print(filtered)
```
:::

:::cell
Multiple `for` clauses behave like nested loops. The leftmost `for` is the outer loop, and the next `for` runs inside it.

```python
colors = ["red", "blue"]
sizes = ["S", "M"]
variants = [(color, size) for color in colors for size in sizes]
print(variants)
```

```output
[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
```
:::

:::cell
Multiple `if` clauses filter values. They are useful for simple conditions, but an explicit loop is clearer when the rules need names or explanation.

```python
numbers = range(10)
filtered = [n for n in numbers if n % 2 == 0 if n > 2]
print(filtered)
```

```output
[4, 6, 8]
```
:::

:::note
- Read comprehension clauses from left to right.
- Multiple `for` clauses act like nested loops.
- Prefer an explicit loop when the comprehension stops being obvious.
:::
