+++
slug = "classes"
title = "Classes"
section = "Classes"
summary = "Classes bundle data and behavior."
doc_path = "/tutorial/classes.html"
+++

Classes define new object types by bundling data with behavior. They are useful when several values and operations belong together.

`__init__` initializes each instance, and methods receive the instance as `self`. Assigning `self.value` stores state on that particular object.

Separate instances keep separate state. Mutating one `Counter` does not change another because each object has its own attributes.

:::cell
Classes define new object types by bundling data with behavior. They are useful when several values and operations belong together.

`__init__` initializes each instance, and methods receive the instance as `self`. Assigning `self.value` stores state on that particular object.

Separate instances keep separate state. Mutating one `Counter` does not change another because each object has its own attributes.

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
- Instance attributes belong to one object, not to the class as a whole.
:::
