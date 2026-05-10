+++
slug = "abstract-base-classes"
title = "Abstract Base Classes"
section = "Classes"
summary = "ABC and abstractmethod enforce that subclasses implement required methods."
doc_path = "/library/abc.html"
see_also = [
  "protocols",
  "inheritance-and-super",
  "classes",
]
+++

`ABC` and `@abstractmethod` describe an interface that subclasses must implement. The base class refuses to instantiate until a concrete subclass provides every abstract method, which catches "I forgot to implement this" at construction time rather than at the first method call.

ABCs are different from `Protocol`. An ABC is nominal: a class participates in the contract by inheriting from it. A `Protocol` is structural: any class with the right methods qualifies, no inheritance required. Reach for an ABC when you want shared implementation in the base class or you want `isinstance()` to mean "explicitly opted in"; reach for a `Protocol` when you only care about behavior at the API boundary.

The cost is a small amount of ceremony at the type level. The benefit is that a half-implemented subclass cannot be created by accident.

:::program
```python
from abc import ABC, abstractmethod
from typing import Protocol

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    def describe(self) -> str:
        return f"shape with area {self.area()}"

try:
    Shape()
except TypeError as error:
    print(error)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Square(3).area())
print(Square(3).describe())

class Incomplete(Shape):
    pass

try:
    Incomplete()
except TypeError as error:
    print(error)

class HasArea(Protocol):
    def area(self) -> float:
        ...

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def total_area(shapes: list[HasArea]) -> float:
    return sum(shape.area() for shape in shapes)

print(total_area([Square(3), Triangle(4, 3)]))
print(isinstance(Triangle(4, 3), Shape))
print(isinstance(Square(3), Shape))
```
:::

:::cell
`ABC` plus `@abstractmethod` declares the contract. Trying to construct the base class itself fails because at least one method has no implementation. A concrete `describe()` lives alongside the abstract `area()` so subclasses inherit shared behavior for free.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    def describe(self) -> str:
        return f"shape with area {self.area()}"

try:
    Shape()
except TypeError as error:
    print(error)
```

```output
Can't instantiate abstract class Shape without an implementation for abstract method 'area'
```
:::

:::cell
A subclass that implements every abstract method is concrete and can be instantiated. It also inherits the non-abstract methods from the base class.

```python
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Square(3).area())
print(Square(3).describe())
```

```output
9
shape with area 9
```
:::

:::cell
A subclass that forgets to implement an abstract method also cannot be instantiated — that is the value the ABC adds. The error fires at construction, not when something later tries to call the missing method.

```python
class Incomplete(Shape):
    pass

try:
    Incomplete()
except TypeError as error:
    print(error)
```

```output
Can't instantiate abstract class Incomplete without an implementation for abstract method 'area'
```
:::

:::cell
Contrast with `Protocol`. A `HasArea` protocol accepts any class with an `area()` method, no inheritance required. `Triangle` does not inherit from `Shape`, so it satisfies the protocol but fails `isinstance(_, Shape)`. `Square` satisfies both because it explicitly inherited from the ABC.

```python
from typing import Protocol

class HasArea(Protocol):
    def area(self) -> float:
        ...

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def total_area(shapes: list[HasArea]) -> float:
    return sum(shape.area() for shape in shapes)

print(total_area([Square(3), Triangle(4, 3)]))
print(isinstance(Triangle(4, 3), Shape))
print(isinstance(Square(3), Shape))
```

```output
15.0
False
True
```
:::

:::note
- `ABC` plus `@abstractmethod` blocks instantiation until every abstract method has an implementation.
- ABCs are nominal — subclasses opt in by inheriting; `isinstance()` reflects that opt-in.
- Protocols are structural — any class with the right shape qualifies, regardless of inheritance.
- Prefer an ABC when shared implementation or explicit opt-in matters; prefer a Protocol when only behavior at the API boundary matters.
:::
