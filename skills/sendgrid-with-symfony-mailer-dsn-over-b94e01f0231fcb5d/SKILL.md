---
name: "sendgrid-with-symfony-mailer-dsn-over-b94e01f0231fcb5d"
description: "Point Symfony Mailer at SendGrid with a MAILER_DSN: smtp host, the literal apikey username, TLS on 587, and a verified sender address. Not the full reference manual."
metadata:
  skill_id: "skl_pYqOa80NMCioO6xvaN7nYQ"
  title: "SendGrid with Symfony: Mailer DSN over SMTP"
  version: "skv_Yd7UK1rZTb8cTDGp-4yS4w"
  updated: "2026-10-03T04:36:56.994133+00:00"
  canonical_url: "https://vectle.com/skills/skl_pYqOa80NMCioO6xvaN7nYQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/integrating-with-the-smtp-api.md\"]"
---

**TL;DR:** Point Symfony Mailer at SendGrid with a MAILER_DSN: smtp host, the literal apikey username, TLS on 587, and a verified sender address. Never commit the real value. The from address must be verified in SendGrid.

## The fix

In .env:

MAILER_DSN=smtp://smtp.sendgrid.net:587

Set the DSN username to the literal string apikey and the DSN password to your SendGrid API key (at least Mail permissions) via your env management; in a real .env that looks like smtp://apikey value YOUR_KEY_AT_smtp.sendgrid.net:587. Never commit the real value.

Then send with a verified from address:

use Symfony\Component\Mime\Email;

$email = (new Email())
  ->from('[YOUR_VERIFIED_SENDER]')  // verified sender
  ->to('[RECIPIENT_EMAIL]')
  ->subject('subject here')
  ->text('plain body');
$mailer->send($email);

Checklist:
1. Username apikey, not your email. Wrong username is the standard auth failure.
2. Port 587 with TLS. Symfony picks TLS for the smtp:// scheme on 587.
3. The from address must be verified in SendGrid.
4. In dev, use a null or file transport so you do not send real mail.

## When to use this

- This covers exactly what the title says: SendGrid with Symfony.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_pYqOa80NMCioO6xvaN7nYQ). Version: `skv_Yd7UK1rZTb8cTDGp-4yS4w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
