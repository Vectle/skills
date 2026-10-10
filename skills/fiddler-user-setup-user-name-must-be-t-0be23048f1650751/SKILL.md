---
name: "fiddler-user-setup-user-name-must-be-t-0be23048f1650751"
description: "Fix for Fiddler user setup: User Name must be the email, and pending-setup users cannot log in: If you choose 'Setup authentication later for this user', that user cannot log in until they complete authentication setup, so use the invitation-email option for anyone who needs access now. Use this when you hit exactly this in Fiddler user setup. Not for different errors or different tools."
metadata:
  skill_id: "skl_gCMWM5LjRgZcsEz0u4Ssgw"
  title: "Fiddler user setup: User Name must be the email, and pending-setup users cannot log in"
  version: "skv_d_CKhUiu5ui79GD6TWsyDg"
  updated: "2026-10-03T13:58:57.335867+00:00"
  canonical_url: "https://vectle.com/skills/skl_gCMWM5LjRgZcsEz0u4Ssgw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If you choose 'Setup authentication later for this user', that user cannot log in until they complete authentication setup, so use the invitation-email option for anyone who needs access now. [Official Fiddler docs (email login)]: When adding users through the AuthN console, the User Name field must contain the email address exactly, it is the login identifier.

```text
Fiddler user setup: User Name must be the email, and pending-setup users cannot log in
```

## Fix
1. If you choose 'Setup authentication later for this user', that user cannot log in until they complete authentication setup, so use the invitation-email option for anyone who needs access now.
   Expected: the request routes instead of erroring.

## Details
[Official Fiddler docs (email login)]: When adding users through the AuthN console, the User Name field must contain the email address exactly, it is the login identifier. Invitation emails do not expire automatically; resend them from the Users section. And keep at least one user with the Org Owner or Org User Manager role, or nobody can manage email-auth users. App roles (Org Admin, Org Member) are assigned separately after login. Context: Official docs (Fiddler email login guide): documents the user-setup gotchas that trip admins. The User Name field must contain the email address exactly, users created with 'setup authentication later' cannot log in at all, and you must always keep at least one Org Owner or Org User Manager.

## When to use
You hit exactly this: Fiddler user setup: User Name must be the email, and pending-setup users cannot log in in Fiddler user setup.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Fiddler user setup.

---

Source: [Vectle](https://vectle.com/skills/skl_gCMWM5LjRgZcsEz0u4Ssgw). Version: `skv_d_CKhUiu5ui79GD6TWsyDg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
