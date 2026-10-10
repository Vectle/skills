---
name: "stigg-credits-and-tiered-pricing-the-c-07463fa3e7c80bb6"
description: "Guide Stigg credits and tiered pricing: the common mistakes (volume vs graduated tiers): Setting recurring grant cadence different from the billing period. Context: Official docs (Stigg skills repo, stigg-pricing-modeling/references/charges-and-pricing-models. Use this when you hit exactly this in Stigg credits and tiered pricing. Not for different errors or different tools."
metadata:
  skill_id: "skl_ya8GR0uW9BetsA6wczAh6A"
  title: "Stigg credits and tiered pricing: the common mistakes (volume vs graduated tiers)"
  version: "skv_r6C2Soxwye8SazvdbemESg"
  updated: "2026-10-03T14:16:13.812556+00:00"
  canonical_url: "https://vectle.com/skills/skl_ya8GR0uW9BetsA6wczAh6A"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

TL;DR: Setting recurring grant cadence different from the billing period. Context: Official docs (Stigg skills repo, stigg-pricing-modeling/references/charges-and-pricing-models.md): the charges and pricing-models reference. Documents the four common credits-charge mistakes, the volume-vs-graduated tiered pricing distinction, and how overages behave for metered features bundled into a plan.

Context: Official docs (Stigg skills repo, stigg-pricing-modeling/references/charges-and-pricing-models.md): the charges and pricing-models reference. Documents the four common credits-charge mistakes, the volume-vs-graduated tiered pricing distinction, and how overages behave for metered features bundled into a plan.

Credits-charge mistakes to avoid: 1. Modeling '$0.001 per credit' as a separate charge type. It is not a primitive; it is a metered-feature overage. 2. Setting recurring grant cadence different from the billing period. Customers expect 'monthly credits' to align with the monthly bill. 3. Forgetting auto-recharge requires Stripe: auto-recharge is a customer-level config, not a plan attribute. 4. Promotional credits with non-zero cost_basis. Promotional must be zero or it pollutes revenue recognition. Tiered pricing variants (the common confusion): volume tiers change the unit price for the whole quantity once you cross a threshold (0-1000 at $0.001, 1001+ at $0.0008). Graduated tiers apply different unit prices to units within each tier (first 1000 at $0.001, next 9000 at $0.0008). Per-unit volume sets the price per unit by the tier reached but applies it to every unit equally. Volume picks one price for the whole; graduated layers multiple prices. Overages: for a metered feature bundled into a plan (e.g. 10k API calls included), overages define what happens past quota: pay-as-you-go overage (bill excess at a per-unit rate), block at quota (a runtime entitlement decision with no overage configured), or tiered overages (volume/graduated mechanics on the overage portion).

## When to use
You hit exactly this: Stigg credits and tiered pricing: the common mistakes (volume vs graduated tiers) in Stigg credits and tiered pricing.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Stigg credits and tiered pricing (versions mentioned here: 0.001, 0.0008).

---

Source: [Vectle](https://vectle.com/skills/skl_ya8GR0uW9BetsA6wczAh6A). Version: `skv_r6C2Soxwye8SazvdbemESg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
