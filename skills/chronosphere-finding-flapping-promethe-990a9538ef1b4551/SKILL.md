---
name: "chronosphere-finding-flapping-promethe-990a9538ef1b4551"
description: "Chronosphere: finding flapping Prometheus endpoints with a PromQL gap pattern. use timestamp() and unless() with a 5-minute offset to spot gaps: query the metric and take the complement of the same metric offset by 5 minutes. Use when hitting this exact issue with Chronosphere. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_BRxCNPfAofOOdbkpyAhPuQ"
  title: "Chronosphere: finding flapping Prometheus endpoints with a PromQL gap pattern"
  version: "skv_m2BQud5JSQgLDu24SMgJKg"
  updated: "2026-10-03T14:07:58.075565+00:00"
  canonical_url: "https://vectle.com/skills/skl_BRxCNPfAofOOdbkpyAhPuQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.chronosphere.io/investigate/querying/metrics/troubleshooting\"]"
---

## TL;DR

Use timestamp() and unless() with a 5-minute offset to spot gaps: query the metric and take the complement of the same metric offset by 5 minutes.

## Fix

1. Use timestamp() and unless() with a 5-minute offset to spot gaps: query the metric and take the complement of the same metric offset by 5 minutes.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this Chronosphere feature.
- The symptom matches: finding flapping Prometheus endpoints with a PromQL gap pattern.

## When NOT to use

- Unrelated Chronosphere issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Chronosphere. Source: https://docs.chronosphere.io/investigate/querying/metrics/troubleshooting.

## Variant phrasings

### finding flapping Prometheus endpoints with a PromQL gap pattern

## Why it happens

Metrics go missing intermittently and you need a repeatable way to see when a Prometheus endpoint stopped emitting.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.chronosphere.io/investigate/querying/metrics/troubleshooting

---

Source: [Vectle](https://vectle.com/skills/skl_BRxCNPfAofOOdbkpyAhPuQ). Version: `skv_m2BQud5JSQgLDu24SMgJKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
