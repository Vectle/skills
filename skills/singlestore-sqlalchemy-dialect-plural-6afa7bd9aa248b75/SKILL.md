---
name: "singlestore-sqlalchemy-dialect-plural-6afa7bd9aa248b75"
description: "SingleStore SQLAlchemy dialect: plural table-arg names emit invalid VECTOR_KEYS SQL. The plural forms compile to invalid VECTOR_KEYS [your value] options instead of index DDL, producing the 1064 error. Use when hitting this exact issue with SingleStore SQLAlchemy dialect. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_agYWmuN0kJdi2RnndLcdyA"
  title: "SingleStore SQLAlchemy dialect: plural table-arg names emit invalid VECTOR_KEYS SQL"
  version: "skv_8-Ade_laiaUY1ka2zFkusA"
  updated: "2026-10-03T05:07:48.248093+00:00"
  canonical_url: "https://vectle.com/skills/skl_agYWmuN0kJdi2RnndLcdyA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/singlestore-labs/sqlalchemy-singlestoredb/issues/15\"]"
---

## TL;DR

The plural forms compile to invalid VECTOR_KEYS [your value] options instead of index DDL, producing the 1064 error. Rename the keys in __table_args__ to the singular forms; this was fixed upstream in the docs so new copies of the tutorial are correct. The dialect recognizes only the singular keys singlestoredb_vector_key, singlestoredb_multi_value_index, singlestoredb_full_text_index.

## The error

```text
plural table-arg names emit invalid VECTOR_KEYS SQL
```

## Fix

1. The plural forms compile to invalid VECTOR_KEYS [your value] options instead of index DDL, producing the 1064 error.
   Expected: You get the expected result; the problem is gone.
2. Rename the keys in __table_args__ to the singular forms; this was fixed upstream in the docs so new copies of the tutorial are correct.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with SingleStore SQLAlchemy dialect.
- The symptom matches: plural table-arg names emit invalid VECTOR_KEYS SQL.

## When NOT to use

- A different error message from SingleStore SQLAlchemy dialect; the cause here is specific to this error.
- Unrelated SingleStore SQLAlchemy dialect issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against SingleStore SQLAlchemy dialect. Source: https://github.com/singlestore-labs/sqlalchemy-singlestoredb/issues/15.

## Variant phrasings

### plural table-arg names emit invalid VECTOR_KEYS SQL

## Why it happens

Alembic migrations fail with a 1064 syntax error near 'VECTOR_KEYS [your value] The table args used the plural option names from the tutorial.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/singlestore-labs/sqlalchemy-singlestoredb/issues/15

---

Source: [Vectle](https://vectle.com/skills/skl_agYWmuN0kJdi2RnndLcdyA). Version: `skv_8-Ade_laiaUY1ka2zFkusA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
