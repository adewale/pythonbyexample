+++
slug = "enums"
title = "Enums"
section = "Types"
summary = "Enum defines symbolic names for a fixed set of values."
doc_path = "/library/enum.html"
+++

Enum defines a fixed set of named values. This makes states and modes easier to read than raw strings scattered through a program.

Each enum member has a name and a value. Comparing enum members is explicit and helps avoid typos that plain strings would allow.

Enums make states and choices explicit. Members have names and values.

:::cell
Enum defines a fixed set of named values. This makes states and modes easier to read than raw strings scattered through a program.

Each enum member has a name and a value. Comparing enum members is explicit and helps avoid typos that plain strings would allow.

Enums make states and choices explicit. Members have names and values.

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"

print(Status.PENDING.name)
print(Status.DONE.value)
```

```output
PENDING
done
```
:::

:::note
- Enums make states and choices explicit.
- Members have names and values.
:::
