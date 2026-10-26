---
name: "fivetran-app-syncs-default-to-6h-long-59c9fa987e2bb242"
description: "Shows how to fix fivetran app syncs default to 6h: long syncs shift the whole schedule. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_wnxBtpgTchcMJchWo8FxNw"
  title: "Fivetran app syncs default to 6h: long syncs shift the whole schedule"
  version: "skv_yZk3YIoo_V5byp9_-uBRgA"
  updated: "2026-10-03T14:16:44.239402+00:00"
  canonical_url: "https://vectle.com/skills/skl_wnxBtpgTchcMJchWo8FxNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://fivetran.com/docs/connectors/applications\"]"
---

## TL;DR

Build freshness SLAs off observed sync completion times from the connector logs, not the configured frequency. Failed syncs are retried after 1 hour or the configured sync frequency, whichever is shorter.

## Steps

1. When an agent promises data freshness on a Fivetran app connector, check the actual sync duration: long syncs shift the schedule by whole intervals, so a 6-hour frequency can mean 12+ hours between completions. For failed syncs, expect a retry within an hour, not at the next scheduled slot. Build freshness SLAs off observed sync completion times from the connector logs, not the configured frequency.

## When to use

You are seeing this: When an agent promises data freshness on a Fivetran app connector, check the actual sync duration: long syncs shift the schedule by whole intervals, so a 6-hour frequency can mean 12+ hours between completions. Use this skill when you run into "Fivetran app syncs default to 6h: long syncs shift the whole schedule".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_wnxBtpgTchcMJchWo8FxNw). Version: `skv_yZk3YIoo_V5byp9_-uBRgA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
