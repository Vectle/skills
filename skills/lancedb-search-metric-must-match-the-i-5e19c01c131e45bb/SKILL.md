---
name: "lancedb-search-metric-must-match-the-i-5e19c01c131e45bb"
description: "Build the index and query with the same metric: l2, cosine, or dot (hamming is IVF_FLAT only). Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_Qc5G7HFFhaG8Ao3uq5qLrQ"
  title: "LanceDB search metric must match the index metric or the index is skipped"
  version: "skv_K0lcfXPCL5MU_zli-vmPyg"
  updated: "2026-10-03T04:48:41.222964+00:00"
  canonical_url: "https://vectle.com/skills/skl_Qc5G7HFFhaG8Ao3uq5qLrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Build the index and query with the same metric: l2, cosine, or dot (hamming is IVF_FLAT only). If you omit the metric, current SDKs inherit the index metric, but on older SDK versions set it explicitly to match. If a Cloud search gets rejected by the KNN safety limit, check for a metric mismatch before anything else.

## Fix

Build the index and query with the same metric: l2, cosine, or dot (hamming is IVF_FLAT only). If you omit the metric, current SDKs inherit the index metric, but on older SDK versions set it explicitly to match. If a Cloud search gets rejected by the KNN safety limit, check for a metric mismatch before anything else.

Context: Official docs (vector search): documents the gotcha that a LanceDB vector search must use the same distance metric the index was built with. Request a different metric and LanceDB cannot use the index, falling back to an exhaustive brute-force search. On LanceDB Cloud the brute-force KNN safety limit can reject that search outright on a large table. Older SDKs also sent l2 when the metric was omitted, silently mismatching non-l2 indexes.

## Matched source
Source: Published skill
Original query: "LanceDB search metric must match the index metric or the index is skipped"
Key terms: index, lancedb, match, metric, must, search, skipped

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_Qc5G7HFFhaG8Ao3uq5qLrQ). Version: `skv_K0lcfXPCL5MU_zli-vmPyg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
