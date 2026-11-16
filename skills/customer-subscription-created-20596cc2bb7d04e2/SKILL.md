---
name: "customer-subscription-created-20596cc2bb7d04e2"
description: "customer.subscription.created"
metadata:
  skill_id: "skl_qK03svY2B42IAAvHdgniwQ"
  title: "customer.subscription.created"
  version: "skv_BIjEezGw34LQBNtuwklYnQ"
  updated: "2026-11-16T01:52:56.998455+00:00"
  canonical_url: "https://vectle.com/skills/skl_qK03svY2B42IAAvHdgniwQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the event object type is a subscription and read its id, customer, status, and current period fields.

Verify the webhook signature using the endpoint signing secret for the mode, test or live, that sent the event.

Create or update the local subscription record keyed by the subscription id, storing status as sent.

Return a 2xx response immediately and do heavier provisioning work in a background job.

Grant access based on status: trialing or active can receive trial or paid access per your product rules, incomplete should not.

Listen for the follow-up invoice payment events to move the record to paid.

Make the handler idempotent by checking whether this event id was already processed.

---

Source: [Vectle](https://vectle.com/skills/skl_qK03svY2B42IAAvHdgniwQ). Version: `skv_BIjEezGw34LQBNtuwklYnQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
