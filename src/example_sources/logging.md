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

`logging` records operational events without using `print` as infrastructure. A logger names where an event came from, a handler decides where records go, a formatter chooses their text shape, and a level decides which records are important enough to emit.

Use logging for services, command-line tools, scheduled jobs, and libraries that need diagnostics operators can filter. Use `print` for a program's intentional user-facing output.

The example writes to stdout so the page stays deterministic. Real applications usually configure handlers once at startup and then call `logging.getLogger(__name__)` from each module.

:::program
```python
import logging
import sys

logger = logging.getLogger("example.worker")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
parts = ["%(levelname)s", "%(name)s", "%(message)s"]
formatter = logging.Formatter(":".join(parts))
handler.setFormatter(formatter)
logger.handlers[:] = [handler]
logger.propagate = False

logger.debug("hidden detail")
logger.info("service started")
logger.warning("disk almost full")

handler.setLevel(logging.WARNING)
logger.info("hidden after threshold change")
logger.error("write failed")
```
:::

:::cell
A logger name records which part of the program produced the event. The handler and formatter choose where and how the event is shown.

```python
import logging
import sys

logger = logging.getLogger("example.worker")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
parts = ["%(levelname)s", "%(name)s", "%(message)s"]
formatter = logging.Formatter(":".join(parts))
handler.setFormatter(formatter)
logger.handlers[:] = [handler]
logger.propagate = False

logger.debug("hidden detail")
logger.info("service started")
logger.warning("disk almost full")
```

```output
INFO:example.worker:service started
WARNING:example.worker:disk almost full
```
:::

:::cell
Levels are thresholds. Raising the handler level to `WARNING` suppresses later `INFO` records without changing the call sites.

```python
import logging
import sys

logger = logging.getLogger("example.worker")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARNING)
parts = ["%(levelname)s", "%(name)s", "%(message)s"]
formatter = logging.Formatter(":".join(parts))
handler.setFormatter(formatter)
logger.handlers[:] = [handler]
logger.propagate = False

logger.info("hidden after threshold change")
logger.error("write failed")
```

```output
ERROR:example.worker:write failed
```
:::

:::note
- Configure logging once; call named loggers throughout the program.
- Logger and handler levels both participate in filtering.
- Use exceptions for control flow failures, logging for operational evidence, and warnings for soft compatibility problems.
:::
