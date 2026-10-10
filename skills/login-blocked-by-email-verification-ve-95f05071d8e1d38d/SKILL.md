---
name: "login-blocked-by-email-verification-ve-95f05071d8e1d38d"
description: "New users who cannot log in right after signup are usually parked behind email verification. The fix is a resend flow, not a support ticket."
metadata:
  skill_id: "skl_J4uK5UZ1ei2rAv5eHfPL6w"
  title: "Login blocked by email verification: verification enforcement and resend flows"
  version: "skv_iAJwhcc36AXRjSwRe4td6Q"
  updated: "2026-10-03T15:16:31.207886+00:00"
  canonical_url: "https://vectle.com/skills/skl_J4uK5UZ1ei2rAv5eHfPL6w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** New users who cannot log in right after signup are usually parked behind email verification. The fix is a resend flow, not a support ticket. Check Authentication > Database > your connection > email verification settings and link lifetime. Auth0's built-in provider is rate-limited and not for production; verification emails silently delayed look exactly like "never arrived".

## The fix

1. The tenant requires verified emails (an Action/Rule enforcing `event.user.email_verified`, or the connection setting).

2. The verification email went to spam, or the built-in Auth0 email provider delivered slowly, or the link expired (links expire after a configurable period).

3. Provide a "resend verification email" button in your app calling the Management API `POST /api/v2/jobs/verification-email` with the user_id. Do not make users re-sign-up.

4. Check Authentication > Database > your connection > email verification settings and link lifetime.

5. For production, configure a custom email provider (SendGrid/SES/etc). Auth0's built-in provider is rate-limited and not for production; verification emails silently delayed look exactly like "never arrived".

6. If the product should allow login before verification, change the enforcement Action to warn instead of deny, but gate sensitive actions on `email_verified`.

7. Tenant logs: look for the verification email job events and the failed login with the verification description.

8. Dashboard > User Management > user detail shows email_verified true/false directly.

9. Resend flow exists before users ask.

10. Custom email provider configured for production.

## When to use this

- This covers exactly what the title says: Login blocked by email verification.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Login; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Login behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_J4uK5UZ1ei2rAv5eHfPL6w). Version: `skv_iAJwhcc36AXRjSwRe4td6Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
