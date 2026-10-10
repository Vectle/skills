---
name: "document-splitter-always-returns-1-doc-d8e05abf5c4143e5"
description: "Haystack: document Splitter always returns 1 document for split_type=\"passage\" in pdfs. The verified fix is Fix: Contributor davidsbatista's fix: use PyPDFToDocument(extraction_mode=PyPDFExtractionMode.LAYOUT) - 'works perfectly!' - since layout mode preserves paragraph spacing. Use this when you hit the symptoms above in haystack; not for unrelated haystack errors or general setup questions."
metadata:
  skill_id: "skl_k0KZJjNmlqaJzRLe0qcvZA"
  title: "Document Splitter always returns 1 document for split_type=\"passage\" in pdfs"
  version: "skv_5JOplwCHHN33D2CaquNhrQ"
  updated: "2026-10-03T06:08:22.73614+00:00"
  canonical_url: "https://vectle.com/skills/skl_k0KZJjNmlqaJzRLe0qcvZA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Contributor davidsbatista's fix: use PyPDFToDocument(extraction_mode=PyPDFExtractionMode.LAYOUT) - 'works perfectly!' - since layout mode preserves paragraph spacing.

## The error

```text
Issue deepset-ai/haystack#8491 (closed, 22 comments): **Describe the bug** When using Document Splitter with pdf and `split_type="passage"`, the result is always one document. This is using pypdf. **Expected behavior** The understanding I have is that it splits based on at least two line breaks `\n\n` **Additional context** When I tested using plain text it seems to be splitting correctly **To Reproduce** dir = '...' files = [ {"filename": "rules.pdf", "meta": {"split_by" : "passage", "split_length":1, "split_overlap":0, "split_threshold":0}}, {"filename": "rules.txt", "meta": {"split_by" : "passage", "split_length":1, "split_overlap":0, "split_t
```

## Fix

1. Contributor davidsbatista's fix: use PyPDFToDocument(extraction_mode=PyPDFExtractionMode.LAYOUT) - 'works perfectly!' - since layout mode preserves paragraph spacing.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in haystack.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in haystack, even a similar-looking one.
- General haystack setup or credential questions.

## Compatibility

- Haystack (deepset-ai/haystack)

## Variant phrasings

- How to fix "document Splitter always returns 1 document for split_type="passage" in pdfs" in haystack
- haystack: document Splitter always returns 1 document for split_type="passage" in pdfs

## Root cause

Root cause identified by contributor lbux: PDF converters store paragraph breaks as single newlines, but split_by='passage' splits on double newlines (\n\n), so passage splitting yields one document.

## Source

- https://github.com/deepset-ai/haystack/issues/8491

---

Source: [Vectle](https://vectle.com/skills/skl_k0KZJjNmlqaJzRLe0qcvZA). Version: `skv_5JOplwCHHN33D2CaquNhrQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
