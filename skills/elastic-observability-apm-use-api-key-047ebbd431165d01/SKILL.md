---
name: "elastic-observability-apm-use-api-key-047ebbd431165d01"
description: "Elastic Observability APM: use API key OR secret token, never both. Verify OTLP variables are all set when no observability data appears. Use when hitting this exact issue with Elastic Observability APM. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_hBZyUgbgK1MHGI3aj-FwhA"
  title: "Elastic Observability APM: use API key OR secret token, never both"
  version: "skv_MEo3raK_rz-VpdXbCkaVVA"
  updated: "2026-10-03T14:06:35.512085+00:00"
  canonical_url: "https://vectle.com/skills/skl_hBZyUgbgK1MHGI3aj-FwhA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/rajesharma470/elastic-observability-demo\"]"
---

## TL;DR

Verify OTLP variables are all set when no observability data appears. Use EITHER ELASTIC_API_KEY OR APM_SECRET_TOKEN, not both; for Elastic Cloud prefer the API key.

## Fix

1. Verify OTLP variables are all set when no observability data appears.
   Expected: You see the expected output instead of the problem.

## When to use

- You are setting up or using this Elastic Observability APM feature.
- The symptom matches: use API key OR secret token, never both.

## When NOT to use

- Unrelated Elastic Observability APM issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Elastic Observability APM. Source: https://github.com/rajesharma470/elastic-observability-demo.

## Variant phrasings

### use API key OR secret token, never both

## Why it happens

APM agent authentication fails or behaves unexpectedly. Elastic Cloud expects exactly one auth method.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/rajesharma470/elastic-observability-demo

---

Source: [Vectle](https://vectle.com/skills/skl_hBZyUgbgK1MHGI3aj-FwhA). Version: `skv_MEo3raK_rz-VpdXbCkaVVA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
