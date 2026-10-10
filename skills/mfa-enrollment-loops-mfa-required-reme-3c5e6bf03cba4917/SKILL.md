---
name: "mfa-enrollment-loops-mfa-required-reme-3c5e6bf03cba4917"
description: "An MFA loop is when the user completes MFA and gets asked again, or can never finish enrollment. Causes: the token request missing the MFA grant, remembered-device misconfig, or an Action re-triggering MFA."
metadata:
  skill_id: "skl_KaIBLh-XMIBB6p9lJp9LGw"
  title: "MFA enrollment loops: mfa_required, remembered devices, and policy conflicts"
  version: "skv_TCnU_uqth7UPAN15maZtuw"
  updated: "2026-10-03T14:35:45.367688+00:00"
  canonical_url: "https://vectle.com/skills/skl_KaIBLh-XMIBB6p9lJp9LGw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** An MFA loop is when the user completes MFA and gets asked again, or can never finish enrollment. Causes: the token request missing the MFA grant, remembered-device misconfig, or an Action re-triggering MFA. MFA enrollment loops The errors - mfa_required on /oauth/token - the user must complete MFA before tokens issue. Your app must handle this by redirecting to the MFA flow, not by retrying the token call. - Endless TOTP/SMS prompts after successful enrollment. - "MFA already enrolled" colliding with "enrollment required".

# MFA enrollment loops

## The errors

- `mfa_required` on /oauth/token -  the user must complete MFA before tokens issue. Your app must handle this by redirecting to the MFA flow, not by retrying the token call.
- Endless TOTP/SMS prompts after successful enrollment.
- "MFA already enrolled" colliding with "enrollment required".

## Handling mfa_required (RaaS / API-driven)

The /oauth/token response includes an `mfa_token`. Use it with the MFA grants:

1. `POST /mfa/challenge` with the mfa token to start the challenge.
2. `POST /oauth/token` with `grant_type=http://auth0.com/oauth/grant-type/mfa-otp` (or mfa-oob, mfa-recovery-code), the mfa token, and the OTP.
3. Only then do you get the real tokens.

Skipping step 2 and retrying the original grant loops forever.

## Remembered devices

Dashboard > Security > Multi-factor Auth > Remember Device. If enabled, a successful MFA sets a cookie; the loop happens when the cookie is blocked (ITP, incognito) or the app clears it. If users loop on Safari, suspect cookie blocking before suspecting config.

## Policy conflicts

- An Action that calls `api.multifactor.enable()` on every login re-prompts even enrolled users. Gate it: check `event.user.multifactor` first.
- Requiring MFA for a connection where enrollment is impossible (e.g. passwordless SMS + SMS MFA) strands users. Keep factor and connection compatible.

## Recovery codes

Enrollment without showing recovery codes burns users later. Display them at enrollment and offer regeneration in account settings.

## Checklist

- mfa_required is handled as a flow, not an error to retry.
- Actions enable MFA conditionally, not unconditionally.
- Test enrollment end to end in a clean browser profile.

## When to use this

- This covers exactly what the title says: MFA enrollment loops.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with MFA; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current MFA behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_KaIBLh-XMIBB6p9lJp9LGw). Version: `skv_TCnU_uqth7UPAN15maZtuw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
