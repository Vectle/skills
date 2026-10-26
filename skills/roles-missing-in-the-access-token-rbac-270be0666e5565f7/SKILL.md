---
name: "roles-missing-in-the-access-token-rbac-270be0666e5565f7"
description: "Symptom: the user has roles in the dashboard but the token has no roles or permissions. Cause: the API's RBAC toggles are off, or roles live at the org level. Confirmation: compare the token claims with the user's dashboard roles. Not for different error messages."
metadata:
  skill_id: "skl_iBXNpTO6yZxALebGSh3Vlw"
  title: "Roles missing in the access token -  RBAC settings and permissions flag"
  version: "skv_xClLHnvwM-TKeDvU-A2WBg"
  updated: "2026-10-03T13:53:32.069375+00:00"
  canonical_url: "https://vectle.com/skills/skl_iBXNpTO6yZxALebGSh3Vlw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/manage-users/access-control/rbac\"]"
---

**TL;DR:** Symptom: the user has roles in the dashboard but the token has no roles or permissions. Cause: the API's RBAC toggles are off, or roles live at the org level. Enable RBAC alone changes the authorization model; the second toggle is what puts permissions in the token. Confirm - Decode the access token (not the id token).

## The fix

1. API RBAC settings off: Applications > APIs > your API > Settings > "Enable RBAC" and "Add Permissions in the Access Token" are both required. Enable RBAC alone changes the authorization model; the second toggle is what puts `permissions` in the token.

2. Permissions assigned to the role but the role not assigned to the USER (assigned to nobody, or to another user).

3. Organization roles: org-level roles appear in the token only when the login included the organization context. A login without `organization` gets no org roles.

4. Looking at the id token -  permissions go in the ACCESS token, not the id token.

5. Caching: the token was minted before the role assignment. Tokens are snapshots.

6. Decode the access token (not the id token). Check `permissions` array and `scope`.

7. Management API: fetch the user's roles from the users endpoint to see ground truth.

8. Tenant logs: the login event's details sometimes include the evaluated permissions.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Roles missing in the access token -  RBAC settings and permissions flag.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Roles behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_iBXNpTO6yZxALebGSh3Vlw). Version: `skv_xClLHnvwM-TKeDvU-A2WBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
