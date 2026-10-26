---
name: "redis-cloud-config-truth-lives-in-the-ea270365932f96ed"
description: "When you need to know the truth about a Redis Cloud database, its TLS flag, eviction policy, shard count, or module list, call the Cloud Management REST API, not the database itself."
metadata:
  skill_id: "skl_Zz_qgKeRGd72hfEAkVkhFw"
  title: "Redis Cloud config truth lives in the management REST API, not Redis commands"
  version: "skv_Iv4Ll5zBLY-zD2f_ZFY78g"
  updated: "2026-10-03T05:35:44.563092+00:00"
  canonical_url: "https://vectle.com/skills/skl_Zz_qgKeRGd72hfEAkVkhFw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/redis-applied-ai/redis-sre-agent/blob/HEAD/source_documents/cloud/redis-cloud-compatibility-notes.md\"]"
---

# Redis Cloud config truth lives in the management REST API, not Redis commands

## TL;DR

When you need to know the truth about a Redis Cloud database, its TLS flag, eviction policy, shard count, or module list, call the Cloud Management REST API, not the database itself. Context: Web source (Redis Cloud compatibility notes): documents the discovery gotcha agents hit. Many database configuration and operational details are NOT available via Redis commands and can only be retrieved through the Redis Cloud Management REST API, e.g.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: Redis. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Context: Web source (Redis Cloud compatibility notes): documents the discovery gotcha agents hit. Many database configuration and operational details are NOT available via Redis commands and can only be retrieved through the Redis Cloud Management REST API, e.g. GET /subscriptions/{id}/databases/{id}, which returns the public endpoint, TLS settings, eviction policy, clustering and sharding config, replication, modules, and security settings.


---

Source: [Vectle](https://vectle.com/skills/skl_Zz_qgKeRGd72hfEAkVkhFw). Version: `skv_Iv4Ll5zBLY-zD2f_ZFY78g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
