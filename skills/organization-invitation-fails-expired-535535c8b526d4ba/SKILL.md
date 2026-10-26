---
name: "organization-invitation-fails-expired-535535c8b526d4ba"
description: "Symptom: invite link errors or the user lands outside the org. Cause: expired invitation, email mismatch, or the login skipped the organization context. Confirmation: the invitation record and the login event's organization field. Not for different error messages."
metadata:
  skill_id: "skl_1fXQXKrCP77XDZlQkF8yhw"
  title: "Organization invitation fails: expired invites, wrong org, JIT membership"
  version: "skv_aUE-ZE37faovgY5ap7iAzA"
  updated: "2026-10-03T14:00:20.434722+00:00"
  canonical_url: "https://vectle.com/skills/skl_1fXQXKrCP77XDZlQkF8yhw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/manage-users/organizations\"]"
---

**TL;DR:** Symptom: invite link errors or the user lands outside the org. Cause: expired invitation, email mismatch, or the login skipped the organization context. Verify New invite to a test email, accept in incognito, confirm membership in the dashboard and the organization claim in the token.

## The error

```text
invitation not found/expired
```

## The fix

1. Expired: invitations expire after 7 days. Old links die.

2. Email mismatch: the invite is bound to an email; logging in with a different email (or a social account with a different email) fails acceptance.

3. Already accepted or already a member: re-invites error.

4. The accept login did not carry the organization context (invitation + organization params both required on the authorize call).

5. Connection mismatch: invite specifies a connection; user authenticated via another.

6. Organizations > your org > Members > Pending invitations: status and expiry.

7. Tenant logs: the failed acceptance event names the reason (expired, email mismatch).

8. The login event: does it carry the organization id? If not, the app dropped the context.

9. Resend the invitation for expired ones; confirm the email matches the user's login identity first.

10. Have the app pass both `invitation` and `organization` on the authorize call.

11. For high-volume onboarding, switch to just-in-time membership on the org's connections and skip invites entirely.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Organization invitation fails.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Organization behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_1fXQXKrCP77XDZlQkF8yhw). Version: `skv_aUE-ZE37faovgY5ap7iAzA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
