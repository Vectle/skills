---
name: "sendgrid-with-rails-actionmailer-smtp-656a9ca185a63886"
description: "Wire ActionMailer to SendGrid: smtp_settings with the apikey username, plain auth, and STARTTLS on 587. Includes the delivery-method check for each environment. Not the full reference manual."
metadata:
  skill_id: "skl_pUkQqvmOsYZ9XdTFOsGdbw"
  title: "SendGrid with Rails: ActionMailer SMTP settings"
  version: "skv_Muj2MQ0ctcB73Z-1PCbBQw"
  updated: "2026-10-03T04:45:32.855627+00:00"
  canonical_url: "https://vectle.com/skills/skl_pUkQqvmOsYZ9XdTFOsGdbw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/integrating-with-the-smtp-api.md\"]"
---

**TL;DR:** Wire ActionMailer to SendGrid: smtp_settings with the apikey username, plain auth, and STARTTLS on 587. Includes the delivery-method check for each environment. Set the default from to a verified sender: config.action_mailer.default_options = { from: '[YOUR_VERIFIED_SENDER]' }.

## The fix

1. user_name is exactly 'apikey'. Your account email here fails auth.

2. enable_starttls_auto with port 587. Port 465 needs tls: true instead, which is a different setting.

3. In development, keep delivery_method at :test or use the letter_opener pattern so you do not send real mail.

4. A 403-style failure from the API usually means the key lacks Mail Send scope; an SMTP auth failure usually means the username or pasted key is wrong.

## When to use this

- This covers exactly what the title says: SendGrid with Rails.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_pUkQqvmOsYZ9XdTFOsGdbw). Version: `skv_Muj2MQ0ctcB73Z-1PCbBQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
