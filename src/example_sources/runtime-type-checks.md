+++
slug = "runtime-type-checks"
title = "Runtime Type Checks"
section = "Types"
summary = "type, isinstance, and issubclass inspect runtime relationships."
doc_path = "/library/functions.html#isinstance"
see_also = [
  "type-hints",
  "protocols",
  "casts-and-any",
  "abstract-base-classes",
]
+++

Runtime type checks inspect real objects while the program is running. They are different from type hints, which mostly guide tools before the program runs.

Use `type()` when the exact class matters, `isinstance()` when subclasses should count, and `issubclass()` when checking class relationships. Most APIs prefer behavior over type checks, but runtime checks are useful at input boundaries.

Do not turn every function into a wall of `isinstance()` calls. If the code only needs an object that can perform an operation, duck typing or a protocol may be clearer.

:::program
```python
class Animal:
    pass

class Dog(Animal):
    pass

pet = Dog()

print(type(pet).__name__)
print(type(pet) is Animal)
print(isinstance(pet, Animal))
print(issubclass(Dog, Animal))
```
:::

:::cell
`type()` reports the exact runtime class. A `Dog` instance is not exactly an `Animal` instance.

```python
class Animal:
    pass

class Dog(Animal):
    pass

pet = Dog()
print(type(pet).__name__)
print(type(pet) is Animal)
```

```output
Dog
False
```
:::

:::cell
`isinstance()` accepts subclasses, which is usually what API boundaries want.

```python
print(isinstance(pet, Dog))
print(isinstance(pet, Animal))
```

```output
True
True
```
:::

:::cell
`issubclass()` checks class relationships rather than individual objects.

```python
print(issubclass(Dog, Animal))
```

```output
True
```
:::

:::note
- `type()` is exact; `isinstance()` follows inheritance.
- Runtime checks inspect objects, not static annotations.
- Prefer behavior, protocols, or clear validation over scattered type checks.
:::
