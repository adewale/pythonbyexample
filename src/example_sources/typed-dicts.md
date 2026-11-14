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
  "structured-data-shapes",
]
min_python = "3.13"
version_notes = "typing.ReadOnly and __readonly_keys__ were added in Python 3.13."
+++

`TypedDict` describes dictionary records with known keys. It is useful for JSON-like data that should remain a dictionary instead of becoming a class instance.

The important boundary is static versus runtime behavior. Type checkers can know that `name` is a string and `score` is an integer, but at runtime the value is still an ordinary `dict`.

Use `TypedDict` for external records and `dataclass` when your own program wants attribute access, methods, and construction behavior.

:::program
```python
from typing import NotRequired, ReadOnly, TypedDict

class User(TypedDict):
    name: str
    score: int
    nickname: NotRequired[str]


class Account(TypedDict):
    id: ReadOnly[int]
    name: str


def describe(user: User) -> str:
    return f"{user['name']}: {user['score']}"

record: User = {"name": "Ada", "score": 98}
print(describe(record))
print(isinstance(record, dict))
print(record.get("nickname", "none"))

account: Account = {"id": 7, "name": "Ada"}
account["name"] = "Grace"
print(account)
print(sorted(Account.__readonly_keys__))
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

:::cell
`ReadOnly`, added in Python 3.13, marks a key that type checkers should not allow code to reassign. Here a checker accepts the update to `name` and would reject `account["id"] = 8`. It is the same static-only boundary: the class records which keys are read-only, but the dictionary itself would still accept the write.

```python
from typing import ReadOnly

class Account(TypedDict):
    id: ReadOnly[int]
    name: str

account: Account = {"id": 7, "name": "Ada"}
account["name"] = "Grace"
print(account)
print(sorted(Account.__readonly_keys__))
```

```output
{'id': 7, 'name': 'Grace'}
['id']
```
:::

:::note
- Use `TypedDict` for dictionary records from JSON or APIs.
- `ReadOnly[...]` (Python 3.13) tells type checkers a key must not be reassigned; it does not freeze the dictionary.
- Type checkers understand required and optional keys.
- Runtime behavior is still ordinary dictionary behavior.
:::
