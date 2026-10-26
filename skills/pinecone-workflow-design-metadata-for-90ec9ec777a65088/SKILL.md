---
name: "pinecone-workflow-design-metadata-for-90ec9ec777a65088"
description: "Metadata is schemaless but filters are typed. Normalize types at ingest, index what you filter, and keep filterable fields small; 40 KB per record is the cap. Not the full reference manual."
metadata:
  skill_id: "skl_-fLnGcsH9wRpaAnuk1TA8g"
  title: "Pinecone workflow: design metadata for filtering that actually works"
  version: "skv_eJa17zESSFheQ4xAoN5knA"
  updated: "2026-10-03T14:06:23.695749+00:00"
  canonical_url: "https://vectle.com/skills/skl_-fLnGcsH9wRpaAnuk1TA8g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/search/filter-by-metadata\",\"https://docs.pinecone.io/guides/index-data/upsert-data\"]"
---

**TL;DR:** Metadata is schemaless but filters are typed. Normalize types at ingest, index what you filter, and keep filterable fields small; 40 KB per record is the cap. Filter on what you index. Keep filterable fields small.

# Metadata filtering: design it, do not accumulate it

## Principles

1. **Types are a contract.** `$gt` on a string field, `$in` with a scalar, `$exists` expecting a boolean: filters assume the stored type. Store every field with one consistent type across all records or filters misbehave silently.
2. **Filter on what you index.** Only metadata you actually upsert is filterable. If the query needs `tenant_id`, `doc_type`, and `published_year`, every record needs those fields.
3. **Keep filterable fields small.** Metadata caps at 40 KB per record. Bloated metadata slows writes and wastes storage; keep full document text in your own store and a pointer in metadata.
4. **Prefer equality and range on low-cardinality fields.** High-cardinality unique-per-record fields as filters are a smell; that is what ids are for.

## Recommended shape

```
{
  "tenant_id": "acme",
  "doc_type": "handbook",
  "published_year": 2025,
  "source": "support-docs",
  "chunk": 3
}
```

Flat, typed, small. Nested objects complicate filters; denormalize one level.

## Operator cheat sheet

`$eq`, `$ne` for equality; `$gt`, `$gte`, `$lt`, `$lte` for ranges on numbers; `$in`, `$nin` for lists; `$exists` for presence; `$and`, `$or` to combine. Text-match operators (`$match_phrase`, `$match_all`, `$match_any`) apply to full-text fields on document-schema indexes.

## Traps

1. Inconsistent types across records (`year` as string in old records, number in new): range filters silently drop the mismatched ones.
2. Filtering on fields that only some records have without `$exists` handling: missing field is not null, it is absent, and absent never matches `$eq`.
3. Stuffing the whole document into metadata "for convenience": hits the 40 KB cap and slows every write.

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

Source: [Vectle](https://vectle.com/skills/skl_-fLnGcsH9wRpaAnuk1TA8g). Version: `skv_eJa17zESSFheQ4xAoN5knA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
