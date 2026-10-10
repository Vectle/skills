---
name: "pscale-401-unauthorized-or-403-forbidd-ae45790baa9c9ef3"
description: "Fixes pscale failing with 401 Unauthorized or 403 Forbidden. Use when API calls reject your credentials: 401 means the session or token is expired/invalid, 403 means it is valid but lacks permission. Refreshes the session for 401s and checks grants for 403s. Not for CLI-not-installed or DNS errors."
metadata:
  skill_id: "skl_kJw4nHYHOzk8bAzpUdkLDA"
  title: "pscale: 401 Unauthorized or 403 Forbidden - refresh session or check token"
  version: "skv_gDRW2pUhd5b1t3Qkt4Ucbg"
  updated: "2026-10-03T05:59:34.158641+00:00"
  canonical_url: "https://vectle.com/skills/skl_kJw4nHYHOzk8bAzpUdkLDA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# pscale: 401 Unauthorized or 403 Forbidden - refresh session or check token

TL;DR: a 401 means the credential is dead: re-run `pscale auth login` (or replace the service token) for a fresh one. A 403 means the credential is alive but not allowed: check the token's grants or your org role for the database/branch you targeted. Do not re-login for a 403 — a fresh token with the same grants fails the same way.

```text
401 Unauthorized / 403 Forbidden from pscale
```

## Steps

1. For a 401: run `pscale auth login` again (interactive) or rotate the service token (CI). Rerun the command. Expected: the 401 is gone.

2. For a 403: open the dashboard and check the service token's grants, or your user's role on the org/database/branch. Add the missing grant.

3. Re-run with the fixed credential. Expected: the command succeeds.

4. If a 403 persists with correct grants, confirm you targeted the right org — tokens are org-scoped and a valid token fails against another org's resources.

## When this applies

- `401 Unauthorized` on any pscale API call
- `403 Forbidden` when the login itself worked
- sudden failures after an org role change

## When it doesn't

- `Authentication failed` on pscale shell — session-level, use the logout/login skill
- network errors or TLS failures
- `unknown flag` CLI usage errors

## Compatibility

pscale CLI; session tokens and service-token grants. Verified against the pscale-auth community skill.

## Variant phrasings

- pscale 401 unauthorized fix
- pscale 403 forbidden service token
- planetscale cli token expired

## Root cause

401 is authentication (who are you — the credential is invalid), 403 is authorization (what may you do — the credential is valid but unpermitted). They need opposite fixes: refresh vs re-grant.

## Edge cases

- an expired session can surface as 401 on one endpoint and 403 on another; check both
- org role demotions revoke access without touching the token
- service-token grants are set at creation; widening needs a new token

---

Source: [Vectle](https://vectle.com/skills/skl_kJw4nHYHOzk8bAzpUdkLDA). Version: `skv_gDRW2pUhd5b1t3Qkt4Ucbg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
