---
name: "m2m-token-request-401s-grant-types-aud-c9f0cf190d439aa2"
description: "Symptom: POST /oauth/token with client_credentials returns 401/403. Cause: the app is not authorized for the audience, the grant is off, or the secret is wrong. Confirmation: the failed client-credentials log event."
metadata:
  skill_id: "skl_hfkrXg-1Uwt_DrVgHSt3Cg"
  title: "M2M token request 401s: grant types, audience registered, client auth method"
  version: "skv_Xq--vcjooaplKi1QnTTjOg"
  updated: "2026-10-03T14:01:33.753313+00:00"
  canonical_url: "https://vectle.com/skills/skl_hfkrXg-1Uwt_DrVgHSt3Cg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/get-started/applications/application-grant-types\",\"https://auth0.com/docs/quickstart/backend\"]"
---

**TL;DR:** Symptom: POST /oauth/token with client_credentials returns 401/403. Cause: the app is not authorized for the audience, the grant is off, or the secret is wrong. The M2M app must be granted the API under its APIs tab with scopes. Audience typo: the audience must be the API identifier exactly.

## The fix

1. The application is not authorized for the API (audience). The M2M app must be granted the API under its APIs tab with scopes.

2. `client_credentials` grant not enabled on the application.

3. Wrong client secret, or the app is public (no secret works).

4. Audience typo: the audience must be the API identifier exactly.

5. Dashboard > Applications > your M2M app > APIs tab: is the API listed with scopes? If not, that is the bug.

6. Settings > Advanced > Grant Types: is client_credentials ticked?

7. Token endpoint auth method: confidential clients need client_secret_basic/post or private_key_jwt. Test with curl and the exact values from the dashboard to isolate code bugs from config bugs.

## When to use this

- This covers exactly what the title says: M2M token request 401s.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with M2M; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current M2M behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_hfkrXg-1Uwt_DrVgHSt3Cg). Version: `skv_Xq--vcjooaplKi1QnTTjOg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
