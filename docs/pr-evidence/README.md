# PR #6 visual evidence

These artifacts provide reviewable evidence for the runner, journey-page, and social-card changes.

| Evidence | Review point | Commit | SHA-256 |
| --- | --- | --- | --- |
| [Runner before](pr-6-before-runner.png) | `/examples/values` uses the prior bright `#FF4801` Run control. | `b61edf1` (`origin/main`) | `be773336d14f1b819ade1a22f6308573b5e26148ec37b322f73ad1d2de232b34` |
| [Runner after](pr-6-after-runner.png) | The same runner keeps its editor/output layout while using the WCAG-AA `#C83800` action color. | `742ae7d` | `281db8bb44daa94af2d99b689b1177fb21427b0051679a3e1de3a56bc4831b04` |
| [Runtime journey page](pr-6-journey-runtime.png) | `/journeys/runtime` renders its overview, first learning outcome, figure, and linked examples at a 1200×1260 desktop viewport. | `a85bbf7` | `eb1db35d5ff7fc7974ad3a3891b694aaa5f8f277ba291b94a24c62767340e04d` |
| [`/journeys` social card](../../public/og/journeys.jpg) | The exact 1200×630 JPEG referenced by the `/journeys` `og:image` tag. | `a85bbf7` | `3042997bb2b3acd9e2ab74106f5b4d3d4c58dafcfe23f1ddc548ed39e4548a3c` |

`public/og/journeys.jpg` is a tracked PR artifact and its deterministic HTML input is recorded in `public/og/manifest.json`. `make check-social-cards` verifies both its provenance and the exact 118-card JPEG set.

Regenerate each page with its commit checked out, serve the rendered `/examples/values` HTML plus `public/` on a local HTTP server, then run:

```bash
TARGET_URL=http://127.0.0.1:<port>/examples/values/ \
CAPTURE_SELECTOR=.playground WIDTH=1200 HEIGHT=900 \
OUTPUT=<output>.png node scripts/capture_browser_screenshot.mjs
```

The captures use the repository's headless-Chrome script; it waits for the selected element and writes the selector's rendered bounding box.

## TODO

- [ ] Add an executable base/head capture wrapper that creates pinned worktrees, installs dependencies, starts each local Worker on a fixed port, waits for readiness, captures the documented URL/viewport/selector, and records SHA-256 hashes. Keep it reviewer tooling rather than a pixel-comparison CI gate so platform font/rasterization differences do not make Verify flaky.
