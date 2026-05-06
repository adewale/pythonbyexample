+++
slug = "tuples"
title = "Tuples"
section = "Collections"
summary = "Tuples are ordered, immutable collections often used for records."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
+++

Tuples are ordered immutable sequences. They are useful for small fixed records such as coordinates, colors, or multiple return values.

Unpacking turns positional data into named local variables. That makes tuple use readable when each position has a clear meaning.

Because tuples are immutable, their length and item references cannot be changed in place after creation.

:::cell
Use tuples for fixed-size groups where the positions are part of the meaning.

Unpacking gives useful names to tuple positions instead of leaving readers to remember indexes.

```python
point = (3, 4)
red = (255, 0, 0)

x, y = point
print(x + y)
```

```output
7
```
:::

:::cell
Tuples compare by value and keep their fixed structure.

```python
print(red)
print(point == (3, 4))
```

```output
(255, 0, 0)
True
```
:::

:::note
- Tuples are immutable sequences with fixed length.
- Use tuples for small records where position has meaning.
- Unpacking gives names to tuple positions at the point of use.
:::
