+++
slug = "unpacking"
title = "Unpacking"
section = "Collections"
summary = "Unpacking binds names from sequences and mappings concisely."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
+++

Unpacking binds multiple names from one iterable or mapping. It makes the structure of data visible at the point where values are introduced.

Starred unpacking handles variable-length sequences by collecting the middle or remaining values. This keeps common head-tail patterns readable.

Dictionary unpacking with ** connects structured data to function calls. It is widely used in configuration, adapters, and code that bridges APIs.

:::program
```python
point = (3, 4)
x, y = point
print(x, y)

first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)

def describe(name, language):
    print(name, language)

data = {"name": "Ada", "language": "Python"}
describe(**data)
```
:::

:::cell
Unpacking binds multiple names from one iterable or mapping. It makes the structure of data visible at the point where values are introduced.

```python
point = (3, 4)
x, y = point
print(x, y)
```

```output
3 4
```
:::

:::cell
Starred unpacking handles variable-length sequences by collecting the middle or remaining values. This keeps common head-tail patterns readable.

```python
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)
```

```output
1 [2, 3] 4
```
:::

:::cell
Dictionary unpacking with ** connects structured data to function calls. It is widely used in configuration, adapters, and code that bridges APIs.

Dictionary unpacking with ** connects structured data to function calls. It is widely used in configuration, adapters, and code that bridges APIs.

```python
def describe(name, language):
    print(name, language)

data = {"name": "Ada", "language": "Python"}
describe(**data)
```

```output
Ada Python
```
:::

:::note
- Starred unpacking collects the remaining values into a list.
- Dictionary unpacking with ** is common when calling functions with structured data.
- Prefer indexing when you need one position; prefer unpacking when naming several positions makes the shape clearer.
:::
