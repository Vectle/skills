---
name: "sendgrid-smtp-relay-settings-host-apik-ad3b62238ca1f06b"
description: "The exact SMTP settings agents get wrong: smtp.sendgrid.net, the literal username apikey, port 587 for TLS, and the per-connection limits. Plus the newline-in-pasted-key auth trap. Not the full reference manual."
metadata:
  skill_id: "skl_hRRLg1GGgsV9bdiN-WWRJg"
  title: "SendGrid SMTP relay settings: host, apikey username, ports, limits"
  version: "skv_xVpCDnisSxtX_Bk_Xy1zGA"
  updated: "2026-10-03T04:39:00.969397+00:00"
  canonical_url: "https://vectle.com/skills/skl_hRRLg1GGgsV9bdiN-WWRJg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The exact SMTP settings agents get wrong: smtp.sendgrid.net, the literal username apikey, port 587 for TLS, and the per-connection limits. Plus the newline-in-pasted-key auth trap. Use these settings in any SMTP client, framework mailer, or relay config: - Host: smtp.sendgrid.net - Username: the literal string apikey. Use the v3 API directly when you need dynamic templates, batch scheduling, or per-recipient personalizations, which SMTP cannot express as cleanly.

## The fix

1. Host: smtp.sendgrid.net

2. Username: the literal string apikey. Not your account email, not the key name. This is the number-one misconfiguration.

3. Password value your SendGrid API key (needs at least Mail permissions). Paste it carefully: no trailing newline or whitespace, because SMTP is line-oriented and stray linefeeds break auth.

4. Port: 587 with TLS (recommended). 25 and 2525 also work for TLS/unencrypted; 465 is for SSL. Limits: 5,000 messages per SMTP connection, and 10,000 concurrent connections from a single server. If you send bulk, reuse connections instead of opening one per message. SMTP is the right call when a framework already speaks SMTP (Django, Laravel, Rails, Flask-Mail) and you do not want an SDK. Use the v3 API directly when you need dynamic templates, batch scheduling, or per-recipient personalizations, which SMTP cannot express as cleanly.

## When to use this

- This covers exactly what the title says: SendGrid SMTP relay settings.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_hRRLg1GGgsV9bdiN-WWRJg). Version: `skv_xVpCDnisSxtX_Bk_Xy1zGA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
