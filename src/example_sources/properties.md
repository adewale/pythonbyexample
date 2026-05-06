+++
slug = "properties"
title = "Properties"
section = "Classes"
summary = "@property exposes computed or validated attributes with normal attribute syntax."
doc_path = "/library/functions.html#property"
+++

Properties let a class expose computed data through attribute access. Callers write obj.area, while the class still runs code to produce the value.

This keeps public APIs pleasant without giving up the ability to validate, derive, or later change how a value is stored.

Use properties for cheap, attribute-like operations. Expensive work or actions with side effects should usually remain explicit methods.

:::cell
Properties let a class expose computed data through attribute access. Callers write obj.area, while the class still runs code to produce the value.

This keeps public APIs pleasant without giving up the ability to validate, derive, or later change how a value is stored.

Use properties for cheap, attribute-like operations. Expensive work or actions with side effects should usually remain explicit methods.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

box = Rectangle(3, 4)
print(box.area)
```

```output
12
```
:::

:::note
- Properties let APIs start simple and grow validation or computation later.
- Callers access a property like an attribute, not like a method.
:::
