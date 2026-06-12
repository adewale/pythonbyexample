+++
slug = "async-await"
title = "Async Await"
section = "Async"
summary = "async def creates coroutines, and await pauses until awaitable work completes."
doc_path = "/library/asyncio-task.html"
see_also = [
  "async-iteration-and-context",
  "functions",
  "context-managers",
]
+++

`async def` creates a coroutine function. Calling it creates a coroutine object; the body runs when an event loop awaits or schedules it.

`await` pauses the current coroutine until another awaitable completes. This lets one event loop make progress on other work while a task waits for I/O.

Cloudflare Workers handlers are asynchronous, so understanding `await` is practical for fetch calls, bindings, and service interactions even when a small example uses `asyncio.sleep(0)` as a stand-in.

The alternative is ordinary `def` for work that completes immediately. Use async code for I/O-shaped waiting, not as a faster replacement for CPU-bound Python.

:::program
```python
import asyncio

def slug_to_title(slug):
    return slug.replace("-", " ").title()

async def fetch_title(slug):
    await asyncio.sleep(0)
    return slug_to_title(slug)

async def main():
    title = await fetch_title("async-await")
    print(title)
    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))
    print(titles)

asyncio.run(main())


class Session:
    async def __aenter__(self):
        print("open")
        return self

    async def __aexit__(self, *_):
        print("close")
        return False


async def stream():
    for slug in ["json", "datetime"]:
        await asyncio.sleep(0)
        yield slug


async def driver():
    async with Session():
        async for slug in stream():
            print(slug)

asyncio.run(driver())
```
:::

:::cell
An ordinary `def` function computes its result immediately: calling it runs the body and hands the value straight back. This synchronous form is the baseline the rest of the page contrasts against.

```python
def slug_to_title(slug):
    return slug.replace("-", " ").title()

print(slug_to_title("async-await"))
```

```output
Async Await
```
:::

:::cell
An `async def` function returns a coroutine object when called. The function body has not produced its final result yet.

```python
import asyncio

async def fetch_title(slug):
    await asyncio.sleep(0)
    return slug_to_title(slug)

coroutine = fetch_title("async-await")
print(coroutine.__class__.__name__)
coroutine.close()
```

```output
coroutine
```
:::

:::cell
Use `await` inside another coroutine to get the eventual result. `asyncio.run()` starts an event loop for the top-level coroutine.

```python
async def main():
    title = await fetch_title("async-await")
    print(title)

asyncio.run(main())
```

```output
Async Await
```
:::

:::cell
`asyncio.gather()` awaits several awaitables and returns their results in order. This is the shape used when independent I/O operations can progress together.

```python
async def main():
    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))
    print(titles)

asyncio.run(main())
```

```output
['Json', 'Datetime']
```
:::

:::cell
`async with` and `async for` are the asynchronous forms of context managers and iteration. A class implements `__aenter__`/`__aexit__` to act as an async context manager; an `async def` function with `yield` becomes an async generator. The dedicated [async iteration and context](/examples/async-iteration-and-context) page explains the protocols in depth.

```python
class Session:
    async def __aenter__(self):
        print("open")
        return self

    async def __aexit__(self, *_):
        print("close")
        return False


async def stream():
    for slug in ["json", "datetime"]:
        await asyncio.sleep(0)
        yield slug


async def driver():
    async with Session():
        async for slug in stream():
            print(slug)

asyncio.run(driver())
```

```output
open
json
datetime
close
```
:::

:::note
- Calling an async function creates a coroutine object.
- `await` yields control until an awaitable completes.
- Workers request handlers are async, so this pattern appears around fetches and bindings.
- Prefer ordinary functions when there is no awaitable work to coordinate.
:::
