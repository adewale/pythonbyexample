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
    step = 1

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
print(first.step)
Counter.step = 5
print(second.step)

class Cart:
    items = []

    def add(self, item):
        self.items.append(item)

shared_a = Cart()
shared_b = Cart()
shared_a.add("apple")
print(shared_b.items)

class FixedCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

own_a = FixedCart()
own_b = FixedCart()
own_a.add("apple")
print(own_b.items)
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

:::cell
A name defined directly on the class body is a class attribute, shared by every instance. Reading falls back to the class when the instance has no attribute of that name; assigning to the class itself changes the value for every instance at once.

```python
class Counter:
    step = 1

    def __init__(self, start=0):
        self.value = start

first = Counter()
second = Counter()
print(first.step)
Counter.step = 5
print(second.step)
```

```output
1
5
```
:::

:::cell
A mutable class attribute is shared mutable state — the classic footgun. Define per-instance containers in `__init__` so each object owns its own copy.

```python
class Cart:
    items = []

    def add(self, item):
        self.items.append(item)

shared_a = Cart()
shared_b = Cart()
shared_a.add("apple")
print(shared_b.items)

class FixedCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

own_a = FixedCart()
own_b = FixedCart()
own_a.add("apple")
print(own_b.items)
```

```output
['apple']
[]
```
:::

:::note
- `self` is the instance the method is operating on.
- `__init__` initializes each new object.
- Class attributes are shared across instances; instance attributes belong to one object.
- Put mutable defaults in `__init__`, not on the class body.
- Use classes when behavior belongs with state; use dictionaries for looser structured data.
:::
