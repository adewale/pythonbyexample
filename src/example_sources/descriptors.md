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

Descriptors customize attribute access through __get__, __set__, or __delete__. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, owner):
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
try:
    item.price = -1
except ValueError as error:
    print(error)
```
:::

:::cell
A descriptor object lives on the class.

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, owner):
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
- A descriptor object lives on the class.
- Attribute access on instances calls descriptor methods.
- Properties, methods, and many ORMs build on the descriptor protocol.
:::
