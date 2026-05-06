+++
slug = "context-managers"
title = "Context Managers"
section = "Data Model"
summary = "with ensures setup and cleanup happen together."
doc_path = "/reference/datamodel.html#context-managers"
+++

Context managers define setup and cleanup around a block of code. The with statement guarantees that cleanup runs when the block exits, even when an exception is raised.

The contextlib.contextmanager decorator is a concise way to write context managers as generators. Production code often uses with for files, locks, transactions, and temporary state.

Files, locks, and temporary state commonly use context managers. __enter__ and __exit__ power the protocol.

:::cell
Context managers define setup and cleanup around a block of code. The with statement guarantees that cleanup runs when the block exits, even when an exception is raised.

The contextlib.contextmanager decorator is a concise way to write context managers as generators. Production code often uses with for files, locks, transactions, and temporary state.

Files, locks, and temporary state commonly use context managers. __enter__ and __exit__ power the protocol.

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
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

:::note
- Files, locks, and temporary state commonly use context managers.
- __enter__ and __exit__ power the protocol.
:::
