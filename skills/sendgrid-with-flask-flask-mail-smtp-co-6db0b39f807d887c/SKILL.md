---
name: "sendgrid-with-flask-flask-mail-smtp-co-6db0b39f807d887c"
description: "Configure Flask-Mail to send through SendGrid's SMTP relay: the five MAIL_* settings, the literal apikey username, and keeping the key in the environment. Not the full reference manual."
metadata:
  skill_id: "skl_7KO_oiA7fB74K_EjHjO2VQ"
  title: "SendGrid with Flask: Flask-Mail SMTP config"
  version: "skv_8hmPX_l36tyMB0yI3lgquQ"
  updated: "2026-10-03T05:31:39.422105+00:00"
  canonical_url: "https://vectle.com/skills/skl_7KO_oiA7fB74K_EjHjO2VQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Configure Flask-Mail to send through SendGrid's SMTP relay: the five MAIL_* settings, the literal apikey username, and keeping the key in the environment. MAIL_DEFAULT_SENDER must be a verified sender.

## The fix

app.config.update(
  MAIL_SERVER='smtp.sendgrid.net',
  MAIL_PORT=587,
  MAIL_USERNAME='apikey',  # literal string, not your key
  MAIL_USE_TLS=True,
  MAIL_DEFAULT_SENDER='[YOUR_VERIFIED_SENDER]'  # verified sender
)

Set MAIL_PASSWORD from the SENDGRID_API_KEY environment variable (for example via os.environ when building config). Do not hardcode it.

Then:

from flask_mail import Mail, Message
mail = Mail(app)
msg = Message('subject here', recipients=['[RECIPIENT_EMAIL]'])
msg.body = 'plain body'
mail.send(msg)

Checklist:
1. MAIL_USERNAME is exactly 'apikey'.
2. MAIL_USE_TLS True with port 587. Port 465 wants MAIL_USE_SSL instead.
3. MAIL_DEFAULT_SENDER must be a verified sender.
4. In tests, suppress sending (MAIL_SUPPRESS_SEND) or point at sandbox mode so CI stays quiet.

## When to use this

- This covers exactly what the title says: SendGrid with Flask.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_7KO_oiA7fB74K_EjHjO2VQ). Version: `skv_8hmPX_l36tyMB0yI3lgquQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
