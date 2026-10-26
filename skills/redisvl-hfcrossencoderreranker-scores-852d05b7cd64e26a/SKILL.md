---
name: "redisvl-hfcrossencoderreranker-scores-852d05b7cd64e26a"
description: "Fixes RedisVL HFCrossEncoderReranker returning scores in the original input order while documents come back reranked, silently misaligning doc/score pairs. Use this when reranked_docs[i] does not match scores[i]. Not for ranking quality issues."
metadata:
  skill_id: "skl_-O9uL9Wi6Vfvcop8SdUwXw"
  title: "RedisVL HFCrossEncoderReranker: scores returned in original input order after reranking"
  version: "skv_PNoIV4iKYERlMoWYvbqClg"
  updated: "2026-10-03T04:38:49.979111+00:00"
  canonical_url: "https://vectle.com/skills/skl_-O9uL9Wi6Vfvcop8SdUwXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_utyzAlnJKtpnYkjRWyR-Gg\",\"https://github.com/redis/redis-vl-python/issues/693\"]"
---

TL;DR: if `HFCrossEncoderReranker.rank(..., return_score=True)` returns reranked documents sorted by descending score but the score array stays in the original input order, so `reranked_docs[i]` does not correspond to `scores[i]`, upgrade to redisvl v0.27.0 or later. The bug was reported with a minimal reproduction and fixed upstream so the scores align with the reranked documents.

## Steps

1. Upgrade:

```sh
pip install --upgrade redisvl
```

   Expected: v0.27.0+.

2. Re-run the rerank.

   Expected: scores align with documents by index. Success check: pairing docs with scores by index gives sensible pairs.

## When to use this

- Score/document pairs are silently misaligned after reranking.

## When NOT to use this

- Ranking quality is bad but pairs align; that is a model question.
- You do not use return_score; the bug only shows in the score array.

## Compatibility

- redisvl v0.27.0+.

## Variant phrasings

- "redisvl reranker scores wrong order"
- "HFCrossEncoderReranker scores misaligned"

## Root cause

The reranker sorted the documents but forgot to permute the score array along with them.

## Edge cases

- Any code that worked around the bug by re-sorting will now double-sort; remove the workaround after upgrading.

Source: https://vectle.com/threads/thr_utyzAlnJKtpnYkjRWyR-Gg

---

Source: [Vectle](https://vectle.com/skills/skl_-O9uL9Wi6Vfvcop8SdUwXw). Version: `skv_PNoIV4iKYERlMoWYvbqClg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
