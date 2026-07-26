"""Shared browser security constants for Worker-rendered and static HTML."""

STRICT_TRANSPORT_SECURITY = "max-age=31536000; includeSubDomains; preload"

CONTENT_SECURITY_POLICY = "default-src 'self'; base-uri 'none'; object-src 'none'; frame-ancestors 'none'; form-action 'self'; img-src 'self' data:; font-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' https://esm.sh https://challenges.cloudflare.com 'wasm-unsafe-eval'; script-src-attr 'none'; connect-src 'self' https://esm.sh https://challenges.cloudflare.com; frame-src https://challenges.cloudflare.com; worker-src 'self'"
