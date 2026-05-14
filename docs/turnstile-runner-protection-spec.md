# Turnstile runner protection spec

This spec records what Python By Example has already implemented around Cloudflare Turnstile, what is intentionally *not* enabled yet, and the candidate next protection models for the editable example runner.

## Goal

Protect the costly endpoint:

```text
POST /examples/{slug}
```

without making the normal learning loop feel like a CAPTCHA form.

The desired learner path is:

```text
read example → edit code → click Run → see output
```

Turnstile should be invisible unless risk or rate policy requires a challenge.

## Current implementation

Implemented in commit:

```text
ae7b47d Add optional Turnstile protection
```

Files touched:

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

### Current behavior

Turnstile is **secret-gated**.

If `TURNSTILE_SECRET_KEY` is absent:

- no server-side Turnstile verification is performed
- Dynamic Worker POST runs behave as before
- local development remains frictionless

If `TURNSTILE_SITE_KEY` is absent:

- no Turnstile widget is rendered on example pages

If both are configured:

- example pages render a Turnstile widget in the run form
- `POST /examples/{slug}` reads `cf-turnstile-response`
- the Worker verifies the token against Cloudflare Siteverify
- failed verification returns the example page with a friendly output message
- failed verification does **not** create a Dynamic Worker
- after AJAX submit, the client calls `turnstile.reset()`

Siteverify endpoint:

```text
https://challenges.cloudflare.com/turnstile/v0/siteverify
```

Token field:

```text
cf-turnstile-response
```

### Smoke-test bypass

Production smoke can bypass app-level Turnstile verification with a separate secret.

Worker secret:

```text
PBE_SMOKE_BYPASS_SECRET
```

Smoke script environment variable:

```text
PBE_SMOKE_BYPASS_SECRET
```

Header sent by `scripts/smoke_deployment.py` when the env var is set:

```text
x-pythonbyexample-smoke-secret: <secret>
```

This bypass is only for deployment verification. It should not be reused as a general user bypass.

### Cache note

Rendered HTML cache keys include a Turnstile-site-key hash fragment when a site key is configured. This prevents a cached page without a widget from being served after Turnstile is enabled, or vice versa.

### Tests and verification added

`tests/test_app.py` checks that:

- the Turnstile widget is not rendered by default
- a site key renders the widget and Turnstile script
- the client resets Turnstile after submit
- the Worker source includes secret-gated Siteverify logic
- the smoke bypass header is recognized by the implementation

`make verify` and GitHub Verify passed after the implementation.

## Current UX problem

The current implementation is safe but not ideal:

- the widget appears as page furniture when enabled
- it can stay visible after completion
- if enforcement is enabled for every run, every Dynamic Worker POST pays the Turnstile token/verification latency

This is acceptable as a first security hook, but not the desired final UX.

## Desired direction

Move from:

```text
Turnstile enabled → every run must solve/verify Turnstile
```

to:

```text
normal run → no widget, no Siteverify call
risky/rate-limited run → challenge required → temporary Turnstile → retry with token
```

## Option A: Conditional challenge-required Turnstile

### Flow

Normal request:

```text
Run → POST /examples/{slug} → Dynamic Worker → output
```

Challenge request:

```text
Run
→ server decides challenge is required
→ response marks challenge_required
→ client renders invisible/temporary Turnstile
→ Turnstile callback returns token
→ client retries POST with cf-turnstile-response
→ server verifies token
→ Dynamic Worker runs
→ widget is removed/reset
```

### Required changes

Client:

- stop rendering the Turnstile widget on initial page load
- add a hidden/empty challenge container near the Run button or output panel
- when a response contains a challenge-required marker, load/render Turnstile
- use invisible or interaction-only appearance
- retry submit after callback
- call `turnstile.remove(widgetId)` or clear the container after success
- reset/remove on error or expiry

Server:

- add a policy function such as `requires_turnstile(request, form)`
- verify token only when the policy requires it or when a token is supplied
- return a challenge-required page fragment/message without creating a Dynamic Worker
- keep smoke bypass

Open requirement:

- this model needs a trigger. Without app gates, rate state, or WAF/rate-limit integration, the challenge flow exists but rarely/never activates.

## Option B: App-side cheap gates

These are not implemented yet; they are candidate triggers for conditional Turnstile.

Possible gates before creating a Dynamic Worker:

- maximum submitted code byte size
- maximum line count
- require `application/x-www-form-urlencoded`
- hidden honeypot field must be empty
- optional same-origin/referer shape check
- reject malformed form submissions

Pros:

- no extra Cloudflare products
- easy to test in repo
- prevents obviously wasteful submissions before Dynamic Worker creation

Cons:

- not strong against targeted abuse
- content-shape rules can be arbitrary
- does not solve high-rate distributed traffic

## Option C: Cloudflare Rate Limiting Rules

Target:

```text
http.request.method eq "POST"
and starts_with(http.request.uri.path, "/examples/")
```

Recommended starting threshold:

```text
30 POSTs / 60 seconds / IP → Managed Challenge
```

Use a higher threshold for classrooms/workshops behind one NAT, for example:

```text
100 POSTs / 60 seconds / IP
```

Pros:

- best first protection against Dynamic Worker cost abuse
- runs before the Worker
- no app latency for normal runs
- no app-side state
- directly matches the abuse mode: repeated runs

Cons:

- IP-based limits can false-positive shared networks
- attackers can distribute across IPs
- config lives in Cloudflare unless managed via Terraform/API
- smoke normally only sends 5 POSTs, but repeated smoke runs may need care

## Option D: Cloudflare WAF / Custom Rules with Managed Challenge

Example shape:

```text
http.request.method eq "POST"
and starts_with(http.request.uri.path, "/examples/")
and <risk signal>
```

Risk signals can include:

- IP reputation / threat score
- country / ASN
- request headers
- user agent
- bot signals, if available on the Cloudflare plan

Pros:

- edge-native risk filtering
- no app state
- no normal-path Turnstile latency
- can challenge traffic before it reaches the Worker

Cons:

- advanced bot signals may require paid features
- rules can be opaque and harder to debug
- less directly tied to “too many example runs” than rate limiting
- config may live outside the repo

Best role:

- second layer for obviously risky traffic, after basic rate limiting

## Option E: Turnstile once per session

This model asks a user to pass Turnstile once, then allows many runs for a time window.

### Possible implementations

1. **Server-signed session cookie**

   Flow:

   ```text
   first run or first challenge → Turnstile token verified → Worker sets signed cookie → later runs skip Siteverify until expiry
   ```

   Cookie stores or proves:

   - clearance timestamp
   - expiry
   - maybe rough run allowance
   - HMAC signature using a Worker secret

2. **Cloudflare clearance / pre-clearance**

   Use Cloudflare challenge/clearance behavior so the edge remembers the browser is cleared for a period.

3. **Durable Object state**

   Store per-session or per-IP run counters and Turnstile clearance state server-side.

### Pros

- much better UX than Turnstile on every run
- reduces Siteverify calls dramatically
- widget can be invisible/temporary
- still blocks repeated anonymous abuse after the first challenge gate

### Cons

- a pure client cookie can be deleted to reset state
- signed-cookie implementation needs a secret, expiry, and careful HMAC handling
- Durable Object is stronger but more code and one extra state lookup
- once-per-session proves “a browser solved once”, not “this request is low cost”
- does not replace rate limiting for high-volume or distributed abuse

### Is once-per-session less trouble?

Compared with conditional challenge-required Turnstile plus app-owned rate state, **yes**, a once-per-session model is less product complexity for users and can be simpler to reason about.

Compared with Cloudflare Rate Limiting, **no**. Rate limiting is less app work and more directly protects Dynamic Worker cost.

### Is once-per-session more effective?

It is more effective than per-request Turnstile for UX, because it avoids repeated challenges and Siteverify latency.

It is less effective than rate limiting for abuse control. A solved session can still send many expensive runs unless paired with a run limit, expiry, or edge rate rule.

Best use:

- combine once-per-session Turnstile with Cloudflare Rate Limiting
- challenge once for suspicious/high-rate clients
- let normal users run freely until they cross a rate threshold

## Recommended architecture

Use layers:

1. **Cloudflare Rate Limiting Rules** for `POST /examples/*` volume abuse.
2. **Conditional app Turnstile** for any app-owned challenge-required flow.
3. **Once-per-session clearance** if we want users to pass Turnstile once and then keep running examples without repeated latency.
4. **Cheap app gates** as a backlog item for obvious malformed or oversized submissions.

Recommended near-term path:

```text
Rate Limiting first → invisible/temporary Turnstile UI → optional once-per-session clearance
```

Avoid making Siteverify part of every normal Dynamic Worker run.

## Operational setup notes

Create keys in Cloudflare Dashboard:

```text
Turnstile → Add widget → hostname www.pythonbyexample.dev → Managed or Invisible mode
```

Secrets/vars currently expected by the Worker:

```bash
npx wrangler secret put TURNSTILE_SITE_KEY
npx wrangler secret put TURNSTILE_SECRET_KEY
npx wrangler secret put PBE_SMOKE_BYPASS_SECRET
```

If using rate limiting, configure in Cloudflare Dashboard:

```text
Security → WAF → Rate limiting rules → Create rule
```

Expression:

```text
http.request.method eq "POST"
and starts_with(http.request.uri.path, "/examples/")
```

Initial action:

```text
Managed Challenge
```

Initial threshold:

```text
30 requests / 60 seconds / IP
```

## Verification checklist

With Turnstile disabled:

```bash
scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

With Turnstile secrets enabled and current always-on app enforcement:

```bash
curl -i -X POST https://www.pythonbyexample.dev/examples/values \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "code=print('should-not-run')"
```

Expected body includes:

```text
Turnstile verification is required
```

With smoke bypass configured:

```bash
PBE_SMOKE_BYPASS_SECRET=... scripts/smoke_deployment.py https://www.pythonbyexample.dev
```

Expected:

```text
Deployment smoke OK
```

After moving to conditional/once-per-session:

- normal smoke should not require Turnstile
- a forced challenge test should render a temporary widget
- completing the widget should remove it from the page
- retry should run the Dynamic Worker
- subsequent cleared-session runs should skip Siteverify until expiry
