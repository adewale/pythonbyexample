+++
slug = "logging"
title = "Logging"
section = "Standard Library"
summary = "logging records operational events without using print as infrastructure."
doc_path = "/library/logging.html"
+++

logging records operational events without using print as infrastructure. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
import logging
import sys

logger = logging.getLogger("example")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
logger.handlers[:] = [handler]

logger.debug("hidden")
logger.info("service started")
logger.warning("disk almost full")
```
:::

:::cell
Loggers name where an event came from.

```python
import logging
import sys

logger = logging.getLogger("example")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
logger.handlers[:] = [handler]

logger.debug("hidden")
logger.info("service started")
logger.warning("disk almost full")
```

```output
INFO:service started
WARNING:disk almost full
```
:::

:::note
- Loggers name where an event came from.
- Handlers decide where records go.
- Levels let operators choose how much detail to see.
:::
