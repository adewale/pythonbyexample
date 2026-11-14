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

The callable must take no arguments. A method taken from an object, such as `queue.popleft`, already fits. Wrap a parameterized reader in a `lambda` or `functools.partial` when the underlying API needs parameters.

:::program
```python
from collections import deque

queue = deque(["py", "thon", "", "ignored"])
print(list(iter(queue.popleft, "")))
print(queue)

queue = deque(["py", "thon", "", "ignored"])
word = ""
while True:
    chunk = queue.popleft()
    if chunk == "":
        break
    word += chunk
print(word)
```
:::

:::cell
The two-argument form turns a polling callable into an iterator. `queue.popleft` (no parentheses) is a zero-argument callable that removes and returns the next queued item each time it is called. The empty string stops the loop without appearing in the result, and anything queued after the sentinel is left unread.

```python
from collections import deque

queue = deque(["py", "thon", "", "ignored"])
print(list(iter(queue.popleft, "")))
print(queue)
```

```output
['py', 'thon']
deque(['ignored'])
```
:::

:::cell
The equivalent manual loop needs an explicit read, comparison, and `break`. Use this shape when the stop condition is more complicated than a single sentinel value.

```python
queue = deque(["py", "thon", "", "ignored"])
word = ""
while True:
    chunk = queue.popleft()
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
