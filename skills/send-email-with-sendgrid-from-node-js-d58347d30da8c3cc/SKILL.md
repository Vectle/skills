---
name: "send-email-with-sendgrid-from-node-js-d58347d30da8c3cc"
description: "The exact working pattern for @sendgrid/mail: setApiKey from the environment, a plain message object, and how to unwrap the response array and the error body when a send fails. Not the full reference manual."
metadata:
  skill_id: "skl_tobesF2X1q0OCaEg4XqkZg"
  title: "Send email with SendGrid from Node.js (@sendgrid/mail v8)"
  version: "skv_qdyqT8u-RX0efLpXV2f8Kw"
  updated: "2026-10-03T05:05:01.031878+00:00"
  canonical_url: "https://vectle.com/skills/skl_tobesF2X1q0OCaEg4XqkZg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/quickstart-nodejs.md\",\"https://github.com/sendgrid/sendgrid-nodejs\",\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\"]"
---

**TL;DR:** The exact working pattern for @sendgrid/mail: setApiKey from the environment, a plain message object, and how to unwrap the response array and the error body when a send fails. Install: npm install @sendgrid/mail. Keep the key out of code: const sgMail = require('@sendgrid/mail') sgMail.setApiKey(process.env.SENDGRID_API_KEY) 3.

## The fix

1. Install: npm install @sendgrid/mail.

2. Keep the key out of code: const sgMail = require('@sendgrid/mail') sgMail.setApiKey(process.env.SENDGRID_API_KEY)

3. Send a plain object: const msg = { to: '[RECIPIENT_EMAIL]', from: '[YOUR_VERIFIED_SENDER]', // must be a verified sender subject: 'Sending with SendGrid is Fun', text: 'plain body', html: '[strong]html body[/strong]', } await sgMail.send(msg)

4. The promise resolves with an array; the status code lives at response[0].statusCode (202 on success).

5. On failure, catch and read error.response.body. That is where SendGrid puts the errors array with field and message; error.message alone is usually useless.

6. Never call setApiKey with a literal key in committed code, and never send from a client bundle. The key belongs in server-side env only.

7. For a dry run in tests, pass mailSettings: { sandboxMode: { enable: true } } and expect 200 with no delivery.

## When to use this

- This covers exactly what the title says: Send email with SendGrid from Node.js (@sendgrid/mail v8).
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Send; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Send behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_tobesF2X1q0OCaEg4XqkZg). Version: `skv_qdyqT8u-RX0efLpXV2f8Kw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
