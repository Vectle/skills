---
name: "the-permit-sdk-is-only-a-client-you-st-b0ab405e12f08fa2"
description: "Shows how to fix the Permit SDK is only a client, you still have to run the PDP. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_YIAZJ4Dq3Oei_YH7fWEseg"
  title: "The Permit SDK is only a client, you still have to run the PDP"
  version: "skv_fLRdHF0-EIAYjq9kJiJ4Xw"
  updated: "2026-10-04T06:54:03.355941+00:00"
  canonical_url: "https://vectle.com/skills/skl_YIAZJ4Dq3Oei_YH7fWEseg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Run the PDP container (permitio/pdp-v2:latest with your environment API key as PDP_API_KEY) before making any permit.check calls, and set the SDK's pdp URL to wherever that container is reachable.

## Steps

1. Run the PDP container (permitio/pdp-v2:latest with your environment API key as PDP_API_KEY) before making any permit.check calls, and set the SDK's pdp URL to wherever that container is reachable. Keep the PDP and PEP roles straight in your head: the PDP answers authorization queries, the PEP (your SDK call, middleware, or gateway plugin) enforces the answer.

## When to use

Use this skill when you run into "The Permit SDK is only a client, you still have to run the PDP".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_YIAZJ4Dq3Oei_YH7fWEseg). Version: `skv_fLRdHF0-EIAYjq9kJiJ4Xw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
