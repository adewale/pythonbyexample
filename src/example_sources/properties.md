+++
slug = "properties"
title = "Properties"
section = "Classes"
summary = "@property keeps attribute syntax while adding computation or validation."
doc_path = "/library/functions.html#property"
+++

Properties let a class keep a simple attribute-style API while running code behind the scenes. Callers write `box.area`, but the class can compute the value from current state.

A property setter can validate assignment without changing the public spelling of the attribute. This is the boundary: plain attributes are enough for plain data, while properties are for computed or protected data.

Use properties for cheap, attribute-like operations. Expensive work or actions with side effects should usually remain explicit methods.

:::program
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = value

box = Rectangle(3, 4)
print(box.area)

box.width = 5
print(box.area)

try:
    box.width = 0
except ValueError as error:
    print(error)
```
:::

:::cell
A read-only property exposes computed data through attribute access. `area` stays current because it is calculated from `width` and `height` each time it is read.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = value

box = Rectangle(3, 4)
print(box.area)
```

```output
12
```
:::

:::cell
A setter lets assignment keep normal attribute syntax while the class validates or normalizes the value.

```python
box.width = 5
print(box.area)
```

```output
20
```
:::

:::cell
Validation belongs inside the class when every caller should obey the same rule. Invalid assignment raises an exception at the boundary.

```python
try:
    box.width = 0
except ValueError as error:
    print(error)
```

```output
width must be positive
```
:::

:::note
- Properties let APIs start simple and grow validation or computation later.
- Callers access a property like an attribute, not like a method.
- Use methods instead when work is expensive or action-like.
:::
