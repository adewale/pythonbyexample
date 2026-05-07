+++
slug = "enums"
title = "Enums"
section = "Types"
summary = "Enum defines symbolic names for a fixed set of values."
doc_path = "/library/enum.html"
+++

`Enum` defines a fixed set of named values. This makes states and modes easier to read than raw strings scattered through a program.

Each enum member has a name and a value. Comparing enum members is explicit and helps avoid typos that plain strings would allow.

Use enums when a value must be one of a small known set: statuses, modes, directions, roles, and similar choices.

:::program
```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"

current = Status.PENDING
print(current.name)
print(current.value)
print(current is Status.PENDING)
print(current == "pending")
```
:::

:::cell
An enum member has a symbolic name and an underlying value. The symbolic name is what readers usually care about in code.

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"

current = Status.PENDING
print(current.name)
print(current.value)
```

```output
PENDING
pending
```
:::

:::cell
Compare enum members with enum members, not with raw strings. This keeps the set of valid states explicit.

```python
print(current is Status.PENDING)
print(current == "pending")
```

```output
True
False
```
:::

:::note
- Enums make states and choices explicit.
- Members have names and values.
- Comparing enum members avoids string typo bugs.
- Prefer raw strings for open-ended text; prefer enums for a closed set of named choices.
:::
