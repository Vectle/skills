---
name: "redis-cloud-free-tier-defaults-to-vola-f9e61adbc0b460ae"
description: "Check the eviction policy on your Redis Cloud database before using it as a queue backend."
metadata:
  skill_id: "skl_qI47AmN_u6WtVTDpxhqgoQ"
  title: "Redis Cloud free tier defaults to volatile lru, switch queues to noeviction"
  version: "skv_2u5Mp_XF70MhVSnV_5syVA"
  updated: "2026-10-03T05:35:02.648511+00:00"
  canonical_url: "https://vectle.com/skills/skl_qI47AmN_u6WtVTDpxhqgoQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Redis Cloud free tier defaults to volatile lru, switch queues to noeviction

## TL;DR

Use allkeys-lru only for pure caches where losing entries is acceptable. Check the eviction policy on your Redis Cloud database before using it as a queue backend. Context: Redis operational skill notes (k8s-ai-operator redis SKILL): documents the eviction-policy mismatch gotcha.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: Redis. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Use allkeys-lru only for pure caches where losing entries is acceptable.

Context: Redis operational skill notes (k8s-ai-operator redis SKILL): documents the eviction-policy mismatch gotcha. Picking the wrong maxmemory-policy is a common source of confusing behavior: noeviction on a cache-only deployment causes writes to start failing under memory pressure instead of evicting, while allkeys-lru on Redis used as a primary store can silently evict data that was never meant to expire. volatile-lru only evicts keys with a TTL set.


---

Source: [Vectle](https://vectle.com/skills/skl_qI47AmN_u6WtVTDpxhqgoQ). Version: `skv_2u5Mp_XF70MhVSnV_5syVA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
