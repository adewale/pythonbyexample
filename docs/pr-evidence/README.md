# PR visual evidence

## Diagram upgrade (2026-09-27)

Before/after contact sheet of every figure whose drawing changed on the
`claude/diagram-upgrade` branch relative to `main`, in both colour schemes.
The base column in the dark sheet sits on the light paper chip the site used
to draw; the head column is recoloured through the `--fig-*` tokens.

| Evidence | Review point | Base | SHA-256 |
| --- | --- | --- | --- |
| [Light contact sheet](diagram-upgrade-contact-sheet-light.png) | 21 changed figure rows: 7 redraws, 10 arrow or accent fixes, 4 demotions, with element counts and shipped captions. | `main` (`3f300af`) | `a189ab1a94242b392d84ade8caa9ae6a43b0cfb3852fc6bbb5f3c8aecb2167f5` |
| [Dark contact sheet](diagram-upgrade-contact-sheet-dark.png) | The same rows under `prefers-color-scheme: dark`: paper chip before, token recolouring after. | `main` (`3f300af`) | `33f6cc23b4a1595f2626d8a34ce77343c90bf39aeb528c7482d7d14fb4e3e2b4` |

Regenerate both from the branch with:

```bash
uv run --python 3.13 scripts/build_figure_contact_sheet.py --base main \
    --output docs/pr-evidence/diagram-upgrade-contact-sheet
```

The script extracts the base revision with `git archive`, renders every attached
figure from both trees, ignores colour, font and text-length attributes when
deciding what changed, and captures the sheet through
`scripts/capture_browser_screenshot.mjs`.

## Audit remediation (2026-07-10)

These captures isolate the dark-mode Run-button contrast correction on the same `/examples/values` runner at a 1200×900 desktop viewport.

| Evidence | Review point | Commit | SHA-256 |
| --- | --- | --- | --- |
| [Before](audit-remediation-before-runner-dark.png) | The prior light text on the orange Run button measured 2.19:1 contrast. | `46000c7` (`origin/main`) | `4f15bc0d6f2c965197265bff2f6b300aee5a7a32e4ef152001aeb6c8d290e860` |
| [After](audit-remediation-after-runner-dark.png) | Dark action text raises measured contrast to 7.87:1 while preserving the runner layout. | `audit-remediation-2026-07-10` | `53882092e58e02bbe323c5ed70e0d1c491f1e8e9f6887416b7ec83222ad305cc` |

Reproduce each capture by serving the corresponding revision, then run:

```bash
TARGET_URL=http://127.0.0.1:<port>/examples/values \
CAPTURE_SELECTOR=.runner-grid WIDTH=1200 HEIGHT=900 COLOR_SCHEME=dark \
OUTPUT=<output>.png node scripts/capture_browser_screenshot.mjs
```

`make browser-layout-test` independently calculates the rendered button contrast and fails below 4.5:1.

## PR #6 evidence

These artifacts provide reviewable evidence for the runner, journey-page, and social-card changes.

| Evidence | Review point | Commit | SHA-256 |
| --- | --- | --- | --- |
| [Runner before](pr-6-before-runner.png) | `/examples/values` uses the prior bright `#FF4801` Run control. | `b61edf1` (`origin/main`) | `be773336d14f1b819ade1a22f6308573b5e26148ec37b322f73ad1d2de232b34` |
| [Runner after](pr-6-after-runner.png) | The same runner keeps its editor/output layout while using the WCAG-AA `#C83800` action color. | `742ae7d` | `281db8bb44daa94af2d99b689b1177fb21427b0051679a3e1de3a56bc4831b04` |
| [Runtime journey page](pr-6-journey-runtime.png) | `/journeys/runtime` renders its overview, first learning outcome, figure, and linked examples at a 1200×1260 desktop viewport. | `a85bbf7` | `eb1db35d5ff7fc7974ad3a3891b694aaa5f8f277ba291b94a24c62767340e04d` |
| [`/journeys` social card](../../public/og/journeys.jpg) | The exact 1200×630 JPEG referenced by the `/journeys` `og:image` tag. | `a85bbf7` | `3042997bb2b3acd9e2ab74106f5b4d3d4c58dafcfe23f1ddc548ed39e4548a3c` |

`public/og/journeys.jpg` is a tracked PR artifact and its deterministic HTML input is recorded in `public/og/manifest.json`. `make check-social-cards` verifies its provenance, the exact 120-card JPEG set, and each card's JPEG decodability and 1200×630 dimensions.

Regenerate each page with its commit checked out, serve the rendered `/examples/values` HTML plus `public/` on a local HTTP server, then run:

```bash
TARGET_URL=http://127.0.0.1:<port>/examples/values/ \
CAPTURE_SELECTOR=.playground WIDTH=1200 HEIGHT=900 \
OUTPUT=<output>.png node scripts/capture_browser_screenshot.mjs
```

The captures use the repository's headless-Chrome script; it waits for the selected element and writes the selector's rendered bounding box.

## TODO

- [ ] Add an executable base/head capture wrapper that creates pinned worktrees, installs dependencies, starts each local Worker on a fixed port, waits for readiness, captures the documented URL/viewport/selector, and records SHA-256 hashes. Keep it reviewer tooling rather than a pixel-comparison CI gate so platform font/rasterization differences do not make Verify flaky.
