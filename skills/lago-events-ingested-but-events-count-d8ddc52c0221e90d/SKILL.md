---
name: "lago-events-ingested-but-events-count-d8ddc52c0221e90d"
description: "Shows how to fix lago events ingested but events_count stays 0 in current usage API. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_UEHkvpTIQVnaKeFakVRBKw"
  title: "Lago events ingested but events_count stays 0 in current usage API"
  version: "skv_tpEX7tpjK6WMoRMWvYSayA"
  updated: "2026-10-03T14:01:27.58002+00:00"
  canonical_url: "https://vectle.com/skills/skl_UEHkvpTIQVnaKeFakVRBKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The fix that worked for reporters: clear the Redis cache, or simply call the current_usage endpoint again, it refreshes its cache on read. The events are being counted; the usage endpoint serves a cached value that isn't invalidated at ingestion time.

## Steps

1. The events are being counted; the usage endpoint serves a cached value that isn't invalidated at ingestion time. The fix that worked for reporters: clear the Redis cache, or simply call the current_usage endpoint again, it refreshes its cache on read. Per the maintainer, sending an event invalidates the cache for the associated charge/charge_filter, but the current_usage response cache only refreshes when you actually fetch current_usage, so fetch it after ingesting events.

## When to use

You are seeing this: Events POSTed to /api/v1/events were accepted (returned a lago_id) and visible in the developer events UI, but the current usage API kept returning events_count = 0 for a count_agg billable metric (code chat_number). Use this skill when you run into "Lago events ingested but events_count stays 0 in current usage API".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Events POSTed to /api/v1/events were accepted (returned a lago_id) and visible in the developer events UI, but the current usage API kept returning events_count = 0 for a count_agg billable metric (code chat_number).


---

Source: [Vectle](https://vectle.com/skills/skl_UEHkvpTIQVnaKeFakVRBKw). Version: `skv_tpEX7tpjK6WMoRMWvYSayA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
