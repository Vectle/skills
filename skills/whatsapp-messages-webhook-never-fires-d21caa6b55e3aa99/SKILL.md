---
name: "whatsapp-messages-webhook-never-fires-d21caa6b55e3aa99"
description: "Shows how to fix whatsApp messages webhook never fires: subscribe the WABA to your app. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_7cqe6Nhm2kBBrX3UV064zw"
  title: "WhatsApp messages webhook never fires: subscribe the WABA to your app"
  version: "skv_jKutX3lWPZsEYfqK5U-3TQ"
  updated: "2026-10-04T15:45:46.572517+00:00"
  canonical_url: "https://vectle.com/skills/skl_7cqe6Nhm2kBBrX3UV064zw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/79175537\"]"
---

## TL;DR

Rechecking the webhook URL in the dashboard will not fix this, it is a separate subscription step. The accepted answer says the fix is subscribing the WhatsApp Business Account to the app, which the dashboard setup flow does not do for you.

## Steps

1. If the WhatsApp "messages" webhook is silent while other webhooks fire, the WhatsApp Business Account is probably not subscribed to your app. Call: POST https://graph.facebook.com/v21.0/{whatsapp-business-account-id}/subscribed_apps with an Authorization bearer header. Expect {"success": true}. Confirm it stuck with GET on the same endpoint; the response should list whatsapp_business_api_data with your app name. Only then will Meta deliver messages webhooks to your callback URL. Rechecking the webhook URL in the dashboard will not fix this, it is a separate subscription step.

## When to use

You are seeing this: If the WhatsApp "messages" webhook is silent while other webhooks fire, the WhatsApp Business Account is probably not subscribed to your app. Use this skill when you run into "WhatsApp messages webhook never fires: subscribe the WABA to your app".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: httpsgraph.facebook.com v21.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://graph.facebook.com/v21.0/{whatsapp-business-account-id}/subscribed_apps


---

Source: [Vectle](https://vectle.com/skills/skl_7cqe6Nhm2kBBrX3UV064zw). Version: `skv_jKutX3lWPZsEYfqK5U-3TQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
