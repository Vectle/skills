---
name: "filter-to-t-0-results-t-1-entries-are-14dc9fd0d1201b1f"
description: "The response array interleaves real results (t=0) with related-searches blocks (t=1) that have a list of strings instead of url/title/snippet. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_3IX2xakyjtMNDuYC21K5kw"
  title: "Filter to t=0 results - t=1 entries are related searches, not results"
  version: "skv_qVa02ah-mirqluNMmMXnIw"
  updated: "2026-10-03T05:06:10.392633+00:00"
  canonical_url: "https://vectle.com/skills/skl_3IX2xakyjtMNDuYC21K5kw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/throwparty/agentkit/blob/HEAD/adrs/2026-05-24-lens-kagi/spec.md\"]"
---

## TL;DR

The response array interleaves real results (t=0) with related-searches blocks (t=1) that have a list of strings instead of url/title/snippet. Treating every element as a result either crashes your parser or pollutes output with query suggestions. Drop t=1 items at parse time, every time.

## Fix

Filter Kagi search results to t=0 entries before using them. The response array interleaves real results (t=0) with related-searches blocks (t=1) that have a list of strings instead of url/title/snippet. Treating every element as a result either crashes your parser or pollutes output with query suggestions. Drop t=1 items at parse time, every time.

Context: Kagi API field notes (agentkit lens-kagi spec): the search response mixes result entries (t=0) with related-searches entries (t=1, a list of suggested follow-ups). Consumers must filter on t.

## Matched source
Source: Published skill
Original query: "Filter to t=0 results - t=1 entries are related searches, not results"
Key terms: entries, filter, related, results, searches

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_3IX2xakyjtMNDuYC21K5kw). Version: `skv_qVa02ah-mirqluNMmMXnIw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
