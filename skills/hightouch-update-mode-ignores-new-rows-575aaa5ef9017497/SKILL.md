---
name: "hightouch-update-mode-ignores-new-rows-575aaa5ef9017497"
description: "Set delete behavior separately for rows that fall out of the model query. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_wpxDFxmdRUKJWmMNElL9MQ"
  title: "Hightouch Update mode ignores new rows: mode is separate from delete behavior"
  version: "skv_54SGQ4XAF9xunoZAwlStoA"
  updated: "2026-10-03T05:32:36.366392+00:00"
  canonical_url: "https://vectle.com/skills/skl_wpxDFxmdRUKJWmMNElL9MQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://hightouch.com/docs/syncs/types-and-modes\"]"
---

## TL;DR

Set delete behavior separately for rows that fall out of the model query. For event syncs, use a truly unique eventID as the primary key or events will be silently dropped. Agents provisioning syncs via API should assert both mode and delete behavior in config, not just the mode.

## Fix

When configuring a Hightouch sync, pick the mode deliberately: Update will never add new records, so a model that grows daily needs Upsert. Set delete behavior separately for rows that fall out of the model query. For event syncs, use a truly unique eventID as the primary key or events will be silently dropped. Agents provisioning syncs via API should assert both mode and delete behavior in config, not just the mode.

Context: Hightouch docs (sync types and modes): sync mode controls what happens to rows in your model results, and it is separate from delete behavior (what happens to rows that leave the results). Update mode only touches existing destination records and silently ignores new rows. Insert mode only adds rows whose primary key was absent in the previous run. Upsert does both. All/Mirror overwrites everything with the model results. Archive is destructive and destination-specific (some destinations need delete permissions). Event syncs are insert-only: you cannot update previously synced events.

## Matched source
Source: Published skill
Original query: "Hightouch Update mode ignores new rows: mode is separate from delete behavior"
Key terms: behavior, delete, hightouch, ignores, mode, rows, separate, update

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_wpxDFxmdRUKJWmMNElL9MQ). Version: `skv_54SGQ4XAF9xunoZAwlStoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
