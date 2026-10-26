---
name: "no-data-is-returned-after-crawling-for-27ef989662536882"
description: "Firecrawl: no Data is Returned After Crawling (formats-JSON). The verified fix is Contributor ftonato investigated with the reporter's real URLs and prompts: no API bug. Use this when you hit the symptoms above in firecrawl; not for unrelated firecrawl errors or general setup questions."
metadata:
  skill_id: "skl_bjkRU0-LGxXFMBSrTXbG9A"
  title: "No Data is Returned After Crawling (formats-JSON)"
  version: "skv_LrNIR4kz1hRef6XR34RtYA"
  updated: "2026-10-03T05:04:23.337615+00:00"
  canonical_url: "https://vectle.com/skills/skl_bjkRU0-LGxXFMBSrTXbG9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/firecrawl/firecrawl/issues/1309\"]"
---

## TL;DR

Contributor ftonato investigated with the reporter's real URLs and prompts: no API bug. The key factor was the reporter's maxDepth: 1 configuration differing from working setups, plus overly long/detailed extraction prompts confusing the LLM - break big extractions into smaller focused prompts.

## The error

```text
Crawl status shows 'completed' but returns an empty data array with formats ['json'] + jsonOptions prompt, where the same code worked the day before.
```

## Fix

1. Contributor ftonato investigated with the reporter's real URLs and prompts: no API bug.
2. The key factor was the reporter's maxDepth: 1 configuration differing from working setups, plus overly long/detailed extraction prompts confusing the LLM - break big extractions into smaller focused prompts.
3. Lesson: empty structured-extraction results are usually a config/prompt problem (check maxDepth and prompt size), not an outage.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in firecrawl.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in firecrawl, even a similar-looking one.
- General firecrawl setup or credential questions.

## Compatibility

- Firecrawl (firecrawl/firecrawl)

## Variant phrasings

- How to fix "no Data is Returned After Crawling (formats-JSON)" in firecrawl
- firecrawl: no Data is Returned After Crawling (formats-JSON)

## Source

- https://github.com/firecrawl/firecrawl/issues/1309

---

Source: [Vectle](https://vectle.com/skills/skl_bjkRU0-LGxXFMBSrTXbG9A). Version: `skv_LrNIR4kz1hRef6XR34RtYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
