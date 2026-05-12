+++
slug = "sentinel-iteration"
title = "Sentinel Iteration"
section = "Iteration"
summary = "iter(callable, sentinel) repeats calls until a marker value appears."
doc_path = "/library/functions.html#iter"
see_also = [
  "iterators",
  "while-loops",
  "break-and-continue",
]
+++

`iter(callable, sentinel)` calls a zero-argument callable over and over. It yields each result until the callable returns the sentinel value, and the sentinel itself is not yielded.

This shape is useful for repeated reads: file blocks until `b""`, socket chunks until an empty response, queue items until a stop marker. It removes the common `while True` plus `break` scaffolding when the loop body is otherwise just "read, then process".

The callable must take no arguments. Wrap a parameterized reader in a `lambda`, `functools.partial`, or object method when the underlying API needs parameters.

:::program
```python
chunks = iter(["py", "thon", ""])


def read_chunk():
    return next(chunks)

print(list(iter(read_chunk, "")))

chunks = iter(["py", "thon", ""])
word = ""
while True:
    chunk = next(chunks)
    if chunk == "":
        break
    word += chunk
print(word)
```
:::

:::cell
The two-argument form turns a polling callable into an iterator. The empty string stops the loop without appearing in the result.

```python
chunks = iter(["py", "thon", ""])


def read_chunk():
    return next(chunks)

print(list(iter(read_chunk, "")))
```

```output
['py', 'thon']
```
:::

:::cell
The equivalent manual loop needs an explicit read, comparison, and `break`. Use this shape when the stop condition is more complicated than a single sentinel value.

```python
chunks = iter(["py", "thon", ""])
word = ""
while True:
    chunk = next(chunks)
    if chunk == "":
        break
    word += chunk
print(word)
```

```output
python
```
:::

:::note
- The callable passed to `iter(callable, sentinel)` must take no arguments.
- The sentinel stops iteration and is not yielded.
- When the loop needs richer branching, an explicit `while` loop may be clearer.
:::
