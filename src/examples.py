"""Versioned example catalog for Python By Example."""
from __future__ import annotations

try:
    from .example_loader import load_examples
except ImportError:  # pragma: no cover - Cloudflare imports src as root.
    from example_loader import load_examples

_CATALOG, EXAMPLES = load_examples()
PYTHON_VERSION = _CATALOG.python_version
REFERENCE_URL = f"{_CATALOG.docs_base_url}/"
SLUG_ORDER = _CATALOG.order
EXAMPLES_BY_SLUG = {example["slug"]: example for example in EXAMPLES}
