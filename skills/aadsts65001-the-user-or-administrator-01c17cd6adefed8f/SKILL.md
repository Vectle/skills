---
name: "aadsts65001-the-user-or-administrator-01c17cd6adefed8f"
description: "Diagnoses Entra ID error AADSTS65001, where sign-in fails because nobody consented to the app's requested permissions. Use when an agent sees this during OAuth login to a Microsoft app. Covers admin consent via the Azure portal, user consent settings, and permissions added after consent was granted. Not for AADSTS700016 (app missing) or credential problems."
metadata:
  skill_id: "skl_hySi8ByIZRqKpNmV4nis8g"
  title: "AADSTS65001: The user or administrator has not consented to use the application"
  version: "skv_YEevXghWCoPFJLV7MmCZGw"
  updated: "2026-10-03T04:43:12.048763+00:00"
  canonical_url: "https://vectle.com/skills/skl_hySi8ByIZRqKpNmV4nis8g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/okapi-ca/ms-365-admin-mcp-server/blob/HEAD/TROUBLESHOOTING.md\"]"
---

# AADSTS65001: The user or administrator has not consented to use the application

## TL;DR
The app is asking for permissions nobody approved yet. A user with admin rights needs to grant consent once in the Azure portal, or an admin needs to allow users to consent themselves. After consent is granted, sign-in works.

## The error
```
AADSTS65001: The user or administrator has not consented to use the application with ID '[app-id]'. Send an interactive authorization request for this user and resource.
```

## Fix it
1. In the Azure portal go to Microsoft Entra ID, App registrations, your app, then API permissions. Expected: you see the list of requested permissions and their consent status.
2. Click "Grant admin consent" and confirm. Expected: the status column changes to granted for the tenant.
3. If the button is missing or fails, you are not an admin. Ask a tenant admin to do it, or have them enable user consent: Entra ID, Enterprise apps, Consent and permissions. Expected: an admin completes the grant.
4. If permissions were added to the app after consent was granted, grant admin consent again. New permissions need fresh consent. Expected: the new permissions show as granted.
5. Retry the sign-in. Expected: the error is gone.

## When to use this
- An agent sees AADSTS65001 during OAuth sign-in to a Microsoft app.
- An app that used to work starts failing after new API permissions were added.

## When NOT to use this
- AADSTS700016 (the app registration does not exist in the tenant at all).
- Bad credentials or expired secrets. Consent errors happen before credential checks.

## Compatibility
- Microsoft Entra ID, any OAuth 2.0 app requesting Microsoft Graph or other API permissions.

### Variant phrasings
- "AADSTS65001" on its own
- "has not consented to use the application"
- "Send an interactive authorization request for this user and resource"

## Root cause
Microsoft's consent framework blocks apps from getting tokens until someone approves the permission list. Admins often lock down user consent, so the first sign-in to any new app fails until an admin grants consent tenant-wide.

## Edge cases
- Multi-tenant apps need admin consent in EACH tenant. Granting it in the home tenant does nothing for customers.
- The "Grant admin consent" button only grants for delegated and application permissions the app currently requests. Changed scopes mean re-consent.


---

Source: [Vectle](https://vectle.com/skills/skl_hySi8ByIZRqKpNmV4nis8g). Version: `skv_YEevXghWCoPFJLV7MmCZGw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
