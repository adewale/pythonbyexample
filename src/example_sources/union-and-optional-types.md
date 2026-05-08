+++
slug = "union-and-optional-types"
title = "Union and Optional Types"
section = "Types"
summary = "The | operator describes values that may have more than one static type."
doc_path = "/library/typing.html#typing.Optional"
see_also = [
  "none",
  "type-hints",
  "match-statements",
]
+++

A union type says that a value may have one of several static shapes. `int | str` means callers may pass either an integer or a string.

`T | None` is the modern spelling for an optional value. The annotation documents that absence is expected, but the code still needs to handle `None` before using the non-optional behavior.

Unions are useful at boundaries where input is flexible. Inside a function, narrow the value with an `is None`, `isinstance()`, or pattern check so the rest of the code has one clear shape.

:::program
```python
def label(value: int | str) -> str:
    return f"item-{value}"


def greeting(name: str | None) -> str:
    if name is None:
        return "hello guest"
    return f"hello {name.upper()}"

print(label(3))
print(label("A"))
print(greeting(None))
print(greeting("Ada"))
print(greeting.__annotations__)
```
:::

:::cell
Use `A | B` when a value may have either type. The function body should use operations that make sense for every member of the union.

```python
def label(value: int | str) -> str:
    return f"item-{value}"

print(label(3))
print(label("A"))
```

```output
item-3
item-A
```
:::

:::cell
`str | None` means the function accepts either a string or explicit absence. Check for `None` before calling string methods.

```python
def greeting(name: str | None) -> str:
    if name is None:
        return "hello guest"
    return f"hello {name.upper()}"

print(greeting(None))
print(greeting("Ada"))
```

```output
hello guest
hello ADA
```
:::

:::cell
Union annotations are visible at runtime, but Python does not enforce them when the function is called.

```python
print(greeting.__annotations__)
```

```output
{'name': str | None, 'return': <class 'str'>}
```
:::

:::note
- Use `A | B` when a value may have either type.
- `T | None` means absence is an expected case, not an error by itself.
- Narrow unions before using behavior that belongs to only one member type.
:::
