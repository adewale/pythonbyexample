+++
slug = "special-methods"
title = "Special Methods"
section = "Data Model"
summary = "Special methods connect your objects to Python syntax and built-ins."
doc_path = "/reference/datamodel.html#special-method-names"
see_also = [
  "container-protocols",
  "operator-overloading",
  "callable-objects",
  "context-managers",
]
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

    def __str__(self):
        return ", ".join(self.items)

    def __eq__(self, other):
        return isinstance(other, Bag) and self.items == other.items

    def __hash__(self):
        return hash(tuple(self.items))

    def __lt__(self, other):
        return self.items < other.items

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __bool__(self):
        return bool(self.items)

bag = Bag(["a", "b"])
print(len(bag))
print(list(bag))
print(bag)
print(repr(bag))
print(Bag(["a", "b"]) == Bag(["a", "b"]))
print(Bag(["a"]) < Bag(["a", "b"]))
print(hash(Bag(["a"])) == hash(Bag(["a"])))
print("a" in bag)
print(bag[0])
bag[1] = "z"
print(list(bag))
print(bool(Bag([])))


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

triple = Multiplier(3)
print(triple(5))


class Trace:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, *exc):
        print("exit")
        return False

with Trace():
    print("inside")
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
Implement `__repr__` to give the object a useful developer-facing representation when it is printed or inspected. With no `__str__` defined, `print()` falls back to `__repr__`.

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

:::cell
Add `__str__` for an end-user representation. `print()` and `str()` prefer `__str__`; `repr()` and the REPL still use `__repr__`. Keep `__repr__` unambiguous for debugging and let `__str__` be the friendly form.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __repr__(self):
        return f"Bag({self.items!r})"

    def __str__(self):
        return ", ".join(self.items)

bag = Bag(["a", "b"])
print(bag)
print(repr(bag))
```

```output
a, b
Bag(['a', 'b'])
```
:::

:::cell
`__eq__` decides what equality means for the type, comparing contents. `__lt__` orders by those same contents, so ordering stays consistent with equality (define one comparison and `functools.total_ordering` can fill in the rest; `__lt__` alone is enough for `<` and `sorted()`). Defining `__eq__` removes the default `__hash__`, so add it back only for types you treat as immutable: this `Bag` hashes its current items, so the last two lines show the hazard — a `Bag` found in a set becomes unfindable once its items change, because its hash no longer points at the bucket it was stored in.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __eq__(self, other):
        return isinstance(other, Bag) and self.items == other.items

    def __hash__(self):
        return hash(tuple(self.items))

    def __lt__(self, other):
        return self.items < other.items

print(Bag(["a", "b"]) == Bag(["a", "b"]))
print(Bag(["a"]) < Bag(["a", "b"]))

bag = Bag(["a"])
seen = {bag}
print(bag in seen)
bag.items.append("b")
print(bag in seen)
```

```output
True
True
True
False
```
:::

:::cell
The container protocols make instances behave like built-in containers. `__contains__` powers `in`, `__getitem__`/`__setitem__` power subscription, and `__bool__` decides truthiness for `if` and `while`. See [container-protocols](/examples/container-protocols) for the full surface.

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __bool__(self):
        return bool(self.items)

bag = Bag(["a", "b"])
print("a" in bag)
print(bag[0])
bag[1] = "z"
print(bag.items)
print(bool(Bag([])))
```

```output
True
a
['a', 'z']
False
```
:::

:::cell
`__call__` makes an instance callable like a function — useful for stateful operations whose configuration deserves a name. `__enter__` and `__exit__` make a class a context manager so it can be used with `with`. The focused [callable-objects](/examples/callable-objects) and [context-managers](/examples/context-managers) pages go deeper.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

triple = Multiplier(3)
print(triple(5))


class Trace:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, *exc):
        print("exit")
        return False

with Trace():
    print("inside")
```

```output
15
enter
inside
exit
```
:::

:::note
- Dunder methods are looked up by Python's data model protocols.
- `__repr__` is the developer-facing form; `__str__` is the user-facing form. `print()` falls back to `__repr__` when `__str__` is missing.
- Defining `__eq__` removes the default `__hash__`; restore it when the type should be hashable.
- Container protocols (`__contains__`, `__getitem__`, `__setitem__`, `__bool__`) make instances behave like built-in containers.
- `__call__` makes instances callable; `__enter__`/`__exit__` make them context managers.
- Implement the smallest protocol that makes your object feel native.
:::
