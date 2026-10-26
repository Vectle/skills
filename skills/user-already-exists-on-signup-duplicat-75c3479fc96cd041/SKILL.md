---
name: "user-already-exists-on-signup-duplicat-75c3479fc96cd041"
description: "Symptom: signup says the user exists, but the user cannot log in. Cause: an identity already exists on another connection. Confirmation: the identities array on the user profile. Not the full reference manual."
metadata:
  skill_id: "skl_RCOB0UhDxtaOSdGk9-KImQ"
  title: "User already exists on signup: duplicate identities and account linking"
  version: "skv_Std7pcFih_MG3VJOo-xn5g"
  updated: "2026-10-03T05:56:23.408349+00:00"
  canonical_url: "https://vectle.com/skills/skl_RCOB0UhDxtaOSdGk9-KImQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/manage-users/user-accounts/user-account-linking\"]"
---

**TL;DR:** Symptom: signup says the user exists, but the user cannot log in. Cause: an identity already exists on another connection. Confirm Dashboard > User Management > search the email: look at the identities array. Check email_verified on each.

## The fix

1. The email exists on a different connection: signed up with Google, now trying database signup. Same email, separate identities.

2. Case or whitespace variance created a near-duplicate.

3. A previous incomplete signup left a database user without a verified email.

4. Link the accounts: Management API link endpoint with the primary user_id and the secondary identity. After linking there is one user with two identities; login works via either.

5. Or delete the stale identity if it was never used (careful: deletion is irreversible; confirm zero logins in tenant logs first).

6. Prevent recurrence: enable account linking via an Action, or use identifier-first to route returning users to their original connection.

## When to use this

- This covers exactly what the title says: User already exists on signup.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with User; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current User behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_RCOB0UhDxtaOSdGk9-KImQ). Version: `skv_Std7pcFih_MG3VJOo-xn5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
