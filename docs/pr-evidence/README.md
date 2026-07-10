# PR #6 visual evidence

These captures show `/examples/values` at a 1200×900 desktop viewport, clipped to the `.playground` runner. The review point is the Run control: the PR changes its action color from `#FF4801` to the WCAG-AA `#C83800` while preserving the editor/output layout.

| Capture | Commit | SHA-256 |
| --- | --- | --- |
| [Before](pr-6-before-runner.png) | `b61edf1` (`origin/main`) | `be773336d14f1b819ade1a22f6308573b5e26148ec37b322f73ad1d2de232b34` |
| [After](pr-6-after-runner.png) | `742ae7d` | `281db8bb44daa94af2d99b689b1177fb21427b0051679a3e1de3a56bc4831b04` |

Regenerate each page with its commit checked out, serve the rendered `/examples/values` HTML plus `public/` on a local HTTP server, then run:

```bash
TARGET_URL=http://127.0.0.1:<port>/examples/values/ \
CAPTURE_SELECTOR=.playground WIDTH=1200 HEIGHT=900 \
OUTPUT=<output>.png node scripts/capture_browser_screenshot.mjs
```

The captures use the repository's headless-Chrome script; it waits for the selected element and writes the selector's rendered bounding box.
