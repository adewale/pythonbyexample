+++
slug = "context-managers"
title = "Context Managers"
section = "Data Model"
summary = "with ensures setup and cleanup happen together."
doc_path = "/reference/datamodel.html#context-managers"
see_also = [
  "exceptions",
  "special-methods",
  "descriptors",
]
+++

Context managers define setup and cleanup around a block of code. The `with` statement guarantees that cleanup runs when the block exits, even when an exception is raised.

The protocol is powered by `__enter__` and `__exit__`. The `contextlib.contextmanager` decorator is a concise way to write the same idea as a generator when a full class would be noisy.

Production code often uses `with` for files, locks, transactions, temporary state, and resources that need reliable release.

:::program
```python
from contextlib import contextmanager

class Tag:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"<{self.name}>")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"</{self.name}>")
        return False

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with Tag("section"):
    print("content")

try:
    with tag("error"):
        raise ValueError("boom")
except ValueError:
    print("handled")
```
:::

:::cell
A class-based context manager implements `__enter__` and `__exit__`. The value returned by `__enter__` is bound by `as` when the `with` statement uses it.

```python
class Tag:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"<{self.name}>")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"</{self.name}>")
        return False

with Tag("section"):
    print("content")
```

```output
<section>
content
</section>
```
:::

:::cell
`contextlib.contextmanager` writes the same setup/cleanup shape as a generator. Code before `yield` is setup, and code after `yield` is cleanup.

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("note"):
    print("body")
```

```output
<note>
body
</note>
```
:::

:::cell
Cleanup still runs when the block raises. Returning `False` from `__exit__`, or letting a generator context manager re-raise, allows the exception to keep propagating.

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
- Returning true from `__exit__` suppresses an exception; do that only intentionally.
:::
