+++
slug = "modules"
title = "Modules"
section = "Modules"
summary = "Modules let you organize code and use the standard library."
doc_path = "/tutorial/modules.html"
+++

Modules organize Python code into files and namespaces. import executes a module once and then gives your program access to its definitions.

The standard library is large and intentionally useful. Importing focused tools such as math.sqrt or statistics.mean keeps examples small while relying on well-tested implementations.

The standard library is Python's batteries-included toolbox. Imports are usually placed at the top of a file.

:::program
```python
import math
from statistics import mean

print(math.sqrt(81))
print(mean([2, 4, 6]))
```
:::

:::cell
Modules organize Python code into files and namespaces. import executes a module once and then gives your program access to its definitions.

The standard library is large and intentionally useful. Importing focused tools such as math.sqrt or statistics.mean keeps examples small while relying on well-tested implementations.

```python
import math
from statistics import mean

print(math.sqrt(81))
print(mean([2, 4, 6]))
```

```output
9.0
4
```
:::

:::note
- The standard library is Python's batteries-included toolbox.
- Imports are usually placed at the top of a file.
:::
