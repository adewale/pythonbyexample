+++
slug = "dataclasses"
title = "Dataclasses"
section = "Classes"
summary = "dataclass generates common class methods for data containers."
doc_path = "/library/dataclasses.html"
+++

`dataclass` is a standard-library decorator for classes that mainly store data. It generates methods such as `__init__` and `__repr__` from type-annotated fields.

Dataclasses reduce boilerplate while keeping classes explicit. They are a good fit for simple records, configuration objects, and values passed between layers.

Type annotations define fields. Defaults work like normal class attributes and appear in the generated initializer.

:::program
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    active: bool = True

user = User("Ada")
print(user)
print(user.name)

inactive = User("Guido", active=False)
print(inactive)
print(inactive.active)
```
:::

:::cell
A dataclass uses annotations to define fields. Python generates an initializer, so the class can be constructed without writing `__init__` by hand.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    active: bool = True

user = User("Ada")
print(user)
```

```output
User(name='Ada', active=True)
```
:::

:::cell
The generated instance still exposes ordinary attributes. A dataclass is a regular class with useful methods filled in.

```python
print(user.name)
```

```output
Ada
```
:::

:::cell
Defaults can be overridden by keyword. The generated representation includes the field names, which is useful during debugging.

```python
inactive = User("Guido", active=False)
print(inactive)
print(inactive.active)
```

```output
User(name='Guido', active=False)
False
```
:::

:::note
- Type annotations define dataclass fields.
- Dataclasses generate methods but remain normal Python classes.
- Use `field()` for advanced defaults such as per-instance lists or dictionaries.
:::
