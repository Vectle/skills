---
name: "account-blocked-brute-force-shield-bre-78c86ded6153a9df"
description: "A blocked account shows a clear message but the cause (brute-force shield vs breached password vs admin block) decides the unblock path. Not the full reference manual."
metadata:
  skill_id: "skl_3ioxGogqpDDHvuFXukh2-Q"
  title: "Account blocked: brute-force shield, breached password, and unblock flows"
  version: "skv_gi0_k1PyLRjriicwyczGKg"
  updated: "2026-10-03T15:20:39.746631+00:00"
  canonical_url: "https://vectle.com/skills/skl_3ioxGogqpDDHvuFXukh2-Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** A blocked account shows a clear message but the cause (brute-force shield vs breached password vs admin block) decides the unblock path. Not the full reference manual. It blocks the account for the offending IP/account pair. - Breached password value user must change the password; the block lifts on reset. - Admin-blocked via Management API or dashboard: only an admin unblocks. Check Security > Attack Protection > Brute-Force Protection settings: thresholds, whether to notify, and shield vs suspend behavior.

## The fix

**TL;DR:** A blocked account shows a clear message but the cause (brute-force shield vs breached password vs admin block) decides the unblock path. It blocks the account for the offending IP/account pair. - Breached password value user must change the password; the block lifts on reset. - Admin-blocked via Management API or dashboard: only an admin unblocks. Check Security > Attack Protection > Brute-Force Protection settings: thresholds, whether to notify, and shield vs suspend behavior.

# Account blocked

## The messages

- "Your account has been blocked after multiple consecutive login attempts": brute-force protection shield tripped. It blocks the account for the offending IP/account pair.
- Breached password value user must change the password; the block lifts on reset.
- Admin-blocked via Management API or dashboard: only an admin unblocks.

## Unblock paths

1. Brute-force shield: the user can usually unblock via the "unblock account" email Auth0 sends, or an admin unblocks in Dashboard > User Management > user > Unblock. The shield resets automatically after the block period if attack protection settings allow.
2. Breached password value password reset flow. Do not just unblock; the password is in breach corpuses.
3. Check Security > Attack Protection > Brute-Force Protection settings: thresholds, whether to notify, and shield vs suspend behavior. Defaults are aggressive; tune before launch.

## Avoiding false blocks

- Shared office IPs + a few users typo-ing passwords = shield trips for everyone behind that NAT. Consider the "suspicious IP throttling" stage before the shield, and set sane thresholds.
- Load tests against login with bad passwords will trip the shield and block your test users. Exclude test traffic or use a separate tenant.
- Notify users: enable the blocked-account email template so users can self-serve instead of filing tickets.

## Checklist

- Know which of the three blocks you are looking at before acting.
- Attack protection tuned before production traffic, not after the first incident.

## When to use this

- This covers exactly what the title says: Account blocked.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Account; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Account behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_3ioxGogqpDDHvuFXukh2-Q). Version: `skv_gi0_k1PyLRjriicwyczGKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
