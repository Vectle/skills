---
name: "fivetran-fivetran-deleted-lies-during-2ec7dae7a8ba8de8"
description: "Shows how to fix fivetran _fivetran_deleted lies during re-syncs: wait for completion. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_6uEEY2Hh12XBZNwQMyk1Mg"
  title: "Fivetran _fivetran_deleted lies during re-syncs: wait for completion"
  version: "skv_iE7_cmZVRsY_lz5l2H3TZw"
  updated: "2026-10-03T14:17:26.123447+00:00"
  canonical_url: "https://vectle.com/skills/skl_6uEEY2Hh12XBZNwQMyk1Mg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://fivetran.com/docs/connectors/troubleshooting/system-columns-during-resync\"]"
---

## TL;DR

Alerting on _fivetran_deleted during a re-sync is a classic false-positive generator. Mid-re-sync, live rows can briefly appear deleted and deleted rows briefly appear active.

## Steps

1. If an agent orchestrates Fivetran re-syncs, gate every downstream consumer on re-sync completion status before trusting system columns: check the sync state via the REST API first. Alerting on _fivetran_deleted during a re-sync is a classic false-positive generator. Build the pause-readers-then-resync-then-resume pattern into any Fivetran automation.

## When to use

You are seeing this: If an agent orchestrates Fivetran re-syncs, gate every downstream consumer on re-sync completion status before trusting system columns: check the sync state via the REST API first. Use this skill when you run into "Fivetran _fivetran_deleted lies during re-syncs: wait for completion".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_6uEEY2Hh12XBZNwQMyk1Mg). Version: `skv_iE7_cmZVRsY_lz5l2H3TZw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
