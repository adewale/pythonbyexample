+++
slug = "unpacking"
title = "Unpacking"
section = "Collections"
summary = "Unpacking binds names from sequences and mappings concisely."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
see_also = [
  "tuples",
  "multiple-return-values",
  "args-and-kwargs",
  "dicts",
]
+++

Unpacking binds multiple names from one iterable or mapping. It makes the structure of data visible at the point where values are introduced.

Starred unpacking handles variable-length sequences by collecting the middle or remaining values. This keeps common head-tail patterns readable.

In a call, `*` spreads a sequence into positional arguments and `**` spreads a dictionary into keyword arguments, connecting structured data to function calls. It is widely used in configuration, adapters, and code that bridges APIs.

:::program
```python
point = (3, 4)
x, y = point
print(x, y)

first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)

print(*point)
print(*point, sep=", ")

data = {"name": "Ada", "language": "Python"}
print("{name} writes {language}".format(**data))
```
:::

:::cell
Tuple unpacking assigns each position to a name in one statement: `x` receives the first element of `point` and `y` the second. The assignment fails loudly if the number of names and elements disagree, which catches shape mistakes early.

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
The starred name collects however many elements the head and tail don't claim — here `first` and `last` take the ends and `*middle` gathers the rest into a list. The same list works whether it has four elements or forty.

```python
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)
```

```output
1 [2, 3] 4
```
:::

:::cell
The same stars work in a call. `print(*point)` spreads the tuple into separate positional arguments, and `format(**data)` spreads the dictionary's keys as keyword arguments, so the call site never repeats `name=` and `language=` by hand. This is the bridge between collection-shaped data (configuration, parsed JSON) and call signatures; [args and kwargs](/examples/args-and-kwargs) shows the receiving side.

```python
print(*point)
print(*point, sep=", ")

data = {"name": "Ada", "language": "Python"}
print("{name} writes {language}".format(**data))
```

```output
3 4
3, 4
Ada writes Python
```
:::

:::note
- Starred unpacking collects the remaining values into a list.
- Dictionary unpacking with ** is common when calling functions with structured data.
- Prefer indexing when you need one position; prefer unpacking when naming several positions makes the shape clearer.
:::
