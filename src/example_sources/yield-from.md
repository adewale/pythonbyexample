+++
slug = "yield-from"
title = "Yield From"
section = "Iteration"
summary = "yield from delegates part of a generator to another iterable."
doc_path = "/reference/expressions.html#yield-expressions"
see_also = [
  "generators",
  "generator-expressions",
  "itertools",
]
+++

`yield from` lets one generator yield every value from another iterable. It is a compact way to delegate part of a stream.

Use it when a generator is mostly stitching together other iterables or sub-generators. It keeps the producer pipeline visible without writing a nested `for` loop.

The consumer still sees one stream of values.

:::program
```python
def page():
    yield "header"
    yield from ["intro", "body"]
    yield "footer"

print(list(page()))


def flatten(rows):
    for row in rows:
        yield from row

print(list(flatten([[1, 2], [3]])))
```
:::

:::cell
`yield from` delegates to another iterable. The caller receives one stream even though part of it came from a list.

```python
def page():
    yield "header"
    yield from ["intro", "body"]
    yield "footer"

print(list(page()))
```

```output
['header', 'intro', 'body', 'footer']
```
:::

:::cell
Delegation is useful when flattening nested iterables. `yield from row` replaces an inner loop that would yield each item by hand.

```python
def flatten(rows):
    for row in rows:
        yield from row

print(list(flatten([[1, 2], [3]])))
```

```output
[1, 2, 3]
```
:::

:::note
- `yield from iterable` yields each value from that iterable.
- It keeps generator pipelines compact.
- Use a plain `yield` when producing one value directly.
:::
