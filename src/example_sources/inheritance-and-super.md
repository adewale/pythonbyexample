+++
slug = "inheritance-and-super"
title = "Inheritance and Super"
section = "Classes"
summary = "Inheritance reuses behavior, and super delegates to a parent implementation."
doc_path = "/tutorial/classes.html#inheritance"
see_also = [
  "classes",
  "properties",
  "special-methods",
]
+++

Inheritance lets one class specialize another class. The child class gets parent behavior and can add or override methods.

Use `super()` when the child method should extend the parent implementation instead of replacing it entirely.

Prefer composition when objects merely collaborate. Inheritance is best when the child really is a specialized version of the parent.

:::program
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return f"{base}; {self.name} barks"

pet = Dog("Nina")
print(pet.name)
print(pet.speak())
print(isinstance(pet, Animal))
```
:::

:::cell
A child class names its parent in parentheses. `Dog` instances get the `Animal.__init__` method because `Dog` does not define its own initializer.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return f"{base}; {self.name} barks"

pet = Dog("Nina")
print(pet.name)
```

```output
Nina
```
:::

:::cell
`super()` delegates to the parent implementation. The child method can reuse the parent result and then add specialized behavior.

```python
print(pet.speak())
print(isinstance(pet, Animal))
```

```output
Nina makes a sound; Nina barks
True
```
:::

:::note
- Inheritance models an “is a specialized kind of” relationship.
- `super()` calls the next implementation in the method resolution order.
- Prefer composition when an object only needs to use another object.
:::
