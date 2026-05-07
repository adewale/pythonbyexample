+++
slug = "async-iteration-and-context"
title = "Async Iteration and Context"
section = "Async"
summary = "async for and async with consume asynchronous streams and cleanup protocols."
doc_path = "/reference/compound_stmts.html#async-for"
see_also = [
  "async-await",
  "iterators",
  "context-managers",
]
+++

`async for` consumes an asynchronous iterator: a stream whose next value may require `await`. `async with` surrounds a block with asynchronous setup and cleanup.

These forms appear around network streams, database cursors, locks, and service clients where both iteration and cleanup may wait on I/O.

Use ordinary `for` and `with` when producing the next value or cleaning up does not need to await anything.

The syntax mirrors `for` and `with`, but the protocol methods are asynchronous.

:::program
```python
import asyncio

async def titles():
    for slug in ["values", "async-await"]:
        await asyncio.sleep(0)
        yield slug.replace("-", " ").title()

class Session:
    async def __aenter__(self):
        print("open")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("close")

async def main():
    async with Session():
        async for title in titles():
            print(title)

asyncio.run(main())
```
:::

:::cell
An async generator can `await` before yielding each value. `async for` consumes those values with the asynchronous iteration protocol.

```python
import asyncio

async def titles():
    for slug in ["values", "async-await"]:
        await asyncio.sleep(0)
        yield slug.replace("-", " ").title()

print(titles.__name__)
```

```output
titles
```
:::

:::cell
An async context manager defines `__aenter__` and `__aexit__`. `async with` awaits setup and cleanup around the block.

```python
class Session:
    async def __aenter__(self):
        print("open")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("close")

print(Session.__name__)
```

```output
Session
```
:::

:::cell
The top-level coroutine combines both protocols: open the async resource, then consume the async stream inside it.

```python
async def main():
    async with Session():
        async for title in titles():
            print(title)

asyncio.run(main())
```

```output
open
Values
Async Await
close
```
:::

:::note
- `async for` consumes asynchronous iterators.
- `async with` awaits asynchronous setup and cleanup.
- These forms are common around I/O-shaped resources.
:::
