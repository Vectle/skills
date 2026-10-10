---
name: "sendgrid-with-laravel-smtp-mailer-env-34aedd585ac66a88"
description: "Configure Laravel's SMTP mailer for SendGrid via MAIL_* env vars: host, the literal apikey username, TLS on 587, and a verified MAIL_FROM_ADDRESS. Not the full reference manual."
metadata:
  skill_id: "skl_jeWwmiORSMzrmaYz7Eh0Zw"
  title: "SendGrid with Laravel: SMTP mailer env config"
  version: "skv_CGg9-PsaidsZntvz-9Gc5Q"
  updated: "2026-10-03T05:09:14.473561+00:00"
  canonical_url: "https://vectle.com/skills/skl_jeWwmiORSMzrmaYz7Eh0Zw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Configure Laravel's SMTP mailer for SendGrid via MAIL_* env vars: host, the literal apikey username, TLS on 587, and a verified MAIL_FROM_ADDRESS. MAIL_FROM_ADDRESS must be a verified sender in SendGrid or the send fails.

## The fix

1. MAIL_USERNAME is the literal string apikey. Putting your email here is the classic failure.

2. MAIL_ENCRYPTION=tls pairs with port 587. Port 465 wants ssl.

3. MAIL_FROM_ADDRESS must be a verified sender in SendGrid or the send fails.

4. After changing .env, clear the config cache (config:clear) or the old values stick.

5. For local dev, set MAIL_MAILER=log or use sandbox mode so you do not send real mail from your laptop.

## When to use this

- This covers exactly what the title says: SendGrid with Laravel.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_jeWwmiORSMzrmaYz7Eh0Zw). Version: `skv_CGg9-PsaidsZntvz-9Gc5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
