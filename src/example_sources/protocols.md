+++
slug = "protocols"
title = "Protocols"
section = "Types"
summary = "Protocol describes required behavior for structural typing."
doc_path = "/library/typing.html#typing.Protocol"
see_also = [
  "type-hints",
  "classes",
  "inheritance-and-super",
]
+++

`Protocol` describes the methods or attributes an object must provide. It exists for structural typing: if an object has the right shape, type checkers can treat it as compatible.

This is different from inheritance. Inheritance says a class is explicitly derived from a parent; a protocol says callers only need a particular behavior.

At runtime, ordinary method lookup still applies. Protocols are mainly for static analysis, documentation, and API boundaries.

:::program
```python
from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str:
        ...

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hello {self.name}"


def welcome(greeter: Greeter):
    print(greeter.greet())

welcome(Person("Ada"))
print(Greeter.__name__)
```
:::

:::cell
A protocol names required behavior. The ellipsis marks the method body as intentionally unspecified, similar to an interface declaration.

```python
from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str:
        ...

print(Greeter.__name__)
```

```output
Greeter
```
:::

:::cell
A class can satisfy the protocol without inheriting from it. `Person` has a compatible `greet()` method, so it has the right shape for static type checkers.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hello {self.name}"

print(Person("Ada").greet())
```

```output
hello Ada
```
:::

:::cell
Use the protocol as an annotation at the API boundary. The function only cares that the object can greet; it does not care about the concrete class.

```python
def welcome(greeter: Greeter):
    print(greeter.greet())

welcome(Person("Ada"))
```

```output
hello Ada
```
:::

:::note
- Protocols are for structural typing: compatibility by shape rather than explicit inheritance.
- Type checkers understand protocols; normal runtime method calls still do the work.
- Prefer inheritance when shared implementation matters, and protocols when only required behavior matters.
:::
