---
name: "aadsts90002-tenant-tenant-id-not-found-c51090105105491b"
description: "Diagnoses Entra ID error AADSTS90002, where the tenant ID or domain in the auth request does not exist. Use when an agent sees this during login or token requests. Covers typos in the tenant ID, using a deleted tenant, and confusing the tenant ID with the subscription ID. Not for AADSTS50034 (user missing) or AADSTS700016 (app missing)."
metadata:
  skill_id: "skl_r4PRHK2cBIFd0K1K5kbNBg"
  title: "AADSTS90002: Tenant '[tenant-id]' not found"
  version: "skv__VQk7OKWEWj0EgS1-edaDg"
  updated: "2026-10-03T04:43:55.633689+00:00"
  canonical_url: "https://vectle.com/skills/skl_r4PRHK2cBIFd0K1K5kbNBg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AADSTS90002: Tenant '[tenant-id]' not found

## TL;DR
The tenant in your auth request does not exist. Nine times out of ten it is a typo in the tenant ID, a tenant that was deleted, or the subscription ID pasted where the tenant ID should be. Verify the tenant ID in the portal and fix the request.

## The error
```
AADSTS90002: Tenant '[tenant-id]' not found. This may happen if there are no active subscriptions for the tenant. Check with your subscription administrator to provide active subscription for the tenant.
```

## Fix it
1. In the Azure portal go to Microsoft Entra ID, Overview, and copy the Tenant ID exactly. Expected: you have the real tenant ID on your clipboard.
2. Compare it character by character with the tenant in your failing request. Expected: you find the typo or mismatch.
3. If you pasted a subscription ID where the tenant ID belongs, swap it. The subscription ID is not the tenant ID. Expected: the auth request carries the tenant ID.
4. If the tenant was recently deleted or the subscription lapsed, recover the subscription first. Expected: an active subscription backs the tenant again.
5. Retry the auth request with the corrected tenant. Expected: the error is gone.

## When to use this
- An agent sees AADSTS90002 during login, token acquisition, or CLI auth.
- A script hardcodes a tenant ID that may have changed.

## When NOT to use this
- AADSTS50034 (the user is missing) or AADSTS700016 (the app is missing). The tenant itself is fine in those cases.
- AADSTS50020 (the account is fine, it just is not in this tenant).

## Compatibility
- Microsoft Entra ID, Azure CLI, MSAL, any OAuth flow that takes a tenant parameter.

### Variant phrasings
- "AADSTS90002" on its own
- "Tenant not found"
- "no active subscriptions for the tenant"

## Root cause
The tenant lookup happens before anything else in the auth pipeline. A wrong tenant ID fails fast, and the error message helpfully but confusingly mentions subscriptions, which sends people chasing subscription problems when the tenant ID is simply wrong.

## Edge cases
- B2C tenants and work tenants have different ID formats in some flows. Make sure you copied the ID from the right directory.
- Cached tokens or config files can hold a stale tenant ID long after a tenant migration. Search your config for the old value.


---

Source: [Vectle](https://vectle.com/skills/skl_r4PRHK2cBIFd0K1K5kbNBg). Version: `skv__VQk7OKWEWj0EgS1-edaDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
