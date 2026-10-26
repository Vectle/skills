---
name: "roll-out-mfa-policies-enrollment-recov-142bb95cc6fad64d"
description: "MFA rollout fails on enrollment UX, not cryptography. Stage it: policy per app, enrollment campaign, recovery codes, then enforcement, with adaptive MFA for the risk-based middle ground."
metadata:
  skill_id: "skl_VE1k0muehQG35k3Pwtw4jg"
  title: "Roll out MFA: policies, enrollment, recovery codes, and adaptive MFA"
  version: "skv_8yByKgsoEW6H7E-obvt-6g"
  updated: "2026-10-03T04:43:33.929318+00:00"
  canonical_url: "https://vectle.com/skills/skl_VE1k0muehQG35k3Pwtw4jg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/secure/multi-factor-authentication\"]"
---

**TL;DR:** MFA rollout fails on enrollment UX, not cryptography. Stage it: policy per app, enrollment campaign, recovery codes, then enforcement, with adaptive MFA for the risk-based middle ground. Policies: - Never: off. - Confidence-based / adaptive: step up when risk signals fire (new device, impossible travel, suspicious IP). Best default for most products. - Always: every login.

## The fix

# MFA rollout

## 1. Policy

Dashboard > Security > Multi-factor Auth. Policies:

- Never: off.
- Confidence-based / adaptive: step up when risk signals fire (new device, impossible travel, suspicious IP). Best default for most products.
- Always: every login. Strongest, most annoying.

Set policy per application if the dashboard supports it for your tier; admin tools get Always, the marketing site gets adaptive.

## 2. Factors

Enable TOTP (authenticator apps) as the baseline; add WebAuthn/passkeys where your users' devices support it; SMS only as a fallback (SIM-swap risk, cost). The factor list is the enrollment screen; keep it short or users bounce.

## 3. Enrollment campaign

Do not flip enforcement on day one. Announce, give 2-4 weeks, show enrollment prompts post-login (an Action can nudge users without one), then enforce. Track enrollment rate in tenant logs before the deadline.

## 4. Recovery codes

Show recovery codes at enrollment and offer regeneration in account settings. Users who lose their factor AND have no codes become support tickets; have a verified-identity recovery flow ready (not "email us").

## 5. Enforcement

An Action or the MFA policy enforces. Gate API-side too for sensitive operations: require `amr` claim containing `mfa` on step-up. The id token's `amr` tells you which factors were used.

## Checklist

- Enrollment rate measured before enforcement day.
- Recovery path exists and has been tested by someone who is not you.

## When to use this

- This covers exactly what the title says: Roll out MFA.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Roll; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Roll behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_VE1k0muehQG35k3Pwtw4jg). Version: `skv_8yByKgsoEW6H7E-obvt-6g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
