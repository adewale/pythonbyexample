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

`as` gives an imported module or imported name a local alias. This is useful when a conventional short name improves readability or when two imports would otherwise collide.

Use aliases sparingly. The best aliases are conventional in the ecosystem or clarify a boundary in the current file.

Avoid star imports in examples and production modules because they hide where names came from.

:::program
```python
import statistics as stats
from math import sqrt as square_root

scores = [8, 10, 9]
print(stats.mean(scores))
print(square_root(81))
```
:::

:::cell
A module alias keeps the namespace but changes the local name. Readers can still see that `mean` comes from the statistics module.

```python
import statistics as stats

scores = [8, 10, 9]
print(stats.mean(scores))
```

```output
9
```
:::

:::cell
A name imported with `from` can also be aliased. This is most useful when the local name explains the role better than the original name.

```python
from math import sqrt as square_root

print(square_root(81))
```

```output
9.0
```
:::

:::note
- `import module as alias` keeps module-style access under a shorter or clearer name.
- `from module import name as alias` imports one name under a local alias.
- Avoid `from module import *` because it makes dependencies harder to see.
:::
