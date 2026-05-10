+++
slug = "packages"
title = "Packages"
section = "Modules"
summary = "Packages organize modules into importable directories."
doc_path = "/tutorial/modules.html#packages"
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


import os
import sys
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    pkg = os.path.join(tmp, "shapes")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "__init__.py"), "w") as init:
        init.write("from .square import area\n__all__ = ['area']\n")
    with open(os.path.join(pkg, "square.py"), "w") as square:
        square.write("def area(side):\n    return side * side\n")
    sys.path.insert(0, tmp)
    try:
        import shapes
        print(shapes.area(3))
        print(shapes.__all__)
    finally:
        sys.path.remove(tmp)
        sys.modules.pop("shapes", None)
        sys.modules.pop("shapes.square", None)
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

:::cell
Inside a package's `__init__.py`, `from .submodule import name` re-exports a submodule's name at the package root, and `__all__` lists the names that `from package import *` should make visible. This cell builds a temporary `shapes` package on disk to make both forms concrete.

```python
import os
import sys
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    pkg = os.path.join(tmp, "shapes")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "__init__.py"), "w") as init:
        init.write("from .square import area\n__all__ = ['area']\n")
    with open(os.path.join(pkg, "square.py"), "w") as square:
        square.write("def area(side):\n    return side * side\n")
    sys.path.insert(0, tmp)
    try:
        import shapes
        print(shapes.area(3))
        print(shapes.__all__)
    finally:
        sys.path.remove(tmp)
        sys.modules.pop("shapes", None)
        sys.modules.pop("shapes.square", None)
```

```output
9
['area']
```
:::

:::note
- A package is a module that can contain submodules.
- Dotted imports should mirror a meaningful project structure.
- Use `from .submodule import name` inside a package to re-export submodule names; set `__all__` to declare the public surface.
- Prefer ordinary imports unless the module name is truly dynamic.
:::
