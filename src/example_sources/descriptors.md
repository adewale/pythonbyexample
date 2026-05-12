+++
slug = "descriptors"
title = "Descriptors"
section = "Data Model"
summary = "Descriptors customize attribute access through __get__, __set__, or __delete__."
doc_path = "/howto/descriptor.html"
see_also = [
  "attribute-access",
  "properties",
  "bound-and-unbound-methods",
]
+++

A descriptor is an object stored on a class that defines `__get__`, `__set__`, or `__delete__`. When an instance attribute lookup finds that object on the class, Python calls the descriptor method instead of returning the descriptor object directly.

Descriptors are the machinery behind methods, `property`, validators, and many ORM fields. Use them when one reusable object should control access for many attributes or classes; use `property` for a single simple managed attribute.

This example implements a positive-number validator. `__set_name__` learns the attribute name when the owner class is created, `__set__` validates writes, and `__get__` reads the stored value back from the instance.

:::program
```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private_name, value)

class Product:
    price = Positive()

    def __init__(self, price):
        self.price = price

item = Product(10)
print(item.price)
print(Product.price.private_name)
try:
    item.price = -1
except ValueError as error:
    print(error)
```
:::

:::cell
A descriptor object lives on the class. `__set_name__` lets it learn which managed attribute it is serving.

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private_name, value)

class Product:
    price = Positive()

print(Product.price.private_name)
```

```output
_price
```
:::

:::cell
Assigning `item.price` calls `Positive.__set__`, and reading it calls `Positive.__get__`.

```python
class Product:
    price = Positive()

    def __init__(self, price):
        self.price = price

item = Product(10)
print(item.price)
try:
    item.price = -1
except ValueError as error:
    print(error)
```

```output
10
must be positive
```
:::

:::note
- Descriptors are class attributes that participate in instance attribute access.
- Data descriptors with `__set__` can validate or transform assignments.
- `property` is usually simpler for one-off managed attributes; descriptors shine when the behavior is reusable.
:::
