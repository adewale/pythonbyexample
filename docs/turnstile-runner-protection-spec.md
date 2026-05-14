# Turnstile runner protection spec

This spec records the current runner-protection design for Python By Example's editable-code endpoint, the Cloudflare setup already completed, and the remaining optional hardening work.

## Cloudflare references

Grounding docs:

- Turnstile overview: <https://developers.cloudflare.com/turnstile/>
- Turnstile client-side rendering: <https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/>
- Turnstile server-side validation / Siteverify: <https://developers.cloudflare.com/turnstile/get-started/server-side-validation/>
- Turnstile widget concepts and appearance options: <https://developers.cloudflare.com/turnstile/concepts/widget/>
- Turnstile widget configuration options: <https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/>
- Cloudflare challenge pages and Managed Challenges: <https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/>
- Ruleset Engine actions, including Managed Challenge and Block: <https://developers.cloudflare.com/ruleset-engine/rules-language/actions/>
- WAF custom rules: <https://developers.cloudflare.com/waf/custom-rules/>
- WAF rate limiting rules: <https://developers.cloudflare.com/waf/rate-limiting-rules/>
- WAF rate limiting parameters: <https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/>
- WAF rate limiting request-rate calculation: <https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/>
- WAF rate limiting dashboard setup: <https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/>
- Ruleset Engine fields and expressions: <https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/>
- Workers secrets: <https://developers.cloudflare.com/workers/configuration/secrets/>
- Workers environment variables: <https://developers.cloudflare.com/workers/configuration/environment-variables/>

## Protected endpoint

The expensive operation is the edited-code runner:

```text
POST /examples/{slug}
```

A successful POST can create/reuse a Dynamic Worker and execute user-edited Python. The protection goal is to stop abusive volume without making the ordinary learner loop feel like a CAPTCHA form.

Normal desired path:

```text
read example → edit code → click Run → see output
```

Protection desired path:

```text
normal learner → no Turnstile visible, no Siteverify call
new/suspicious session → temporary Invisible-mode Turnstile → clearance cookie → many normal runs
high-volume abuse → Cloudflare Rate Limiting Block/429 before Worker execution
```

## Current repository implementation

Implemented in:

```text
ae7b47d Add optional Turnstile protection
10d90ca Document Turnstile runner protection
8684479 Make Turnstile session-scoped and conditional
16da978 Harden Turnstile runner protection
d49b432 Make deployment smoke assert rendered output
```

The deployed model is conditional once-per-session Turnstile, not visible/per-request Turnstile.

Files involved:

```text
src/main.py
src/app.py
src/templates/example.html
scripts/smoke_deployment.py
scripts/lint_seo_cache.py
tests/test_app.py
docs/lessons-learned.md
src/asset_manifest.py
```

## Current behavior after this spec update

Turnstile remains **secret/config gated** and is not active by default.

If `TURNSTILE_SECRET_KEY` is absent:

- no Turnstile policy is enforced
- no Siteverify request is made
- Dynamic Worker POST runs behave normally
- local development remains frictionless

If `TURNSTILE_SITE_KEY` is absent:

- no challenge container is rendered
- a challenge-required policy cannot complete in the browser

If `TURNSTILE_CHALLENGE_MODE` is absent or `off`:

- normal POSTs do not require Turnstile
- a configured site/secret key alone does not slow every run

If `TURNSTILE_CHALLENGE_MODE=session` and both site/secret keys are configured:

1. A browser without valid clearance posts edited code.
2. The server returns the example page with a hidden `data-turnstile-required` marker and does **not** create a Dynamic Worker.
3. Client JS lazily loads Turnstile using explicit rendering.
4. It renders the configured Invisible-mode Turnstile widget only for that challenge.
5. The Turnstile callback provides a token.
6. The client removes the widget and retries the POST with `cf-turnstile-response`.
7. The Worker validates the token through Siteverify.
8. On success, the Worker sets a signed `pbe_turnstile_clearance` cookie.
9. Later runs in that clearance window skip Turnstile and go straight to the Dynamic Worker.

Siteverify endpoint from Cloudflare docs:

```text
https://challenges.cloudflare.com/turnstile/v0/siteverify
```

Token field:

```text
cf-turnstile-response
```

## Current environment variables / secrets

### Required for app-level session Turnstile

```text
TURNSTILE_SITE_KEY
TURNSTILE_SECRET_KEY
TURNSTILE_CHALLENGE_MODE=session
```

### Recommended

```text
TURNSTILE_CLEARANCE_SECRET
TURNSTILE_CLEARANCE_SECONDS
PBE_SMOKE_BYPASS_SECRET
```

`TURNSTILE_CLEARANCE_SECRET` signs the clearance cookie. If absent, the Worker falls back to `TURNSTILE_SECRET_KEY` for signing. A separate secret is cleaner.

`TURNSTILE_CLEARANCE_SECONDS` defaults to 8 hours and is clamped between 60 seconds and 7 days.

`PBE_SMOKE_BYPASS_SECRET` lets deployment smoke test edited-code execution without solving Turnstile.

Smoke header:

```text
x-pythonbyexample-smoke-secret: <secret>
```

## Current app-level security properties

- Turnstile is not visible on initial page load.
- The Turnstile script is not loaded until a challenge-required response is received.
- The Turnstile widget should be configured in Cloudflare as **Invisible** mode. Client code uses explicit rendering with `execution: "execute"`; `size: "invisible"` is not a valid current Turnstile size option.
- The widget is removed after callback success or failure.
- Siteverify is called only when a challenge-required request retries with a token.
- A valid challenge creates a signed, HttpOnly, Secure, SameSite=Lax clearance cookie scoped to `/examples`.
- Failed or missing verification does not create a Dynamic Worker.
- POST responses are still never cached.
- Rendered HTML cache keys account for Turnstile site-key presence to avoid stale widget/no-widget HTML.

## Smoke-test behavior

Normal smoke:

```bash
scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

If app-level session Turnstile is enabled, use the bypass secret:

```bash
PBE_SMOKE_BYPASS_SECRET=... scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

The script sends:

```text
x-pythonbyexample-smoke-secret: <secret>
```

This is only an app-level bypass. If Cloudflare Rate Limiting challenges smoke traffic before it reaches the Worker, either keep smoke below the threshold or add a Cloudflare-side skip/exception.

## Recommended Cloudflare layer: Rate Limiting Rules

The best first production protection for Dynamic Worker cost is Cloudflare Rate Limiting, because it runs before the Worker and limits repeated runner traffic at the edge.

Docs:

- Overview: <https://developers.cloudflare.com/waf/rate-limiting-rules/>
- Parameters and plan limits: <https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/>
- Request-rate calculation: <https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/>
- Dashboard setup: <https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/>

Important Cloudflare details that affect this project:

- Rate limit counters are kept per unique combination of configured characteristics, and Cloudflare implicitly includes the data-center ID (`cf.colo.id`). They are not global counters across the whole Cloudflare network.
- Available expression fields, characteristics, counting periods, mitigation periods, and rule counts vary by Cloudflare plan.
- Per Cloudflare's availability table, matching on HTTP method in a rate limiting rule expression is available on Business and Enterprise plans, not Free/Pro.
- On Free/Pro/Business, challenge actions (`managed_challenge`, `js_challenge`, `challenge`) use request throttling; you do not configure a mitigation duration. After a visitor passes the challenge, that request counter is reset. Enterprise can configure challenge-action duration.
- Cloudflare Challenge Pages interrupt the request flow and are not ideal for AJAX/fetch API-style calls. The runner POST is submitted by browser JavaScript, so a `Block` action with a `429` response is more predictable for high-rate POST abuse than a Managed Challenge on the POST itself. Use app-level Turnstile, or Cloudflare Turnstile Pre-clearance, when the desired behavior is browser verification rather than a hard edge cap.

### Business/Enterprise precise POST rule

If the zone plan supports the `http.request.method` field in rate limiting expressions, use this precise rule:

```text
Rule name:
  Protect Python By Example runner POSTs

When incoming requests match:
  http.request.method eq "POST"
  and starts_with(http.request.uri.path, "/examples/")

With the same characteristics:
  IP
  # or IP with NAT support, if available and classroom/shared-network false positives matter

When rate exceeds:
  30 requests / 60 seconds

Then take action:
  Block

Response code:
  429

Duration:
  5 minutes
```

For classrooms/workshops behind one NAT, start higher:

```text
100 requests / 60 seconds / IP or IP-with-NAT-support bucket
```

### Free/Pro fallback rule

If the zone plan does not allow `http.request.method` in rate limiting expressions, do **not** use the POST-only expression above. Use a path-only rule and set the threshold high enough that normal page reading is unaffected:

```text
Rule name:
  Protect Python By Example examples path

When incoming requests match:
  starts_with(http.request.uri.path, "/examples/")

With the same characteristics:
  IP

Then take action:
  Block

Response code:
  429
```

Plan-aware starting points:

```text
Free:  20 requests / 10 seconds / IP, 10-second mitigation
Pro:   120 requests / 60 seconds / IP, 5-minute mitigation
```

Because this fallback counts both example page GETs and runner POSTs, tune it from Cloudflare Security Events before lowering thresholds.

Why this is the recommended first layer:

- it runs before Worker execution
- normal learners do not see Turnstile
- no app-side state is needed
- Business/Enterprise can target the precise expensive POST path
- Free/Pro can still provide a coarse emergency brake on the `/examples/` path

Tradeoffs:

- IP-based thresholds can false-positive shared networks
- Free/Pro path-only rules count GETs as well as POSTs
- distributed abuse can evade a per-IP rule
- rule configuration lives in Cloudflare unless managed through API/Terraform
- smoke can be affected if repeated many times in a short window

## Optional Cloudflare layer: WAF custom rules

Docs: <https://developers.cloudflare.com/waf/custom-rules/>

WAF rules are a good second layer for risky-looking traffic, for example low reputation, suspicious user agents, or bot-management signals if available on the Cloudflare plan.

For top-level HTML page requests, a Managed Challenge custom rule can be appropriate:

```text
starts_with(http.request.uri.path, "/examples/")
and <risk signal>
```

Action:

```text
Managed Challenge
```

Managed Challenge docs: <https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenges>

For the AJAX/fetch runner endpoint itself, avoid returning a Challenge Page directly to the POST request. Cloudflare documents that Challenge Pages can fail when the browser expects a non-HTML AJAX/XHR/fetch response. Prefer one of these instead:

- app-level Turnstile, as implemented here
- Cloudflare Turnstile Pre-clearance if integrating WAF challenges with API requests
- `Block` / `429` for hard abuse caps

Use WAF custom rules for risk filtering. Use Rate Limiting for volume control.

## App-side cheap gates backlog

These are not the primary protection, but remain useful before Dynamic Worker creation:

- maximum submitted code byte size
- maximum line count
- require `application/x-www-form-urlencoded`
- hidden honeypot field must be empty
- optional same-origin/referer shape check
- reject malformed form submissions

These gates should return friendly output-panel messages and must not create Dynamic Workers when they fail.

## Why once-per-session is worth doing

Once-per-session Turnstile is less disruptive than per-run Turnstile:

- only the first challenged run pays the Turnstile cost
- later runs use a signed clearance cookie
- the widget is invisible/temporary
- Siteverify is not part of every Dynamic Worker request

It is not a replacement for rate limiting:

- a cleared browser can still send many runs
- bots can create many cleared sessions
- cookie-only state is weaker than edge rate enforcement

Best use:

```text
Rate Limiting controls volume.
Once-per-session Turnstile controls browser proof when app policy requires it.
```

## Production setup status

### Completed

Cloudflare Dashboard Turnstile setup is complete:

```text
Hostname: www.pythonbyexample.dev
Mode: Invisible
```

The following Worker secrets have been configured in Cloudflare:

```text
TURNSTILE_SITE_KEY
TURNSTILE_SECRET_KEY
TURNSTILE_CLEARANCE_SECRET
PBE_SMOKE_BYPASS_SECRET
```

The following non-secret Worker vars are checked into `wrangler.jsonc`:

```jsonc
"vars": {
  "TURNSTILE_CHALLENGE_MODE": "session",
  "TURNSTILE_CLEARANCE_SECONDS": "28800"
}
```

Do **not** put secret keys in `wrangler.jsonc`.

Manual browser verification and production smoke with `PBE_SMOKE_BYPASS_SECRET` both passed after deploying session-scoped Invisible-mode Turnstile.

Docs:

- Turnstile overview: <https://developers.cloudflare.com/turnstile/>
- Widget modes: <https://developers.cloudflare.com/turnstile/concepts/widget/>
- Widget configuration options: <https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/>
- Workers secrets: <https://developers.cloudflare.com/workers/configuration/secrets/>

Invisible mode note: Cloudflare documents that invisible widgets have no visual footprint, and that widget `size` values are `normal`, `flexible`, or `compact`; invisibility is selected by widget mode, not by `size="invisible"`.

Privacy note: Cloudflare documents that using Invisible mode requires referencing the Cloudflare Turnstile Privacy Addendum in your own privacy policy.

## Remaining TODO

### 1. Add Cloudflare Rate Limiting rule (optional, recommended for cost caps)

Cloudflare Dashboard:

```text
Security rules → Create rule → Rate limiting rule
```

or, in the WAF dashboard:

```text
Security → WAF → Rate limiting rules → Create rule
```

Docs: <https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/>

Use the plan-aware guidance above:

- Business/Enterprise: match `POST` + `/examples/`, start at `30 requests / 60 seconds`, action `Block`, response `429`, duration `5 minutes`.
- Classroom/shared NAT: start around `100 requests / 60 seconds` or use `IP with NAT support` if available.
- Free/Pro: if method matching is unavailable, use a path-only `/examples/` rule with a higher threshold because it also counts GET page views.

Do not configure `Managed Challenge for 5 minutes` on Free/Pro/Business rate limiting rules. Cloudflare documents that challenge actions on those plans use request throttling and have no selected duration; only Enterprise can configure a challenge-action duration. For this AJAX/fetch POST endpoint, a predictable `Block`/`429` edge cap is preferable.

### 2. Keep production deployment checks using the bypass secret

For protected production POST smoke, run:

```bash
PBE_SMOKE_BYPASS_SECRET=... scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

For GET-only public smoke without a secret:

```bash
scripts/smoke_deployment.py --skip-post https://www.pythonbyexample.dev
```

Expected:

```text
Deployment smoke OK
```

The smoke script checks the rendered output panel for POST runs. This is important because a Turnstile-required response can echo submitted code in the editor textarea without executing it.

## Verification checklist

### Verify no visible widget on page load

```bash
curl -s https://www.pythonbyexample.dev/examples/values | grep -i "cf-turnstile"
```

Expected:

```text
(no output)
```

The page may include runner JavaScript containing the Turnstile API URL string, but it should not include a loaded Turnstile `<script src=...>` tag or visible widget markup on first render.

### Verify app-level challenge-required mode

With:

```text
TURNSTILE_SECRET_KEY configured
TURNSTILE_SITE_KEY configured
TURNSTILE_CHALLENGE_MODE=session
```

A first POST without a token should not run edited code. It should return a page that contains:

```text
data-turnstile-required="true"
```

Browser behavior:

1. click Run
2. challenge is requested
3. Invisible-mode Turnstile runs without page-load widget furniture
4. widget disappears after callback
5. run retries and produces output
6. later runs in the same clearance window skip Turnstile

### Verify no Dynamic Worker on missing challenge

POST without token in session mode:

```bash
curl -i -X POST https://www.pythonbyexample.dev/examples/values \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "code=print('should-not-run')"
```

Expected body:

```text
Verification required before running edited code
```

Expected absent:

```text
should-not-run
```

### Verify clearance cookie exists after browser success

In browser DevTools:

```text
Application → Cookies → pbe_turnstile_clearance
```

Expected attributes:

```text
HttpOnly
Secure
SameSite=Lax
Path=/examples
```

### Verify Rate Limiting rule

Carefully test above threshold, or inspect Cloudflare Security Events after controlled POST bursts.

Do not tune solely from one local curl loop; check classroom/shared-IP scenarios before lowering thresholds.

## Decision summary

Recommended final model:

```text
Cloudflare Rate Limiting first
+ optional WAF risk rules
+ app-level once-per-session Turnstile when configured
+ cheap app gates later
```

Avoid:

```text
Turnstile Siteverify on every normal Dynamic Worker run
visible Turnstile widget as permanent page furniture
```
