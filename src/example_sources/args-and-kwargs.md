+++
slug = "args-and-kwargs"
title = "Args and Kwargs"
section = "Functions"
summary = "*args collects extra positional arguments and **kwargs collects named ones."
doc_path = "/tutorial/controlflow.html#arbitrary-argument-lists"
+++

`*args` and `**kwargs` let a function accept flexible positional and keyword arguments. They are the function-definition counterpart to unpacking at a call site.

These parameters are useful for wrappers, decorators, logging helpers, and APIs that forward arguments to another function.

They should not replace clear signatures. If a function has a stable interface, explicit parameters document expectations better than a bag of arguments.

:::program
```python
def total(*numbers):
    return sum(numbers)

print(total(2, 3, 5))


def describe(**metadata):
    print(metadata)

describe(owner="Ada", public=True)


def report(title, *items, **metadata):
    print(title)
    print(items)
    print(metadata)

report("scores", 10, 9, owner="Ada")
```
:::

:::cell
`*args` collects extra positional arguments into a tuple. This fits functions that naturally accept any number of similar values.

```python
def total(*numbers):
    return sum(numbers)

print(total(2, 3, 5))
```

```output
10
```
:::

:::cell
`**kwargs` collects named arguments into a dictionary. The names become string keys.

```python
def describe(**metadata):
    print(metadata)

describe(owner="Ada", public=True)
```

```output
{'owner': 'Ada', 'public': True}
```
:::

:::cell
A function can combine explicit parameters, `*args`, and `**kwargs`. Put the flexible parts last so the fixed shape remains visible.

```python
def report(title, *items, **metadata):
    print(title)
    print(items)
    print(metadata)

report("scores", 10, 9, owner="Ada")
```

```output
scores
(10, 9)
{'owner': 'Ada'}
```
:::

:::note
- Use these tools when a function naturally accepts a flexible shape.
- Prefer explicit parameters when the accepted arguments are known and fixed.
- `*args` is a tuple; `**kwargs` is a dictionary.
:::
