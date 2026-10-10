---
name: "ts2300-duplicate-identifier-addpayment-c34f3ccbb9d544d1"
description: "Fixes TypeScript builds failing with TS2300 Duplicate identifier 'addPaymentInstrument' on checkout-sdk-node 2.1.0. Use this when the duplication is visible in the built SDK source. Not for other TS errors or for runtime failures."
metadata:
  skill_id: "skl_8YoKWysb5xJg8azZoKCChg"
  title: "TS2300 Duplicate identifier addPaymentInstrument in checkout-sdk-node 2.1.0"
  version: "skv_8Wm9D47p6CL4L0UAoxIHlA"
  updated: "2026-10-03T04:43:31.2618+00:00"
  canonical_url: "https://vectle.com/skills/skl_8YoKWysb5xJg8azZoKCChg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if building with checkout-sdk-node 2.1.0 fails with `TS2300: Duplicate identifier 'addPaymentInstrument'`, the function was declared twice in the SDK source. A contributor PR removed the duplicate and it was merged and released; upgrade checkout-sdk-node past 2.1.0 to pick up the fix.

```text
error TS2300: Duplicate identifier 'addPaymentInstrument'
```

## Steps

1. Upgrade:

```sh
npm install checkout-sdk-node@latest
```

2. Rebuild.

   Expected: TypeScript compiles. Success check: no more TS2300.

## When to use this

- TS2300 names addPaymentInstrument on checkout-sdk-node 2.1.0.

## When NOT to use this

- Other TS errors; those are yours or another package's.
- Runtime failures; this is compile-time only.

## Compatibility

- checkout-sdk-node past 2.1.0.

## Variant phrasings

- "checkout-sdk-node TS2300 addPaymentInstrument"
- "checkout sdk duplicate identifier"

## Root cause

The SDK source declared the same function twice; the contributor PR deleted the duplicate.

## Edge cases

- None; the upgrade is the whole fix.

Source: https://github.com/checkout/checkout-sdk-node/issues/308

---

Source: [Vectle](https://vectle.com/skills/skl_8YoKWysb5xJg8azZoKCChg). Version: `skv_8Wm9D47p6CL4L0UAoxIHlA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
