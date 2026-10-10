---
name: "failed-exchange-at-oauth-token-code-ve-60885dee420ac995"
description: "The code-for-token exchange fails with 401/403 when the verifier, redirect URI, or client auth does not match the authorize request. Authorization codes are single-use and short-lived."
metadata:
  skill_id: "skl_Yv3g5dCSmrmFPs9lAKohmg"
  title: "Failed exchange at /oauth/token -  code_verifier, redirect_uri, and one-time codes"
  version: "skv_SzVNnkcDkfZSgSK1vnxsmQ"
  updated: "2026-10-03T15:13:26.162345+00:00"
  canonical_url: "https://vectle.com/skills/skl_Yv3g5dCSmrmFPs9lAKohmg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The code-for-token exchange fails with 401/403 when the verifier, redirect URI, or client auth does not match the authorize request. Authorization codes are single-use and short-lived. The verifier must be the exact string that produced the code_challenge in the authorize call, same code_challenge_method (S256). The token call's redirect_uri must be byte-identical to the authorize call's.

## The error

```text
{"error": "invalid_grant", "error_description": "Failed exchange"}
```

# Failed code exchange

## The error

`POST /oauth/token` with `grant_type=authorization_code` returns `401 Unauthorized` or `{"error": "invalid_grant", "error_description": "Failed exchange"}`.

## Causes

1. PKCE `code_verifier` mismatch. The verifier must be the exact string that produced the `code_challenge` in the authorize call, same `code_challenge_method` (S256). SDKs handle this; hand-rolled flows lose the verifier between redirect hops (stored in memory, page reloaded) and fail.
2. `redirect_uri` mismatch. The token call's redirect_uri must be byte-identical to the authorize call's. Trailing slash and port drift strike here too.
3. Code reuse or expiry. Codes are single-use and expire in ~10 minutes. Double-submitting the callback (React StrictMode double effects, double-clicks) exchanges the code twice; the second fails. Guard the callback handler to run once.
4. Wrong client auth. Confidential clients must authenticate (client_secret_basic or post) with the CURRENT secret. A rotated secret breaks the exchange until the app config is updated.
5. Clock skew: the client assertion or request outside the allowed window.

## Diagnose

- Tenant logs: the failed exchange event names the reason (invalid verifier vs unknown code).
- Check the callback handler runs exactly once (log it).
- Diff the authorize redirect_uri against the token call's.

## Checklist

- Verifier persisted across the redirect (SDK default storage, not a JS variable that dies on reload).
- Single exchange per code; idempotent callback handling.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Failed exchange at /oauth/token -  code_verifier, redirect_uri, and one-time codes.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Failed behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_Yv3g5dCSmrmFPs9lAKohmg). Version: `skv_SzVNnkcDkfZSgSK1vnxsmQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
