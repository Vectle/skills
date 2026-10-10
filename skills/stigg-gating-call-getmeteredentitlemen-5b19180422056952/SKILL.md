---
name: "stigg-gating-call-getmeteredentitlemen-5b19180422056952"
description: "Stigg gating: call getMeteredEntitlement with requestedUsage, then report usage. Always configure cache plus fallback rules: with no fallback, a cold cache during an outage leaves the SDK nothing to return. Use when hitting this exact issue with Stigg gating. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_FUj9NDXF0INYVWB_eR7rLQ"
  title: "Stigg gating: call getMeteredEntitlement with requestedUsage, then report usage"
  version: "skv_tIhNHKr3kFKKEPh2X4mQ2g"
  updated: "2026-10-03T17:29:19.937172+00:00"
  canonical_url: "https://vectle.com/skills/skl_FUj9NDXF0INYVWB_eR7rLQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Always configure cache plus fallback rules: with no fallback, a cold cache during an outage leaves the SDK nothing to return. Gate each request with getMeteredEntitlement passing the amount the customer is about to consume as requestedUsage.

## Fix

1. Always configure cache plus fallback rules: with no fallback, a cold cache during an outage leaves the SDK nothing to return.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Stigg gating feature.
- The symptom matches: call getMeteredEntitlement with requestedUsage, then report usage.

## When NOT to use

- Unrelated Stigg gating issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Stigg gating. Source: https://github.com/stiggio/skills/blob/HEAD/skills/stigg-entitlements/references/gating.md.

## Variant phrasings

### call getMeteredEntitlement with requestedUsage, then report usage

## Why it happens

Stigg gates in two steps: check, then report. Skipping the report underbills.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/stiggio/skills/blob/HEAD/skills/stigg-entitlements/references/gating.md

---

Source: [Vectle](https://vectle.com/skills/skl_FUj9NDXF0INYVWB_eR7rLQ). Version: `skv_tIhNHKr3kFKKEPh2X4mQ2g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
