---
name: "neon-pgvector-hnsw-index-fails-on-3072-0dc471a64b5cb2e5"
description: "Neon pgvector: HNSW index fails on 3072-dimension embeddings (2000-dim limit). Also note Neon free's default maintenance_work_mem is 64 MB: raise it before building the index (SET maintenance_work_mem='256MB') or the build falls back to the slow on-disk two-pass path. Use when hitting this exact issue with Neon pgvector. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_-b5OXMTFnkPfuV4bRul3iA"
  title: "Neon pgvector: HNSW index fails on 3072-dimension embeddings (2000-dim limit)"
  version: "skv_fB_Lp62ZC5K-WIfd5RzImw"
  updated: "2026-10-03T05:11:59.990753+00:00"
  canonical_url: "https://vectle.com/skills/skl_-b5OXMTFnkPfuV4bRul3iA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/aurahq-ai/aura/blob/HEAD/content/blog/why-neon-postgres.mdx\"]"
---

## TL;DR

Also note Neon free's default maintenance_work_mem is 64 MB: raise it before building the index (SET maintenance_work_mem='256MB') or the build falls back to the slow on-disk two-pass path. Do not ANN-index vector(3072) directly: use text-embedding-3-small (1536 dims) or another &lt;=2000-dim representation, or switch the column to halfvec to halve the dimension footprint.

## The error

```text
HNSW index fails on 3072-dimension embeddings (2000-dim limit)
```

## Fix

1. Also note Neon free's default maintenance_work_mem is 64 MB: raise it before building the index (SET maintenance_work_mem='256MB') or the build falls back to the slow on-disk two-pass path.
   Expected: You get the expected result; the problem is gone.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Neon pgvector.
- The symptom matches: HNSW index fails on 3072-dimension embeddings (2000-dim limit).

## When NOT to use

- A different error message from Neon pgvector; the cause here is specific to this error.
- Unrelated Neon pgvector issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Neon pgvector. Source: https://github.com/aurahq-ai/aura/blob/HEAD/content/blog/why-neon-postgres.mdx.

## Variant phrasings

### HNSW index fails on 3072-dimension embeddings (2000-dim limit)

## Why it happens

Creating an HNSW index on a vector(3072) column fails. pgvector has a hard 2000-dimension limit for HNSW indexes on the vector type.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/aurahq-ai/aura/blob/HEAD/content/blog/why-neon-postgres.mdx

---

Source: [Vectle](https://vectle.com/skills/skl_-b5OXMTFnkPfuV4bRul3iA). Version: `skv_fB_Lp62ZC5K-WIfd5RzImw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
