# Turnstile runner protection spec

This spec records the current runner-protection design for Python By Example's editable-code endpoint and the remaining Cloudflare setup required outside the repository.

## Cloudflare references

Grounding docs:

- Turnstile overview: <https://developers.cloudflare.com/turnstile/>
- Turnstile client-side rendering: <https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/>
- Turnstile server-side validation / Siteverify: <https://developers.cloudflare.com/turnstile/get-started/server-side-validation/>
- Turnstile widget concepts and appearance options: <https://developers.cloudflare.com/turnstile/concepts/widget/>
- Cloudflare Managed Challenge: <https://developers.cloudflare.com/cloudflare-challenges/challenge-types/managed-challenge/>
- WAF custom rules: <https://developers.cloudflare.com/waf/custom-rules/>
- WAF rate limiting rules: <https://developers.cloudflare.com/waf/rate-limiting-rules/>
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
new/suspicious/high-rate session → temporary invisible Turnstile → clearance cookie → many normal runs
high-volume abuse → Cloudflare Rate Limiting / Managed Challenge before Worker execution
```

## Current repository implementation

Implemented in:

```text
ae7b47d Add optional Turnstile protection
10d90ca Document Turnstile runner protection
```

Current follow-up implementation changes this model from visible/per-request Turnstile to conditional once-per-session Turnstile.

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
4. It renders an invisible Turnstile widget only for that challenge.
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
- The rendered widget uses invisible mode.
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

The best first production protection for Dynamic Worker cost is Cloudflare Rate Limiting, because it runs before the Worker and directly targets repeated POST runs.

Docs: <https://developers.cloudflare.com/waf/rate-limiting-rules/>

Suggested rule:

```text
Rule name:
  Protect Python By Example runner

Expression:
  http.request.method eq "POST"
  and starts_with(http.request.uri.path, "/examples/")

Threshold:
  30 requests / 60 seconds / IP

Action:
  Managed Challenge

Mitigation timeout:
  5 minutes
```

For classrooms/workshops behind one NAT, start higher:

```text
100 requests / 60 seconds / IP
```

Why this is the recommended first layer:

- it runs before Worker execution
- normal learners do not see Turnstile
- no app-side state is needed
- it protects the precise expensive path
- it is easier to reason about than broad bot-risk rules

Tradeoffs:

- IP-based thresholds can false-positive shared networks
- distributed abuse can evade a per-IP rule
- rule configuration lives in Cloudflare unless managed through API/Terraform
- smoke can be affected if repeated many times in a short window

## Optional Cloudflare layer: WAF custom rules

Docs: <https://developers.cloudflare.com/waf/custom-rules/>

WAF rules are a good second layer for risky-looking traffic, for example low reputation, suspicious user agents, or bot-management signals if available on the Cloudflare plan.

Shape:

```text
http.request.method eq "POST"
and starts_with(http.request.uri.path, "/examples/")
and <risk signal>
```

Action:

```text
Managed Challenge
```

Managed Challenge docs: <https://developers.cloudflare.com/cloudflare-challenges/challenge-types/managed-challenge/>

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

## What still needs to be done manually in Cloudflare

### 1. Create Turnstile keys

Cloudflare Dashboard:

```text
Turnstile → Add widget
```

Recommended settings:

```text
Name: pythonbyexample-production
Hostname: www.pythonbyexample.dev
Mode: Managed or Invisible
```

Docs: <https://developers.cloudflare.com/turnstile/>

Copy:

```text
Site key
Secret key
```

### 2. Set Worker secrets / vars

Use Wrangler secrets docs: <https://developers.cloudflare.com/workers/configuration/secrets/>

```bash
npx wrangler secret put TURNSTILE_SITE_KEY
npx wrangler secret put TURNSTILE_SECRET_KEY
npx wrangler secret put TURNSTILE_CLEARANCE_SECRET
npx wrangler secret put PBE_SMOKE_BYPASS_SECRET
```

Set non-secret vars either through Wrangler config or Cloudflare dashboard:

```text
TURNSTILE_CHALLENGE_MODE=session
TURNSTILE_CLEARANCE_SECONDS=28800
```

If using `wrangler.jsonc`, add for non-secret values only:

```jsonc
"vars": {
  "TURNSTILE_CHALLENGE_MODE": "session",
  "TURNSTILE_CLEARANCE_SECONDS": "28800"
}
```

Do **not** put secret keys in `wrangler.jsonc`.

### 3. Add Cloudflare Rate Limiting rule

Cloudflare Dashboard:

```text
Security → WAF → Rate limiting rules → Create rule
```

Docs: <https://developers.cloudflare.com/waf/rate-limiting-rules/>

Expression:

```text
http.request.method eq "POST"
and starts_with(http.request.uri.path, "/examples/")
```

Start with:

```text
30 requests / 60 seconds / IP → Managed Challenge for 5 minutes
```

Raise the threshold if teaching cohorts behind a shared IP hit it.

### 4. Deploy

```bash
make deploy
```

### 5. Smoke test

If `TURNSTILE_CHALLENGE_MODE` is `off` or secrets are absent:

```bash
scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

If app-level session Turnstile is enabled:

```bash
PBE_SMOKE_BYPASS_SECRET=... scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

Expected:

```text
Deployment smoke OK
```

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
3. invisible Turnstile runs or displays only if Cloudflare needs interaction
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
