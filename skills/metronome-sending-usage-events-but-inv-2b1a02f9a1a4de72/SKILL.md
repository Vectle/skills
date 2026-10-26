---
name: "metronome-sending-usage-events-but-inv-2b1a02f9a1a4de72"
description: "Metronome: sending usage events but invoice shows zero usage - silent drops. The checklist: event_type must exactly match a billable metric's event_type_filter (the #1 cause; the filter is immutable, so a wrong one means archiving the metric and creating a new one); events older than 34 days are silently dropped and unrecoverable; string numbers like \"tokens\": \"1500\" make SUM aggregation produce zero; and a missing or misspelled aggregation_key property does the same. Use when hitting this exact"
metadata:
  skill_id: "skl_UE_rIDaQFubtNWyeGoQSHA"
  title: "Metronome: sending usage events but invoice shows zero usage - silent drops"
  version: "skv_181hmlW400Y469P3k5RMvA"
  updated: "2026-10-03T18:06:09.947871+00:00"
  canonical_url: "https://vectle.com/skills/skl_UE_rIDaQFubtNWyeGoQSHA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/metronome-industries/ai/blob/HEAD/skills/metronome-plg-billing/references/diagnostics.md\"]"
---

## TL;DR

The checklist: event_type must exactly match a billable metric's event_type_filter (the #1 cause; the filter is immutable, so a wrong one means archiving the metric and creating a new one); events older than 34 days are silently dropped and unrecoverable; string numbers like "tokens": "1500" make SUM aggregation produce zero; and a missing or misspelled aggregation_key property does the same.

## Fix

1. The checklist: event_type must exactly match a billable metric's event_type_filter (the #1 cause; the filter is immutable, so a wrong one means archiving the metric and creating a new one); events older than 34 days are silently dropped and unrecoverable; string numbers like "tokens": "1500" make SUM aggregation produce zero; and a missing or misspelled aggregation_key property does the same.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this Metronome feature.
- The symptom matches: sending usage events but invoice shows zero usage - silent drops.

## When NOT to use

- Unrelated Metronome issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Metronome. Source: https://github.com/metronome-industries/ai/blob/HEAD/skills/metronome-plg-billing/references/diagnostics.md.

## Variant phrasings

### sending usage events but invoice shows zero usage - silent drops

## Why it happens

Usage events are ingested by Metronome but the invoice shows zero usage. Metronome silently drops or ignores several kinds of bad input with no error.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/metronome-industries/ai/blob/HEAD/skills/metronome-plg-billing/references/diagnostics.md

---

Source: [Vectle](https://vectle.com/skills/skl_UE_rIDaQFubtNWyeGoQSHA). Version: `skv_181hmlW400Y469P3k5RMvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
