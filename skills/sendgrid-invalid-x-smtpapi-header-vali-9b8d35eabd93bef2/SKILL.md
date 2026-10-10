---
name: "sendgrid-invalid-x-smtpapi-header-vali-9b8d35eabd93bef2"
description: "SendGrid SMTP sends fail or misbehave and the Email Activity page or Event Webhook points at the X-SMTPAPI header. Covers validating the header JSON and the usual suspects (trailing commas, single quotes, unescaped characters). Not for v3 API errors, bounces, or delivery problems with no header mention."
metadata:
  skill_id: "skl_9zNU3cksyKYdFTaZX-blFA"
  title: "SendGrid invalid X-SMTPAPI header: validate the JSON"
  version: "skv_6GZTEdBAsw5ZuJ1xi0-aKA"
  updated: "2026-10-03T04:29:02.252879+00:00"
  canonical_url: "https://vectle.com/skills/skl_9zNU3cksyKYdFTaZX-blFA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If SendGrid SMTP sends fail and Email Activity or the Event Webhook blames the X-SMTPAPI header, the header value is almost certainly not valid JSON. Copy the exact value your code produces, paste it into a JSON validator, and fix whatever it flags. Trailing commas, single quotes, and unescaped characters are the usual suspects.

What it looks like:

```text
Symptom: sends fail or behave oddly, and the Email Activity page / Event Webhook
data points at the X-SMTPAPI header. It is almost always invalid JSON.
```

Steps:

1. Grab the exact header value your code produces. Log it or print it, dont eyeball the source. Success: you have the literal string being sent.
2. Run it through a JSON validator. Success: the validator passes, or it names the exact position of the problem.
3. Fix the top three offenders: trailing commas, single quotes where JSON wants double quotes, unescaped control characters. Success: the validator passes clean.
4. Resend and check Email Activity. Success: no header errors on the message.

When to use: SMTP sends to SendGrid fail or behave oddly AND Email Activity or the Event Webhook points at the X-SMTPAPI header.

When not to use: you send via the v3 API (there is no X-SMTPAPI header there, debug the JSON body instead), bounces or blocks with no header mention, or auth failures.

Compatibility: SendGrid SMTP (smtp.sendgrid.net), any SMTP library. The filters block works across API versions.

Variants:
- sendgrid x-smtpapi invalid json
- x-smtpapi header malformed
- sendgrid smtp header error

Root cause: the header is parsed as JSON at send time, and one bad byte kills the whole header silently. The failure surfaces later in Email Activity, not at send, which is why it looks mysterious.

Edge cases:
- Your SMTP library may fold or truncate long headers. A valid header can still break if the library rewrites it in transit, so check what actually goes on the wire.
- Keep the header small. It is metadata, not a second message body.
- To turn click tracking off for one SMTP message, the doc shows the filters block: {"filters": {"clicktrack": {"settings": {"enable": 0}}}} in the X-SMTPAPI header.
- If you only need per-message settings over SMTP (categories, unique args, send_at, asm groups), prefer the v3 API: the JSON body is easier to debug than a header.

---

Source: [Vectle](https://vectle.com/skills/skl_9zNU3cksyKYdFTaZX-blFA). Version: `skv_6GZTEdBAsw5ZuJ1xi0-aKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
