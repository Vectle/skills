---
name: "tinybird-analytics-dashboard-empty-out-cf67c094dbf027c7"
description: "Explains why the Tinybird web analytics starter dashboard shows no data outside Europe: the time selector defaults to UTC, so 'Today' late in the US day queries tomorrow, which has no events. Fixed in the starter kit; older versions can adjust the time selector manually. Use when the Tinybird dashboard is empty but the 'users in last 30 minutes' widget shows data. Not for missing events in the data source itself."
metadata:
  skill_id: "skl_IHDDC41MLpUS5jnRS6edyA"
  title: "Tinybird analytics dashboard empty outside Europe unless date adjusted (UTC default)"
  version: "skv_o8LV10kK_79K09Mec5LtTQ"
  updated: "2026-10-03T05:32:42.427093+00:00"
  canonical_url: "https://vectle.com/skills/skl_IHDDC41MLpUS5jnRS6edyA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if the Tinybird analytics dashboard is empty for you outside Europe, check the time selector. It defaulted to UTC, so picking "Today" late in the US day actually queried tomorrow, a day with no data. The team fixed the default in the starter kit. On an older version, manually move the time selector off the UTC default.

What you see:

```text
Tinybird web analytics dashboard shows no data at all, except the
"users in the last 30 minutes" widget; loading it in the US gives an empty dashboard
```

## Steps

1. Look at the dashboard's time selector and check which timezone it is using. If it says UTC and you are hours behind UTC, this is your problem.

2. Change the date range so it covers your local today (or switch the selector off the UTC default). Expected: the selector now spans a day that actually has events.

3. Reload the dashboard. Success check: widgets populate with data, matching what the 30-minute widget already showed.

4. Long term: update to the starter kit version with the fixed default so you stop fighting the selector.

## When to use this

- Tinybird analytics dashboard empty outside Europe, while the "last 30 minutes" widget shows users.
- The emptiness lines up with your local time being far behind UTC.

## When NOT to use this

- The 30-minute widget is also empty; then events are not arriving at all and this is a data-source problem.
- You are querying the API directly; this is purely a dashboard default.

## Compatibility

- Tinybird web analytics starter-kit dashboard before the timezone-default fix. Reporter confirmed the dashboard showed data correctly after the fix.

## Variant phrasings

- tinybird dashboard no data wrong timezone
- tinybird analytics empty dashboard UTC default
- tinybird "today" shows nothing but realtime widget works

## Root cause

The dashboard's time range defaulted to UTC instead of the viewer's local time. Once the US day got late enough, "Today" in UTC was already tomorrow, so every widget queried a day with no events. Only the rolling 30-minute widget was unaffected because it does not depend on the calendar day.

## Edge cases

- Anyone sufficiently behind UTC hits this late in their day; near UTC it only bites around midnight.
- Custom date ranges you set yourself are unaffected; only the default "Today"-style presets were wrong.

Source: Tinybird web analytics starter kit thread

---

Source: [Vectle](https://vectle.com/skills/skl_IHDDC41MLpUS5jnRS6edyA). Version: `skv_o8LV10kK_79K09Mec5LtTQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
