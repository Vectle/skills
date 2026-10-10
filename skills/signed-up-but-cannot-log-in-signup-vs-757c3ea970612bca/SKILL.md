---
name: "signed-up-but-cannot-log-in-signup-vs-757c3ea970612bca"
description: "Symptom: user created an account minutes ago and login fails. Cause: usually email verification enforcement or a password/connection mixup. Confirmation: compare the signup event with the failed login event. Not for different error messages."
metadata:
  skill_id: "skl_Qu1g-Y-9Te98BAlBdVsH8w"
  title: "Signed up but cannot log in: signup vs login event types"
  version: "skv_EUjFUroQG5a__1MVJJrQhQ"
  updated: "2026-10-03T14:06:33.557268+00:00"
  canonical_url: "https://vectle.com/skills/skl_Qu1g-Y-9Te98BAlBdVsH8w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Symptom: user created an account minutes ago and login fails. Cause: usually email verification enforcement or a password/connection mixup. Confirm Monitoring > Logs: find the signup event for the email, note the connection. Check Dashboard > User Management > the user: email_verified flag and the identities array (one entry per connection).

## The fix

1. Email verification required before first login.

2. User signed up with social but tries password login (or the reverse): two different connections, two different credential sets.

3. Password manager saved a typo'd password at signup.

4. Database connection import mode or custom DB script failing the login half.

5. Verification gate: provide the resend-verification flow; do not delete and recreate the user.

6. Wrong connection: point the user at the right button, or enable account linking so both identities merge.

7. Typo'd password value password reset flow.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Signed up but cannot log in.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Signed behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_Qu1g-Y-9Te98BAlBdVsH8w). Version: `skv_EUjFUroQG5a__1MVJJrQhQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
