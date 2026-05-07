+++
slug = "import-aliases"
title = "Import Aliases"
section = "Modules"
summary = "as gives imported modules or names a local alias."
doc_path = "/reference/simple_stmts.html#the-import-statement"
see_also = [
  "modules",
  "functions",
]
+++

`as` gives an imported module or imported name a local alias. Use it when a conventional short name improves readability or when two imports would otherwise collide.

The alternative is a plain import, which is usually better when the module name is already clear. Avoid aliases that make readers guess where a name came from.

Avoid star imports in examples and production modules because they hide dependencies and blur the boundary between modules.

:::program
```python
import statistics as stats
from math import sqrt as square_root

scores = [8, 10, 9]
print(stats.mean(scores))
print(stats.__name__)

print(square_root(81))
print(square_root.__name__)
```
:::

:::cell
A module alias keeps the namespace but changes the local name. Here `stats` is shorter, but readers can still see that `mean` belongs to the statistics module.

```python
import statistics as stats

scores = [8, 10, 9]
print(stats.mean(scores))
print(stats.__name__)
```

```output
9
statistics
```
:::

:::cell
A name imported with `from` can also be aliased. Use this when the local name explains the role better than the original name.

```python
from math import sqrt as square_root

print(square_root(81))
print(square_root.__name__)
```

```output
9.0
sqrt
```
:::

:::note
- `import module as alias` keeps module-style access under a shorter or clearer name.
- `from module import name as alias` imports one name under a local alias.
- Prefer plain imports unless an alias improves clarity or follows a strong convention.
- Avoid `from module import *` because it makes dependencies harder to see.
:::
