---
name: "binary-vectors-querying-the-nearest-ne-998df78b40c761db"
description: "Guide Binary vectors - querying the nearest neighbors by Hamming distance with HNSW gives wrong results: [ankane (maintainer)]: Thanks, it looks like the index is working fine. Approximate indexing won't provide perfect recall. Use this when you hit exactly this in Binary. Not for different errors or different tools."
metadata:
  skill_id: "skl_OuhDJMtg0g8iVylmH37nbQ"
  title: "Binary vectors - querying the nearest neighbors by Hamming distance with HNSW gives wrong results"
  version: "skv_LGkXn5qYUhw4SJQNP6cmNg"
  updated: "2026-10-03T04:45:28.336732+00:00"
  canonical_url: "https://vectle.com/skills/skl_OuhDJMtg0g8iVylmH37nbQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: [ankane (maintainer)]: Thanks, it looks like the index is working fine. Approximate indexing won't provide perfect recall. Also, you may see better recall by splitting unique hashes into a separate table, as well as increasing

[ankane (maintainer)]: Thanks, it looks like the index is working fine. Approximate indexing won't provide perfect recall. Also, you may see better recall by splitting unique hashes into a separate table, as well as increasing `ef_construction` even further (I'd try 512 next).

Context:
GitHub issue pgvector/pgvector#972 (closed, 8 comments): Hi. So, I have pgvector 0.8.1, postgres 17.7, and a table like this with ~20kk records: ```ruby create_table :image_hashes do |t| t.column :external_id, :integer, null: false t.column :vector_binary, :bit, limit: 576 t.timestamps end add_index :image_hashes, :external_id, unique: true execute 'CREATE INDEX ON image_hashes USING hnsw (vector_binary bit_hamming_ops);' ``` I clearly see that the needed record is in the table: ``` SELECT (vector_binary [~] '[576 bits omitted]') AS distance FROM image_hashes WHERE external_id = 608810322 LIMIT 1; distance ---------- 0 (1 row) ``` But querying the n

## When to use
You hit exactly this: Binary vectors - querying the nearest neighbors by Hamming distance with HNSW gives wrong results in Binary.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Binary (versions mentioned here: 0.8.1, 17.7).

## Edge cases
- Also, you may see better recall by splitting unique hashes into a separate table, as well as increasing.

---

Source: [Vectle](https://vectle.com/skills/skl_OuhDJMtg0g8iVylmH37nbQ). Version: `skv_LGkXn5qYUhw4SJQNP6cmNg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
