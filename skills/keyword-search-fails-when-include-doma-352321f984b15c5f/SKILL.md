---
name: "keyword-search-fails-when-include-doma-352321f984b15c5f"
description: "Exa Py: keyword search fails when include_domains is specified.. The verified fix is Fix: Lesson: for type='keyword' searches, pass at most one domain in include_domains. Use this when you hit the symptoms above in exa-py; not for unrelated exa-py errors or general setup questions."
metadata:
  skill_id: "skl_IczmpBSRyeUgN5IyYNnOLA"
  title: "Keyword search fails when include_domains is specified."
  version: "skv_zQoSsljFuJ7SuP4hkS-zQw"
  updated: "2026-10-03T05:56:16.817382+00:00"
  canonical_url: "https://vectle.com/skills/skl_IczmpBSRyeUgN5IyYNnOLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Lesson: for type='keyword' searches, pass at most one domain in include_domains.

## The error

```text
Keyword search fails with 'Request failed with status code 500: An error occurred during the keyword search' when include_domains is specified; removing it succeeds.
```

## Fix

1. Lesson: for type='keyword' searches, pass at most one domain in include_domains.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in exa-py.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in exa-py, even a similar-looking one.
- General exa-py setup or credential questions.

## Compatibility

- Exa Py (exa-labs/exa-py)

## Variant phrasings

- How to fix "keyword search fails when include_domains is specified." in exa-py
- exa-py: keyword search fails when include_domains is specified.

## Source

- https://github.com/exa-labs/exa-py/issues/6

---

Source: [Vectle](https://vectle.com/skills/skl_IczmpBSRyeUgN5IyYNnOLA). Version: `skv_zQoSsljFuJ7SuP4hkS-zQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
