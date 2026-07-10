+++
slug = "threads-and-processes"
title = "Threads and Processes"
section = "Standard Library"
summary = "Threads share memory, while processes run in separate interpreters."
doc_path = "/library/concurrent.futures.html"
see_also = [
  "async-await",
  "subprocesses",
  "networking",
]
expected_output = "[1, 4, 9]\nProcessPoolExecutor\n"
+++

Threads and processes are two ways to run work outside the current control path. Threads are useful for overlapping I/O-shaped waits, while processes are useful when CPU-bound work needs separate interpreter processes.

In standard Python, `ThreadPoolExecutor` and `ProcessPoolExecutor` are the ordinary tools for this lesson. This site's live example runner does not expose native threads or child processes, so this page keeps the proper executor model visible and separates the standard Python idea from what can execute here.

This is different from `asyncio`: threads and processes run ordinary callables through executors, while `async` code cooperatively awaits coroutines. Choose the smallest concurrency model that matches the bottleneck.

:::program
```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def square(number):
    return number * number

with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(square, [1, 2, 3])))

print(ProcessPoolExecutor.__name__)
```
:::

:::cell
`ThreadPoolExecutor` runs `square` across worker threads that share this interpreter and its GIL; `map()` returns results in input order, and the `with` block joins the workers when the body exits. The in-browser sandbox cannot create native threads, so pressing Run here fails; this thread-pool output was produced under standard CPython at build time.

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def square(number):
    return number * number

with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(square, [1, 2, 3])))
```

```output
[1, 4, 9]
```
:::

:::cell
`ProcessPoolExecutor` is the heavier boundary: separate Python processes with isolated memory, for CPU-bound work that the GIL would otherwise serialise. The sandbox cannot spawn processes either, so this cell only inspects the class name rather than running a pool.

```python
print(ProcessPoolExecutor.__name__)
```

```output
ProcessPoolExecutor
```
:::

:::note
- Threads share memory, so mutable shared state needs care.
- Processes avoid shared interpreter state but require values to cross a process boundary.
- Prefer `asyncio` for coroutine-based I/O and executors for ordinary blocking callables.
- The thread-pool output came from real worker threads under standard CPython at build time; the in-browser sandbox cannot create threads or processes, so live runs of this page fail there.
:::
