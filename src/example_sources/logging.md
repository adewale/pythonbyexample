+++
slug = "logging"
title = "Logging"
section = "Standard Library"
summary = "logging records operational events without using print as infrastructure."
doc_path = "/library/logging.html"
see_also = [
  "exceptions",
  "testing",
  "modules",
]
+++

`logging` records operational events without using `print` as infrastructure. Loggers name where each event came from, handlers route records to outputs, and levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`) let operators choose how much detail they want to see.

Use it when a program needs structured records with thresholds — production services, command-line tools, scheduled jobs. Prefer plain `print` when a small script just needs to show a line of human output.

The example wires a single stream handler to stdout to keep the output deterministic. Real applications usually configure logging once at startup and then call `logging.getLogger(__name__)` from each module.

:::program
```python
import logging
import sys

logger = logging.getLogger("example")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(levelname)s:%(message)s")
handler.setFormatter(formatter)
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
formatter = logging.Formatter("%(levelname)s:%(message)s")
handler.setFormatter(formatter)
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
