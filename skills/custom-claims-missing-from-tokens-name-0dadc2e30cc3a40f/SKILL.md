---
name: "custom-claims-missing-from-tokens-name-0dadc2e30cc3a40f"
description: "Symptom: the claim your API needs is not in the token. Cause: non-namespaced claims are dropped, the Action is not deployed, or it is not attached to the flow. Confirmation: decode the token and check the Action's deployed version."
metadata:
  skill_id: "skl_2tkVbgS7P8iNZo1TL30O0g"
  title: "Custom claims missing from tokens: namespaced claims and undeployed Actions"
  version: "skv_FcaR9bGIMSbegdu7cwigSg"
  updated: "2026-10-03T14:05:16.030542+00:00"
  canonical_url: "https://vectle.com/skills/skl_2tkVbgS7P8iNZo1TL30O0g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/customize/actions/triggers/post-login\"]"
---

**TL;DR:** Symptom: the claim your API needs is not in the token. Cause: non-namespaced claims are dropped, the Action is not deployed, or it is not attached to the flow. Draft code never runs. Wrong trigger: claims for tokens belong in post-login; a post-registration Action runs once at signup and never touches later tokens.

# Diagnose: custom claims missing

## Symptom

`api.idToken.setCustomClaim` / `api.accessToken.setCustomClaim` ran, but the claim is absent from the decoded token.

## Likely causes

1. Claim name not namespaced. Auth0 drops custom claims whose names are not namespaced (a URL like `YOUR_HOST/[claim]`). `api.idToken.setCustomClaim("role", "admin")` silently does nothing; `("YOUR_HOST/role", "admin")` works. Reserved OIDC names are also protected.
2. Action written but not DEPLOYED. Draft code never runs.
3. Action deployed but not attached to the login flow (Actions > Flows > Login). Deployment alone does nothing.
4. Wrong trigger: claims for tokens belong in post-login; a post-registration Action runs once at signup and never touches later tokens.
5. Conditional logic skipped: the `if` around setCustomClaim did not match (e.g. checking event.authorization.roles before roles load).

## Confirm

- Decode the access token AND the id token separately; claims set on one do not appear on the other.
- Actions > Library: confirm the version says Deployed with today's timestamp.
- Actions > Flows > Login: confirm the Action tile is in the flow, in the right position.
- Add a temporary log line or use real-time logs to confirm the Action executed and the condition was true.

## Fix

Namespace the claim, deploy, attach to the flow, in that order. Then log in fresh (existing tokens do not retroactively gain claims).

## Verify

Fresh login, decode the new token, claim present with the expected value. Keep a token-claim assertion in CI against a test tenant.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Custom claims missing from tokens.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

---

Source: [Vectle](https://vectle.com/skills/skl_2tkVbgS7P8iNZo1TL30O0g). Version: `skv_FcaR9bGIMSbegdu7cwigSg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
