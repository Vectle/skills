---
name: "set-numcandidates-to-10-20x-the-limit-2651ecd7c399e730"
description: "Guide Set numCandidates to 10-20x the limit or Atlas Vector Search recall suffers: Start with numCandidates = limit * 20 (for example limit 10 -> numCandidates 200) and tune from there against a recall benchmark. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_i5mebNPYHNXB3S4DpXHm3A"
  title: "Set numCandidates to 10-20x the limit or Atlas Vector Search recall suffers"
  version: "skv_8Nw5ifuQObnVbvantYQ5bQ"
  updated: "2026-10-03T05:10:25.337311+00:00"
  canonical_url: "https://vectle.com/skills/skl_i5mebNPYHNXB3S4DpXHm3A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/romiluz13/hybrid-search-rag/blob/HEAD/docs/cookbook/04-vector-search-optimization.md\"]"
---

TL;DR: Start with numCandidates = limit * 20 (for example limit 10 -> numCandidates 200) and tune from there against a recall benchmark. If retrieval quality is poor, raise numCandidates before blaming the embedding model. If latency is too high, lower it and measure recall so the tradeoff is explicit.

## Fix
1. Start with numCandidates = limit * 20 (for example limit 10 -> numCandidates 200) and tune from there against a recall benchmark.
   Expected: this specific failure stops.
2. Never set numCandidates below limit; the query will not do what you expect.
   Expected: this specific failure stops.

## Details
If retrieval quality is poor, raise numCandidates before blaming the embedding model. If latency is too high, lower it and measure recall so the tradeoff is explicit. Context: Vector search optimization notes: numCandidates is the number of nearest neighbors considered during the search, and the practical rule is 10 to 20 times the limit for good recall. limit cannot exceed numCandidates when numCandidates is specified. Setting numCandidates equal to limit gives the fastest but least accurate search, and it is the most common cause of mysteriously poor RAG retrieval quality. Higher numCandidates improves recall at the cost of latency.

## When to use
You hit exactly this: Set numCandidates to 10-20x the limit or Atlas Vector Search recall suffers.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title.

---

Source: [Vectle](https://vectle.com/skills/skl_i5mebNPYHNXB3S4DpXHm3A). Version: `skv_8Nw5ifuQObnVbvantYQ5bQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
