---
name: "pinecone-rest-api-direct-calls-control-dab8b3725a35457e"
description: "Shows how to fix pinecone REST API direct calls: control plane, data plane, headers. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_7XW1VyJTuWSiPnvwafkN0A"
  title: "Pinecone REST API direct calls: control plane, data plane, headers"
  version: "skv_q6z9-iVUi1i-qyERzUVJiw"
  updated: "2026-10-03T14:02:38.238666+00:00"
  canonical_url: "https://vectle.com/skills/skl_7XW1VyJTuWSiPnvwafkN0A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/api-reference\",\"https://docs.pinecone.io/guides/indexes/create-an-index\"]"
---

## TL;DR

Index-scoped host per index. - Data plane (YOUR_YOUR_INDEX_HOST_HOST): upsert, query, fetch, delete vectors. Hosts change; resolve via describe_index every time or cache with a TTL.

## Steps

1. - **Control plane** (`https://api.pinecone.io`): create, describe, list, and delete indexes and collections. Index-scoped host per index.
- **Data plane** (`YOUR_YOUR_INDEX_HOST_HOST`): upsert, query, fetch, delete vectors. Get the host from `describe_index`; it differs per index.

2. Prefer an SDK. Direct REST is for languages without one or for debugging; SDKs handle host routing, retries, and serialization.
2. Never hardcode an index host. Hosts change; resolve via describe_index every time or cache with a TTL.
3. Version-pin with `X-Pinecone-Api-Version` so a server-side default change does not silently alter behavior.
4. Handle 429 and 5xx with backoff; the retry rules are the same as the SDK path.

## When to use

You are seeing this: Get the host from describe\_index; it differs per index. Use this skill when you run into "Pinecone REST API direct calls: control plane, data plane, headers".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://api.pinecone.io`

- YOUR_YOUR_INDEX_HOST_HOST`


---

Source: [Vectle](https://vectle.com/skills/skl_7XW1VyJTuWSiPnvwafkN0A). Version: `skv_q6z9-iVUi1i-qyERzUVJiw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
