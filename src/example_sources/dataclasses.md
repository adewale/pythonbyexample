+++
slug = "dataclasses"
title = "Dataclasses"
section = "Classes"
summary = "dataclass generates common class methods for data containers."
doc_path = "/library/dataclasses.html"
+++

dataclass is a standard-library decorator for classes that mainly store data. It generates methods such as __init__ and __repr__ from type-annotated fields.

Dataclasses reduce boilerplate while keeping classes explicit. They are a good fit for simple records, configuration objects, and values passed between layers.

Type annotations define dataclass fields. Defaults can be supplied like normal class attributes.

:::cell
dataclass is a standard-library decorator for classes that mainly store data. It generates methods such as __init__ and __repr__ from type-annotated fields.

Dataclasses reduce boilerplate while keeping classes explicit. They are a good fit for simple records, configuration objects, and values passed between layers.

Type annotations define dataclass fields. Defaults can be supplied like normal class attributes.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    active: bool = True

user = User("Ada")
print(user)
print(user.active)
```

```output
User(name='Ada', active=True)
True
```
:::

:::note
- Type annotations define dataclass fields.
- Defaults can be supplied like normal class attributes.
:::
