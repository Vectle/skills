---
name: "tidb-vector-index-restrictions-tiflash-1bda0c67e19cb960"
description: "TiDB vector index restrictions: TiFlash required, cosine and L2 only. TiFlash nodes must be deployed in the cluster first; the feature relies on TiFlash replicas, so set TIFLASH REPLICA 1 before creating the index unless it is in CREATE TABLE. Use when hitting this exact issue with TiDB vector index restrictions. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_Qcq3OcmERyqolLE5AFMZ4A"
  title: "TiDB vector index restrictions: TiFlash required, cosine and L2 only"
  version: "skv_6n8Hr3KcSGOJziqnNTgjlQ"
  updated: "2026-10-03T04:47:06.732181+00:00"
  canonical_url: "https://vectle.com/skills/skl_Qcq3OcmERyqolLE5AFMZ4A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

TiFlash nodes must be deployed in the cluster first; the feature relies on TiFlash replicas, so set TIFLASH REPLICA 1 before creating the index unless it is in CREATE TABLE. Only VEC_COSINE_DISTANCE and VEC_L2_DISTANCE are indexable.

## Fix

1. TiFlash nodes must be deployed in the cluster first; the feature relies on TiFlash replicas, so set TIFLASH REPLICA 1 before creating the index unless it is in CREATE TABLE.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this TiDB vector index restrictions feature.
- The symptom matches: TiFlash required, cosine and L2 only.

## When NOT to use

- Unrelated TiDB vector index restrictions issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against TiDB vector index restrictions (mentions v8.4, v8.5). Source: https://docs.pingcap.com/tidb/dev/vector-search-index/.

## Variant phrasings

### TiFlash required, cosine and L2 only

## Why it happens

TiDB vector search indexes have hard restrictions. Hitting one produces a confusing failure far from the real cause.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.pingcap.com/tidb/dev/vector-search-index/

---

Source: [Vectle](https://vectle.com/skills/skl_Qcq3OcmERyqolLE5AFMZ4A). Version: `skv_6n8Hr3KcSGOJziqnNTgjlQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
