---
name: "aadsts50034-the-user-account-does-not-e86cfb51adb6825a"
description: "Diagnoses Entra ID error AADSTS50034, where the user account in the sign-in request is not in the targeted tenant. Use when an agent sees this during login or token acquisition. Covers guest vs member mixups, typos in the UPN, wrong tenant in the request, and deleted or never-provisioned accounts. Not for AADSTS700016 (app missing) or AADSTS90002 (tenant missing)."
metadata:
  skill_id: "skl_6GvrgjVWHfR_igvhsKL_sw"
  title: "AADSTS50034: The user account does not exist in the directory"
  version: "skv_HNgoGYyKZmeOGzxzMCuzew"
  updated: "2026-10-03T04:41:51.933097+00:00"
  canonical_url: "https://vectle.com/skills/skl_6GvrgjVWHfR_igvhsKL_sw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AADSTS50034: The user account does not exist in the directory

## TL;DR
The username in the sign-in request is not a member or guest of the tenant being authenticated against. Usually it is a typo in the UPN, the wrong tenant in the auth request, or the account is a guest in one tenant but you are signing into another. Confirm the exact UPN and the tenant, then fix whichever is wrong.

## The error
```
AADSTS50034: The user account does not exist in the [tenant] directory. To sign into this application, the account must be added to the directory.
```

## Fix it
1. Read the UPN in the error carefully and compare it to the real one, character by character. Expected: you spot (or rule out) a typo.
2. Check which tenant the auth request targets. If the user is a guest in tenant B but the request targets tenant A, point the request at tenant B. Expected: the tenant in the request matches where the account actually lives.
3. In the Azure portal, search Microsoft Entra ID users for the account. Expected: the user shows up as a member or guest in the target tenant.
4. If the user should exist but does not, invite them as a guest or create the account, then retry. Expected: sign-in succeeds after the account exists.
5. For service automation hitting this with a user credential, switch to a managed identity or service principal. User accounts get deleted and break automation. Expected: auth no longer depends on a human account.

## When to use this
- An agent sees AADSTS50034 during interactive login or username-based token acquisition.
- A guest user tries to access a resource in the wrong tenant.

## When NOT to use this
- AADSTS700016 (the app is missing) or AADSTS90002 (the tenant is missing).
- AADSTS50020 (the account exists in its identity provider but not in this tenant). Close cousin, different fix.

## Compatibility
- Microsoft Entra ID, all auth flows that take a username.

### Variant phrasings
- "AADSTS50034" on its own
- "To sign into this application, the account must be added to the directory"

## Root cause
Entra resolves the user in the tenant named by the auth request. Guests are the usual surprise: someone invited into tenant B tries to sign into an app targeting tenant A and gets this error, even though their account is perfectly valid somewhere else.

## Edge cases
- Recently deleted accounts can linger in caches. If the portal shows the user but auth says otherwise, wait for replication or check for a soft-deleted account.
- B2B guests must redeem their invitation before first sign-in. An unredeemed guest gets this error.


---

Source: [Vectle](https://vectle.com/skills/skl_6GvrgjVWHfR_igvhsKL_sw). Version: `skv_HNgoGYyKZmeOGzxzMCuzew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
