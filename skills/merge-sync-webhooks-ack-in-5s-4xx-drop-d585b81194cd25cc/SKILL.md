---
name: "merge-sync-webhooks-ack-in-5s-4xx-drop-d585b81194cd25cc"
description: "Guide Merge sync webhooks: ACK in 5s, 4xx drops the event forever, run polling as backstop: Run a polling backstop in production: periodic For Merge sync webhooks: (1) always return 200 fast, under 5 seconds. Use this when you hit exactly this in Merge sync webhooks. Not for different errors or different tools."
metadata:
  skill_id: "skl_sbMy7O1RsZAtrdSUsqj-LQ"
  title: "Merge sync webhooks: ACK in 5s, 4xx drops the event forever, run polling as backstop"
  version: "skv_m9Y7jIKjRpvfWZAxD9tABQ"
  updated: "2026-10-03T04:40:00.959436+00:00"
  canonical_url: "https://vectle.com/skills/skl_sbMy7O1RsZAtrdSUsqj-LQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/merge-api/merge-unified-skills/blob/HEAD/skills/implementing-sync/SKILL.md\"]"
---

TL;DR: Run a polling backstop in production: periodic For Merge sync webhooks: (1) always return 200 fast, under 5 seconds. A 4xx from your endpoint is treated as permanent failure and the event is dropped with no retry, so never do real work inside the webhook handler; enqueue it and return. (2) Do not rely on webhooks alone.

For Merge sync webhooks: (1) always return 200 fast, under 5 seconds. A 4xx from your endpoint is treated as permanent failure and the event is dropped with no retry, so never do real work inside the webhook handler; enqueue it and return. (2) Do not rely on webhooks alone. Run a polling backstop in production: periodic `GET /sync-status` checks or a `modified_after` sweep, because a deploy window or a 400 from a framework that cannot parse the payload loses the event outright. (3) If polling shows `sync_status` stuck on SYNCING, that is often just the initial sync taking 15 minutes to several hours on large accounts; confirm `initial_sync_complete` gets set when status reaches DONE. (4) If HMAC validation fails on every event, check two things: the webhook secret matches, and you computed the HMAC against the raw body before JSON parsing (Express `json()` middleware eating the raw body is the classic cause).

## When to use
You hit exactly this: Merge sync webhooks: ACK in 5s, 4xx drops the event forever, run polling as backstop in Merge sync webhooks.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Merge sync webhooks.

## Edge cases
- For Merge sync webhooks: (1) always return 200 fast, under 5 seconds.

---

Source: [Vectle](https://vectle.com/skills/skl_sbMy7O1RsZAtrdSUsqj-LQ). Version: `skv_m9Y7jIKjRpvfWZAxD9tABQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
