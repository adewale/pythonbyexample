# Observability spec

This spec describes the observability stack for the deployed Worker. The goal is to emit one canonical, queryable JSON event per request so we can answer questions we have not yet thought to ask, without pulling in a heavyweight tracing SDK.

The current state is minimal. `wrangler.jsonc:21-23` enables Cloudflare Workers' built-in observability, which forwards stdout to the dashboard. No application logging exists in `src/main.py`; the only loggers in the tree are inside the vendored ASGI shim (`src/worker_asgi_bridge.py`) and only fire on internal failures.

## Goals

- One context-rich JSON event per request, per service.
- Every event carries a propagated request ID, deploy provenance, business context, and outcome.
- Cache-hit paths that bypass the FastAPI app are still observed.
- Zero new runtime dependencies. Cloudflare Workers' built-in observability is the sink.
- Idiomatic for FastAPI and Starlette — uses the patterns the official docs recommend, not the ones they warn against.

## Non-goals

- No Sentry, Datadog, or OpenTelemetry SDK. The Python Workers runtime is constrained; a heavyweight SDK risks startup-time regressions.
- No per-step logs inside handlers. Handlers enrich the wide event instead.
- No PII. `CF-Connecting-IP` is already used to verify Turnstile (`src/main.py:140-142`) and must not be logged. Country and Ray ID are sufficient.
- No new log levels. Only `info` (normal completions) and `error` (unexpected failures).

## Pattern: wide events

Adapted from Boris Tane's logging-best-practices skill, which itself draws on Stripe's "canonical log lines". The rule: build one event through the request lifecycle, emit once in a `finally` block with full context, even on failure.

What this replaces:

- Scattered `print()` calls (we have none today, but the pattern prevents them).
- Multiple loggers per file.
- Free-form string logs.
- Per-step logs that are useless to query at scale.

## Components

### `src/observability.py` — single emit function

One module, configured once at import time. Captures deploy and runtime context. Exposes `emit(event)` which writes a single JSON line to stdout (Cloudflare's observability backend ingests stdout).

```python
# src/observability.py
import json, os, sys, time, uuid

_ENV = {
    "service": "pythonbyexample",
    "version": os.environ.get("CF_VERSION_METADATA_ID") or "",
    "commit_hash": os.environ.get("PBE_COMMIT_SHA") or "",
    "python_version": sys.version.split()[0],
}

def new_request_id() -> str:
    return uuid.uuid4().hex

def emit(event: dict) -> None:
    print(json.dumps({**_ENV, **event, "timestamp": time.time()}, default=str))
```

Module-scope `_ENV` capture is deliberate. Python Workers isolates initialise module state once per cold start; using FastAPI's `lifespan` would re-run the snapshot per request boundary unnecessarily.

### `src/main.py` — pure-ASGI middleware

**Use a pure-ASGI middleware class registered via `app.add_middleware(...)`. Do not use `@app.middleware("http")`.**

Starlette's middleware docs warn explicitly:

> Using `BaseHTTPMiddleware` will prevent changes to `contextvars.ContextVar`s from propagating upwards.
>
> If a `BaseHTTPMiddleware` is positioned earlier in the middleware stack, it will disrupt `contextvars` propagation for any subsequent Pure ASGI Middleware that relies on them.
>
> To overcome these limitations, use pure ASGI middleware.

`@app.middleware("http")` is sugar over `BaseHTTPMiddleware`. It also buffers streamed response bodies, which would harm any future SSE or streaming endpoint. The existing `add_worker_request_to_scope` middleware at `src/main.py:35-38` has the same defect; port it at the same time.

Shape:

```python
class WideEventMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        started = time.perf_counter()
        ray = _header(scope, b"cf-ray") or ""
        event = {
            "request_id": ray or observability.new_request_id(),
            "method": scope["method"],
            "path": scope["path"],
            "colo": ray.split("-")[-1] if "-" in ray else None,
            "country": _header(scope, b"cf-ipcountry"),
            "cache": "miss",
        }
        scope["state"] = {**scope.get("state", {}), "wide_event": event}

        status_holder = {"code": 500}

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                status_holder["code"] = message["status"]
            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
            event["status_code"] = status_holder["code"]
            event["outcome"] = "success" if status_holder["code"] < 400 else "client_error"
        except Exception as exc:
            event["status_code"] = 500
            event["outcome"] = "error"
            event["error"] = {"type": type(exc).__name__, "message": str(exc)}
            raise
        finally:
            event["duration_ms"] = round((time.perf_counter() - started) * 1000, 2)
            observability.emit(event)

app.add_middleware(WideEventMiddleware)
```

The existing worker-request injection collapses into the same middleware (it can write `scope["worker_request"] = _CURRENT_WORKER_REQUEST` alongside `scope["state"]`).

### Handlers enrich `request.state`

FastAPI exposes `request.state` for per-request data shared between middleware and handlers. The wide event lives there. Handlers do not log; they assign fields.

The two enrichment sites that matter:

- **`run_example` at `src/main.py:92-122`** — adds `example.slug`, `code_hash` (sha256 hex, first 12 chars), `code_length`, `code_edited` (boolean, `submitted != example["code"]`), `turnstile.outcome` (`pass` / `fail` / `bypass` / `disabled`), and `execution_ms`.
- **`_run_example` at `src/main.py:160-193`** — adds `worker.outcome` and, if the dynamic Worker fetch raises, `worker.error.{type,message}`.

Example:

```python
request.state.wide_event["example"] = {
    "slug": example["slug"],
    "code_hash": hashlib.sha256(submitted.encode("utf-8")).hexdigest()[:12],
    "code_length": len(submitted),
    "code_edited": submitted != example["code"],
}
```

### Exception handlers for the responses FastAPI converts

FastAPI converts `RequestValidationError` and `HTTPException` into responses *before* middleware sees them as exceptions. The middleware's `try/except` will record `outcome=client_error` but miss the structured error detail.

Register two handlers that enrich the wide event before delegating to the default response:

```python
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(RequestValidationError)
async def _log_validation(request: Request, exc: RequestValidationError):
    request.state.wide_event["error"] = {
        "type": "RequestValidationError",
        "details": exc.errors(),
    }
    return await request_validation_exception_handler(request, exc)

@app.exception_handler(StarletteHTTPException)
async def _log_http(request: Request, exc: StarletteHTTPException):
    request.state.wide_event["error"] = {
        "type": "HTTPException",
        "status_code": exc.status_code,
        "detail": exc.detail,
    }
    return await http_exception_handler(request, exc)
```

### `Default.fetch` — cache-hit emission

Cache hits in `Default.fetch` (`src/main.py:202-225`) return without entering the FastAPI app. They must still be observed, otherwise we cannot measure cache effectiveness.

Emit a second wide event from the outer layer for the cache-hit path:

```python
if cached:
    observability.emit({
        "request_id": request.headers.get("cf-ray") or "",
        "method": "GET",
        "path": urlparse(request.url).path,
        "status_code": cached.status,
        "outcome": "success",
        "cache": "hit",
        "duration_ms": round((time.perf_counter() - started) * 1000, 2),
    })
    return cached
```

The miss/bypass paths fall through to FastAPI, where the middleware does the job; the middleware sets `cache="miss"` by default, and the outer layer overwrites it to `"bypass"` for the no-cache POST path before invoking `asgi.fetch`.

### Replace the silent `except`

`src/main.py:188-193` swallows cleanup failures:

```python
finally:
    if hasattr(code_callback, "destroy"):
        try:
            code_callback.destroy()
        except Exception:
            pass
```

Becomes:

```python
finally:
    if hasattr(code_callback, "destroy"):
        try:
            code_callback.destroy()
        except Exception as exc:
            observability.emit({
                "event": "code_callback_destroy_failed",
                "error": {"type": type(exc).__name__, "message": str(exc)},
            })
```

### `wrangler.jsonc` — deploy provenance

Add a `version_metadata` binding so every event carries a Cloudflare-assigned version ID, plus a build-time `PBE_COMMIT_SHA` var:

```jsonc
"version_metadata": { "binding": "CF_VERSION_METADATA" },
"vars": { "PBE_COMMIT_SHA": "" }  // overridden in CI via `wrangler deploy --var PBE_COMMIT_SHA:$(git rev-parse HEAD)`
```

CI's deploy step sets `PBE_COMMIT_SHA` to the commit being deployed.

## Canonical event schema

Every event carries the env block from `observability.py` plus a subset of the per-request fields below. Field names are `snake_case` throughout.

| Field | Type | Source | Notes |
|---|---|---|---|
| `service` | string | env | Constant: `"pythonbyexample"`. |
| `version` | string | env | Cloudflare version metadata ID. |
| `commit_hash` | string | env | Git SHA injected at deploy. |
| `python_version` | string | env | `sys.version` first token. |
| `timestamp` | float | env | Unix epoch seconds. |
| `request_id` | string | middleware | `cf-ray` header, or generated UUID. |
| `method` | string | middleware | HTTP method. |
| `path` | string | middleware | Request path, no query. |
| `colo` | string \| null | middleware | Cloudflare colo from `cf-ray` suffix. |
| `country` | string \| null | middleware | `cf-ipcountry`. |
| `cache` | string | middleware / outer | `hit` / `miss` / `bypass`. |
| `status_code` | int | middleware | Response status. |
| `outcome` | string | middleware | `success` / `client_error` / `error`. |
| `duration_ms` | float | middleware | Total request duration. |
| `error.type` | string | middleware / exc handler | Exception class name. |
| `error.message` | string | middleware | `str(exc)`. |
| `error.details` | array | exc handler | `RequestValidationError.errors()`. |
| `example.slug` | string | handler | Example identifier. |
| `example.code_hash` | string | handler | First 12 hex chars of sha256. |
| `example.code_length` | int | handler | Byte length of submitted code. |
| `example.code_edited` | bool | handler | True when submitted differs from canonical. |
| `turnstile.outcome` | string | handler | `pass` / `fail` / `bypass` / `disabled`. |
| `execution_ms` | float | handler | Sandboxed run duration. |
| `worker.outcome` | string | handler | Dynamic-Worker outcome. |
| `worker.error.type` | string | handler | When the dynamic-Worker fetch raises. |
| `worker.error.message` | string | handler | `str(exc)`. |
| `html_cache_version` | int | outer | From `asset_manifest.HTML_CACHE_VERSION`. |

## High-cardinality fields we will query against

The fields below are deliberately unbounded; the value of the wide-event pattern is that any one of them is a queryable dimension.

- `request_id` — pinpoint one user's experience.
- `example.slug` — "which example is broken?".
- `example.code_hash` — group identical user submissions; spot replay attacks.
- `commit_hash` — correlate regressions with deploys.
- `cf.colo`, `cf.country` — region-specific failures.

## What FastAPI / Starlette tell us to change vs. an obvious first draft

These corrections are baked into the spec above; listing them here so reviewers see the reasoning.

1. **Pure ASGI middleware, not `@app.middleware("http")`.** Starlette explicitly warns that `BaseHTTPMiddleware` breaks `ContextVar` propagation and disrupts downstream pure-ASGI middleware. Source: [Starlette middleware docs](https://www.starlette.dev/middleware/).
2. **`request.state.wide_event`, not `request.scope["wide_event"]`.** `request.state` is the documented per-request namespace FastAPI handlers expect.
3. **Register `@app.exception_handler` for `RequestValidationError` and `HTTPException`.** FastAPI converts these to responses before middleware sees an exception; without dedicated handlers, structured error context is lost.
4. **Use `app.add_middleware(...)`, not direct wrapping.** FastAPI's advanced-middleware docs: "FastAPI (actually Starlette) provides a simpler way to do it that makes sure that the internal middlewares handle server errors and custom exception handlers work properly."

FastAPI itself does not recommend a specific logger; stdlib `json` + `print` is in tension with nothing official.

## Order of work

1. Add `src/observability.py`.
2. Port `add_worker_request_to_scope` and add the wide-event behaviour as a single pure-ASGI `WideEventMiddleware`. Register with `app.add_middleware(...)`.
3. Register the two exception handlers.
4. Enrich `run_example` and `_run_example` via `request.state.wide_event`.
5. Emit the cache-hit / bypass events from `Default.fetch`.
6. Replace the silent `except` in `_run_example`.
7. Add `version_metadata` binding and `PBE_COMMIT_SHA` var to `wrangler.jsonc`; wire the deploy step in CI.
8. Optional follow-up: enable Logpush to R2 for long-retention querying once the field set is stable.

## Open questions

- Do we want `Cache-Control` and `If-None-Match` echoed into the event for cache-debugging? Cheap to add; trims context if we never need it.
- Should the cache-hit emit live in `Default.fetch` or in a thin Python helper that both the outer layer and the middleware call, to keep the schema declared in one place? Lean toward one helper once the second emit site exists.
