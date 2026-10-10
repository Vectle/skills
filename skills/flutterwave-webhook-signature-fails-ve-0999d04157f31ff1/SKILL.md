---
name: "flutterwave-webhook-signature-fails-ve-0999d04157f31ff1"
description: "Shows how to fix flutterwave webhook signature fails: verify the verif-hash header over the raw body. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_c7NhMPCg8qmTlD2Mlmlk7g"
  title: "Flutterwave webhook signature fails: verify the verif-hash header over the raw body"
  version: "skv_c89FFEneS43RCrTEb3FD2w"
  updated: "2026-10-03T14:13:15.175515+00:00"
  canonical_url: "https://vectle.com/skills/skl_c7NhMPCg8qmTlD2Mlmlk7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set a long random secret hash in the Flutterwave dashboard under Settings, Webhooks, and read it from an environment variable, never hardcode it.

## Steps

1. Do two things when wiring Flutterwave webhooks in Express. Set a long random secret hash in the Flutterwave dashboard under Settings, Webhooks, and read it from an environment variable, never hardcode it. Capture the raw body for the webhook route: use express.raw for application/json on that route, or the json verify hook that stashes the buffer, then HMAC-SHA256 the raw bytes with your secret hash and compare against the verif-hash header. Respond 200 immediately and push real work to a queue, since Flutterwave retries failed deliveries three times at 30-minute intervals when retries are enabled.

## When to use

You are seeing this: Do two things when wiring Flutterwave webhooks in Express. Use this skill when you run into "Flutterwave webhook signature fails: verify the verif-hash header over the raw body".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_c7NhMPCg8qmTlD2Mlmlk7g). Version: `skv_c89FFEneS43RCrTEb3FD2w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
