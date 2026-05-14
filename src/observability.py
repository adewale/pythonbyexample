from __future__ import annotations

import json
import re
import sys
import time
import uuid
from urllib.parse import urlparse

try:
    from asset_manifest import HTML_CACHE_VERSION
except ImportError:  # Imported as src.observability in local tests.
    try:
        from src.asset_manifest import HTML_CACHE_VERSION
    except ImportError:  # pragma: no cover - only for isolated editor tooling.
        HTML_CACHE_VERSION = ""

try:
    from js import Object, console
    from pyodide.ffi import to_js
except ImportError:  # Allows local tests/editor tooling outside Workers.
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
_MAX_COUNTRY_CHARS = 8
_MAX_REQUEST_ID_CHARS = 128
_MAX_SAFE_COLLECTION_ITEMS = 20
_REQUEST_ID_RE = re.compile(r"^[!-~]+$")
_URL_QUERY_RE = re.compile(r"\b(https?://[^\s?#]+)\?[^\s\"'<>]+")
_SENSITIVE_KV_RE = re.compile(
    r"(?i)\b(authorization|cf-connecting-ip|cf-turnstile-response|code|cookie|password|"
    r"remoteip|secret|token|turnstile[_-]?token)=([^&\s]+)"
)
_SAFE_HTTP_DETAIL_STRINGS = {
    "Bad Request",
    "Forbidden",
    "Internal Server Error",
    "Method Not Allowed",
    "Not Found",
    "Unauthorized",
}


def new_request_id() -> str:
    return uuid.uuid4().hex


def _text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (bool, int, float)):
        return str(value)
    return ""


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
    value = value.replace("\r", " ").replace("\n", " ")
    value = _URL_QUERY_RE.sub(r"\1?<redacted>", value)
    value = _SENSITIVE_KV_RE.sub(lambda match: f"{match.group(1)}=<redacted>", value)
    if len(value) > max_chars:
        return f"{value[:max_chars]}…"
    return value


def _safe_json_value(value, *, depth: int = 0):
    if depth > 4:
        return {"type": type(value).__name__}
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return _redact_sensitive_text(value, max_chars=_MAX_SAFE_STRING_CHARS)
    if isinstance(value, (bytes, bytearray, memoryview)):
        return {"type": type(value).__name__, "length": len(value)}
    if isinstance(value, (list, tuple)):
        safe_items = [
            _safe_json_value(item, depth=depth + 1)
            for item in list(value)[:_MAX_SAFE_COLLECTION_ITEMS]
        ]
        if len(value) > _MAX_SAFE_COLLECTION_ITEMS:
            safe_items.append({"type": "truncated", "omitted": len(value) - _MAX_SAFE_COLLECTION_ITEMS})
        return safe_items
    if isinstance(value, dict):
        safe_dict = {}
        items = list(value.items())
        for key, item in items[:_MAX_SAFE_COLLECTION_ITEMS]:
            key_text = _redact_sensitive_text(str(key), max_chars=64)
            safe_dict[key_text] = _safe_json_value(item, depth=depth + 1)
        if len(items) > _MAX_SAFE_COLLECTION_ITEMS:
            safe_dict["__truncated__"] = len(items) - _MAX_SAFE_COLLECTION_ITEMS
        return safe_dict
    return {"type": type(value).__name__}


def error_dict(exc: Exception) -> dict:
    return {
        "type": type(exc).__name__,
        "message": _redact_sensitive_text(str(exc), max_chars=_MAX_ERROR_MESSAGE_CHARS),
    }


def safe_validation_errors(exc) -> list[dict]:
    try:
        raw_errors = exc.errors()
    except Exception:
        return [{"type": type(exc).__name__}]

    errors = []
    for error in raw_errors[:_MAX_SAFE_COLLECTION_ITEMS]:
        errors.append(
            {
                str(key): _safe_json_value(value)
                for key, value in error.items()
                if key not in {"ctx", "input"}
            }
        )
    if len(raw_errors) > _MAX_SAFE_COLLECTION_ITEMS:
        errors.append({"type": "truncated", "omitted": len(raw_errors) - _MAX_SAFE_COLLECTION_ITEMS})
    return errors


def safe_http_detail(detail):
    if isinstance(detail, str):
        if detail in _SAFE_HTTP_DETAIL_STRINGS:
            return detail
        return {"type": "str", "length": len(detail)}
    if detail is None or isinstance(detail, (bool, int, float)):
        return detail
    return {"type": type(detail).__name__}


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
        # Observability must never mask the request result. Fall back to a JSON line.
        pass

    stream = sys.stderr if payload["level"] == "error" else sys.stdout
    try:
        print(json.dumps(payload, default=str), file=stream)
    except Exception:
        pass


def _decode_header_part(value) -> str:
    if isinstance(value, bytes):
        return value.decode("latin-1")
    if isinstance(value, str):
        return value
    return str(value)


def header_value(headers, name: str) -> str | None:
    wanted = name.lower()
    if headers is None:
        return None

    get = getattr(headers, "get", None)
    if callable(get):
        for candidate in (name, wanted, name.title()):
            try:
                value = get(candidate)
            except Exception:
                continue
            if value is not None:
                return _decode_header_part(value)

    items = getattr(headers, "items", None)
    try:
        iterable = items() if callable(items) else headers
        for key, value in iterable:
            if _decode_header_part(key).lower() == wanted:
                return _decode_header_part(value)
    except Exception:
        return None
    return None


def _safe_header_token(value: str | None, *, max_chars: int) -> str | None:
    if value is None:
        return None
    value = value.strip()
    if not value or len(value) > max_chars:
        return None
    if not _REQUEST_ID_RE.fullmatch(value):
        return None
    return value


def safe_request_id(value: str | None) -> str | None:
    return _safe_header_token(value, max_chars=_MAX_REQUEST_ID_CHARS)


def _mapping_or_attr_value(value, key: str):
    if value is None:
        return None
    get = getattr(value, "get", None)
    if callable(get):
        try:
            found = get(key)
        except Exception:
            found = None
        if found is not None:
            return found
    try:
        return getattr(value, key)
    except Exception:
        return None


def cf_context(headers, cf=None) -> dict:
    ray = _safe_header_token(header_value(headers, "cf-ray"), max_chars=_MAX_HEADER_CHARS)
    country = _safe_header_token(
        _text(_mapping_or_attr_value(cf, "country")) or header_value(headers, "cf-ipcountry"),
        max_chars=_MAX_COUNTRY_CHARS,
    )
    colo = _safe_header_token(_text(_mapping_or_attr_value(cf, "colo")), max_chars=_MAX_HEADER_CHARS)
    if colo is None and ray and "-" in ray:
        colo = _safe_header_token(ray.rsplit("-", 1)[-1], max_chars=_MAX_HEADER_CHARS)
    return {"ray": ray, "colo": colo, "country": country}


def _request_id_from_headers(headers) -> str:
    return (
        safe_request_id(header_value(headers, "x-request-id"))
        or safe_request_id(header_value(headers, "cf-ray"))
        or new_request_id()
    )


def _path_from_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed.path or "/"


def _fallback_cache_mode(method: str, path: str) -> str:
    if method.upper() != "GET":
        return "bypass"
    if path.startswith("/layout-options/"):
        return "bypass"
    return "miss"


def event_from_worker_request(request, *, cache: str, html_cache_version=HTML_CACHE_VERSION) -> dict:
    headers = getattr(request, "headers", None)
    method = _text(getattr(request, "method", "")) or ""
    url = _text(getattr(request, "url", "")) or ""
    cf = _mapping_or_attr_value(request, "cf") or _mapping_or_attr_value(
        _mapping_or_attr_value(request, "js_object"), "cf"
    )
    return {
        "request_id": _request_id_from_headers(headers),
        "method": method,
        "path": _path_from_url(url),
        "cf": cf_context(headers, cf=cf),
        "cache": cache,
        "html_cache_version": html_cache_version,
    }


def event_from_scope(scope, *, cache: str | None = None, html_cache_version=HTML_CACHE_VERSION) -> dict:
    headers = scope.get("headers")
    method = _text(scope.get("method", "")) or ""
    path = _text(scope.get("path", "")) or "/"
    return {
        "request_id": _request_id_from_headers(headers),
        "method": method,
        "path": path,
        "cf": cf_context(headers),
        "cache": cache or _fallback_cache_mode(method, path),
        "html_cache_version": html_cache_version,
    }


def record_status(event: dict, status_code: int) -> None:
    try:
        status_code = int(status_code)
    except Exception:
        status_code = 500
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


class WideEventMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        state = scope.setdefault("state", {})
        owns_event = "wide_event" not in state
        event = state.setdefault("wide_event", event_from_scope(scope))
        started = time.perf_counter()
        status_holder = {"code": 500}

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                status_holder["code"] = message["status"]
            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
            record_status(event, status_holder["code"])
        except Exception as exc:
            event["status_code"] = 500
            event["outcome"] = "error"
            event["level"] = "error"
            event["error"] = error_dict(exc)
            raise
        finally:
            event["app_duration_ms"] = round((time.perf_counter() - started) * 1000, 2)
            if owns_event:
                event["duration_ms"] = event["app_duration_ms"]
                emit(event, env=scope.get("env"))
