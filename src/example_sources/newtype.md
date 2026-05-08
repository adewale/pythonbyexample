+++
slug = "newtype"
title = "NewType"
section = "Types"
summary = "NewType creates distinct static identities for runtime-compatible values."
doc_path = "/library/typing.html#typing.NewType"
see_also = [
  "type-aliases",
  "type-hints",
  "runtime-type-checks",
]
+++

`NewType` creates a distinct static identity for a value that is represented by an existing runtime type. It is useful for IDs, units, and other values that should not be mixed accidentally.

The key boundary is static versus runtime behavior. A type checker can distinguish `UserId` from `OrderId`, but at runtime both values are plain integers.

Use a type alias when you only want a clearer name for a shape. Use `NewType` when mixing two compatible shapes should be treated as a mistake by static analysis.

:::program
```python
from typing import NewType

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def load_user(user_id: UserId) -> str:
    return f"user {user_id}"

uid = UserId(42)
oid = OrderId(42)
print(load_user(uid))
print(uid == oid)
print(type(uid).__name__)
print(UserId.__name__)
```
:::

:::cell
`NewType` helps type checkers distinguish values that share a runtime representation.

```python
from typing import NewType

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def load_user(user_id: UserId) -> str:
    return f"user {user_id}"

uid = UserId(42)
print(load_user(uid))
```

```output
user 42
```
:::

:::cell
At runtime, a `NewType` value is the underlying value. It compares like that value and has the same runtime type.

```python
oid = OrderId(42)
print(uid == oid)
print(type(uid).__name__)
```

```output
True
int
```
:::

:::cell
The `NewType` constructor keeps a name for static tools and introspection.

```python
print(UserId.__name__)
print(OrderId.__name__)
```

```output
UserId
OrderId
```
:::

:::note
- `NewType` helps type checkers distinguish values that share a runtime representation.
- At runtime, the value is still the underlying type.
- Use aliases for readability; use `NewType` for static separation.
:::
