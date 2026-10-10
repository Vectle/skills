---
name: "api-rejects-the-access-token-decode-ch-5aca75b72e37344d"
description: "Symptom: API returns 401 for a token the app just obtained. Cause: almost always audience or issuer mismatch, sometimes expiry. Confirmation: decode the JWT and diff its claims against the API's expected values. Not for different error messages."
metadata:
  skill_id: "skl_CVgPPGwf3kJLu5uvJveGWA"
  title: "API rejects the access token -  decode, check iss and aud, compare with /userinfo"
  version: "skv_og7x39xRv2PF6UKVJjqR9A"
  updated: "2026-10-03T14:07:54.530975+00:00"
  canonical_url: "https://vectle.com/skills/skl_CVgPPGwf3kJLu5uvJveGWA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: API returns 401 for a token the app just obtained. Cause: almost always audience or issuer mismatch, sometimes expiry. Check the API middleware config: audience string, issuerBaseURL, and that the JWKS URL is reachable from the API host. Verify Replay the request with a fresh token and get 200.

## The fix

1. `aud` is not your API identifier (opaque token, or minted for another API).

2. `iss` mismatch: custom domain vs canonical domain.

3. Expired token (clock skew) or wrong signing key (JWKS cached stale).

4. `aud`: must equal your API identifier exactly.

5. `iss`: must equal `YOUR_HOST/` (or your custom-domain issuer if configured).

6. `exp`: must be in the future on the API server's clock.

7. `azp`: the client id that requested it. Then call `GET YOUR_HOST/userinfo` with the token. If /userinfo 401s too, the token itself is bad (expired, revoked, malformed). If /userinfo 200s but your API 401s, your API's validation config is wrong, not the token. Check the API middleware config: audience string, issuerBaseURL, and that the JWKS URL is reachable from the API host.

8. Wrong/missing aud: set the audience at login to the API identifier.

9. iss mismatch: align the middleware issuer with the domain the tokens are actually minted from.

10. Stale JWKS cache: clear it; key rotation happens.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: API rejects the access token -  decode, check iss and aud, compare with /userinfo.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current API behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_CVgPPGwf3kJLu5uvJveGWA). Version: `skv_og7x39xRv2PF6UKVJjqR9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
