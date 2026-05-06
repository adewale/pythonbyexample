+++
slug = "special-methods"
title = "Special Methods"
section = "Data Model"
summary = "Special methods connect your objects to Python syntax and built-ins."
doc_path = "/reference/datamodel.html#special-method-names"
+++

Special methods, often called dunder methods, connect user-defined classes to Python syntax and built-ins such as len(), iter(), and repr().

Implementing these methods lets your objects participate in Python protocols rather than forcing callers to learn custom method names for common operations.

Good special methods make objects feel boring in the best way: they work with the language features Python programmers already know.

:::program
```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Bag({self.items!r})"

bag = Bag(["a", "b"])
print(len(bag))
print(list(bag))
print(bag)
```
:::

:::cell
Start with a normal class that stores its data. Special methods build on ordinary instance state.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

bag = Bag(["a", "b"])
print(bag.items)
```

```output
['a', 'b']
```
:::

:::cell
Implement `__len__` to let `len()` ask the object for its size using Python's standard protocol.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

bag = Bag(["a", "b"])
print(len(bag))
```

```output
2
```
:::

:::cell
Implement `__iter__` to make the object iterable. Then tools such as `list()` can consume it without a custom method name.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

bag = Bag(["a", "b"])
print(list(bag))
```

```output
['a', 'b']
```
:::

:::cell
Implement `__repr__` to give the object a useful developer-facing representation when it is printed or inspected.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Bag({self.items!r})"

bag = Bag(["a", "b"])
print(bag)
```

```output
Bag(['a', 'b'])
```
:::

:::note
- Dunder methods are looked up by Python's data model protocols.
- Implement the smallest protocol that makes your object feel native.
:::
