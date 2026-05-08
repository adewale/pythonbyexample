+++
slug = "attribute-access"
title = "Attribute Access"
section = "Data Model"
summary = "Attribute hooks customize lookup, missing attributes, and assignment."
doc_path = "/reference/datamodel.html#customizing-attribute-access"
see_also = [
  "properties",
  "descriptors",
  "special-methods",
]
+++

Attribute access is usually simple: `obj.name` looks up an attribute. Python exposes hooks for the uncommon cases where lookup or assignment needs to be customized.

`__getattr__` runs only when normal lookup fails, which makes it a safer hook for computed fallback attributes. `__setattr__` runs for every assignment, so it should be used sparingly and carefully.

Prefer ordinary attributes and `@property` first. Reach for these hooks when an object is intentionally adapting another interface, validating all assignments, or exposing dynamic fields.

:::program
```python
class Settings:
    def __init__(self, values):
        self._values = dict(values)

    def __getattr__(self, name):
        try:
            return self._values[name]
        except KeyError as error:
            raise AttributeError(name) from error

    def __setattr__(self, name, value):
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self._values[name] = value

settings = Settings({"theme": "dark"})
print(settings.theme)
settings.volume = 7
print(settings._values["volume"])
```
:::

:::cell
Normal initialization still needs to set real attributes. Calling `object.__setattr__` avoids recursing through your own hook.

```python
class Settings:
    def __init__(self, values):
        self._values = dict(values)

settings = Settings({"theme": "dark"})
print(settings._values)
```

```output
{'theme': 'dark'}
```
:::

:::cell
`__getattr__` runs only for missing attributes, so it can provide fallback lookup.

```python
class Settings:
    def __init__(self, values):
        self._values = dict(values)

    def __getattr__(self, name):
        try:
            return self._values[name]
        except KeyError as error:
            raise AttributeError(name) from error

settings = Settings({"theme": "dark"})
print(settings.theme)
```

```output
dark
```
:::

:::cell
`__setattr__` intercepts assignment. This example stores public names in the backing dictionary.

```python
class Settings:
    def __init__(self, values):
        self._values = dict(values)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self._values[name] = value

settings = Settings({"theme": "dark"})
settings.volume = 7
print(settings._values["volume"])
```

```output
7
```
:::

:::note
- `__getattr__` is narrower than `__getattribute__` because it handles only missing attributes.
- `__setattr__` affects every assignment on the instance.
- Use `property` or descriptors when the behavior is attached to a known attribute name.
:::
