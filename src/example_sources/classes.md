+++
slug = "classes"
title = "Classes"
section = "Classes"
summary = "Classes bundle data and behavior into new object types."
doc_path = "/tutorial/classes.html"
+++

Classes define new object types by bundling data with behavior. They are useful when several values and operations belong together and should travel as one object.

The alternative is often a dictionary plus separate functions. That is fine for loose data, but a class gives the data a stable API and keeps behavior next to the state it changes.

`__init__` initializes each instance, and methods receive the instance as `self`. Separate instances keep separate state because each object has its own attributes.

:::program
```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self, amount=1):
        self.value += amount
        return self.value

first = Counter()
second = Counter(10)

print(first.value)
print(second.value)
print(first.increment())
print(second.increment(5))
```
:::

:::cell
Define a class when data and behavior should travel together. The initializer gives each object its starting state.

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

first = Counter()
second = Counter(10)
print(first.value)
print(second.value)
```

```output
0
10
```
:::

:::cell
Methods are functions attached to the class. `self` is the particular object receiving the method call, so separate instances keep separate state.

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self, amount=1):
        self.value += amount
        return self.value

first = Counter()
second = Counter(10)
print(first.increment())
print(second.increment(5))
```

```output
1
15
```
:::

:::note
- `self` is the instance the method is operating on.
- `__init__` initializes each new object.
- Use classes when behavior belongs with state; use dictionaries for looser structured data.
- Instance attributes belong to one object, not to the class as a whole.
:::
