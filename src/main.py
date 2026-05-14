import hashlib
import hmac
import json
import time
from urllib.parse import parse_qs, urlencode, urlparse

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from workers import WorkerEntrypoint, python_from_rpc

from app import FAVICON_SVG, build_dynamic_worker_code, get_example, render_example_page, route
from asset_manifest import HTML_CACHE_VERSION
from examples import PYTHON_VERSION

import worker_asgi_bridge as asgi

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
SMOKE_BYPASS_HEADER = "x-pythonbyexample-smoke-secret"
TURNSTILE_CLEARANCE_COOKIE = "pbe_turnstile_clearance"
DEFAULT_TURNSTILE_CLEARANCE_SECONDS = 60 * 60 * 8

try:
    from js import Object, Request as JsRequest, caches, fetch as js_fetch
    from pyodide.ffi import create_once_callable, jsnull, to_js
except ImportError:  # Allows editor tooling outside Workers.
    Object = None
    JsRequest = None
    jsnull = None
    create_once_callable = None
    to_js = None
    caches = None
    js_fetch = None

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


def html_cache_key_url(url: str, turnstile_site_key: str = "") -> str:
    separator = "&" if "?" in url else "?"
    turnstile_fragment = ""
    if turnstile_site_key:
        digest = hashlib.sha256(turnstile_site_key.encode("utf-8")).hexdigest()[:8]
        turnstile_fragment = f"&__turnstile={digest}"
    return f"{url}{separator}__html_v={HTML_CACHE_VERSION}{turnstile_fragment}"


@app.get("/favicon.svg")
async def favicon():
    return Response(FAVICON_SVG, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=31536000, immutable"})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    response = route(str(request.url), method="GET")
    return _html(response.body, response.status)


def _env_text(request: Request, name: str) -> str:
    env = request.scope.get("env")
    value = getattr(env, name, "") if env is not None else ""
    return value if isinstance(value, str) else ""


def _turnstile_site_key(request: Request) -> str:
    return _env_text(request, "TURNSTILE_SITE_KEY")


def _turnstile_secret(request: Request) -> str:
    return _env_text(request, "TURNSTILE_SECRET_KEY")


def _turnstile_clearance_secret(request: Request) -> str:
    return _env_text(request, "TURNSTILE_CLEARANCE_SECRET") or _turnstile_secret(request)


def _turnstile_challenge_mode(request: Request) -> str:
    return (_env_text(request, "TURNSTILE_CHALLENGE_MODE") or "off").lower()


def _turnstile_clearance_seconds(request: Request) -> int:
    raw = _env_text(request, "TURNSTILE_CLEARANCE_SECONDS")
    try:
        return max(60, min(int(raw), 60 * 60 * 24 * 7)) if raw else DEFAULT_TURNSTILE_CLEARANCE_SECONDS
    except ValueError:
        return DEFAULT_TURNSTILE_CLEARANCE_SECONDS


def _smoke_bypass_ok(request: Request) -> bool:
    bypass_secret = _env_text(request, "PBE_SMOKE_BYPASS_SECRET")
    return bool(bypass_secret and request.headers.get(SMOKE_BYPASS_HEADER) == bypass_secret)


def _sign_clearance(secret: str, expires: int) -> str:
    payload = str(expires)
    signature = hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{payload}.{signature}"


def _clearance_valid(request: Request) -> bool:
    secret = _turnstile_clearance_secret(request)
    value = request.cookies.get(TURNSTILE_CLEARANCE_COOKIE, "")
    if not secret or not value or "." not in value:
        return False
    expires_text, signature = value.split(".", 1)
    try:
        expires = int(expires_text)
    except ValueError:
        return False
    if expires <= int(time.time()):
        return False
    expected = _sign_clearance(secret, expires).split(".", 1)[1]
    return hmac.compare_digest(signature, expected)


def _requires_turnstile(request: Request) -> bool:
    if not _turnstile_secret(request) or _smoke_bypass_ok(request):
        return False
    mode = _turnstile_challenge_mode(request)
    if mode in {"session", "once", "once-per-session"}:
        return not _clearance_valid(request)
    return False


def _set_turnstile_clearance(response: HTMLResponse, request: Request) -> None:
    secret = _turnstile_clearance_secret(request)
    if not secret:
        return
    max_age = _turnstile_clearance_seconds(request)
    expires = int(time.time()) + max_age
    response.set_cookie(
        TURNSTILE_CLEARANCE_COOKIE,
        _sign_clearance(secret, expires),
        max_age=max_age,
        path="/examples",
        secure=True,
        httponly=True,
        samesite="Lax",
    )


@app.get("/examples/{slug}", response_class=HTMLResponse)
async def example_page(slug: str, request: Request):
    response = route(str(request.url), method="GET", turnstile_site_key=_turnstile_site_key(request))
    return _html(response.body, response.status)


@app.post("/examples/{slug}", response_class=HTMLResponse)
async def run_example(slug: str, request: Request):
    example = get_example(slug)
    if example is None:
        return _html("<h1>Example not found</h1>", 404)
    body = (await request.body()).decode("utf-8")
    form = parse_qs(body)
    submitted = form.get("code", [example["code"]])[0]
    turnstile_token = form.get("cf-turnstile-response", [""])[0]
    needs_turnstile = _requires_turnstile(request)
    if needs_turnstile and not turnstile_token:
        site_key = _turnstile_site_key(request)
        message = "Verification required before running edited code."
        if not site_key:
            message = "Turnstile verification is required, but TURNSTILE_SITE_KEY is not configured."
        return _html(
            render_example_page(
                example,
                output=message,
                code=submitted,
                turnstile_site_key=site_key,
                turnstile_required=bool(site_key),
            )
        )

    turnstile_verified = False
    if needs_turnstile:
        ok, message = await _verify_turnstile(request, turnstile_token)
        if not ok:
            return _html(
                render_example_page(
                    example,
                    output=message,
                    code=submitted,
                    turnstile_site_key=_turnstile_site_key(request),
                    turnstile_required=True,
                )
            )
        turnstile_verified = True
    started = time.perf_counter()
    output = await _run_example(request, example["slug"], submitted)
    elapsed_ms = (time.perf_counter() - started) * 1000
    response = _html(
        render_example_page(
            example,
            output=output,
            code=submitted,
            execution_time_ms=elapsed_ms,
            turnstile_site_key=_turnstile_site_key(request),
        )
    )
    if turnstile_verified:
        _set_turnstile_clearance(response, request)
    return response


async def _verify_turnstile(request: Request, token: str) -> tuple[bool, str]:
    secret = _turnstile_secret(request)
    if not secret:
        return True, ""

    if _smoke_bypass_ok(request):
        return True, ""

    if not token:
        return False, "Turnstile verification is required before running edited code. Please retry."
    if js_fetch is None or JsRequest is None:
        return False, "Turnstile verification is unavailable outside the Cloudflare runtime."

    payload = {"secret": secret, "response": token}
    remote_ip = request.headers.get("CF-Connecting-IP")
    if remote_ip:
        payload["remoteip"] = remote_ip
    verify_request = JsRequest.new(
        TURNSTILE_VERIFY_URL,
        _to_js_object(
            {
                "method": "POST",
                "body": urlencode(payload),
                "headers": {"Content-Type": "application/x-www-form-urlencoded"},
            }
        ),
    )
    response = await js_fetch(verify_request)
    result = json.loads(await response.text())
    if result.get("success") is True:
        return True, ""
    return False, "Turnstile verification failed. Please refresh the challenge and try again."


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
                turnstile_site_key = getattr(self.env, "TURNSTILE_SITE_KEY", "")
                cache_key = JsRequest.new(html_cache_key_url(getattr(request, "url", ""), turnstile_site_key), _to_js_object({"method": "GET"}))
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
