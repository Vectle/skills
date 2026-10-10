---
name: "telnyx-webhook-signature-is-invalid-an-c77c7e7a7c926081"
description: "Shows how to fix telnyx webhook 'Signature is invalid and does not match the payload' (Node). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_WTYVv9jZs2ClrUCuyo0LXA"
  title: "Telnyx webhook 'Signature is invalid and does not match the payload' (Node)"
  version: "skv_Hlwx-FW9zPNpqaSJlw2OTg"
  updated: "2026-10-03T14:08:50.258638+00:00"
  canonical_url: "https://vectle.com/skills/skl_WTYVv9jZs2ClrUCuyo0LXA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

What fixed it The signature must be verified against the raw request body bytes, not the parsed JSON object.

## Steps

1. What was going on
Verifying a Telnyx webhook signature in Express with telnyx-node 1.17.0 fails: `telnyx.webhooks.constructEvent(rawBody, signatureHeader, timestampHeader, publicKey)` throws 'Signature is invalid and does not match the payload'. The handler needs both the parsed JSON body and the raw body. The raw body is captured via body-parser's verify option.

2. What fixed it
The signature must be verified against the raw request body bytes, not the parsed JSON object. Capture the raw buffer with body-parser's `verify` option:

```js
app.use(bodyParser.json({ verify(req, res, buffer) { req.rawBody = buffer; } }));
```

3. then pass `req.rawBody` (the Buffer) to `telnyx.webhooks.constructEvent(req.rawBody, req.header('telnyx-signature-ed25519'), req.header('telnyx-timestamp'), TELNYX_PUBLIC_KEY)`. The reporter confirmed verification passes with the raw body.

## When to use

You are seeing this: What was going on Verifying a Telnyx webhook signature in Express with telnyx-node 1.17.0 fails: telnyx.webhooks.constructEvent(rawBody, signatureHeader, timestampHeader, publicKey) throws 'Signature is invalid and does not match the payload'. Use this skill when you run into "Telnyx webhook 'Signature is invalid and does not match the payload' (Node)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: telnyx-node 1.17.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_WTYVv9jZs2ClrUCuyo0LXA). Version: `skv_Hlwx-FW9zPNpqaSJlw2OTg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
