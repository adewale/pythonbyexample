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

:::unsupported
`ThreadPoolExecutor` runs `square` across two worker threads sharing the same interpreter (and the GIL); `ProcessPoolExecutor` runs `pow` across two child processes with isolated memory. Each `pool.map` returns an iterator over results in input order, and the surrounding `with` block joins the workers when the body exits. (This fragment runs in standard Python only — the Python By Example runner does not provide native threads or child processes.)

```python
with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(square, [1, 2, 3])))

with ProcessPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(pow, [4, 5], [2, 2])))
```
:::

:::cell
A thread pool runs ordinary callables while sharing memory with the current process. `map()` returns results in input order.

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
A process pool uses separate Python processes. That boundary is heavier, but it can run CPU-bound work outside the current interpreter.

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
- The displayed executor names are standard Python concepts; the site avoids actually creating host threads or processes in the live runner.
:::
