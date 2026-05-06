+++
slug = "args-and-kwargs"
title = "Args and Kwargs"
section = "Functions"
summary = "*args collects extra positional arguments and **kwargs collects named ones."
doc_path = "/tutorial/controlflow.html#arbitrary-argument-lists"
+++

*args and **kwargs let a function accept flexible positional and keyword arguments. They are the function-call counterpart to unpacking.

These parameters are useful for wrappers, decorators, logging helpers, and APIs that forward arguments to another function.

They should not replace clear signatures. If a function has a stable interface, explicit parameters document expectations better than a bag of arguments.

:::program
```python
def report(title, *items, **metadata):
    print(title)
    print(items)
    print(metadata)

report("scores", 10, 9, owner="Ada", public=True)
```
:::

:::cell
*args and **kwargs let a function accept flexible positional and keyword arguments. They are the function-call counterpart to unpacking.

These parameters are useful for wrappers, decorators, logging helpers, and APIs that forward arguments to another function.

```python
def report(title, *items, **metadata):
    print(title)
    print(items)
    print(metadata)

report("scores", 10, 9, owner="Ada", public=True)
```

```output
scores
(10, 9)
{'owner': 'Ada', 'public': True}
```
:::

:::note
- Use these tools when a function naturally accepts a flexible shape.
- Prefer explicit parameters when the accepted arguments are known and fixed.
:::
