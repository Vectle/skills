---
name: "sendgrid-552-message-too-large-or-mail-28caf001a82699fc"
description: "SendGrid SMTP 552: either the message exceeds the size limit or the recipient mailbox is full. Covers telling the two apart, the deliberate handling for each, and why these are never retried. Not for 550 rejections or deferrals."
metadata:
  skill_id: "skl_e96fYTTj3eXtp59InFkGeg"
  title: "SendGrid 552 message too large or mailbox full"
  version: "skv_Eobhgaf9K7OjjCuX_UWJuw"
  updated: "2026-10-03T05:13:02.195707+00:00"
  canonical_url: "https://vectle.com/skills/skl_e96fYTTj3eXtp59InFkGeg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"http://sendgrid.com/docs/Glossary/email_error_messages.html\"]"
---

TL;DR: 552 is either your message being too big or the recipient's mailbox being full, and SendGrid does not retry these, so handle them deliberately. Read the human-readable portion of the 552 text to tell the two apart before deciding. Too large: shorten the body, drop or link attachments instead of embedding them, then resend. Mailbox full: do not resend on a loop; one retry after a day is reasonable, and repeated mailbox-full on the same address is a dead address wearing a temporary error's clothes, so suppress it.

What it looks like:

```text
Symptom: 552, either 'message larger than the current system limit' or
'recipient mailbox full'.
```

Steps:

1. Read the human-readable portion of the 552 text. Success: you know which of the two cases it is.
2. Message too large: shorten the body and drop or link attachments instead of embedding them, then resend. Success: the resend goes through.
3. Mailbox full: wait a day, retry once. Success: delivered, or still full.
4. Track 552s per recipient. Repeated mailbox-full on the same address means suppress it. Success: the dead address stops costing retries.

When to use: 552 responses from SendGrid SMTP sends.

When not to use: 550 rejections (different cause), deferrals (those ARE retried), or the v3 API (the equivalent there is 413 content too large).

Compatibility: SendGrid SMTP; v3 API equivalent is 413.

Variants:
- sendgrid 552 message too large
- sendgrid recipient mailbox full
- sendgrid 552 not retried

Root cause: 552 is permanent for that attempt. It is not a deferral and will not be retried for you, which is why the handling has to be deliberate instead of fire-and-forget.

Edge cases:
- The v3 API equivalent is 413 content too large. Same root cause, same fix.
- A full mailbox is usually an abandoned address. One retry is courtesy; a loop is list rot.

---

Source: [Vectle](https://vectle.com/skills/skl_e96fYTTj3eXtp59InFkGeg). Version: `skv_Eobhgaf9K7OjjCuX_UWJuw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
