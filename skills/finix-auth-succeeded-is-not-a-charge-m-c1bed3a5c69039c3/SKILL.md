---
name: "finix-auth-succeeded-is-not-a-charge-m-c1bed3a5c69039c3"
description: "Guide Finix auth SUCCEEDED is not a charge: map order states off authorizations vs transfers vs reversals: When you handle Finix webhooks, do not treat every SUCCEEDED the same. The event families carry different money semantics: authorization SUCCEEDED means the card was approved (hold placed), transfer. Use this when you hit exactly this in Finix. Not for different errors or different tools."
metadata:
  skill_id: "skl_iw90kxnVG2FNO62gJisoQQ"
  title: "Finix auth SUCCEEDED is not a charge: map order states off authorizations vs transfers vs reversals"
  version: "skv_xqMYhgo5Ah_9keYJZWeiBw"
  updated: "2026-10-03T05:31:39.259528+00:00"
  canonical_url: "https://vectle.com/skills/skl_iw90kxnVG2FNO62gJisoQQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: When you handle Finix webhooks, do not treat every SUCCEEDED the same. The event families carry different money semantics: authorization SUCCEEDED means the card was approved (hold placed), transfer SUCCEEDED means funds actually moved, so only the transfer marks the order as paid. An authorization with

## Fix
1. When you handle Finix webhooks, do not treat every SUCCEEDED the same.
   Expected: this specific failure stops.
2. The event families carry different money semantics: authorization SUCCEEDED means the card was approved (hold placed), transfer SUCCEEDED means funds actually moved, so only the transfer marks the order as paid.
   Expected: this specific failure stops.
3. An authorization with.
   Expected: this specific failure stops.
4. `is_void=true`.
   Expected: this specific failure stops.

## Details
An authorization with `is_void=true` SUCCEEDED is a voided hold, not a payment. A transfer of type REVERSAL is the refund family: SUCCEEDED = refund done, FAILED/CANCELED = refund failed, and a PENDING reversal is an unsupported state to log, not a failure to act on. Disputes are their own family (PENDING = opened, INQUIRY = challenged, WON/LOST = decided). Map your order states off these families, not off the status string alone.

## When to use
You hit exactly this: Finix auth SUCCEEDED is not a charge: map order states off authorizations vs transfers vs reversals in Finix.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Finix.

## Root cause
The event families carry different money semantics: authorization SUCCEEDED means the card was approved (hold placed), transfer SUCCEEDED means funds actually moved, so only the transfer marks the order as paid.

## Edge cases
- When you handle Finix webhooks, do not treat every SUCCEEDED the same.

---

Source: [Vectle](https://vectle.com/skills/skl_iw90kxnVG2FNO62gJisoQQ). Version: `skv_xqMYhgo5Ah_9keYJZWeiBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
