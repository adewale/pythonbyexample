import hashlib
import time
from urllib.parse import parse_qs, urlparse

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from workers import WorkerEntrypoint, python_from_rpc

from app import FAVICON_SVG, build_dynamic_worker_code, get_example, render_example_page, route
from asset_manifest import HTML_CACHE_VERSION
from examples import PYTHON_VERSION

import asgi

try:
    from js import Object, Request as JsRequest, caches
    from pyodide.ffi import create_once_callable, jsnull, to_js
except ImportError:  # Allows editor tooling outside Workers.
    Object = None
    JsRequest = None
    jsnull = None
    create_once_callable = None
    to_js = None
    caches = None

app = FastAPI(title="Python By Example")
_CURRENT_WORKER_REQUEST = None


@app.middleware("http")
async def add_worker_request_to_scope(request: Request, call_next):
    request.scope["worker_request"] = _CURRENT_WORKER_REQUEST
    return await call_next(request)


def _to_js_object(value):
    if to_js is None or Object is None:
        return value
    return to_js(value, dict_converter=Object.fromEntries)


def _html(body, status=200):
    return HTMLResponse(body, status_code=status)


def should_cache_get_url(url: str) -> bool:
    path = urlparse(url).path
    return not path.startswith("/layout-options/")


def html_cache_key_url(url: str) -> str:
    separator = "&" if "?" in url else "?"
    return f"{url}{separator}__html_v={HTML_CACHE_VERSION}"


@app.get("/favicon.svg")
async def favicon():
    return Response(FAVICON_SVG, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=31536000, immutable"})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    response = route(str(request.url), method="GET")
    return _html(response.body, response.status)


@app.get("/examples/{slug}", response_class=HTMLResponse)
async def example_page(slug: str, request: Request):
    response = route(str(request.url), method="GET")
    return _html(response.body, response.status)


@app.post("/examples/{slug}", response_class=HTMLResponse)
async def run_example(slug: str, request: Request):
    example = get_example(slug)
    if example is None:
        return _html("<h1>Example not found</h1>", 404)
    body = (await request.body()).decode("utf-8")
    submitted = parse_qs(body).get("code", [example["code"]])[0]
    started = time.perf_counter()
    output = await _run_example(request, example["slug"], submitted)
    elapsed_ms = (time.perf_counter() - started) * 1000
    return _html(render_example_page(example, output=output, code=submitted, execution_time_ms=elapsed_ms))


async def _run_example(request: Request, slug, code):
    module_name = "runner.py"
    worker_code = {
        "compatibilityDate": "2026-05-04",
        "compatibilityFlags": [
            "python_workers",
            "python_dedicated_snapshot",
            "disable_python_external_sdk",
        ],
        "mainModule": module_name,
        "modules": {module_name: build_dynamic_worker_code(code)},
        "globalOutbound": jsnull,
        "limits": {"cpuMs": 1000, "subRequests": 0},
        "env": {"PYTHON_VERSION": PYTHON_VERSION, "EXAMPLE_SLUG": slug},
    }
    env = request.scope["env"]
    code_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()
    worker_id = f"pythonbyexample:{PYTHON_VERSION}:{slug}:{code_hash}"
    js_worker_code = _to_js_object(worker_code)
    code_callback = create_once_callable(lambda: js_worker_code)
    worker = env.LOADER.get(worker_id, code_callback)
    entrypoint = worker.getEntrypoint()
    if JsRequest is None:
        return "Dynamic Workers are only available in the Cloudflare runtime."
    dynamic_request = JsRequest.new(str(request.url), _to_js_object({"method": "GET"}))
    try:
        response = python_from_rpc(await entrypoint.fetch(dynamic_request))
        return await response.text()
    finally:
        if hasattr(code_callback, "destroy"):
            try:
                code_callback.destroy()
            except Exception:
                pass


@app.get("/{path:path}")
async def not_found(path: str, request: Request):
    response = route(str(request.url), method="GET")
    return _html(response.body, response.status)


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        global _CURRENT_WORKER_REQUEST
        _CURRENT_WORKER_REQUEST = request

        # Cache static GET responses at the Worker edge. Edited example runs are
        # POST requests and are intentionally never cached.
        if getattr(request, "method", None) == "GET" and caches is not None:
            if should_cache_get_url(getattr(request, "url", "")):
                cache_key = JsRequest.new(html_cache_key_url(getattr(request, "url", "")), _to_js_object({"method": "GET"}))
                cached = await caches.default.match(cache_key)
                if cached:
                    return cached
                response = await asgi.fetch(app, request.js_object, self.env)
                if getattr(response, "status", 200) == 200:
                    response.headers.set("Cache-Control", "public, max-age=300, stale-while-revalidate=86400")
                    await caches.default.put(cache_key, response.clone())
                return response
            response = await asgi.fetch(app, request.js_object, self.env)
            response.headers.set("Cache-Control", "no-store")
            return response

        return await asgi.fetch(app, request.js_object, self.env)
