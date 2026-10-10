---
name: "growthbook-self-hosted-error-sending-e-f63d6c329a944078"
description: "Shows how to fix growthBook self-hosted Error sending email SSL routines ssl3_get_record wrong version number. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_tcZP3QOUyF9Rcmq-dV9fNw"
  title: "GrowthBook self-hosted Error sending email SSL routines ssl3_get_record wrong version number"
  version: "skv_lcnNI5qDCYdBtoKOYcSY4A"
  updated: "2026-10-03T13:54:00.134054+00:00"
  canonical_url: "https://vectle.com/skills/skl_tcZP3QOUyF9Rcmq-dV9fNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Error sending email: Error: :error:1408F10B:SSL routines:ssl3_get_record:wrong version number": what actually fixes it (verified in the thread): The maintainer fixed a bug with port 587 and simplified the SMTP settings: you no longer need to specify EMAIL_USE_TLS at all. Port 465 always uses TLS; every other port starts plain and upgrades via STARTTLS if the server supports it.

```text
Error sending email: Error: :error:1408F10B:SSL routines:ssl3_get_record:wrong version number
```

## Steps

1. Self-hosted GrowthBook cannot send email: "Error sending email: Error: :error:1408F10B:SSL routines:ssl3_get_record:wrong version number". The config used EMAIL_HOST, EMAIL_PORT 587, with EMAIL_USE_TLS tried both true and false. The error means TLS was attempted against a port expecting a plain connection (or vice versa).

2. What actually fixes it (verified in the thread):

3. The maintainer fixed a bug with port 587 and simplified the SMTP settings: you no longer need to specify EMAIL_USE_TLS at all. Port 465 always uses TLS; every other port starts plain and upgrades via STARTTLS if the server supports it. Pull the latest Docker image and drop the EMAIL_USE_TLS setting, two reporters confirmed email sending worked after the fix.

## When to use

You are seeing this: The situation: Self-hosted GrowthBook cannot send email: "Error sending email: Error: :error:1408F10B:SSL routines:ssl3_get_record:wrong version number". Use this skill when you run into "GrowthBook self-hosted Error sending email SSL routines ssl3_get_record wrong version number".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_tcZP3QOUyF9Rcmq-dV9fNw). Version: `skv_lcnNI5qDCYdBtoKOYcSY4A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
