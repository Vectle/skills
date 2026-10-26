---
name: "gocardless-webhooks-will-not-deseriali-54d0fb6e33021577"
description: "Shows how to fix goCardless webhooks will not deserialize into a bare event: wrap in a root object. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_-67brCbSlxJSkzodafa6SQ"
  title: "GoCardless webhooks will not deserialize into a bare event: wrap in a root object"
  version: "skv_ghAh4uyWiVOPTBD3NRTEVQ"
  updated: "2026-10-03T14:06:34.350656+00:00"
  canonical_url: "https://vectle.com/skills/skl_-67brCbSlxJSkzodafa6SQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/45413721\"]"
---

## TL;DR

Deserialize GoCardless webhooks into a root object that has an events list, not into a single event. The body shape is an object with an events array, each entry carrying id, resource_type, action, links, and details.

## Steps

1. Deserialize GoCardless webhooks into a root object that has an events list, not into a single event. The body shape is an object with an events array, each entry carrying id, resource_type, action, links, and details. In .NET that means a Root class with a List of the SDK's event resource, then read each event's action to route it. If webhook parsing throws, check the wrapper shape first before suspecting the signature or the stream reading.

## When to use

You are seeing this: Deserialize GoCardless webhooks into a root object that has an events list, not into a single event. Use this skill when you run into "GoCardless webhooks will not deserialize into a bare event: wrap in a root object".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_-67brCbSlxJSkzodafa6SQ). Version: `skv_ghAh4uyWiVOPTBD3NRTEVQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
