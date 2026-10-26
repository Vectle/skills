---
name: "pinecone-workflow-bulk-upsert-millions-11ae54941d3687df"
description: "Batch by byte size under the 2 MB request cap, parallelize batches with backoff, and verify totals with describe_index_stats. The naive loop is 10x slower and 429-prone. Not the full reference manual."
metadata:
  skill_id: "skl_qKKsjIt1Q1ACuXSQFIHHsw"
  title: "Pinecone workflow: bulk upsert millions of vectors with batching"
  version: "skv_r5rThtg015b36hkOA5F7wA"
  updated: "2026-10-03T14:14:39.692055+00:00"
  canonical_url: "https://vectle.com/skills/skl_qKKsjIt1Q1ACuXSQFIHHsw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/index-data/upsert-data\",\"https://docs.pinecone.io/guides/production/error-handling\"]"
---

**TL;DR:** Batch by byte size under the 2 MB request cap, parallelize batches with backoff, and verify totals with describe_index_stats. The naive loop is 10x slower and 429-prone. Batch by bytes. Retry 429 and 5xx with backoff.

## The fix

1. **Embed first, or stream.** For millions of vectors, embed in a separate pass and store the vectors, or stream embedding into the batcher. Do not re-embed on retry.

2. **Batch by bytes.** A request caps at about 2 MB. Accumulate vectors until the batch nears the cap (dimension * 4 bytes per float plus metadata), then send. Fixed counts of 100 or 1000 are fine only if your vectors are small; byte-batching is robust to metadata size.

3. **Parallelize with a cap.** 4 to 10 concurrent upserts is a sane starting point. More than that and 429s eat the gains.

4. **Retry 429 and 5xx with backoff.** Never retry 400: a 400 is a malformed batch, and resending it is a loop.

5. **Checkpoint.** Record the last successfully sent batch id. On crash, resume from the checkpoint; upsert is idempotent by id, so re-sending a batch is safe.

6. **Verify.** `describe_index_stats()` total must equal the source count. Sample-fetch random ids.

7. One vector per upsert call: works for 100 vectors, 429s and crawls at 100k.

8. Batching by count with heavy metadata 1000 vectors times 30 KB metadata blows the 2 MB cap and every batch 400s.

9. No checkpointing: a crash at 90 percent restarts the whole ingest.

10. Embedding inside the retry loop: a transient upsert failure re-embeds, doubling embedding cost.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_qKKsjIt1Q1ACuXSQFIHHsw). Version: `skv_r5rThtg015b36hkOA5F7wA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
