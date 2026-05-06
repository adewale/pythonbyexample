+++
slug = "async-await"
title = "Async Await"
section = "Async"
summary = "async def defines coroutines that can be awaited."
doc_path = "/library/asyncio-task.html"
+++

async def creates a coroutine function, and await pauses that coroutine until another awaitable completes. This lets one worker handle other tasks while waiting for I/O.

Cloudflare Workers handlers are asynchronous, so understanding await is practical for fetch calls, bindings, and service interactions even when a small example only sleeps briefly.

await yields control until an awaitable completes. Cloudflare Workers handlers are async functions.

:::program
```python
import asyncio

async def answer():
    await asyncio.sleep(0)
    return 42

print(asyncio.run(answer()))
```
:::

:::cell
async def creates a coroutine function, and await pauses that coroutine until another awaitable completes. This lets one worker handle other tasks while waiting for I/O.

Cloudflare Workers handlers are asynchronous, so understanding await is practical for fetch calls, bindings, and service interactions even when a small example only sleeps briefly.

await yields control until an awaitable completes. Cloudflare Workers handlers are async functions.

```python
import asyncio

async def answer():
    await asyncio.sleep(0)
    return 42

print(asyncio.run(answer()))
```

```output
42
```
:::

:::note
- await yields control until an awaitable completes.
- Cloudflare Workers handlers are async functions.
:::
