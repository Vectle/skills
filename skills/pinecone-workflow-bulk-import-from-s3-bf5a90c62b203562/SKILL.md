---
name: "pinecone-workflow-bulk-import-from-s3-bf5a90c62b203562"
description: "For very large datasets, skip the upsert API and import Parquet files directly from object storage. Stage the files, create the import, poll to completion. Not the full reference manual."
metadata:
  skill_id: "skl_wbj1e5OUczwO-sh-LvERgg"
  title: "Pinecone workflow: bulk import from S3, GCS, or Azure Blob"
  version: "skv_tWsJBuMdaxH376eTrkAz0A"
  updated: "2026-10-03T13:59:11.464497+00:00"
  canonical_url: "https://vectle.com/skills/skl_wbj1e5OUczwO-sh-LvERgg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** For very large datasets, skip the upsert API and import Parquet files directly from object storage. Stage the files, create the import, poll to completion. Keep files at a sane size (hundreds of MB, not tens of GB each). Grant Pinecone read access to the bucket or container via the documented storage integration.

## The fix

**TL;DR:** For very large datasets, skip the upsert API and import Parquet files directly from object storage. Stage the files, create the import, poll to completion. Keep files at a sane size (hundreds of MB, not tens of GB each). Grant Pinecone read access to the bucket or container via the documented storage integration.

# Bulk import from object storage

## When to use it

Millions of vectors or a recurring full refresh. Import reads Parquet files from your bucket; it bypasses per-request upsert limits and is the fastest path for bulk loads.

## Steps

1. **Stage Parquet files** in S3, GCS, or Azure Blob Storage. Records carry id, values, optional sparse values, and metadata. Keep files at a sane size (hundreds of MB, not tens of GB each).
2. **Grant Pinecone read access** to the bucket or container via the documented storage integration. The import cannot read what it cannot access; permission errors here are the most common failure.
3. **Create the target index first** with the right dimension, metric, and vector type. Import does not create indexes.
4. **Start the import** pointing at the bucket prefix. One import per prefix; do not overlap prefixes between concurrent imports.
5. **Poll to completion.** Imports run async. Watch for partial failures: a few bad records can fail while the rest succeed, so check the error counts, not just the status.
6. **Verify.** `describe_index_stats` totals vs source row counts; sample-fetch.

## Traps

1. Schema drift between files: one file with a missing metadata column or wrong vector width fails its records. Validate one file end to end before launching the full import.
2. Importing into the live serving index during peak traffic: schedule bulk imports off-peak or into a fresh index and cut over.
3. Assuming import upserts are visible instantly: allow settle time before the verification queries.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_wbj1e5OUczwO-sh-LvERgg). Version: `skv_tWsJBuMdaxH376eTrkAz0A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
