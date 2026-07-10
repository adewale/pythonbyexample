import hashlib
import hmac
import json
import time
from urllib.parse import parse_qs, urlencode, urlparse

from fastapi import FastAPI, Request
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, Response
from starlette.exceptions import HTTPException as StarletteHTTPException
from workers import WorkerEntrypoint, python_from_rpc

from app import (
    FAVICON_SVG,
    JOURNEYS_BY_SLUG,
    build_dynamic_worker_code,
    get_example,
    render_cell_output_flow_option,
    render_example_not_found,
    render_example_page,
    render_home,
    render_journey_not_found,
    render_journey_page,
    render_journeys_index,
    render_mobile_run_first_option,
    render_not_found,
    render_sitemap,
)
from asset_manifest import HTML_CACHE_VERSION
from examples import PYTHON_VERSION
from security import CONTENT_SECURITY_POLICY, STRICT_TRANSPORT_SECURITY

import observability
import worker_asgi_bridge as asgi

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
SMOKE_BYPASS_HEADER = "x-pythonbyexample-smoke-secret"
TURNSTILE_CLEARANCE_COOKIE = "pbe_turnstile_clearance"
DEFAULT_TURNSTILE_CLEARANCE_SECONDS = 60 * 60 * 8
# Generous ceiling for an edited example program (the largest curated
# program is well under 4 KB). Bounds the bytes we hash, embed in a
# Dynamic Worker module, and echo back into the page.
MAX_SUBMITTED_BODY_BYTES = 100_000

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
app.add_middleware(observability.WideEventMiddleware)


def _to_js_object(value):
    if to_js is None or Object is None:
        return value
    return to_js(value, dict_converter=Object.fromEntries)


def _html(body, status=200):
    return HTMLResponse(body, status_code=status, headers={"Content-Type": "text/html; charset=utf-8"})


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


def should_cache_get_url(url: str) -> bool:
    path = urlparse(url).path
    return not path.startswith("/layout-options/")


# Static assets get the same set from public/_headers; Worker-rendered
# HTML needs them applied here. frame-ancestors 'none' (plus the legacy
# X-Frame-Options) keeps the Run button out of clickjacking frames.
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Frame-Options": "DENY",
    "Strict-Transport-Security": STRICT_TRANSPORT_SECURITY,
    "Content-Security-Policy": CONTENT_SECURITY_POLICY,
}


def _apply_security_headers(response) -> None:
    headers = getattr(response, "headers", None)
    if headers is None:
        return
    for name, value in SECURITY_HEADERS.items():
        headers.set(name, value)


def html_cache_key_url(url: str, turnstile_site_key: str = "") -> str:
    parsed = urlparse(url)
    # Routes ignore ordinary query strings, so the Worker cache key must ignore
    # them too. This prevents tracking or cache-busting parameters from creating
    # unbounded copies of identical HTML.
    base_url = parsed._replace(path=parsed.path or "/", params="", query="", fragment="").geturl()
    turnstile_fragment = ""
    if turnstile_site_key:
        digest = hashlib.sha256(turnstile_site_key.encode("utf-8")).hexdigest()[:8]
        turnstile_fragment = f"&__turnstile={digest}"
    return f"{base_url}?__html_v={HTML_CACHE_VERSION}{turnstile_fragment}"


@app.get("/favicon.svg")
async def favicon():
    return Response(FAVICON_SVG, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=31536000, immutable"})


@app.get("/", response_class=HTMLResponse)
async def home():
    return _html(render_home())


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
    supplied = request.headers.get(SMOKE_BYPASS_HEADER, "")
    return bool(bypass_secret) and hmac.compare_digest(supplied, bypass_secret)


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
    if mode == "off":
        return False
    # Any other value — including a typo of "session" — fails closed and
    # requires the challenge rather than silently disabling protection.
    return not _clearance_valid(request)


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


@app.get("/layout-options/mobile-run-first", response_class=HTMLResponse)
async def mobile_run_first_option():
    return _html(render_mobile_run_first_option(get_example("values")))


@app.get("/layout-options/cell-output-flow", response_class=HTMLResponse)
async def cell_output_flow_option():
    return _html(render_cell_output_flow_option(get_example("values")))


@app.get("/journeys", response_class=HTMLResponse)
async def journeys_index():
    return _html(render_journeys_index())


@app.get("/journeys/{slug}", response_class=HTMLResponse)
async def journey_page(slug: str):
    journey = JOURNEYS_BY_SLUG.get(slug)
    if journey is None:
        return _html(render_journey_not_found(), 404)
    return _html(render_journey_page(journey))


@app.get("/examples/{slug}", response_class=HTMLResponse)
async def example_page(slug: str, request: Request):
    example = get_example(slug)
    if example is None:
        return _html(render_example_not_found(slug), 404)
    return _html(render_example_page(example, turnstile_site_key=_turnstile_site_key(request)))


@app.post("/examples/{slug}", response_class=HTMLResponse)
async def run_example(slug: str, request: Request):
    example = get_example(slug)
    if example is None:
        return _html("<h1>Example not found</h1>", 404)
    raw_body = await request.body()
    if len(raw_body) > MAX_SUBMITTED_BODY_BYTES:
        if event := _wide_event(request):
            event["example"] = {"slug": example["slug"], "code_bytes": len(raw_body), "rejected": "too_large"}
        return _html(
            render_example_page(
                example,
                output=f"Submitted code is too large (over {MAX_SUBMITTED_BODY_BYTES // 1000} kB). Trim it and run again.",
                turnstile_site_key=_turnstile_site_key(request),
            ),
            413,
        )
    body = raw_body.decode("utf-8")
    form = parse_qs(body)
    submitted = form.get("code", [example["code"]])[0]
    submitted_bytes = submitted.encode("utf-8")
    if event := _wide_event(request):
        event["example"] = {
            "slug": example["slug"],
            "code_hash": hashlib.sha256(submitted_bytes).hexdigest()[:12],
            "code_bytes": len(submitted_bytes),
            "code_edited": submitted != example["code"],
        }
    turnstile_token = form.get("cf-turnstile-response", [""])[0]
    needs_turnstile = _requires_turnstile(request)
    turnstile_verified = False

    if needs_turnstile and not turnstile_token:
        if event := _wide_event(request):
            event["turnstile"] = {"outcome": "fail"}
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

    if needs_turnstile:
        ok, message, turnstile_outcome = await _verify_turnstile(request, turnstile_token)
        if event := _wide_event(request):
            event["turnstile"] = {"outcome": turnstile_outcome}
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
    elif event := _wide_event(request):
        event["turnstile"] = {"outcome": _turnstile_not_required_outcome(request)}

    started = time.perf_counter()
    try:
        output = await _run_example(request, example["slug"], submitted)
    finally:
        elapsed_ms = (time.perf_counter() - started) * 1000
        if event := _wide_event(request):
            event["execution_ms"] = round(elapsed_ms, 2)
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


def _turnstile_not_required_outcome(request: Request) -> str:
    if not _turnstile_secret(request) or _turnstile_challenge_mode(request) == "off":
        return "disabled"
    if _smoke_bypass_ok(request):
        return "bypass"
    if _clearance_valid(request):
        return "pass"
    return "disabled"


async def _verify_turnstile(request: Request, token: str) -> tuple[bool, str, str]:
    secret = _turnstile_secret(request)
    if not secret:
        return True, "", "disabled"

    if _smoke_bypass_ok(request):
        return True, "", "bypass"

    if not token:
        return False, "Turnstile verification is required before running edited code. Please retry.", "fail"
    if js_fetch is None or JsRequest is None:
        return False, "Turnstile verification is unavailable outside the Cloudflare runtime.", "fail"

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
        return True, "", "pass"
    return False, "Turnstile verification failed. Please refresh the challenge and try again.", "fail"


async def _run_example(request: Request, slug, code):
    event = _wide_event(request)
    if event is None:
        event = {}
    worker_event = event.setdefault("worker", {})
    if JsRequest is None or create_once_callable is None:
        worker_event["outcome"] = "runtime_unavailable"
        return "Dynamic Workers are only available in the Cloudflare runtime."

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
    code_callback = None
    code_callback_used = False
    try:
        env = request.scope["env"]
        code_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()
        worker_id = f"pythonbyexample:{PYTHON_VERSION}:{slug}:{code_hash}"
        js_worker_code = _to_js_object(worker_code)

        def provide_worker_code():
            nonlocal code_callback_used
            code_callback_used = True
            return js_worker_code

        code_callback = create_once_callable(provide_worker_code)
        worker = env.LOADER.get(worker_id, code_callback)
        entrypoint = worker.getEntrypoint()
        dynamic_request = JsRequest.new(
            str(request.url),
            _to_js_object(
                {
                    "method": "GET",
                    "headers": {"x-request-id": event.get("request_id", "")},
                }
            ),
        )
        response = python_from_rpc(await entrypoint.fetch(dynamic_request))
        status_code = int(getattr(response, "status", 200) or 200)
        worker_event["status_code"] = status_code
        output = await response.text()
        if status_code >= 500:
            worker_event["outcome"] = "error"
            worker_event["error"] = {
                "type": "DynamicWorkerHTTPError",
                "message": f"Dynamic Worker returned HTTP {status_code}",
            }
            event["level"] = "error"
        else:
            worker_event["outcome"] = "success"
        return output
    except Exception as exc:
        worker_event["outcome"] = "error"
        worker_event["error"] = observability.error_dict(exc)
        event["level"] = "error"
        raise
    finally:
        # create_once_callable destroys itself after the Dynamic Loader invokes it.
        # Destroy only unused callbacks, such as cache-hit callbacks, to avoid
        # false cleanup errors like "OnceProxy has already been destroyed".
        if code_callback is not None and not code_callback_used and hasattr(code_callback, "destroy"):
            try:
                code_callback.destroy()
            except Exception as exc:
                worker_event["cleanup_error"] = observability.error_dict(exc)
                event["level"] = "error"


@app.get("/{path:path}")
async def not_found(path: str, request: Request):
    # FastAPI dispatches the explicit routes above in production. Keep these
    # fallbacks for direct Worker calls to the catch-all as well.
    if path == "sitemap.xml":
        return Response(
            render_sitemap(),
            headers={"Content-Type": "application/xml; charset=utf-8"},
        )
    if path == "journeys":
        return _html(render_journeys_index())
    if path.startswith("journeys/"):
        journey = JOURNEYS_BY_SLUG.get(path.removeprefix("journeys/"))
        if journey is not None:
            return _html(render_journey_page(journey))
        return _html(render_journey_not_found(), 404)
    return _html(render_not_found(), 404)


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
            # Cache static GET responses at the Worker edge. Edited example runs are
            # POST requests and are intentionally never cached.
            if getattr(request, "method", None) == "GET" and caches is not None:
                if should_cache_get_url(getattr(request, "url", "")):
                    event["cache"] = "miss"
                    turnstile_site_key = getattr(self.env, "TURNSTILE_SITE_KEY", "")
                    cache_key = JsRequest.new(
                        html_cache_key_url(getattr(request, "url", ""), turnstile_site_key),
                        _to_js_object({"method": "GET"}),
                    )
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
                        max_body_bytes=MAX_SUBMITTED_BODY_BYTES,
                    )
                    _apply_security_headers(response)
                    if getattr(response, "status", 200) == 200:
                        response.headers.set(
                            "Cache-Control",
                            "public, max-age=300, stale-while-revalidate=86400",
                        )
                        await caches.default.put(cache_key, response.clone())
                    else:
                        # Error pages must not linger in browser heuristic caches.
                        response.headers.set("Cache-Control", "no-store")
                    return response
                event["cache"] = "bypass"
                response = await asgi.fetch(
                    app,
                    asgi_request,
                    self.env,
                    state={"wide_event": event},
                    max_body_bytes=MAX_SUBMITTED_BODY_BYTES,
                )
                _apply_security_headers(response)
                response.headers.set("Cache-Control", "no-store")
                return response

            event["cache"] = "bypass"
            response = await asgi.fetch(
                app,
                asgi_request,
                self.env,
                state={"wide_event": event},
                max_body_bytes=MAX_SUBMITTED_BODY_BYTES,
            )
            _apply_security_headers(response)
            return response
        except Exception as exc:
            event["status_code"] = 500
            event["outcome"] = "error"
            event["level"] = "error"
            event.setdefault("error", observability.error_dict(exc))
            raise
        finally:
            event["duration_ms"] = round((time.perf_counter() - started) * 1000, 2)
            observability.emit(event, env=self.env)
