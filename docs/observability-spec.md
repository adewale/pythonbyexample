# Observability spec

This spec describes the observability stack for the deployed Cloudflare Python Worker. The goal is to emit one canonical, queryable, structured event per request so we can answer questions we have not yet thought to ask, without adding a heavyweight tracing SDK.

The implementation is intentionally lightweight: application code emits one structured custom event per request to Cloudflare Workers Logs, while the vendored ASGI shim keeps its internal failure logging.

## Source constraints this spec follows

- Boris Tane's `logging-best-practices` skill: one wide event per request per service, high-cardinality fields, business context, deployment context, a single logger/emitter, middleware-managed infrastructure, JSON structure, and only `info` / `error` levels.
- FastAPI middleware docs: middleware runs before path operations and after responses; `time.perf_counter()` is appropriate for request timing; when adding ASGI middleware, use `app.add_middleware()` so FastAPI/Starlette internal error handling and custom exception handlers still work.
- FastAPI error handling docs: use `@app.exception_handler(...)` for `RequestValidationError` and Starlette's `HTTPException`, and reuse FastAPI's default exception handlers when preserving response behavior.
- Starlette middleware docs: avoid `BaseHTTPMiddleware` for this use case because it breaks upward `ContextVar` propagation; use pure ASGI middleware, keep request-specific state local to `__call__`, and share request data through `scope` / `request.state`.
- Cloudflare Python Workers docs: Python Workers run in a `Default(WorkerEntrypoint).fetch(...)` handler; FastAPI is served through the Workers ASGI bridge; bindings are available through `self.env` and `request.scope["env"]`, not by assuming process environment variables.
- Cloudflare Workers Logs docs: structured JSON objects logged through the Worker runtime are indexed for filtering and grouping; Workers Logs also emit invocation logs; each log entry is limited to 256 KB.
- Cloudflare version metadata docs: `version_metadata` exposes Worker version metadata via `env.CF_VERSION_METADATA`; this spec uses only `id` as the deploy provenance key.

## Evidence and verification for Workers Logs

The Cloudflare docs do not currently have a single Python-specific observability guide that says "a Python dict converted with `to_js` and passed to `console.log` is indexed as Workers Logs fields." The evidence is by documented composition:

1. Python Workers examples document `from js import console; console.log(...)`, Python `logging`, and `print()` as supported logging paths.
2. Python Workers FFI docs document calling JavaScript globals from Python and converting Python dictionaries to JavaScript objects with `pyodide.ffi.to_js(..., dict_converter=Object.fromEntries)`.
3. Workers Logs docs state that custom `console.log` statements are visible in Workers Logs and recommend structured object logging because fields are extracted and indexed for filtering/grouping.

Therefore the implementation uses `console.log(to_js(payload, ...))` for both info and error events, with `level` as a field in the payload and JSON-line `print(...)` only as a local fallback. Verify the field indexing in a deployed preview before treating dashboard queries as production contracts: emit a request, inspect Workers Logs or `wrangler tail`, and confirm fields such as `request_id`, `cf.ray`, `cache`, and `worker_version.id` are filterable.

## Deployed verification checklist

Local tests can prove schema construction and privacy guardrails, but they cannot prove Workers Logs indexing. Before relying on dashboards/alerts:

1. Deploy a preview/staging Worker with this config.
2. Tail or inspect Workers Logs while sending requests with unique `x-request-id` values.
3. Exercise cache miss, cache hit, cache bypass, 404/client error, and Dynamic Worker HTTP 5xx paths.
4. Confirm exactly one custom application event per request and no separate invocation log when `observability.logs.invocation_logs = false` is honored.
5. Confirm Workers Logs exposes `request_id`, `path`, `cache`, `status_code`, `outcome`, `level`, `cf.ray`, and `worker_version.id` as filterable fields, not only as text inside a JSON string.
6. Confirm privacy negatives in the custom payload: no query string values, raw submitted code, Turnstile token, cookies, authorization header, request body, or `CF-Connecting-IP` in structured application fields or fallback messages.
7. Also inspect the Cloudflare-provided log envelope separately. `wrangler tail` may include request URL and headers outside the custom payload even when invocation logs are disabled. If that envelope is retained/queryable in Workers Logs, Cloudflare Workers Logs alone does not satisfy a strict "no query strings / no CF-Connecting-IP anywhere in logs" requirement.

Example probes:

```bash
PROBE="obs-$(date +%s)"
BASE="https://<preview-url>"

curl -sS -o /dev/null -H "x-request-id: $PROBE-miss" "$BASE/?obs_probe=$PROBE"
curl -sS -o /dev/null -H "x-request-id: $PROBE-hit" "$BASE/?obs_probe=$PROBE"
curl -sS -o /dev/null -H "x-request-id: $PROBE-bypass" "$BASE/layout-options/$PROBE?secret=do-not-log"
curl -sS -o /dev/null -H "x-request-id: $PROBE-404" "$BASE/does-not-exist-$PROBE?secret=do-not-log"
```

If the preview environment has Turnstile disabled or a smoke bypass secret, post code that raises to `/examples/hello-world` and verify `level="error"`, top-level `outcome="error"`, `worker.outcome="error"`, `worker.status_code=500`, and `worker.error.type="DynamicWorkerHTTPError"` without raw code in the event.

## Goals

- One context-rich custom event per request, per service.
- Every event carries a propagated request ID, deploy provenance, business context, and outcome.
- Cache-hit paths that bypass FastAPI are still observed.
- GET cache misses and cache bypasses are emitted once, after the outer Worker cache layer has finished, so `duration_ms` is end-to-end Worker time.
- Zero new runtime dependencies. Cloudflare Workers Logs are the sink.
- Idiomatic FastAPI and Starlette usage: pure ASGI middleware registered with `app.add_middleware(...)`, plus documented FastAPI exception handlers.

## Non-goals

- No Sentry, Datadog, OpenTelemetry SDK, or tracing client in the Python runtime.
- No per-step logs inside handlers. Handlers enrich the wide event.
- No PII: do not log `CF-Connecting-IP`, Turnstile tokens, cookies, raw submitted code, request bodies, or query strings. Country, colo, Ray ID, code hash, and code size are sufficient.
- No log levels beyond `info` and `error`.

## Pattern: wide events

The rule is: build one event through the request lifecycle, enrich it as work happens, and emit once when the Worker request is complete.

What this replaces:

- Scattered `print()` / `console.log()` calls.
- Multiple loggers per file.
- Free-form string logs.
- Per-step logs that cannot be queried at scale.

Expected custom log volume is one event per request. Cloudflare Workers invocation logs are disabled with `observability.logs.invocation_logs = false` so the wide event is the single per-request log we pay for and query.

## Lifecycle owner

The request lifecycle has two layers:

1. `Default.fetch` owns the full Worker request: cache lookup, possible cache hit return, FastAPI invocation, response cache write, and final emission.
2. FastAPI owns app routing and handler execution. A pure-ASGI middleware exposes the shared wide event as `request.state.wide_event` and records ASGI status/outcome, but it does not emit when the event was supplied by `Default.fetch`.

This division is deliberate. If the FastAPI middleware emitted in its own `finally` block for cache misses, it would miss time spent in the outer cache lookup/cache write path. `Default.fetch` is the only place that can emit exactly once for both cache hits and app-handled requests with end-to-end `duration_ms`.

For tests or local ASGI-only invocation that bypasses `Default.fetch`, the middleware may create and emit a fallback event itself.

## Components

### `src/observability.py` — single structured emitter

One module, configured once. It exposes request ID generation, safe error shaping, deploy context extraction from Worker bindings, shared request-event builders, status mapping, the pure-ASGI middleware, and `emit(event, env=...)`.

Use the JavaScript console API through Pyodide FFI so Workers Logs receives an object, not a JSON string. Workers Logs indexes object fields; `print(json.dumps(...))` is only a local fallback.

```python
# src/observability.py
import json
import sys
import time
import uuid

try:
    from js import Object, console
    from pyodide.ffi import to_js
except ImportError:  # Local/editor execution outside Workers.
    Object = None
    console = None
    to_js = None

_SERVICE_CONTEXT = {
    "service": "pythonbyexample",
    "python_version": sys.version.split()[0],
}
_MAX_ERROR_MESSAGE_CHARS = 512
_MAX_SAFE_STRING_CHARS = 256
_MAX_HEADER_CHARS = 128
_MAX_SAFE_COLLECTION_ITEMS = 20


def new_request_id() -> str:
    return uuid.uuid4().hex


def _text(value) -> str:
    return value if isinstance(value, str) else ""


def deploy_context(env) -> dict:
    metadata = None
    if env is not None:
        try:
            metadata = getattr(env, "CF_VERSION_METADATA", None)
        except Exception:
            metadata = None
    try:
        version_id = _text(getattr(metadata, "id", ""))
    except Exception:
        version_id = ""
    return {"worker_version": {"id": version_id}}


def _redact_sensitive_text(value: str, *, max_chars: int) -> str:
    # Redact obvious URL/form/query leaks such as code=..., token=..., secret=...,
    # cf-turnstile-response=..., cookies, auth, and CF-Connecting-IP before logging.
    ...


def error_dict(exc: Exception) -> dict:
    return {
        "type": type(exc).__name__,
        "message": _redact_sensitive_text(str(exc), max_chars=_MAX_ERROR_MESSAGE_CHARS),
    }


def safe_validation_errors(exc) -> list[dict]:
    # Return JSON-safe validation errors with `input` and `ctx` removed.
    ...


def safe_http_detail(detail):
    # Preserve only known framework default strings such as "Not Found".
    # Represent other strings by type/length to avoid logging user-derived values.
    ...


def emit(event: dict, *, env=None) -> None:
    payload = {
        **_SERVICE_CONTEXT,
        **deploy_context(env),
        **event,
        "timestamp": time.time(),
    }
    payload.setdefault("level", "error" if payload.get("outcome") == "error" else "info")

    try:
        if console is not None and to_js is not None and Object is not None:
            console.log(to_js(payload, dict_converter=Object.fromEntries))
            return
    except Exception:
        # Logging must never mask the request result. Fall back to a JSON line.
        pass

    stream = sys.stderr if payload["level"] == "error" else sys.stdout
    try:
        print(json.dumps(payload, default=str), file=stream)
    except Exception:
        pass
```

Do not read deploy provenance from `os.environ`. In Python Workers, `version_metadata` is exposed as a binding on `env`; FastAPI receives that same object at `request.scope["env"]`. `emit(...)` is best effort and must not raise back into request handling.

### `src/worker_asgi_bridge.py` — pass request state explicitly

Remove the global `_CURRENT_WORKER_REQUEST` handoff. It is request-specific state stored at module scope, which is unsafe under async interleaving and contradicts Starlette's stateless middleware guidance.

Instead, extend the vendored ASGI bridge to accept explicit ASGI `scope["state"]`:

```python
def request_to_scope(req, env, ws=False, *, state=None):
    scope = {
        "asgi": ASGI,
        "headers": headers,
        "http_version": "1.1",
        "method": req.method,
        "scheme": scheme,
        "path": path,
        "query_string": query_string,
        "type": ty,
        "env": env,
        "state": dict(state or {}),
    }
    return scope

async def process_request(app, req, env, ctx=None, *, state=None):
    ...
    await app(request_to_scope(req, env, state=state), receive, send)

async def fetch(app, req, env, ctx=None, *, state=None):
    ...
    result = await process_request(app, req, env, ctx, state=state)
```

`Default.fetch` then calls:

```python
asgi_request = getattr(request, "js_object", request)
await asgi.fetch(app, asgi_request, self.env, state={"wide_event": event})
```

Cloudflare's FastAPI example passes the Python Workers `request` object directly. This code keeps compatibility with the repo's existing vendored bridge by passing `request.js_object` when present, while passing only the shared wide event through ASGI state. Do not use a module global for request handoff.

### `observability.WideEventMiddleware` registered in `src/main.py`

Use a pure-ASGI middleware class registered with `app.add_middleware(observability.WideEventMiddleware)`. Do not use `@app.middleware("http")`; that decorator uses Starlette's `BaseHTTPMiddleware`, whose docs warn about `ContextVar` propagation limitations.

The middleware's job is to expose the event to handlers, record app status/outcome, and optionally emit only when no outer Worker event exists.

```python
class WideEventMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        state = scope.setdefault("state", {})
        owns_event = "wide_event" not in state
        event = state.setdefault("wide_event", observability.event_from_scope(scope))
        started = time.perf_counter()
        status_holder = {"code": 500}

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                status_holder["code"] = message["status"]
            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
            observability.record_status(event, status_holder["code"])
        except Exception as exc:
            event["status_code"] = 500
            event["outcome"] = "error"
            event["level"] = "error"
            event["error"] = observability.error_dict(exc)
            raise
        finally:
            event["app_duration_ms"] = round((time.perf_counter() - started) * 1000, 2)
            if owns_event:
                event["duration_ms"] = event["app_duration_ms"]
                observability.emit(event, env=scope.get("env"))

app.add_middleware(observability.WideEventMiddleware)
```

Status mapping:

```python
def record_status(event: dict, status_code: int) -> None:
    status_code = int(status_code)
    event["status_code"] = status_code
    if status_code >= 500 or event.get("level") == "error" or event.get("outcome") == "error":
        event["outcome"] = "error"
        event["level"] = "error"
    elif status_code >= 400:
        event["outcome"] = "client_error"
        event["level"] = "info"
    else:
        event["outcome"] = "success"
        event["level"] = "info"
```

Register this middleware with `app.add_middleware(...)`, not by directly wrapping `app = WideEventMiddleware(app)`, so FastAPI/Starlette internal server-error middleware and custom exception handlers continue to work. Keep all request-specific state inside `__call__` local variables or `scope["state"]`; do not mutate middleware instance state per request.

### Request event construction

Use the same request-event builder for `Default.fetch` cache hits and ASGI fallback events to avoid schema drift.

Required behavior:

- `request_id` comes from `x-request-id` if supplied by an upstream service and it passes a printable-ASCII allowlist and length check, otherwise from a sanitized `cf-ray`, otherwise from `observability.new_request_id()`.
- Preserve Cloudflare context under `cf`: Ray ID from `cf-ray`, colo/country from `request.cf` when available, country fallback from `cf-ipcountry`, and colo fallback from a Ray ID suffix for local/fake requests. Treat these as allowlisted but still bounded/sanitized values so spoofed local/preview headers cannot bloat logs or inject control characters.
- Store `path` without query string.
- Set `html_cache_version` on every HTTP request event.
- Set `cache` in `Default.fetch`: `hit`, `miss`, or `bypass`.

Cache mode rules:

```python
def _cache_mode_for_request(method: str, url: str) -> str:
    if method != "GET":
        return "bypass"
    return "miss" if should_cache_get_url(url) else "bypass"
```

For ASGI fallback tests that bypass `Default.fetch`, derive the same value from the ASGI scope (`method` and `path`).

### `Default.fetch` — one emit for every Worker request

`Default.fetch` creates the event before cache lookup and emits it in `finally`.

Shape:

```python
class Default(WorkerEntrypoint):
    async def fetch(self, request):
        started = time.perf_counter()
        event = observability.event_from_worker_request(
            request,
            cache="bypass",
            html_cache_version=HTML_CACHE_VERSION,
        )
        asgi_request = getattr(request, "js_object", request)

        try:
            if getattr(request, "method", None) == "GET" and caches is not None:
                if should_cache_get_url(getattr(request, "url", "")):
                    event["cache"] = "miss"
                    cached = await caches.default.match(cache_key)
                    if cached:
                        event["cache"] = "hit"
                        observability.record_status(event, cached.status)
                        return cached

                    response = await asgi.fetch(
                        app,
                        asgi_request,
                        self.env,
                        state={"wide_event": event},
                    )
                    if getattr(response, "status", 200) == 200:
                        response.headers.set(
                            "Cache-Control",
                            "public, max-age=300, stale-while-revalidate=86400",
                        )
                        await caches.default.put(cache_key, response.clone())
                    return response

                event["cache"] = "bypass"
                response = await asgi.fetch(
                    app,
                    asgi_request,
                    self.env,
                    state={"wide_event": event},
                )
                response.headers.set("Cache-Control", "no-store")
                return response

            event["cache"] = "bypass"
            return await asgi.fetch(
                app,
                asgi_request,
                self.env,
                state={"wide_event": event},
            )
        except Exception as exc:
            event["status_code"] = 500
            event["outcome"] = "error"
            event["level"] = "error"
            event.setdefault("error", observability.error_dict(exc))
            raise
        finally:
            event["duration_ms"] = round((time.perf_counter() - started) * 1000, 2)
            observability.emit(event, env=self.env)
```

This is the only normal emission site for deployed requests. Cache hits are observed because the event is emitted from `Default.fetch`; cache misses/bypasses are observed because the same event is passed into FastAPI and enriched there.

### Handlers enrich `request.state.wide_event`

FastAPI exposes `request.state` for per-request data. The wide event lives at `request.state.wide_event`. Handlers never emit logs; they only assign fields.

#### `run_example`

Add:

- `example.slug`
- `example.code_hash` — sha256 hex of submitted UTF-8 bytes, first 12 chars
- `example.code_bytes` — `len(submitted.encode("utf-8"))`
- `example.code_edited` — `submitted != example["code"]`
- `turnstile.outcome` — `pass` / `fail` / `bypass` / `disabled`
- `execution_ms` — duration around `_run_example`, recorded in a `finally` if execution started

Example:

```python
submitted_bytes = submitted.encode("utf-8")
request.state.wide_event["example"] = {
    "slug": example["slug"],
    "code_hash": hashlib.sha256(submitted_bytes).hexdigest()[:12],
    "code_bytes": len(submitted_bytes),
    "code_edited": submitted != example["code"],
}
```

Change `_verify_turnstile(...)` to return `(ok, message, outcome)` so the caller can record the outcome without re-deriving it. Do not log the token or `CF-Connecting-IP`; the latter may still be sent to Turnstile verification but must not enter the event.

#### `_run_example`

Add:

- `worker.outcome` — `success` / `runtime_unavailable` / `error`
- `worker.status_code` — HTTP status returned by the Dynamic Worker when a fetch completes
- `worker.error.{type,message}` when the Dynamic Worker fetch raises or returns HTTP 5xx
- `worker.cleanup_error.{type,message}` if `code_callback.destroy()` fails

On Dynamic Worker fetch failure, set `event["level"] = "error"` and re-raise so the request is correctly recorded as a 500. If the Dynamic Worker returns an HTTP 5xx response instead of raising, keep returning the response text to the page but set `worker.outcome="error"`, `worker.error.type="DynamicWorkerHTTPError"`, and `event["level"]="error"`. `record_status(...)` must preserve that pre-existing error state even when the outer HTML response is HTTP 200, so these business/runtime failures remain queryable as top-level `outcome="error"`.

When creating the Dynamic Worker request, propagate the request ID:

```python
dynamic_request = JsRequest.new(
    str(request.url),
    _to_js_object({
        "method": "GET",
        "headers": {"x-request-id": request.state.wide_event["request_id"]},
    }),
)
```

### Exception handlers for FastAPI-converted responses

FastAPI converts `RequestValidationError` and Starlette/FastAPI `HTTPException` into responses before middleware sees them as exceptions. The middleware records `outcome=client_error` or `outcome=error` from the status code, but dedicated handlers are needed for structured error context.

Register handlers that enrich the event and then delegate to FastAPI's defaults:

```python
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


def _wide_event(request: Request) -> dict | None:
    return getattr(request.state, "wide_event", None)


@app.exception_handler(RequestValidationError)
async def _log_validation(request: Request, exc: RequestValidationError):
    if event := _wide_event(request):
        event["error"] = {
            "type": "RequestValidationError",
            "details": observability.safe_validation_errors(exc),
        }
    return await request_validation_exception_handler(request, exc)


@app.exception_handler(StarletteHTTPException)
async def _log_http(request: Request, exc: StarletteHTTPException):
    if event := _wide_event(request):
        event["error"] = {
            "type": "HTTPException",
            "status_code": exc.status_code,
            "detail": observability.safe_http_detail(exc.detail),
        }
    return await http_exception_handler(request, exc)
```

Do not log `RequestValidationError.body`; FastAPI documents it as available for debugging, but body logging violates the no-PII/no-raw-code rule. `safe_validation_errors(...)` removes `input` and `ctx`, converts tuples/objects to JSON-safe primitives, bounds collection sizes, and redacts obvious sensitive query/form values. If an `HTTPException.detail` value is not one of FastAPI/Starlette's standard short strings, store only its type/length rather than the string value.

### Replace the silent cleanup `except`

Current code swallows cleanup failures:

```python
finally:
    if hasattr(code_callback, "destroy"):
        try:
            code_callback.destroy()
        except Exception:
            pass
```

Do not emit a second per-request log. Attach the cleanup failure to the same wide event:

```python
finally:
    if code_callback is not None and hasattr(code_callback, "destroy"):
        try:
            code_callback.destroy()
        except Exception as exc:
            worker_event["cleanup_error"] = observability.error_dict(exc)
            event["level"] = "error"
```

Only use a standalone `observability.emit({"event": "..."})` for failures that truly occur outside any request event.

### `wrangler.jsonc` — Workers Logs and deploy provenance

Make the logging sink and provenance explicit:

```jsonc
"observability": {
  "enabled": true,
  "head_sampling_rate": 1,
  "logs": {
    "invocation_logs": false
  }
},
"version_metadata": { "binding": "CF_VERSION_METADATA" }
```

`worker_version.id` is the deploy provenance key. It is Cloudflare-assigned, available through the version metadata binding, and avoids a separate CI/Wrangler var-injection step. Do not add a parallel Git SHA field unless we later prove `worker_version.id` is insufficient for rollback/debug workflows.

Keep `head_sampling_rate = 1` for launch so every request can be validated. Revisit sampling after dashboards and alert queries are stable. Keep invocation logs disabled unless the custom wide event proves insufficient.

## Canonical event schema

Every event carries the context from `observability.py` plus a subset of the per-request fields below. Nested fields are shown with dot notation.

| Field | Type | Source | Notes |
|---|---|---|---|
| `service` | string | emitter | Constant: `pythonbyexample`. |
| `python_version` | string | emitter | `sys.version` first token. |
| `timestamp` | float | emitter | Unix epoch seconds. |
| `level` | string | emitter / lifecycle | `info` or `error`. |
| `worker_version.id` | string | version metadata binding | Cloudflare Worker version ID; primary deploy provenance key. |
| `request_id` | string | outer / middleware fallback | `x-request-id`, else `cf-ray`, else generated UUID. |
| `method` | string | request | HTTP method. |
| `path` | string | request | Request path, no query. |
| `cf.ray` | string \| null | request headers | Cloudflare Ray ID. |
| `cf.colo` | string \| null | request.cf / request headers | Cloudflare colo from `request.cf.colo`, falling back to Ray ID suffix when present. |
| `cf.country` | string \| null | request.cf / request headers | `request.cf.country`, falling back to `cf-ipcountry`. |
| `cache` | string | outer / fallback | `hit` / `miss` / `bypass`. |
| `html_cache_version` | string | outer / fallback | From `asset_manifest.HTML_CACHE_VERSION`. |
| `status_code` | int | middleware / cache hit | Response status. |
| `outcome` | string | lifecycle | `success` / `client_error` / `error`; preserves handler-marked runtime/business errors even when HTTP status is 200. |
| `duration_ms` | float | outer | End-to-end Worker request duration. |
| `app_duration_ms` | float | middleware | FastAPI/ASGI duration only. Missing on cache hits. |
| `error.type` | string | middleware / exception handler | Exception class or logical error type. |
| `error.message` | string | middleware | Truncated and redacted `str(exc)` for unexpected exceptions. |
| `error.status_code` | int | HTTP exception handler | HTTPException status. |
| `error.detail` | JSON-safe | HTTP exception handler | Standard short detail only; otherwise type/length only. |
| `error.details` | array | validation handler | `exc.errors()` with `input` and `ctx` removed, values normalized to JSON-safe primitives. |
| `example.slug` | string | handler | Example identifier. |
| `example.code_hash` | string | handler | First 12 hex chars of sha256(submitted UTF-8 bytes). |
| `example.code_bytes` | int | handler | Byte length of submitted UTF-8 code. |
| `example.code_edited` | bool | handler | True when submitted differs from canonical. |
| `turnstile.outcome` | string | handler | `pass` / `fail` / `bypass` / `disabled`. |
| `execution_ms` | float | handler | Sandboxed run duration. |
| `worker.outcome` | string | handler | Dynamic Worker outcome. |
| `worker.status_code` | int | handler | Dynamic Worker HTTP status when fetch completes. |
| `worker.error.type` | string | handler | Dynamic Worker fetch exception type or `DynamicWorkerHTTPError`. |
| `worker.error.message` | string | handler | Truncated and redacted `str(exc)`. |
| `worker.cleanup_error.type` | string | handler | Cleanup exception type. |
| `worker.cleanup_error.message` | string | handler | Truncated and redacted `str(exc)`. |

## High-cardinality fields we expect to query

These dimensions are intentionally queryable:

- `request_id` — pinpoint one user's experience across service hops.
- `example.slug` — identify which example is broken.
- `example.code_hash` — group identical user submissions and spot replay attacks without logging code.
- `worker_version.id` — correlate regressions with deploys.
- `cf.colo` and `cf.country` — find region-specific failures.

## Privacy and size guardrails

- Never place request bodies, raw code, Turnstile tokens, cookies, `Authorization`, or `CF-Connecting-IP` in the custom payload.
- Do not place query strings in the custom payload. Use `path` only.
- Known platform caveat from deployed verification: `wrangler tail` wraps custom console logs in a Cloudflare event envelope that can include the raw request URL and headers such as `cf-connecting-ip`. Treat this as a sink-level privacy risk to validate in the Workers Logs dashboard before declaring the whole logging pipeline PII-free.
- Truncate and redact exception messages and validation details so the full event remains far below Workers Logs' 256 KB limit. Redact obvious URL/form/query leaks for keys such as `code`, `token`, `secret`, `cf-turnstile-response`, cookies, auth, and `CF-Connecting-IP`.
- Use an allowlist for headers: `x-request-id`, `cf-ray`, and `cf-ipcountry`; cap all accepted header values to small printable strings before logging them.
- Treat ordinary 4xx responses as `level=info`, `outcome=client_error`; reserve `level=error` for 5xx/internal failures and handler-marked runtime/business failures such as Dynamic Worker HTTP 5xx.

## Order of work

1. Add `src/observability.py` with structured `console.log` object emission and local `print` fallback.
2. Extend the vendored ASGI bridge to accept `state`; remove `_CURRENT_WORKER_REQUEST` and the `@app.middleware("http")` worker-request shim.
3. Add Worker-level event creation/emission in `Default.fetch`, including cache hit/miss/bypass handling and end-to-end `duration_ms`.
4. Add pure-ASGI `observability.WideEventMiddleware` via `app.add_middleware(...)` to expose `request.state.wide_event`, record `status_code`, `outcome`, and `app_duration_ms`, and emit only for ASGI-only fallback calls.
5. Register the `RequestValidationError` and Starlette `HTTPException` handlers with safe detail shaping.
6. Enrich `run_example`, `_verify_turnstile`, and `_run_example` via `request.state.wide_event`.
7. Preserve handler-marked runtime/business errors when recording HTTP status.
8. Replace the silent cleanup `except` by attaching `worker.cleanup_error` to the same event.
9. Add `version_metadata`, explicit `head_sampling_rate`, and disabled invocation logs to `wrangler.jsonc`.
10. Verify Workers Logs field extraction in a deployed preview.
11. Optional follow-up: once the field set is stable, consider Logpush/Tail Workers for longer retention or downstream analytics.

## Open questions

- Do we need an allowlisted cache-debug block (`cache_control`, `if_none_match_present`) for diagnosing edge cache behavior, or is `cache` + `html_cache_version` enough?
- Does the Workers Logs dashboard retain/query the same raw request URL/header envelope observed in `wrangler tail` for custom console logs? If yes, use a different sink or accept that Workers Logs is not strictly PII-free at the platform-envelope layer.
