---
name: "sendgrid-click-tracking-rewrites-links-05d387fec407f2bc"
description: "Links work in tests but fail in sent mail with invalid-signature or expired-token errors because SendGrid click tracking wraps links in a redirect. Covers confirming the cause, per-message and per-link opt-out. Not for open tracking or links that were broken before sending."
metadata:
  skill_id: "skl_VZrF_kuj_PVVa4IwotBh5w"
  title: "SendGrid click tracking rewrites links and breaks signed URLs"
  version: "skv_LuRbSMi--nUzQoYpi8Xi-g"
  updated: "2026-10-03T04:44:19.438963+00:00"
  canonical_url: "https://vectle.com/skills/skl_VZrF_kuj_PVVa4IwotBh5w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"http://sendgrid.com/docs/Glossary/email_error_messages.html\",\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\"]"
---

TL;DR: Click tracking wraps every link in a SendGrid redirect, which breaks signed URLs, password-reset tokens, and any link whose signature covers the exact URL. Confirm it by comparing the link in the received mail with the original: a sendgrid.net redirect wrapper means the signature no longer matches. Disable tracking per message (tracking_settings.click_tracking.enable false in the v3 API, or the clicktrack filter in X-SMTPAPI for SMTP) or per link with the clicktracking=false attribute on the anchor tag. Do not disable tracking globally to fix one flow.

What it looks like:

```text
Symptom: links work in tests but fail in sent mail with invalid-signature or
expired-token errors.
```

Steps:

1. Confirm click tracking is the cause: compare the link in the received mail with the original. Success: you see the sendgrid.net redirect wrapper.
2. Disable for the message: tracking_settings.click_tracking.enable false (v3 API) or the clicktrack filter (SMTP). Success: the setting is off for that send only.
3. Or disable for one link inside an otherwise tracked mail: add clicktracking=false to that anchor tag. Success: that link arrives byte-identical, the rest still tracked.
4. Resend and verify the raw link survives byte-identical. Success: signatures validate.

When to use: signed or tokenized links failing only in sent mail.

When not to use: links broken in tests too (the bug is yours), open-tracking questions, or engagement data you actually want to keep (use the per-link opt-out).

Compatibility: SendGrid v3 API and SMTP, all plans with click tracking.

Variants:
- sendgrid click tracking breaks signed url
- sendgrid password reset link invalid
- disable click tracking one link

Root cause: the signature was computed over the original URL, and click tracking changes the URL the recipient clicks. The signature check then fails, correctly, against a URL it never signed.

Edge cases:
- Rule: any URL carrying a cryptographic signature or single-use token goes out untracked.
- Do not disable tracking globally to fix one flow. You lose engagement data everywhere for a local problem.

---

Source: [Vectle](https://vectle.com/skills/skl_VZrF_kuj_PVVa4IwotBh5w). Version: `skv_LuRbSMi--nUzQoYpi8Xi-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
