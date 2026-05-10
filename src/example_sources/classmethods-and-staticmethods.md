+++
slug = "classmethods-and-staticmethods"
title = "Classmethods and Staticmethods"
section = "Classes"
summary = "Three method shapes: instance, class, and static — each receives a different first argument."
doc_path = "/library/functions.html#classmethod"
see_also = [
  "classes",
  "decorators",
  "inheritance-and-super",
]
+++

A regular method receives the instance as `self`. `@classmethod` makes a method receive the class as `cls` instead, which is the standard shape for alternate constructors. `@staticmethod` removes the implicit first argument entirely, leaving a plain function attached to the class for namespacing.

The pressure that justifies the decorators is name organization. `Date.from_string("2026-05-09")` reads better than a free-floating `parse_date` function, and `Date.is_leap_year(2024)` keeps the helper next to the class it belongs to even when the helper does not need any class state.

Pick instance methods when the work depends on instance state, classmethods when an alternate constructor or class-level operation is the right shape, and staticmethods when the function only happens to live near a class.

:::program
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, text):
        year, month, day = (int(part) for part in text.split("-"))
        return cls(year, month, day)

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

today = Date(2026, 5, 9)
print(today.display())

later = Date.from_string("2026-12-31")
print(later.display())

print(Date.is_leap_year(2024))
print(Date.is_leap_year(2025))

class Demo:
    def instance_method(self):
        return type(self).__name__

    @classmethod
    def class_method(cls):
        return cls.__name__

    @staticmethod
    def static_method():
        return "no receiver"

print(Demo().instance_method())
print(Demo.class_method())
print(Demo.static_method())
```
:::

:::cell
An instance method receives the instance as `self` and reads its state. This is the default and the right shape when the work depends on a particular object's data.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

today = Date(2026, 5, 9)
print(today.display())
```

```output
2026-05-09
```
:::

:::cell
`@classmethod` makes the method receive the class itself as `cls`. The canonical use is an alternate constructor that parses some other input format and calls `cls(...)`. Because `cls` is the actual class, subclasses calling the same method get an instance of their own type.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):
        year, month, day = (int(part) for part in text.split("-"))
        return cls(year, month, day)

later = Date.from_string("2026-12-31")
print(later.year, later.month, later.day)
```

```output
2026 12 31
```
:::

:::cell
`@staticmethod` strips the implicit first argument. The function lives on the class for namespacing — like `Date.is_leap_year(2024)` — but does not touch any instance or class state.

```python
class Date:
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(Date.is_leap_year(2024))
print(Date.is_leap_year(2025))
```

```output
True
False
```
:::

:::cell
Side by side: instance methods receive the instance, classmethods receive the class, staticmethods receive nothing. Classmethods and staticmethods can be called on either the class or an instance.

```python
class Demo:
    def instance_method(self):
        return type(self).__name__

    @classmethod
    def class_method(cls):
        return cls.__name__

    @staticmethod
    def static_method():
        return "no receiver"

print(Demo().instance_method())
print(Demo.class_method())
print(Demo.static_method())
```

```output
Demo
Demo
no receiver
```
:::

:::note
- Instance methods need an instance; classmethods and staticmethods can be called on the class.
- Use `@classmethod` for alternate constructors and class-level operations that respect subclassing.
- Use `@staticmethod` only when a function is truly independent of instance and class state but still belongs in the class's namespace.
- A free function is often the right answer when neither decorator applies.
:::
