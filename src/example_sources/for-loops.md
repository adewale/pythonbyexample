+++
slug = "for-loops"
title = "For Loops"
section = "Control Flow"
summary = "for iterates over any iterable object."
doc_path = "/tutorial/controlflow.html#for-statements"
+++

Python for loops iterate over values from an iterable. This is different from languages where for primarily means incrementing a numeric counter.

range() is itself an iterable that produces numbers lazily. Use it when you need a sequence of integers, but prefer direct iteration when you already have a collection.

Blocks are defined by indentation. range(3) yields 0, 1, and 2.

:::cell
Python for loops iterate over values from an iterable. This is different from languages where for primarily means incrementing a numeric counter.

```python
for name in ["Ada", "Grace", "Guido"]:
    print(name)
```

```output
Ada
Grace
Guido
```
:::

:::cell
range() is itself an iterable that produces numbers lazily. Use it when you need a sequence of integers, but prefer direct iteration when you already have a collection.

```python
for number in range(3):
    print(number)
```

```output
0
1
2
```
:::

:::note
- Blocks are defined by indentation.
- range(3) yields 0, 1, and 2.
:::
