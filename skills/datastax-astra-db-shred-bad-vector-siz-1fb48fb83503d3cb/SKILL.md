---
name: "datastax-astra-db-shred-bad-vector-siz-1fb48fb83503d3cb"
description: "DataStax Astra DB: SHRED_BAD_VECTOR_SIZE / dimension mismatch after model switch. The fix is to delete the collection in the Astra DB Data Explorer and re-create it with the correct dimension, then re-seed. Use when hitting this exact issue with DataStax Astra DB. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_QWu7W2eUnK8XR9_jsmVfkQ"
  title: "DataStax Astra DB: SHRED_BAD_VECTOR_SIZE / dimension mismatch after model switch"
  version: "skv_Fc0dEq6vRmhlF4s9j7yfcA"
  updated: "2026-10-03T13:55:24.193541+00:00"
  canonical_url: "https://vectle.com/skills/skl_QWu7W2eUnK8XR9_jsmVfkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/abhinavjd7/chatbotrc\"]"
---

## TL;DR

The fix is to delete the collection in the Astra DB Data Explorer and re-create it with the correct dimension, then re-seed. Astra DB collections pin the vector dimension at creation time, so switching embedding models (for example 1024-dim to 768-dim) breaks the collection.

## Fix

1. The fix is to delete the collection in the Astra DB Data Explorer and re-create it with the correct dimension, then re-seed.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this DataStax Astra DB feature.
- The symptom matches: SHRED_BAD_VECTOR_SIZE / dimension mismatch after model switch.

## When NOT to use

- Unrelated DataStax Astra DB issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against DataStax Astra DB. Source: https://github.com/abhinavjd7/chatbotrc.

## Variant phrasings

### SHRED_BAD_VECTOR_SIZE / dimension mismatch after model switch

## Why it happens

Inserts or vector searches fail with a vector dimension error. The collection was created with a different vector dimension than the embedding model now produces.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/abhinavjd7/chatbotrc

---

Source: [Vectle](https://vectle.com/skills/skl_QWu7W2eUnK8XR9_jsmVfkQ). Version: `skv_Fc0dEq6vRmhlF4s9j7yfcA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
