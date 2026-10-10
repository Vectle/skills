---
name: "hightouch-mirror-mode-truncates-snowfl-794f78bce4168ce2"
description: "Use Insert for append-only loads and Upsert for dimensional updates. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_pBUnNxI5K0JTwKjynu3AzQ"
  title: "Hightouch Mirror mode TRUNCATEs Snowflake tables before reload"
  version: "skv_dOQw6vlf3hmREwvcuaH_PQ"
  updated: "2026-10-03T05:31:31.029092+00:00"
  canonical_url: "https://vectle.com/skills/skl_pBUnNxI5K0JTwKjynu3AzQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use Insert for append-only loads and Upsert for dimensional updates. Ensure the matching column is actually declared UNIQUE or PRIMARY KEY in Snowflake or record matching will silently have no options. Tune the 50k default batch down if you need per-row error visibility.

## Fix

When syncing to Snowflake via Hightouch, never use Mirror mode on a table that other processes write to: the TRUNCATE wipes everything first. Use Insert for append-only loads and Upsert for dimensional updates. Ensure the matching column is actually declared UNIQUE or PRIMARY KEY in Snowflake or record matching will silently have no options. Tune the 50k default batch down if you need per-row error visibility.

Context: Hightouch docs (Snowflake destination): Mirror mode TRUNCATEs the destination table and then COPY INTOs all model rows, wiping existing data before reload. Insert mode is faster and better for pure row additions with per-row error identification. Upsert uses MERGE INTO. The record-matching column you select must be a UNIQUE or PRIMARY KEY column in Snowflake, or it will not appear in the dropdown. Default batch size is 50,000 rows per query and is tunable.

## Matched source
Source: Published skill
Original query: "Hightouch Mirror mode TRUNCATEs Snowflake tables before reload"
Key terms: before, hightouch, mirror, mode, reload, snowflake, tables, truncates

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_pBUnNxI5K0JTwKjynu3AzQ). Version: `skv_dOQw6vlf3hmREwvcuaH_PQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
