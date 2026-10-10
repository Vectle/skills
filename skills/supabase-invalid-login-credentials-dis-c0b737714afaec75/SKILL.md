---
name: "supabase-invalid-login-credentials-dis-c0b737714afaec75"
description: "Shows how to fix supabase invalid login credentials: distinguish wrong password from unconfirmed email. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_T8Lw7MJxU107OPsxl0DzVQ"
  title: "Supabase invalid login credentials: distinguish wrong password from unconfirmed email"
  version: "skv_wg1A0vfVKYF3IPPjPnrZsA"
  updated: "2026-10-03T14:19:21.830171+00:00"
  canonical_url: "https://vectle.com/skills/skl_T8Lw7MJxU107OPsxl0DzVQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Invalid login credentials": check whether email confirmation is required. If it is, the most common cause is the user never confirmed.

```text
Invalid login credentials
```

## Steps

1. Check whether email confirmation is required. If it is, the most common cause is the user never confirmed. Resend the confirmation email and check spam, the sender reputation, and your SMTP config.
2. Check the user exists and is confirmed in the dashboard Auth users list. Do this as the developer, never expose the distinction in the UI. If the user is confirmed and the password fails, it is genuinely a wrong password or a stale credential.
3. For password resets, confirm the recovery email arrived and the link was used within its validity window. Expired recovery links produce the same class of confusion.
4. If signups work but logins fail for everyone, check the Auth configuration: a misconfigured SMTP or a disabled email provider breaks the whole confirmation chain at once.
5. Rate limits can masquerade as credential failures during testing. If a script hammered login, wait out the limit before concluding passwords are wrong.

## When to use

You are seeing this: Resend the confirmation email and check spam, the sender reputation, and your SMTP config. Use this skill when you run into "Supabase invalid login credentials: distinguish wrong password from unconfirmed email".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

If it is, the most common cause is the user never confirmed.


---

Source: [Vectle](https://vectle.com/skills/skl_T8Lw7MJxU107OPsxl0DzVQ). Version: `skv_wg1A0vfVKYF3IPPjPnrZsA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
