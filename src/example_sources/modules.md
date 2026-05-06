+++
slug = "modules"
title = "Modules"
section = "Modules"
summary = "Modules organize code into namespaces and expose reusable definitions."
doc_path = "/tutorial/modules.html"
+++

Modules organize Python code into files and namespaces. `import` executes a module once and then gives your program access to its definitions.

Use module namespaces such as `math.sqrt` when the source of a name should stay visible. Use focused imports such as `from statistics import mean` when the imported name is clear at the call site.

The standard library is Python's batteries-included toolbox. Imports usually live at the top of a file so dependencies are visible before the program body.

:::program
```python
import math
from statistics import mean

radius = 3
area = math.pi * radius ** 2
print(round(area, 2))

scores = [8, 10, 9]
print(mean(scores))

print(math.__name__)
```
:::

:::cell
Importing a module gives access to its namespace. The `math.` prefix makes it clear where `pi` came from.

```python
import math

radius = 3
area = math.pi * radius ** 2
print(round(area, 2))
```

```output
28.27
```
:::

:::cell
A focused `from ... import ...` brings one definition into the current namespace. This keeps a common operation concise without importing every name.

```python
from statistics import mean

scores = [8, 10, 9]
print(mean(scores))
```

```output
9
```
:::

:::cell
Modules are objects too. Their attributes include metadata such as `__name__`, which records the module's import name.

```python
print(math.__name__)
```

```output
math
```
:::

:::note
- Prefer plain `import module` when the namespace improves readability.
- Use focused imports for a small number of clear names.
- Place imports near the top of the file.
:::
