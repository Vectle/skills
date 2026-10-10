---
name: "refresh-every-views-return-nothing-dur-bae2eebbd0ee9552"
description: "Guide REFRESH EVERY views return nothing during the refresh window: Always include REFRESH AT CREATION so the view has data before the first scheduled run, and use ALIGNED TO to pin the daily or weekly phase instead of accepting the creation-time default. Use this when you hit exactly this in REFRESH EVERY. Not for different errors or different tools."
metadata:
  skill_id: "skl_EDIHMVYyXKqyThHISQ5V6A"
  title: "REFRESH EVERY views return nothing during the refresh window"
  version: "skv_KGwStEOZybQip3m6HJWxyQ"
  updated: "2026-10-03T04:46:02.906205+00:00"
  canonical_url: "https://vectle.com/skills/skl_EDIHMVYyXKqyThHISQ5V6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Always include REFRESH AT CREATION so the view has data before the first scheduled run, and use ALIGNED TO to pin the daily or weekly phase instead of accepting the creation-time default. A REFRESH EVERY materialized view goes dark around each refresh and returns no results in that window; that is by design, not a bug. Put scheduled views in a scheduled cluster (SCHEDULE = ON REFRESH) so compute is hydrated before the refresh lands.

A REFRESH EVERY materialized view goes dark around each refresh and returns no results in that window; that is by design, not a bug. Put scheduled views in a scheduled cluster (SCHEDULE = ON REFRESH) so compute is hydrated before the refresh lands. Always include REFRESH AT CREATION so the view has data before the first scheduled run, and use ALIGNED TO to pin the daily or weekly phase instead of accepting the creation-time default.

Context: Materialize docs CREATE MATERIALIZED VIEW (materializeinclabs/lisp .agents/skills/materialize-docs/sql/create-materialized-view/index.md): Views with REFRESH EVERY strategies have a period of unavailability around each scheduled refresh, during which the view returns no results at all. To avoid that, host them in scheduled clusters that turn on ahead of refresh time. The docs recommend always pairing REFRESH EVERY with REFRESH AT CREATION so the view is queryable ahead of the first scheduled refresh, and ALIGNED TO sets the phase of the schedule.

## When to use
You hit exactly this: REFRESH EVERY views return nothing during the refresh window in REFRESH EVERY.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
REFRESH EVERY.

---

Source: [Vectle](https://vectle.com/skills/skl_EDIHMVYyXKqyThHISQ5V6A). Version: `skv_KGwStEOZybQip3m6HJWxyQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
