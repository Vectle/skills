---
name: "429-on-oauth-token-rate-limits-backoff-c1ed690e5f9e574b"
description: "Auth0 rate-limits the token endpoint per tenant. Agents that mint a fresh M2M token per request or retry aggressively hit 429s; the fix is caching plus backoff. Not the full reference manual."
metadata:
  skill_id: "skl_OiQEq1zHiNrjcTdi6l9SeA"
  title: "429 on /oauth/token -  rate limits, backoff, and token caching"
  version: "skv_dDeFsAJBNmhxbk3UStoVjg"
  updated: "2026-10-03T14:15:52.684245+00:00"
  canonical_url: "https://vectle.com/skills/skl_OiQEq1zHiNrjcTdi6l9SeA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Auth0 rate-limits the token endpoint per tenant. Agents that mint a fresh M2M token per request or retry aggressively hit 429s; the fix is caching plus backoff. Cache the token. Never retry immediately in a tight loop.

# 429 on /oauth/token

## The error

`429 Too Many Requests` from `/oauth/token`, sometimes with a `Retry-After` header. The authentication endpoint rate limits are documented in Auth0's rate limit policy and apply per tenant (burst and sustained).

## Why agents hit it

- M2M code that requests a new client_credentials token on every API call. Tokens live for hours; re-minting per request is pure waste.
- Retry storms: a failing token call retried immediately in a loop multiplies the load.
- Load tests or bulk jobs that authenticate per item instead of per batch.

## Fix

1. Cache the token. Store the access token with its `expires_in`; reuse until ~60 seconds before expiry, then refresh once. A simple in-memory cache with a lock (single-flight) is enough for most services.
2. Back off on 429: honor `Retry-After` if present, else exponential backoff with jitter. Never retry immediately in a tight loop.
3. For user flows, prefer refresh tokens / sessions over re-authenticating.
4. If legitimate traffic exceeds the limits, the answer is request a limit increase or an enterprise tier, not cleverer retries. Check Dashboard > Monitoring > Logs for the rate-limit event types to confirm which endpoint is hot.

## M2M token caching pattern

```
# pseudocode
def get_token():
    with lock:
        if cached and cached.expires_at - now() > 60:
            return cached.value
        tok = request_new_token()   # single POST /oauth/token
        cached = (tok.value, now() + tok.expires_in)
        return tok.value
```

## Checklist

- One token per lifetime, not per request.
- 429s back off with jitter and respect Retry-After.

## When to use this

- This covers exactly what the title says: 429 on /oauth/token -  rate limits, backoff, and token caching.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with 429; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current 429 behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_OiQEq1zHiNrjcTdi6l9SeA). Version: `skv_dDeFsAJBNmhxbk3UStoVjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
