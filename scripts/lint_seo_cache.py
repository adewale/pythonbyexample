#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.fingerprint_assets import ASSETS, PUBLIC, html_version  # noqa: E402
from src.app import JOURNEYS, SITE_URL, list_examples, render_example_page, render_home, render_journey_page, render_sitemap  # noqa: E402
from src.asset_manifest import ASSET_PATHS, HTML_CACHE_VERSION  # noqa: E402

META_DESCRIPTION_RE = re.compile(r'<meta name="description" content="([^"]+)">')
CANONICAL_RE = re.compile(r'<link rel="canonical" href="([^"]+)">')
OG_URL_RE = re.compile(r'<meta property="og:url" content="([^"]+)">')
HASHED_ASSET_RE = re.compile(r'/(site|syntax-highlight|editor|runner|search)\.[0-9a-f]{12}\.(css|js)')
JSON_LD_RE = re.compile(r'<script type="application/ld\+json">(.+?)</script>', re.S)
OG_IMAGE_RE = re.compile(r'<meta property="og:image" content="([^"]+)">')


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def assert_page_metadata(name: str, html: str, path: str, failures: list[str]) -> None:
    if re.search(r"__[A-Z][A-Z0-9_]+__", html):
        fail(f"{name}: contains unreplaced template placeholder", failures)
    description = META_DESCRIPTION_RE.search(html)
    if not description:
        fail(f"{name}: missing meta description", failures)
    else:
        text = description.group(1)
        if not 80 <= len(text) <= 180:
            fail(f"{name}: meta description length {len(text)} outside 80..180", failures)
    canonical = CANONICAL_RE.search(html)
    expected_url = f"{SITE_URL}{path}"
    if not canonical or canonical.group(1) != expected_url:
        fail(f"{name}: canonical URL is {canonical.group(1) if canonical else None}, expected {expected_url}", failures)
    og_url = OG_URL_RE.search(html)
    if not og_url or og_url.group(1) != expected_url:
        fail(f"{name}: og:url is {og_url.group(1) if og_url else None}, expected {expected_url}", failures)
    if '/site.css' in html or '/syntax-highlight.js' in html or '/editor.js' in html or '/runner.js' in html:
        fail(f"{name}: references unfingerprinted CSS/JS asset", failures)
    if len(HASHED_ASSET_RE.findall(html)) < 2:
        fail(f"{name}: missing fingerprinted CSS/JS assets", failures)
    og_image = OG_IMAGE_RE.search(html)
    if not og_image:
        fail(f"{name}: missing og:image social card", failures)
    else:
        image_url = og_image.group(1)
        if not image_url.startswith(f"{SITE_URL}/og/"):
            fail(f"{name}: og:image {image_url} is not a site social card", failures)
        else:
            card = PUBLIC / "og" / image_url.rsplit("/", 1)[1]
            if not card.exists():
                fail(f"{name}: og:image file missing — run `make social-cards` ({card})", failures)
    json_ld = JSON_LD_RE.search(html)
    if not json_ld:
        fail(f"{name}: missing JSON-LD structured data", failures)
    else:
        try:
            data = json.loads(json_ld.group(1).replace("\\u003c", "<").replace("\\u003e", ">").replace("\\u0026", "&"))
        except ValueError:
            fail(f"{name}: JSON-LD is not valid JSON", failures)
        else:
            if data.get("@context") != "https://schema.org":
                fail(f"{name}: JSON-LD missing schema.org context", failures)


def assert_sitemap(failures: list[str]) -> None:
    sitemap = render_sitemap()
    for example in list_examples():
        url = f"{SITE_URL}/examples/{example['slug']}"
        if f"<loc>{url}</loc>" not in sitemap:
            fail(f"sitemap: missing {url}", failures)
    for journey in JOURNEYS:
        url = f"{SITE_URL}/journeys/{journey['slug']}"
        if f"<loc>{url}</loc>" not in sitemap:
            fail(f"sitemap: missing {url}", failures)
    if f"<loc>{SITE_URL}/</loc>" not in sitemap:
        fail("sitemap: missing home URL", failures)
    robots = (ROOT / "public" / "robots.txt").read_text()
    if f"Sitemap: {SITE_URL}/sitemap.xml" not in robots:
        fail("robots.txt: missing Sitemap directive", failures)


def assert_asset_manifest(failures: list[str]) -> None:
    expected_paths = {}
    for key, filename in ASSETS.items():
        digest = hashlib.sha256((PUBLIC / filename).read_bytes()).hexdigest()[:12]
        source = PUBLIC / filename
        expected_paths[key] = f"/{source.stem}.{digest}{source.suffix}"
    if ASSET_PATHS != expected_paths:
        fail(f"asset manifest paths stale: {ASSET_PATHS!r} != {expected_paths!r}", failures)
    for path in ASSET_PATHS.values():
        if not (PUBLIC / path.lstrip("/")).exists():
            fail(f"fingerprinted asset missing from public/: {path}", failures)
    expected_html_version = html_version(ASSET_PATHS)
    if HTML_CACHE_VERSION != expected_html_version:
        fail(f"HTML_CACHE_VERSION stale: {HTML_CACHE_VERSION} != {expected_html_version}", failures)


def assert_worker_cache_policy(failures: list[str]) -> None:
    source = (ROOT / "src" / "main.py").read_text()
    required = [
        "def html_cache_key_url(url: str, turnstile_site_key: str = \"\") -> str:",
        "__html_v={HTML_CACHE_VERSION}",
        "caches.default.match(cache_key)",
        "caches.default.put(cache_key, response.clone())",
        "return not path.startswith(\"/layout-options/\")",
        "Cache-Control\", \"no-store",
    ]
    for needle in required:
        if needle not in source:
            fail(f"worker cache policy missing {needle!r}", failures)


def main() -> int:
    failures: list[str] = []
    assert_asset_manifest(failures)
    assert_worker_cache_policy(failures)
    assert_sitemap(failures)
    assert_page_metadata("home", render_home(), "/", failures)
    for example in list_examples():
        assert_page_metadata(
            f"example:{example['slug']}",
            render_example_page(example),
            f"/examples/{example['slug']}",
            failures,
        )
    for journey in JOURNEYS:
        assert_page_metadata(
            f"journey:{journey['slug']}",
            render_journey_page(journey),
            f"/journeys/{journey['slug']}",
            failures,
        )
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"SEO/cache lint passed for 1 home page, {len(JOURNEYS)} journeys, and {len(list_examples())} example pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
