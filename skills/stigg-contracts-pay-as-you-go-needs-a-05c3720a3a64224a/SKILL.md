---
name: "stigg-contracts-pay-as-you-go-needs-a-05c3720a3a64224a"
description: "Guide Stigg contracts: pay-as-you-go needs a metered item, and order-form traps: Check the legal entity has a payment account before building: GET the legal entities and confirm paymentAccounts is non-empty. Use this when you hit exactly this in Stigg contracts. Not for different errors or different tools."
metadata:
  skill_id: "skl_vVIKtmUk3tzTi1sB0GmABA"
  title: "Stigg contracts: pay-as-you-go needs a metered item, and order-form traps"
  version: "skv_p7EX7D0V7UvlkkdrQmpvog"
  updated: "2026-10-03T05:30:16.359097+00:00"
  canonical_url: "https://vectle.com/skills/skl_vVIKtmUk3tzTi1sB0GmABA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Check the legal entity has a payment account before building: GET the legal entities and confirm paymentAccounts is non-empty. Context: Official docs (Stigg skills repo, stigg-contracts/references/billing-and-invoices.md): the billing-contracts reference for building contracts from real order forms. Documents the isPayAsYouGo/pricing-model mechanics, the legal-entity payment-account blocker, and the four traps agents hit reading real order forms.

Context: Official docs (Stigg skills repo, stigg-contracts/references/billing-and-invoices.md): the billing-contracts reference for building contracts from real order forms. Documents the isPayAsYouGo/pricing-model mechanics, the legal-entity payment-account blocker, and the four traps agents hit reading real order forms.

Pay-as-you-go mechanics that trip people up: a pay-as-you-go pricing model resolves quantity from reported usage, so the line item must be metered. Pairing a usage model with a plain catalog item is rejected outright: 'Line item uses a pay-as-you-go pricing model, which requires a metered item.' Either meter the item first or price the commitment with a fixed model. The isPayAsYouGo flag on the pricing model decides the charge timing (usage always bills in arrears) and the model takes no quantity input: sending a quantity with a usage-model line is rejected. Row values are limited to the model's editableInputs (quantity, price, from, to, packageSize); a value for an input the model does not expose is ignored, not rejected, so typos silently do nothing. A row carrying any other key is rejected outright. Four order-form traps: 1. Usage-based lines vanish: a line whose total reads 'In arrears' or 'As incurred' contributes nothing to the subtotal, so it is invisible if you work from totals. It is still a line item: price it pay-as-you-go in arrears, or the overage is never billed. 2. 'Included' lines are still lines: price them at 0 so they appear on the invoice and the entitlement exists. 3. Check the legal entity has a payment account before building: GET the legal entities and confirm paymentAccounts is non-empty. There is no API to create a payment account; someone must add it in the dashboard, or the contract can never be published. 4. A table repeated per period is one contract if amounts are identical (yearly billing cycle across both), but one contract per period if amounts differ (ramps), because a line item carries a billing cycle, never its own period.

## When to use
You hit exactly this: Stigg contracts: pay-as-you-go needs a metered item, and order-form traps in Stigg contracts.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Stigg contracts.

## Edge cases
- Row values are limited to the model's editableInputs (quantity, price, from, to, packageSize); a value for an input the model does not expose is ignored, not rejected, so typos silently do nothing.

---

Source: [Vectle](https://vectle.com/skills/skl_vVIKtmUk3tzTi1sB0GmABA). Version: `skv_p7EX7D0V7UvlkkdrQmpvog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
