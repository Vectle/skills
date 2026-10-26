---
name: "metabase-clickhouse-date-filters-ignor-a3a5df3a5f909b69"
description: "If Metabase date filters on ClickHouse return rows that straddle the month boundary, first check the version: this was fixed and backported to the 58.x through 64.x lines, so upgrading is the real fix. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_z-VzxiOq-LAJ21oCy2lByg"
  title: "Metabase ClickHouse date filters ignore report timezone: session_timezone not sent"
  version: "skv_anTYnaJjDk-bTAwJldV4Yg"
  updated: "2026-10-03T04:29:54.899909+00:00"
  canonical_url: "https://vectle.com/skills/skl_z-VzxiOq-LAJ21oCy2lByg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/metabase/metabase/issues/79671\"]"
---

## TL;DR

If Metabase date filters on ClickHouse return rows that straddle the month boundary, first check the version: this was fixed and backported to the 58.x through 64.x lines, so upgrading is the real fix. To confirm you are hitting this bug and not a data issue, run a native question with SELECT timezone(), getSetting('session_timezone'); if it does not return your report timezone, the session timezone is not being applied and relative filters will misbehave.

## Fix

If Metabase date filters on ClickHouse return rows that straddle the month boundary, first check the version: this was fixed and backported to the 58.x through 64.x lines, so upgrading is the real fix. To confirm you are hitting this bug and not a data issue, run a native question with SELECT timezone(), getSetting('session_timezone'); if it does not return your report timezone, the session timezone is not being applied and relative filters will misbehave. Workaround on affected versions: use explicit date ranges instead of relative filters, or wrap the column with toTimeZone in a custom column so the grouping uses the right zone.

Context: GitHub issue metabase/metabase#79671 (closed, 7 comments): with a ClickHouse database and the Metabase report timezone set to anything other than UTC, relative date filters like Current month silently selected the wrong rows: timestamps from the end of the previous month leaked in and rows from the end of the current month were dropped. The ClickHouse driver claimed to set session_timezone but the setting never reached the server, verified by running SELECT timezone(), getSetting('session_timezone') as a native question, which returned UTC and an empty value.

## Matched source
Source: Published skill
Original query: "Metabase ClickHouse date filters ignore report timezone: session_timezone not sent"
Key terms: clickhouse, date, filters, ignore, metabase, report, sent, session, timezone

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_z-VzxiOq-LAJ21oCy2lByg). Version: `skv_anTYnaJjDk-bTAwJldV4Yg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
