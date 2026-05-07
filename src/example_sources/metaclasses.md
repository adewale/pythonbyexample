+++
slug = "metaclasses"
title = "Metaclasses"
section = "Classes"
summary = "A metaclass customizes how classes themselves are created."
doc_path = "/reference/datamodel.html#metaclasses"
see_also = [
  "classes",
  "inheritance-and-super",
  "special-methods",
]
+++

A metaclass is the class of a class. Most Python code never needs one, but the syntax appears in frameworks that register, validate, or modify classes as they are created.

The `metaclass=` keyword in a class statement chooses the object that builds the class. This is advanced machinery; decorators and ordinary functions are usually simpler.

Use metaclasses only when class creation itself is the problem being solved.

:::program
```python
class Tagged(type):
    def __new__(mcls, name, bases, namespace):
        namespace["tag"] = name.lower()
        return super().__new__(mcls, name, bases, namespace)

class Event(metaclass=Tagged):
    pass

print(Event.tag)
print(type(Event).__name__)
```
:::

:::cell
A metaclass customizes class creation. `__new__` receives the class name, bases, and namespace before the class object exists.

```python
class Tagged(type):
    def __new__(mcls, name, bases, namespace):
        namespace["tag"] = name.lower()
        return super().__new__(mcls, name, bases, namespace)

print(Tagged.__name__)
```

```output
Tagged
```
:::

:::cell
The `metaclass=` keyword applies that class-building rule. Here the metaclass adds a `tag` attribute to the new class.

```python
class Event(metaclass=Tagged):
    pass

print(Event.tag)
print(type(Event).__name__)
```

```output
event
Tagged
```
:::

:::note
- Metaclasses customize class creation, not instance behavior directly.
- Most code should prefer class decorators, functions, or ordinary inheritance.
- You are most likely to meet metaclasses inside frameworks and ORMs.
:::
