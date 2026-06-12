"""Shared browser security constants for Worker-rendered and static HTML."""

# The inline runner scripts are curated application code. They carry this
# nonce so script-src can avoid unsafe-inline while still serving cached HTML.
CSP_SCRIPT_NONCE = "pbe-inline-v1"
STRICT_TRANSPORT_SECURITY = "max-age=31536000; includeSubDomains; preload"

CONTENT_SECURITY_POLICY = "; ".join(
    [
        "default-src 'self'",
        "base-uri 'none'",
        "object-src 'none'",
        "frame-ancestors 'none'",
        "form-action 'self'",
        "img-src 'self' data:",
        "font-src 'self'",
        # CodeMirror injects style elements and Shiki emits style attributes.
        # Keep script execution strict while allowing those rendering styles.
        "style-src 'self' 'unsafe-inline'",
        (
            "script-src 'self' "
            f"'nonce-{CSP_SCRIPT_NONCE}' "
            "https://esm.sh https://challenges.cloudflare.com 'wasm-unsafe-eval'"
        ),
        "script-src-attr 'none'",
        "connect-src 'self' https://esm.sh https://challenges.cloudflare.com",
        "frame-src https://challenges.cloudflare.com",
        "worker-src 'self'",
    ]
)
