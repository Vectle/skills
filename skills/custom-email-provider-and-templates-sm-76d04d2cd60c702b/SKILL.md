---
name: "custom-email-provider-and-templates-sm-76d04d2cd60c702b"
description: "Auth0's built-in email provider is for testing. Production needs your own provider before the first real user, plus templates that users actually recognize. Not the full reference manual."
metadata:
  skill_id: "skl_mfkDWlthysyEvr-ljcG27Q"
  title: "Custom email provider and templates: SMTP setup, verification emails, liquid"
  version: "skv_Fkn1l-b5IFqVPwPIhSUDUA"
  updated: "2026-10-03T05:04:28.829092+00:00"
  canonical_url: "https://vectle.com/skills/skl_mfkDWlthysyEvr-ljcG27Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Auth0's built-in email provider is for testing. Production needs your own provider before the first real user, plus templates that users actually recognize. Configure the provider Dashboard > Branding > Email Provider. Verify the domain (SPF/DKIM) at your DNS; without it, verification and reset emails land in spam and your login funnel silently leaks.

## The fix

# Custom email provider

## 1. Configure the provider

Dashboard > Branding > Email Provider. Options: SendGrid, SES, Mailgun, Mandrill, SparkPost, or custom SMTP. Fill in credentials and the from address. Verify the domain (SPF/DKIM) at your DNS; without it, verification and reset emails land in spam and your login funnel silently leaks.

## 2. Templates

Branding > Email Templates: verification email, welcome, password reset, blocked account, MFA enrollment. Each supports Liquid syntax for variables (`user.email`, `application.name`). Customize:

- From name users recognize (your product, not "Auth0").
- Subject lines that survive spam filters (no ALL CAPS, no excessive links).
- The blocked-account template MUST be clear: it is the self-serve unblock path.

## 3. Test

Send test emails from the dashboard. Then do a real signup in incognito and time the verification email arrival. Over a minute consistently means provider or DNS issues.

## 4. Monitor

Watch the provider's bounce/suppression lists. One hard bounce suppresses that address; users then report "never got the email" and resends do nothing until the suppression is cleared.

## Checklist

- Custom provider + verified domain before launch.
- Every template a user can receive has been read by a human on your team.

## When to use this

- This covers exactly what the title says: Custom email provider and templates.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Custom; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Custom behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_mfkDWlthysyEvr-ljcG27Q). Version: `skv_Fkn1l-b5IFqVPwPIhSUDUA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
