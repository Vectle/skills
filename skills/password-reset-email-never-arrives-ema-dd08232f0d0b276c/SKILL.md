---
name: "password-reset-email-never-arrives-ema-dd08232f0d0b276c"
description: "Symptom: user requests a reset, no email arrives. Cause: email provider config, spam, or an expired/consumed ticket. Confirmation: the password-reset job events in tenant logs. Not the full reference manual."
metadata:
  skill_id: "skl_HeAznOo-PQvTv-vSKCduJg"
  title: "Password reset email never arrives: email provider, ticket expiry, logs"
  version: "skv_nW25NFyXggO-6ShjO6jETg"
  updated: "2026-10-03T13:58:31.699543+00:00"
  canonical_url: "https://vectle.com/skills/skl_HeAznOo-PQvTv-vSKCduJg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/customize/email\"]"
---

**TL;DR:** Symptom: user requests a reset, no email arrives. Cause: email provider config, spam, or an expired/consumed ticket. Configure a custom provider (SendGrid, SES, Mailgun, SMTP). Check the provider's suppression/bounce list: one hard bounce suppresses future sends to that address.

# Diagnose: password reset email missing

## Symptom

"Forgot password" submits fine; nothing lands in the inbox.

## Likely causes

1. Built-in Auth0 email provider: rate-limited, not for production, delivers slowly or not at all under load. Configure a custom provider (SendGrid, SES, Mailgun, SMTP).
2. Spam/junk, or corporate filters eating it. Check the provider's suppression/bounce list: one hard bounce suppresses future sends to that address.
3. Ticket expired or already used: reset links expire (configurable lifetime) and are single-use. Requesting twice invalidates the first link.
4. Wrong connection: the reset was requested against a database connection the user is not on (e.g. user is social-only; password reset is meaningless for them).

## Confirm

- Tenant logs: look for the password reset request and email job events. "Sent" with no arrival = provider/deliverability. No event at all = the request never reached Auth0 (check the app's call).
- Email provider dashboard: bounces, suppressions, deferred queues.
- User Management > the user: which connection are they on? Social-only users cannot reset a database password.

## Fix

Custom email provider, warm it up, monitor bounces. Set the ticket lifetime deliberately (short enough to be safe, long enough for slow inboxes). One active ticket per user; tell users to use the newest email.

## Verify

Request a reset for a test user on the same provider and confirm arrival within a minute, link works once, second click fails cleanly.

## When to use this

- This covers exactly what the title says: Password reset email never arrives.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Password; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Password behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_HeAznOo-PQvTv-vSKCduJg). Version: `skv_nW25NFyXggO-6ShjO6jETg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
