+++
slug = "typed-dicts"
title = "TypedDict"
section = "Types"
summary = "TypedDict describes dictionaries with known string keys."
doc_path = "/library/typing.html#typing.TypedDict"
see_also = [
  "dicts",
  "json",
  "dataclasses",
]
+++

`TypedDict` describes dictionary records with known keys. It is useful for JSON-like data that should remain a dictionary instead of becoming a class instance.

The important boundary is static versus runtime behavior. Type checkers can know that `name` is a string and `score` is an integer, but at runtime the value is still an ordinary `dict`.

Use `TypedDict` for external records and `dataclass` when your own program wants attribute access, methods, and construction behavior.

:::program
```python
from typing import NotRequired, TypedDict

class User(TypedDict):
    name: str
    score: int
    nickname: NotRequired[str]


def describe(user: User) -> str:
    return f"{user['name']}: {user['score']}"

record: User = {"name": "Ada", "score": 98}
print(describe(record))
print(isinstance(record, dict))
print(record.get("nickname", "none"))
```
:::

:::cell
Use `TypedDict` for JSON-like records that remain dictionaries.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    score: int


def describe(user: User) -> str:
    return f"{user['name']}: {user['score']}"

record: User = {"name": "Ada", "score": 98}
print(describe(record))
```

```output
Ada: 98
```
:::

:::cell
At runtime, a `TypedDict` value is still a plain dictionary.

```python
print(isinstance(record, dict))
print(type(record).__name__)
```

```output
True
dict
```
:::

:::cell
`NotRequired` marks a key that type checkers should treat as optional. Runtime lookup still uses normal dictionary tools such as `get()`.

```python
from typing import NotRequired

class UserWithNickname(TypedDict):
    name: str
    score: int
    nickname: NotRequired[str]

record: UserWithNickname = {"name": "Ada", "score": 98}
print(record.get("nickname", "none"))
```

```output
none
```
:::

:::note
- Use `TypedDict` for dictionary records from JSON or APIs.
- Type checkers understand required and optional keys.
- Runtime behavior is still ordinary dictionary behavior.
:::
