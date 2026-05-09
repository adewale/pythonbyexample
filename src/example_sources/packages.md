+++
slug = "packages"
title = "Packages"
section = "Modules"
summary = "Packages organize modules into importable directories."
doc_path = "/tutorial/modules.html#packages"
scope_first_pass = true
see_also = [
  "modules",
  "import-aliases",
  "virtual-environments",
]
+++

Packages are modules that can contain other modules. They let a project group related code behind dotted import paths such as `json.decoder` or `email.message`.

At runtime, importing a submodule gives Python a path through that package structure. In a project on disk, that structure is usually a directory with Python files and often an `__init__.py` file.

Use packages when one module has grown into a small namespace of related modules. Keep module names boring and explicit so readers can tell where imported definitions come from.

:::program
```python
import importlib
import json
import json.decoder

module = importlib.import_module("json.decoder")

print(json.__name__)
print(json.decoder.__name__)
print(module.JSONDecoder.__name__)
print(module is json.decoder)
```
:::

:::cell
A package is itself a module. The `json` package exposes a namespace that can contain submodules.

```python
import json

print(json.__name__)
```

```output
json
```
:::

:::cell
Dotted imports name a path through a package. Importing `json.decoder` makes that submodule available under the package namespace.

```python
import json.decoder

print(json.decoder.__name__)
print(json.decoder.JSONDecoder.__name__)
```

```output
json.decoder
JSONDecoder
```
:::

:::cell
`importlib.import_module()` imports by string. It is useful for plugin systems and dynamic imports, but ordinary `import` is clearer when the dependency is known.

```python
import importlib

module = importlib.import_module("json.decoder")
print(module is json.decoder)
```

```output
True
```
:::

:::note
- A package is a module that can contain submodules.
- Dotted imports should mirror a meaningful project structure.
- Prefer ordinary imports unless the module name is truly dynamic.
:::
