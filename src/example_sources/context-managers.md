+++
slug = "context-managers"
title = "Context Managers"
section = "Data Model"
summary = "with ensures setup and cleanup happen together."
doc_path = "/reference/datamodel.html#context-managers"
+++

Context managers define setup and cleanup around a block of code. The `with` statement guarantees that cleanup runs when the block exits, even when an exception is raised.

The `contextlib.contextmanager` decorator is a concise way to write context managers as generators. Production code often uses `with` for files, locks, transactions, and temporary state.

The protocol is powered by `__enter__` and `__exit__`, but many custom context managers can be written clearly with `contextmanager`.

:::program
```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("section"):
    print("content")

try:
    with tag("error"):
        raise ValueError("boom")
except ValueError:
    print("handled")
```
:::

:::cell
A context manager surrounds a block. Code before `yield` is setup, and code after `yield` is cleanup.

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("section"):
    print("content")
```

```output
<section>
content
</section>
```
:::

:::cell
Putting cleanup in `finally` ensures it runs even when the block raises. The surrounding `try` catches the error after cleanup has happened.

```python
try:
    with tag("error"):
        raise ValueError("boom")
except ValueError:
    print("handled")
```

```output
<error>
</error>
handled
```
:::

:::note
- Files, locks, and temporary state commonly use context managers.
- `__enter__` and `__exit__` power the protocol.
- Use `finally` when cleanup must happen after errors too.
:::
