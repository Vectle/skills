---
name: "passwordless-errors-expired-codes-rate-e159b3833193b3bd"
description: "Passwordless (email/SMS magic link or OTP) fails when the code expires, the link is opened in a different browser, or the app requests the wrong connection. Not for different error messages."
metadata:
  skill_id: "skl_OhhXt9gl5txTJq6HSlegNg"
  title: "Passwordless errors: expired codes, rate limits, and connection mixups"
  version: "skv_PvchctbppxjZIOVvKysrOA"
  updated: "2026-10-03T14:17:01.110762+00:00"
  canonical_url: "https://vectle.com/skills/skl_OhhXt9gl5txTJq6HSlegNg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Passwordless (email/SMS magic link or OTP) fails when the code expires, the link is opened in a different browser, or the app requests the wrong connection. "Too many requests" means back off; repeated resends lock the user out longer. - Connection mixup: the app must specify the passwordless connection (email or sms).

## The error

```text
Wrong email or verification code
```

# Passwordless errors

## Common failures

- "Wrong email or verification code" / expired code: OTPs expire (configurable, minutes). Users who request twice then enter the FIRST code fail; only the latest code is valid. Tell users to use the newest message.
- Magic link opened on a different device/browser: the link is bound to the browser session that requested it (PKCE verifier in storage). Opening the email on the phone when the login started on desktop fails. Either complete on the same device or use OTP codes which are device-independent.
- Rate limits: passwordless endpoints are throttled per phone/email. "Too many requests" means back off; repeated resends lock the user out longer.
- Connection mixup: the app must specify the passwordless connection (`email` or `sms`). If the tenant has both database and passwordless connections and the app does not pin one, users land on the wrong flow.

## Setup checklist

1. Authentication > Passwordless: enable Email or SMS, configure the provider (Auth0's built-in email is for testing; production needs your own provider).
2. Application > Connections: enable the passwordless connection on the app.
3. Code path: `passwordlessStart` then verify with the code; link path: configure the link lifetime and the redirect.

## Debugging

- Tenant logs show passwordless start/verify events with the failure reason (expired, wrong code, throttled).
- Test with a real inbox/phone; mocked flows hide the newest-code-wins behavior.

## Checklist

- Users told to use the latest code.
- Same-device requirement communicated for magic links.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Passwordless errors.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Passwordless behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_OhhXt9gl5txTJq6HSlegNg). Version: `skv_PvchctbppxjZIOVvKysrOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
