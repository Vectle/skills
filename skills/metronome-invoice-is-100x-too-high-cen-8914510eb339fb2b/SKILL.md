---
name: "metronome-invoice-is-100x-too-high-cen-8914510eb339fb2b"
description: "Metronome: invoice is 100x too high - cents vs dollars. Other likely causes of a wrong invoice: the customer is on default rate-card rates because the negotiated override was never created or was created on the wrong product; SUM vs COUNT aggregation mismatch; and case-sensitive dimension values (rate card says gpt-4, events send GPT-4) leaving usage unpriced. Use when hitting this exact issue with Metronome. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_k_JGRU6ChOs5DFdsxFzKXg"
  title: "Metronome: invoice is 100x too high - cents vs dollars"
  version: "skv_IRkKCKyy2wfy_duKwZWqGQ"
  updated: "2026-10-03T18:04:42.559731+00:00"
  canonical_url: "https://vectle.com/skills/skl_k_JGRU6ChOs5DFdsxFzKXg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Other likely causes of a wrong invoice: the customer is on default rate-card rates because the negotiated override was never created or was created on the wrong product; SUM vs COUNT aggregation mismatch; and case-sensitive dimension values (rate card says gpt-4, events send GPT-4) leaving usage unpriced. Pass 10000 for $100.00.

## Fix

1. Other likely causes of a wrong invoice: the customer is on default rate-card rates because the negotiated override was never created or was created on the wrong product; SUM vs COUNT aggregation mismatch; and case-sensitive dimension values (rate card says gpt-4, events send GPT-4) leaving usage unpriced.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Metronome feature.
- The symptom matches: invoice is 100x too high - cents vs dollars.

## When NOT to use

- Unrelated Metronome issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Metronome (mentions 1.00, 100.00). Source: https://github.com/metronome-industries/ai/blob/HEAD/skills/metronome-plg-billing/SKILL.md.

## Variant phrasings

### invoice is 100x too high - cents vs dollars

## Why it happens

A Metronome invoice comes out 100x too high or 100x too low. The Metronome API accepts monetary amounts in cents (integer), and mixing up the units is the most common invoice-amount error.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/metronome-industries/ai/blob/HEAD/skills/metronome-plg-billing/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_k_JGRU6ChOs5DFdsxFzKXg). Version: `skv_IRkKCKyy2wfy_duKwZWqGQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
