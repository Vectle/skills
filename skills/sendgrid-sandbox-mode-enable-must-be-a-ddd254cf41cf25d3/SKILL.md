---
name: "sendgrid-sandbox-mode-enable-must-be-a-ddd254cf41cf25d3"
description: "Quoting the sandbox enable flag gives a confusing validation error. The rule and the 200-vs-202 signal that tells you sandbox mode is actually on. Not for different error messages."
metadata:
  skill_id: "skl_Ei9S7RpSxQeBSxlOeIj_pw"
  title: "SendGrid sandbox mode: enable must be a boolean, not the string true"
  version: "skv_zmhAZmnVqzDEZ-N1iJd6hQ"
  updated: "2026-10-03T04:31:22.06103+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ei9S7RpSxQeBSxlOeIj_pw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sendgrid.com/for-developers/sending-email/sandbox-mode/\"]"
---

**TL;DR:** Quoting the sandbox enable flag gives a confusing validation error. The rule and the 200-vs-202 signal that tells you sandbox mode is actually on. Symptom: 'The sandbox mode enable param should be a boolean value.' 1. Send "mail_settings": {"sandbox_mode": {"enable": true}} with a real JSON boolean.

## The error

```text
The sandbox mode enable param should be a boolean value.
```

## The fix

1. Send "mail_settings": {"sandbox_mode": {"enable": true}} with a real JSON boolean. The string "true" fails.

2. This usually happens when a template language or form encoder stringifies the payload. Check what actually goes on the wire, not what your object looks like.

3. A valid sandbox request returns 200 OK. A real send returns 202. If you see 202, sandbox mode was not applied and the mail went out.

4. Sandbox mode validates form, type, and shape; it delivers nothing, fires no webhook events, logs no email activity, and consumes no credits.

5. With a template_id in the request, the subject and body are assumed to come from the template and are not validated. A sandbox 200 does not prove the template renders. Use sandbox mode in CI for every mail path. It is the cheapest contract test SendGrid offers.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: SendGrid sandbox mode.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_Ei9S7RpSxQeBSxlOeIj_pw). Version: `skv_zmhAZmnVqzDEZ-N1iJd6hQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
