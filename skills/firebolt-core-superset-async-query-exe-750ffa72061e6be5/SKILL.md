---
name: "firebolt-core-superset-async-query-exe-750ffa72061e6be5"
description: "Shows how to fix firebolt Core + Superset: async query execution not supported, charts load sequentially. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_naN3Hg4gMln5MJrGmK165A"
  title: "Firebolt Core + Superset: async query execution not supported, charts load sequentially"
  version: "skv_rYa_pLq2EgN5z_kJnZrNfg"
  updated: "2026-10-03T14:12:45.628663+00:00"
  canonical_url: "https://vectle.com/skills/skl_naN3Hg4gMln5MJrGmK165A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_K2mCDObUgiOYsAm_XuDUkQ\",\"https://github.com/firebolt-db/firebolt-core/issues/12\"]"
---

## TL;DR

Use a connection string like: `` firebolt://{database}?url={url} ` Point url` at your Firebolt Core container's address and port. Second, to actually connect Superset to Firebolt Core you need firebolt-sqlalchemy 1.1.0+, which added Core support.

## Steps

1. While evaluating Firebolt Core for Superset dashboards, the reporter noticed the docs say async query execution (`set async=true`) isnt supported in Core. Dashboard charts rendered one after another instead of in parallel. They asked whether async was on the roadmap and whether there was a workaround, since they only run SELECTs.

2. What actually fixes it (verified in the thread):

3. The Firebolt team clarified two things. First, the sequential charts were a driver/setup issue, not a Core limitation: Firebolt Core accepts multiple queries concurrently and executes them in parallel, so you dont need the cloud async feature for dashboard parallelism.

4. Second, to actually connect Superset to Firebolt Core you need `firebolt-sqlalchemy` 1.1.0+, which added Core support. Use a connection string like:

```
firebolt://{database}?url={url}
```

5. Point `url` at your Firebolt Core container's address and port. The reporter got it fully working on Superset 4.1.3 (a stable pre-built Superset; their custom build had the connection problem) and confirmed queries ran.

## When to use

You are seeing this: First, the sequential charts were a driver/setup issue, not a Core limitation: Firebolt Core accepts multiple queries concurrently and executes them in parallel, so you dont need the cloud async feature for dashboard parallelism. Use this skill when you run into "Firebolt Core + Superset: async query execution not supported, charts load sequentially".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: firebolt-sqlalchemy 1.1.0, Superset 4.1.3. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_naN3Hg4gMln5MJrGmK165A). Version: `skv_rYa_pLq2EgN5z_kJnZrNfg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
