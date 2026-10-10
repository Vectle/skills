---
name: "track-lemon-squeezy-checkout-payment-s-6fe285910ef37c3e"
description: "To track whether a Lemon Squeezy checkout payment succeeded or failed, subscribe to the subscription_payment_success and subscription_payment_failed webhook events, not just order_created. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_s5Vh87yVCAX1dfCBHvuKVQ"
  title: "Track Lemon Squeezy checkout payment status with the payment webhooks, not polling"
  version: "skv_PlhDYKRM9abRMhtXVzsEvA"
  updated: "2026-10-03T04:45:50.804771+00:00"
  canonical_url: "https://vectle.com/skills/skl_s5Vh87yVCAX1dfCBHvuKVQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

To track whether a Lemon Squeezy checkout payment succeeded or failed, subscribe to the subscription_payment_success and subscription_payment_failed webhook events, not just order_created. Correlate them back to your own records by passing your internal id as checkout_data.custom when creating the checkout; Lemon Squeezy echoes it in the webhook under meta.custom_data. There is no synchronous payment-status return from the checkout URL itself, so build the client flow around these webhooks.

## Fix

To track whether a Lemon Squeezy checkout payment succeeded or failed, subscribe to the subscription_payment_success and subscription_payment_failed webhook events, not just order_created. Correlate them back to your own records by passing your internal id as checkout_data.custom when creating the checkout; Lemon Squeezy echoes it in the webhook under meta.custom_data. There is no synchronous payment-status return from the checkout URL itself, so build the client flow around these webhooks.

Context: GitHub issue lmsqueezy/lemonsqueezy.js#120: A developer needed to know on the client side whether a checkout payment actually completed, including failure cases like insufficient funds, but only saw order_created and subscription_created webhooks. The Lemon Squeezy maintainer pointed to the subscription_payment_success and subscription_payment_failed webhook events for exactly this, and showed that custom values passed as checkout_data.custom on checkout creation come back in the webhook payload under meta.custom_data for correlation.

## Matched source
Source: Published skill
Original query: "Track Lemon Squeezy checkout payment status with the payment webhooks, not polling"
Key terms: checkout, lemon, payment, polling, squeezy, status, track, webhooks

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_s5Vh87yVCAX1dfCBHvuKVQ). Version: `skv_PlhDYKRM9abRMhtXVzsEvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
