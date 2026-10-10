---
name: "user-still-logged-in-after-logout-app-360aa6859f630667"
description: "Symptom: after logout, visiting login instantly re-authenticates. Cause: only one of the two sessions was cleared. Confirmation: check whether the Auth0 session cookie survives and whether /v2/logout was hit. Not the full reference manual."
metadata:
  skill_id: "skl_FFYBCKUwY3m84XFnctXgAw"
  title: "User still logged in after logout: app session vs Auth0 session vs federated"
  version: "skv_EvdDiYsgjNAitk4hrPmHbA"
  updated: "2026-10-03T14:02:51.926198+00:00"
  canonical_url: "https://vectle.com/skills/skl_FFYBCKUwY3m84XFnctXgAw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: after logout, visiting login instantly re-authenticates. Cause: only one of the two sessions was cleared. App cleared its own session but never hit YOUR_HOST/v2/logout. Confirm - DevTools network: after logout, is there a request to /v2/logout?

## The fix

1. App cleared its own session but never hit `YOUR_HOST/v2/logout`. The Auth0 SSO cookie survives; the next authorize silently re-authenticates.

2. Hit /v2/logout but returnTo was not allowlisted, so Auth0 showed an error page and the user closed it mid-flow; the session may or may not have cleared.

3. Federated IdP session: the user logged in via Google/enterprise; Auth0 session cleared but the IdP session survives, so the next login round-trips the IdP silently. Needs `federated=true` on logout.

4. SDK logout called without logoutParams, so no redirect happened at all (SPA cleared local state only).

5. DevTools network: after logout, is there a request to /v2/logout? If not, the app never logged out of Auth0.

6. After logout, open the tenant domain in a tab: if the Auth0 session cookie is still present, /v2/logout did not complete.

7. Tenant logs: logout events (type `slo` / `flo`) confirm server-side logout.

## When to use this

- This covers exactly what the title says: User still logged in after logout.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with User; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current User behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_FFYBCKUwY3m84XFnctXgAw). Version: `skv_EvdDiYsgjNAitk4hrPmHbA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
