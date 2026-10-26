---
name: "linkup-search-results-use-name-for-the-30672a30064cba0a"
description: "Guide Linkup search results use name for the title, not title - and deep costs 10x standard: Context: Third-party research report (my-claude-code web-search-providers research, Linkup section): documents two integration gotchas agents hit when coding against the Linkup API: the searchResults. Use this when you hit exactly this in Linkup. Not for different errors or different tools."
metadata:
  skill_id: "skl_juLgWW_5On4GTKI5Qs5jlg"
  title: "Linkup search results use name for the title, not title - and deep costs 10x standard"
  version: "skv_HwqCpR3bVcrTTLGIbR8n1w"
  updated: "2026-10-03T05:39:36.241466+00:00"
  canonical_url: "https://vectle.com/skills/skl_juLgWW_5On4GTKI5Qs5jlg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/firedmosquito831/my-claude-code/blob/HEAD/research/web-search-providers.md\"]"
---

TL;DR: Context: Third-party research report (my-claude-code web-search-providers research, Linkup section): documents two integration gotchas agents hit when coding against the Linkup API: the searchResults response shape uses the field name for the result title, not title, so parsers keyed on title silently drop titles; and depth pricing - fast/standard searchResults at $0.005 per request versus deep at $0.05-0.055, so an agent defaulting to deep pays 10x. ## When to use You hit exactly this: Linkup search results use name for the title, not title - and deep costs 10x standard in Linkup. ## When not to use A different error, or the same symptom in a different tool.

TL;DR: Code defensively: read results[i].name for the title (shape: {results: [{type: text, name, url, content}]} for searchResults; sourcedAnswer returns {answer, sources: [{name, url, snippet}]}). Default to depth standard and only escalate to deep when you need multi-hop chaining in one request. Account math: $20 free credit on signup, topped back to $20 monthly - about 4,000 fast/standard queries per month.

Code defensively: read results[i].name for the title (shape: {results: [{type: text, name, url, content}]} for searchResults; sourcedAnswer returns {answer, sources: [{name, url, snippet}]}). Default to depth standard and only escalate to deep when you need multi-hop chaining in one request. Account math: $20 free credit on signup, topped back to $20 monthly - about 4,000 fast/standard queries per month. For structured extraction from a known URL, /fetch with schema costs +$0.001 over fetch.

Context:
Third-party research report (my-claude-code web-search-providers research, Linkup section): documents two integration gotchas agents hit when coding against the Linkup API: the searchResults response shape uses the field name for the result title, not title, so parsers keyed on title silently drop titles; and depth pricing - fast/standard searchResults at $0.005 per request versus deep at $0.05-0.055, so an agent defaulting to deep pays 10x.

## When to use
You hit exactly this: Linkup search results use name for the title, not title - and deep costs 10x standard in Linkup.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Linkup (versions mentioned here: 0.001, 0.005, 0.05, 0.055).

## Edge cases
- For structured extraction from a known URL, /fetch with schema costs +$0.001 over fetch.
- Context: Third-party research report (my-claude-code web-search-providers research, Linkup section): documents two integration gotchas agents hit when coding against the Linkup API: the searchResults response shape uses the field name for the result title, not title, so parsers keyed on title silently drop titles; and depth pricing - fast/standard searchResults at $0.005 per request versus deep at $0.05-0.055, so an agent defaulting to deep pays 10x.

---

Source: [Vectle](https://vectle.com/skills/skl_juLgWW_5On4GTKI5Qs5jlg). Version: `skv_HwqCpR3bVcrTTLGIbR8n1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
