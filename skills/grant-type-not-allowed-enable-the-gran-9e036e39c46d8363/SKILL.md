---
name: "grant-type-not-allowed-enable-the-gran-9e036e39c46d8363"
description: "Auth0 rejects token requests with grant types the application is not allowed to use. The fix is in the dashboard's grant settings, not in the request code."
metadata:
  skill_id: "skl_4wzyIcGz8AZvQtGWsGMhpw"
  title: "Grant type not allowed: enable the grant on the application first"
  version: "skv_Pl5a0926oOZSzSHwJO_n4A"
  updated: "2026-10-03T14:45:12.946192+00:00"
  canonical_url: "https://vectle.com/skills/skl_4wzyIcGz8AZvQtGWsGMhpw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Auth0 rejects token requests with grant types the application is not allowed to use. The fix is in the dashboard's grant settings, not in the request code. Native can also use the device code grant. - Confidential apps (regular web, M2M): add client_credentials and the password-realm extension grants. - Public apps can NEVER use client_credentials. Change the type or create a new app of the right type.

## The fix

**TL;DR:** Auth0 rejects token requests with grant types the application is not allowed to use. The fix is in the dashboard's grant settings, not in the request code. Native can also use the device code grant. - Confidential apps (regular web, M2M): add client_credentials and the password-realm extension grants. - Public apps can NEVER use client_credentials. Change the type or create a new app of the right type.

# Grant type not allowed

## The error

`/oauth/token` returns `403` with `{"error": "unauthorized_client", "error_description": "Grant type 'X' not allowed for the client."}`

## Why it happens

Every application has an allowlist of grant types, derived from its type. Defaults from Auth0's docs:

- Public apps (SPA, native): implicit, authorization_code, refresh_token. Native can also use the device code grant.
- Confidential apps (regular web, M2M): add client_credentials and the password-realm extension grants.
- Public apps can NEVER use client_credentials. That is by design, not a toggle.

## Fix

1. Dashboard > Applications > your app > Settings > Show Advanced Settings > Grant Types. Tick the grant you need.
2. If the grant you need is unavailable for the type (e.g. client_credentials on an SPA), the application TYPE is wrong. Change the type or create a new app of the right type. Do not try to force it.
3. To make a public app confidential (so it can use client_credentials), set token endpoint auth to client_secret_post, client_secret_basic, or private_key_jwt via the Management API Update Client endpoint. But if the app is really a browser app, it should stay public and you should use the authorization code flow instead.

## Common cases

- M2M script using authorization_code: wrong, M2M apps use client_credentials only.
- SPA backend trying client_credentials with the SPA's client id: create a separate M2M application for the backend.
- `password` grant on a new app: disabled by default; enable it explicitly, or better, stop using the password grant.

## Checklist

- The grant in the request is ticked on the application.
- Public vs confidential matches where the code runs.

## When to use this

- This covers exactly what the title says: Grant type not allowed.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Grant; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Grant behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_4wzyIcGz8AZvQtGWsGMhpw). Version: `skv_Pl5a0926oOZSzSHwJO_n4A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
