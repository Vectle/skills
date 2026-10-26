---
name: "sendgrid-with-django-smtp-backend-sett-a3e28e7f962ce504"
description: "Wiring Django's SMTP email backend to SendGrid. Covers the six settings, the literal apikey username trap, pulling the key from the environment, and the verified-sender requirement. Not for the SendGrid v3 API, django-anymail, or delivery/reputation problems."
metadata:
  skill_id: "skl_LIGv5aUK85jWjd6w5IeX-g"
  title: "SendGrid with Django: SMTP backend settings that actually work"
  version: "skv_qcEjWskI-6UU4tg2lIVYOQ"
  updated: "2026-10-03T04:37:35.830361+00:00"
  canonical_url: "https://vectle.com/skills/skl_LIGv5aUK85jWjd6w5IeX-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/integrating-with-the-smtp-api.md\",\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\"]"
---

TL;DR: Django talks to SendGrid over plain SMTP with six settings. Backend is django.core.mail.backends.smtp.EmailBackend, host smtp.sendgrid.net, port 587 with TLS, the username is the literal string apikey (not your key, not your email), and the password comes from the SENDGRID_API_KEY environment variable, never committed to settings. The from address must be a verified sender. In tests, use the locmem backend or sandbox mode so CI never sends real mail.

Settings (in settings.py or your settings module):

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'  # literal string, not your key
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '[YOUR_VERIFIED_SENDER]'  # must be a verified sender
```

Set the mail password from the SENDGRID_API_KEY environment variable (via os.environ in settings or your process manager). Do not commit the key in settings.py.

Checklist when mail does not go out:

1. EMAIL_HOST_USER is exactly 'apikey'. Using your email or key name here gives an auth failure. Success: auth passes.
2. TLS on 587, not SSL. Port 465 wants SSL, which Django's backend does not do with USE_TLS. Success: the handshake completes.
3. The from address is verified in the SendGrid console (domain auth or single sender). Success: no sender-identity rejection.

When to use: wiring Django to SendGrid for the first time, or debugging Django mail that silently never arrives.

When not to use: the SendGrid v3 API or django-anymail (different integration), bounces/blocks/deliverability problems (different layer), or non-Django frameworks.

Compatibility: Django's SMTP email backend, SendGrid SMTP, Python 3.

Variants:
- django sendgrid smtp settings
- sendgrid apikey username django
- django email sendgrid not sending

Root cause: almost every Django-plus-SendGrid failure is one of three things: the username is not the literal string apikey, the port/TLS combo is wrong, or the from address was never verified. The settings look right at a glance, which is why the checklist reads top to bottom.

Edge cases:
- In tests, use Django's locmem backend or sandbox mode so CI never sends real mail.
- Rotating the API key means updating the environment variable, not settings.py. If mail breaks right after a rotation, the env var is the first place to look.

---

Source: [Vectle](https://vectle.com/skills/skl_LIGv5aUK85jWjd6w5IeX-g). Version: `skv_qcEjWskI-6UU4tg2lIVYOQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
