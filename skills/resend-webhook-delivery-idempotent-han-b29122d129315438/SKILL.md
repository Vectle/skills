---
name: "resend-webhook-delivery-idempotent-han-b29122d129315438"
description: "Resend retries webhook endpoints that do not return HTTP 200. Covers making handlers idempotent with svix-id dedupe, returning 200 fast, the retry schedule, and replaying events. Not for signature verification failures or events that never fire."
metadata:
  skill_id: "skl_2gFEIkzfLn2gKoPfyQ0vUA"
  title: "Resend webhook delivery: idempotent handlers, retry schedule, replay"
  version: "skv_exlL8-OKaXxlCaUmokZaVQ"
  updated: "2026-10-03T04:40:22.026857+00:00"
  canonical_url: "https://vectle.com/skills/skl_2gFEIkzfLn2gKoPfyQ0vUA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If your endpoint does not return HTTP 200, Resend retries with backoff: immediate, 5 seconds, 5 minutes, 30 minutes, 2 hours, 5 hours, 10 hours. Make every handler idempotent (dedupe on the svix-id header or event id before any side effect), return 200 quickly and process asynchronously, and only return non-200 when you genuinely failed and want a retry. A slow handler that times out retries work that already succeeded, which is how duplicate emails happen.

The retry schedule:

```text
immediate, 5s, 5min, 30min, 2h, 5h, 10h
```

Steps:

1. Make every handler idempotent. Dedupe on the svix-id header (unique per message) or the event id: check your processed-events store first, record it, then act. Success: a redelivered event causes no second side effect.
2. Return 200 quickly, then process asynchronously. Success: the handler responds in well under the timeout.
3. Return non-200 only when you genuinely failed and want a retry. Returning 200 for an event you cannot handle yet is a lie; fix the handler instead. Success: retries happen only for real failures.
4. When events go missing, debug with the delivery history API: list events on the webhook, inspect each attempt's status code and response body, and replay from the dashboard or API to reprocess with fixed handler code. Success: the replayed event processes cleanly.

When to use: Resend webhook handlers with duplicate side effects, missed events, or retry storms.

When not to use: webhook signature verification failures (different problem), events that never fire at all (check the webhook is configured), or a provider other than Resend.

Compatibility: Resend webhooks, Svix-style delivery (svix-id header).

Variants:
- resend webhook retries
- resend duplicate webhook events
- resend webhook idempotency

Root cause: at-least-once delivery plus a 10-hour retry schedule means any handler that is neither idempotent nor fast will re-run side effects over and over. The trap is a handler that times out after succeeding: the retry treats it as failed.

Edge cases:
- Treating a replayed event as suspicious is wrong. Replays are a normal operations tool; your idempotency dedupe is what makes them safe.
- Returning 200 for an event you cannot handle yet hides the problem. Fix the handler so it can handle it.

---

Source: [Vectle](https://vectle.com/skills/skl_2gFEIkzfLn2gKoPfyQ0vUA). Version: `skv_exlL8-OKaXxlCaUmokZaVQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
