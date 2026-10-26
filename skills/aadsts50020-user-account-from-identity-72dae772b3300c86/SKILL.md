---
name: "aadsts50020-user-account-from-identity-72dae772b3300c86"
description: "Diagnoses Entra ID error AADSTS50020, where the account exists at its identity provider but is not in the tenant the app targets. Use when an agent sees this during cross-tenant or federated sign-in. Covers personal accounts hitting work apps, missing B2B guest setup, and wrong tenant in the request. Not for AADSTS50034 (account missing everywhere) or AADSTS90002 (tenant missing)."
metadata:
  skill_id: "skl_0a-q4x72pV_QM2da9KXc4g"
  title: "AADSTS50020: User account from identity provider does not exist in tenant"
  version: "skv_u4GocZ8D7UyIrR1DKB8jYQ"
  updated: "2026-10-03T04:42:30.850637+00:00"
  canonical_url: "https://vectle.com/skills/skl_0a-q4x72pV_QM2da9KXc4g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/microsoft/openclaw-dev/blob/HEAD/docs/troubleshooting/tenant-subscription-troubleshooting.md\"]"
---

# AADSTS50020: User account from identity provider does not exist in tenant

## TL;DR
The account is real at its identity provider (say, a personal Microsoft account), but it has no footprint in the tenant the app is asking about. The fix is usually on the tenant side: invite the user as a guest, or point the auth request at the tenant where the account actually lives.

## The error
```
AADSTS50020: User account '[user]' from identity provider '[provider]' does not exist in tenant '[tenant]' and cannot access the application '[app]' in that tenant. The account needs to be added as an external user in the tenant first.
```

## Fix it
1. Confirm which tenant the auth request targets and which identity provider the account belongs to. Expected: you can state both plainly, and they do not match.
2. If the user should access this tenant, add them as a B2B guest: Entra ID, Users, New guest user, send the invite. Expected: the user appears in the tenant's user list.
3. Have the guest redeem the invitation before retrying. Expected: first sign-in completes the redemption and the error goes away.
4. If the app should just work for anyone, change the app registration to multi-tenant and have the user sign in against their home tenant. Expected: no guest account needed.
5. Double-check you are not mixing personal and work accounts. A personal account signing into a work-only app is the most common form of this error. Expected: using the right account type clears it.

## When to use this
- An agent sees AADSTS50020 during federated or cross-tenant sign-in.
- A personal Microsoft account tries to use an app registered in a work tenant.

## When NOT to use this
- AADSTS50034 (the account does not exist in any directory you checked).
- AADSTS700016 (the app registration itself is missing).

## Compatibility
- Microsoft Entra ID, B2B collaboration, multi-tenant apps.

### Variant phrasings
- "AADSTS50020" on its own
- "The account needs to be added as an external user in the tenant first"

## Root cause
Entra separates "the account exists somewhere" from "the account exists in this tenant". Federated and personal accounts trip this constantly: the identity provider happily authenticates the user, then the tenant says it has never heard of them.

## Edge cases
- Guests who changed their home-tenant UPN can end up with a stale guest object. Remove and re-invite.
- Conditional Access policies can block the guest even after the invite is redeemed. Check the sign-in log for the real blocker.


---

Source: [Vectle](https://vectle.com/skills/skl_0a-q4x72pV_QM2da9KXc4g). Version: `skv_u4GocZ8D7UyIrR1DKB8jYQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
