---
name: "aadsts700016-application-with-identifi-93e0f17b4fece3ce"
description: "Diagnoses Entra ID error AADSTS700016, where the app ID in your auth request does not exist in the targeted tenant. Use when an agent hits this during az login, MSAL, or OAuth sign-in. Covers single-tenant vs multi-tenant app registrations, wrong tenant ID in the request, and propagation delays. Not for AADSTS50034 (user missing) or AADSTS90002 (tenant missing)."
metadata:
  skill_id: "skl_A8TLFys-hrvLfD1hrxFnDg"
  title: "AADSTS700016: Application with identifier '[app-id]' was not found in the directory"
  version: "skv_qB9hO0FXkMOHAhRhXDvpxg"
  updated: "2026-10-03T04:41:05.514425+00:00"
  canonical_url: "https://vectle.com/skills/skl_A8TLFys-hrvLfD1hrxFnDg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AADSTS700016: Application with identifier '[app-id]' was not found in the directory

## TL;DR
The app registration you are authenticating against does not exist in the tenant your auth request targets. Either the app is single-tenant and you are pointing at the wrong tenant, or the app ID itself is wrong. Check the app registration's home tenant, then make the app multi-tenant or fix the tenant ID in your auth request.

## The error
```
AADSTS700016: Application with identifier '[app-id]' was not found in the directory '[directory]'. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant.
```

## Fix it
1. In the Azure portal go to Microsoft Entra ID, then App registrations, and search for the app ID from the error. Expected: you find the app and see its home tenant on the overview page.
2. If the app is registered in tenant A but your auth request targets tenant B, switch the request to tenant A. In the portal: Authentication, then Supported account types. Expected: you can see which account types the app allows.
3. If users from other tenants need to sign in, change Supported account types to "Accounts in any organizational directory". Expected: the setting saves and the app can be consented into other tenants.
4. If the app ID matches nothing anywhere, you copied it wrong. Re-copy the Application (client) ID from the overview page. Expected: the identifier matches character for character.
5. If the app was created minutes ago, wait a few minutes and retry. New registrations take time to propagate. Expected: the error clears on retry.

## When to use this
- An agent sees AADSTS700016 during az login, MSAL, or an OAuth sign-in flow.
- A single-tenant app (like a Teams bot) works for its home tenant but fails for anyone else.

## When NOT to use this
- AADSTS50034 (the user account does not exist) or AADSTS90002 (the tenant itself is not found). Different root causes.
- AADSTS65001 (admin consent missing). The app exists there, consent is the problem.

## Compatibility
- Microsoft Entra ID (formerly Azure AD), MSAL libraries, Azure Identity SDKs, Azure CLI.

### Variant phrasings
- "Application with identifier was not found in the directory"
- "AADSTS700016" on its own
- "The application has not been installed by the administrator of the tenant"

## Root cause
Entra looks up the app by ID in the tenant named in the auth request. If the app was never created or consented in that tenant, the lookup fails. The classic trigger is a single-tenant registration used from a different tenant. That is exactly what the microsoft-teams-samples issue hit: a bot configured single-tenant failed the moment auth came from another directory.

## Edge cases
- Personal Microsoft accounts hitting this against a work app: the app must allow personal accounts, or the user needs a guest account in the tenant.
- A deleted and re-created registration keeps the same app ID but the service principal in other tenants can go stale. Re-consent after recreating.


---

Source: [Vectle](https://vectle.com/skills/skl_A8TLFys-hrvLfD1hrxFnDg). Version: `skv_qB9hO0FXkMOHAhRhXDvpxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
