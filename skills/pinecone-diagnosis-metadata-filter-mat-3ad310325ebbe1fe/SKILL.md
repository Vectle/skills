---
name: "pinecone-diagnosis-metadata-filter-mat-3ad310325ebbe1fe"
description: "Symptom: query with a filter returns empty but unfiltered query works. Check field names, value types, and operator shapes; one wrong type poisons the whole filter. Not the full reference manual."
metadata:
  skill_id: "skl_FMG-gjlt41OjU53-89xtwA"
  title: "Pinecone diagnosis: metadata filter matches nothing"
  version: "skv_Pgt99oOWy6Bg__VV0z2KBg"
  updated: "2026-10-03T14:44:37.281389+00:00"
  canonical_url: "https://vectle.com/skills/skl_FMG-gjlt41OjU53-89xtwA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/search/filter-by-metadata\"]"
---

**TL;DR:** Symptom: query with a filter returns empty but unfiltered query works. Check field names, value types, and operator shapes; one wrong type poisons the whole filter. Confirm it 1. Fetch a known record and print its metadata keys and value types.

## The error

```text
query with a filter returns empty but unfiltered query works. Check field names, value types, and operator shapes; one wrong type poisons the whole filter. Confirm it 1. Fetch a known record and print its metadata keys and value types.
```

## The fix

1. Fetch a known record and print its metadata keys and value types.

2. Compare each filter clause against those exact keys and types.

3. Test clauses one at a time: add them incrementally until matches vanish; the last clause added is the culprit.

4. Check operator shapes: `$in` needs a list, `$gt` needs a number, `$exists` needs a boolean.

5. Fix the field name or type to match what is actually stored.

6. If metadata was stored with inconsistent types across records (some string, some number), re-ingest with normalized types.

7. Keep a schema document for metadata fields; filters are only as reliable as the schema.

8. This covers exactly what the title says: Pinecone diagnosis.

9. You are setting this up for the first time, or auditing an existing setup.

10. You want the key gotchas in one place before you start.

11. You are doing a different workflow with Pinecone; these steps are specific to the title above.

12. You need the full reference docs; this is the short path, not the manual.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Pinecone diagnosis.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_FMG-gjlt41OjU53-89xtwA). Version: `skv_Pgt99oOWy6Bg__VV0z2KBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
