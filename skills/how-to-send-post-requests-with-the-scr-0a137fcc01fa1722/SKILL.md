---
name: "how-to-send-post-requests-with-the-scr-0a137fcc01fa1722"
description: "Walks through send POST requests with the ScrapingAnt Python client, step by step. Use it when you need to do exactly this. Not a troubleshooting guide, so skip it if you are here because of an error."
metadata:
  skill_id: "skl_QfUVVI02CYziVbNrBKeY_Q"
  title: "How to send POST requests with the ScrapingAnt Python client"
  version: "skv_8P0A-su0grhn3Gr5ue4nEg"
  updated: "2026-10-03T14:16:10.039861+00:00"
  canonical_url: "https://vectle.com/skills/skl_QfUVVI02CYziVbNrBKeY_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_X1ye997nnFtkwd9vrWRZow\",\"https://github.com/ScrapingAnt/scrapingant-client-python/issues/30\"]"
---

## TL;DR

Fix: upgrade with pip install --upgrade scrapingant-client to 2.0.0+, then use the POST example from the client's 2.0.0 README (sending POST requests section). POST requests were added in ScrapingAnt's API v2, and the Python client 1.x only targets API v1.

## Steps

1. POST requests were added in ScrapingAnt's API v2, and the Python client 1.x only targets API v1. The maintainer confirmed the gap and released client 2.0.0 with POST support against the v2 API. Fix: upgrade with `pip install --upgrade scrapingant-client` to 2.0.0+, then use the POST example from the client's 2.0.0 README (sending POST requests section).

Expected: The maintainer confirmed the gap and released client 2.0.0 with POST support against the v2 API.

## When to use

You are seeing this: The ScrapingAnt Python client only sends GET requests through API v1. Use this skill when you run into "How to send POST requests with the ScrapingAnt Python client".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: client 2.0.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_QfUVVI02CYziVbNrBKeY_Q). Version: `skv_8P0A-su0grhn3Gr5ue4nEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
