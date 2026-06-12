+++
slug = "operator-overloading"
title = "Operator Overloading"
section = "Data Model"
summary = "Operator methods let objects define arithmetic and comparison syntax."
doc_path = "/reference/datamodel.html#emulating-numeric-types"
see_also = [
  "operators",
  "special-methods",
  "equality-and-identity",
]
+++

Operator overloading lets a class define what expressions such as `a + b` mean for its objects. This is useful when the operation is part of the domain vocabulary.

The method should preserve the meaning readers expect from the operator. Vectors can add component by component; money can add amounts in the same currency; surprising overloads make code harder to trust.

Python also has reflected methods such as `__radd__` for cases where the left operand does not know how to handle the right operand. That keeps mixed operations possible without making every type know every other type.

:::program
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(2, 3) + Vector(4, 5))
print(Vector(1, 1) == Vector(1, 1))
print(Vector(1, 1) == 5)
```
:::

:::cell
`__add__` defines how the `+` operator combines two objects. Checking the operand type and returning `NotImplemented` for foreign types lets Python try the other operand's reflected method instead of crashing inside yours.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(2, 3) + Vector(4, 5))
```

```output
Vector(6, 8)
```
:::

:::cell
`__eq__` defines value equality for `==`. Without it, user-defined objects compare by identity. Returning `NotImplemented` for foreign types matters most here: equality against an unrelated value should answer `False`, never raise — Python falls back to identity when both sides decline.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

print(Vector(1, 1) == Vector(1, 1))
print(Vector(1, 1) == 5)
```

```output
True
False
```
:::

:::cell
A useful `__repr__` makes operator results inspectable while debugging.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(repr(Vector(2, 3) + Vector(4, 5)))
```

```output
Vector(6, 8)
```
:::

:::note
- Overload operators only when the operation is unsurprising.
- Return `NotImplemented` when an operand type is unsupported.
- Implement equality deliberately when value comparison matters.
:::
