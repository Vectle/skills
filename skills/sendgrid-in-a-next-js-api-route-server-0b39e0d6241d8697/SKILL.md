---
name: "sendgrid-in-a-next-js-api-route-server-0b39e0d6241d8697"
description: "Send mail from a Next.js route handler without leaking the key to the client: initialize @sendgrid/mail in the route, validate input, and return SendGrid's real error body. Not for different error messages."
metadata:
  skill_id: "skl_nd2FzfU077ibaDb5SPSQng"
  title: "SendGrid in a Next.js API route: server-only key, @sendgrid/mail"
  version: "skv_xEd12lc3rQKJ1F_UHoutaA"
  updated: "2026-10-03T05:07:23.554092+00:00"
  canonical_url: "https://vectle.com/skills/skl_nd2FzfU077ibaDb5SPSQng"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/quickstart-nodejs.md\",\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\"]"
---

**TL;DR:** Send mail from a Next.js route handler without leaking the key to the client: initialize @sendgrid/mail in the route, validate input, and return SendGrid's real error body. Never import this module or the key into a client component. Validate the address yourself; a bad address gives a 400 you could have avoided.

## The error

```text
)) {
    return Response.json({ error:
```

## The fix

app/api/invite/route.js:

import sgMail from '@sendgrid/mail'
sgMail.setApiKey(process.env.SENDGRID_API_KEY)

export async function POST(req) {
  const { email } = await req.json()
  if (!email || !email.includes('@')) {
    return Response.json({ error: 'valid email required' }, { status: 400 })
  }
  try {
    await sgMail.send({
      to: email,
      from: '[YOUR_VERIFIED_SENDER]', // verified sender
      subject: 'Your invite',
      text: 'Welcome aboard',
    })
    return Response.json({ sent: true }, { status: 202 })
  } catch (error) {
    const body = error.response && error.response.body
    console.error(body)
    return Response.json({ sent: false, detail: body }, { status: 502 })
  }
}

Rules:
1. The key lives in server env only. Never import this module or the key into a client component.
2. Validate the address yourself; a bad address gives a 400 you could have avoided.
3. Rate-limit the route or add a captcha if it is public; an open mail endpoint gets abused fast.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: SendGrid in a Next.js API route.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_nd2FzfU077ibaDb5SPSQng). Version: `skv_xEd12lc3rQKJ1F_UHoutaA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
