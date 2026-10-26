---
name: "too-many-attempts-passwordless-and-sig-736682c05486142e"
description: "Auth0 throttles signup, passwordless sends, and password resets per identifier. Users who hammer resend get locked out longer; the app should rate-limit itself first. Not the full reference manual."
metadata:
  skill_id: "skl_h9oOFSJ_WjnN8eATRx7xIw"
  title: "Too many attempts: passwordless and signup throttles"
  version: "skv_aqpAGwd-N56brKf8ACfwpA"
  updated: "2026-10-03T14:11:39.430699+00:00"
  canonical_url: "https://vectle.com/skills/skl_h9oOFSJ_WjnN8eATRx7xIw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/troubleshoot/customer-support/operational-policies/rate-limit-policy\"]"
---

**TL;DR:** Auth0 throttles signup, passwordless sends, and password resets per identifier. Users who hammer resend get locked out longer; the app should rate-limit itself first. Disable the resend button with a countdown (60s) after each send. Never - Do not auto-retry these endpoints in code. - Do not build a "resend every 10 seconds" loop for tests; use the Management API to verify users in test tenants instead.

## The fix

**TL;DR:** Auth0 throttles signup, passwordless sends, and password resets per identifier. Users who hammer resend get locked out longer; the app should rate-limit itself first. Disable the resend button with a countdown (60s) after each send. Never - Do not auto-retry these endpoints in code. - Do not build a "resend every 10 seconds" loop for tests; use the Management API to verify users in test tenants instead.

## The fix

1. "You have exceeded the maximum number of passwordless tries" / SMS/email throttled.

2. Signup blocked after repeated attempts.

3. "Too many requests" on /dbconnections/change_password.

4. Disable the resend button with a countdown (60s) after each send. This single UI change eliminates most throttle hits.

5. Show the throttle message honestly: "We have sent you several codes; wait a few minutes and try the latest one." Do not show a generic error.

6. Cap resends per session (e.g. 5) then require starting over.

7. For password reset, same pattern: one active ticket at a time; resending invalidates the previous link, so tell the user to use the newest email.

8. Do not auto-retry these endpoints in code.

9. Do not build a "resend every 10 seconds" loop for tests; use the Management API to verify users in test tenants instead.

10. Resend UI is self-throttling with visible countdowns.

11. Users are told to use the newest code/link.

## When to use this

- This covers exactly what the title says: Too many attempts.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Too; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Too behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_h9oOFSJ_WjnN8eATRx7xIw). Version: `skv_aqpAGwd-N56brKf8ACfwpA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
