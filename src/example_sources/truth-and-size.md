+++
slug = "truth-and-size"
title = "Truth and Size"
section = "Data Model"
summary = "__bool__ and __len__ decide how objects behave in truth tests and len()."
doc_path = "/reference/datamodel.html#object.__bool__"
see_also = [
  "truthiness",
  "special-methods",
  "container-protocols",
]
+++

Truth tests ask an object whether it should count as true. Containers usually answer through their size, while domain objects can answer with `__bool__` when emptiness is not the right idea.

`__len__` supports `len(obj)` and also provides a fallback truth value: length zero is false, non-zero length is true. `__bool__` is more direct and wins when both are present.

Use these methods to match the meaning of your object. A queue can be false when it has no items; an account might be true only when it is active, regardless of its balance.

:::program
```python
class Inbox:
    def __init__(self, messages):
        self.messages = list(messages)

    def __len__(self):
        return len(self.messages)

class Account:
    def __init__(self, active):
        self.active = active

    def __bool__(self):
        return self.active

print(len(Inbox(["hi", "bye"])))
print(bool(Inbox([])))
print(bool(Account(False)))
```
:::

:::cell
`__len__` lets `len()` ask an object for its size.

```python
class Inbox:
    def __init__(self, messages):
        self.messages = list(messages)

    def __len__(self):
        return len(self.messages)

print(len(Inbox(["hi", "bye"])))
```

```output
2
```
:::

:::cell
If a class has `__len__` but no `__bool__`, Python uses zero length as false.

```python
print(bool(Inbox([])))
```

```output
False
```
:::

:::cell
`__bool__` expresses truth directly when the answer is not just container size.

```python
class Account:
    def __init__(self, active):
        self.active = active

    def __bool__(self):
        return self.active

print(bool(Account(False)))
```

```output
False
```
:::

:::note
- Prefer `__len__` for sized containers.
- Prefer `__bool__` when truth has domain meaning.
- Keep truth tests unsurprising; surprising falsy objects make conditionals harder to read.
:::
