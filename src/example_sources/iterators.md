+++
slug = "iterators"
title = "Iterators"
section = "Iteration"
summary = "iter and next expose the protocol behind for loops."
doc_path = "/library/stdtypes.html#iterator-types"
+++

An iterable is an object that can produce values for a loop. An iterator is the object that remembers where that production currently is.

`iter()` asks an iterable for an iterator, and `next()` consumes one value from that iterator. A `for` loop performs those steps for you until the iterator is exhausted.

This is the core value-stream protocol in Python: one object produces values, another piece of code consumes them, and many streams are one-pass.

:::program
```python
names = ["Ada", "Grace", "Guido"]
iterator = iter(names)
print(next(iterator))
print(next(iterator))

for name in iterator:
    print(name)

again = iter(names)
print(next(again))
```
:::

:::cell
`iter()` asks an iterable for an iterator. `next()` consumes one value and advances the iterator's position.

```python
names = ["Ada", "Grace", "Guido"]
iterator = iter(names)
print(next(iterator))
print(next(iterator))
```

```output
Ada
Grace
```
:::

:::cell
A `for` loop consumes the same iterator protocol. Because two values were already consumed, the loop sees only the remaining value.

```python
for name in iterator:
    print(name)
```

```output
Guido
```
:::

:::cell
The list itself is reusable. Asking it for a fresh iterator starts a new pass over the same stored values.

```python
again = iter(names)
print(next(again))
```

```output
Ada
```
:::

:::note
- Iterables produce iterators; iterators produce values.
- `next()` consumes one value from an iterator.
- Many iterators are one-pass even when the original collection is reusable.
:::
