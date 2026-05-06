+++
slug = "comprehensions"
title = "Comprehensions"
section = "Collections"
summary = "Comprehensions build collections from iterables concisely."
doc_path = "/tutorial/datastructures.html#list-comprehensions"
+++

Comprehensions build lists, dictionaries, and sets from iterables in a compact form. They combine mapping and optional filtering in one expression.

Use comprehensions for straightforward transformations. If the expression becomes hard to read, an explicit loop is often the better teaching and maintenance choice.

Comprehensions combine mapping and filtering. Keep complex comprehensions readable.

:::program
```python
squares = [n * n for n in range(6)]
even_squares = {n: n * n for n in range(6) if n % 2 == 0}
print(squares)
print(even_squares)
```
:::

:::cell
Comprehensions build lists, dictionaries, and sets from iterables in a compact form. They combine mapping and optional filtering in one expression.

```python
squares = [n * n for n in range(6)]
even_squares = {n: n * n for n in range(6) if n % 2 == 0}
print(squares)
print(even_squares)
```

```output
[0, 1, 4, 9, 16, 25]
{0: 0, 2: 4, 4: 16}
```
:::

:::note
- Comprehensions combine mapping and filtering.
- Keep complex comprehensions readable.
:::
