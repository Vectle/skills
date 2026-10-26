---
name: "pinecone-diagnosis-upsert-400s-on-larg-62d51b79763fdca2"
description: "Symptom: big upsert batches fail with 400 Invalid Argument while small ones work. The request exceeds the size cap; split into smaller batches. Not the full reference manual."
metadata:
  skill_id: "skl_DFgA2tbOsEqR4G5rmTceIw"
  title: "Pinecone diagnosis: upsert 400s on large batches"
  version: "skv_GHdnK4KE37UIEpjacE2wNA"
  updated: "2026-10-03T14:36:22.027044+00:00"
  canonical_url: "https://vectle.com/skills/skl_DFgA2tbOsEqR4G5rmTceIw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/index-data/upsert-data\",\"https://docs.pinecone.io/guides/production/error-handling\"]"
---

**TL;DR:** Symptom: big upsert batches fail with 400 Invalid Argument while small ones work. The request exceeds the size cap; split into smaller batches. Confirm it 1. Check per-record limits too: 512-char ids, 40 KB metadata, 2048 sparse non-zeros.

## The fix

# Diagnosis

## Symptom

Upserting thousands of vectors in one call returns 400; the same vectors succeed in smaller batches.

## Likely cause

Single upsert requests are capped at about 2 MB. Large batches with rich metadata exceed it. The 400 is deterministic for the same payload.

## Confirm it

1. Halve the batch until it succeeds; the threshold you find is your effective cap for that vector shape.
2. Estimate: dimension times 4 bytes per vector plus metadata; keep batches comfortably under 2 MB.
3. Check per-record limits too: 512-char ids, 40 KB metadata, 2048 sparse non-zeros.

## Fix

Batch by byte size, not just count: accumulate vectors until near the cap, then send. Parallelize across batches for throughput, with backoff on 429.

## Verify the fix

Ingest the full dataset with the new batcher and assert `describe_index_stats` totals equal the source count.

## When to use this

- This covers exactly what the title says: Pinecone diagnosis.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_DFgA2tbOsEqR4G5rmTceIw). Version: `skv_GHdnK4KE37UIEpjacE2wNA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
