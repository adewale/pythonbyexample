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

:::cell
Special methods connect your objects to Python syntax and built-ins.

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

```output
2
['a', 'b']
Bag(['a', 'b'])
```
:::

:::note
- Dunder methods are looked up by Python's data model protocols.
- Implement the smallest protocol that makes your object feel native.
:::
