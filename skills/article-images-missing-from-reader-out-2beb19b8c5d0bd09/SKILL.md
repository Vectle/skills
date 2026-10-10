---
name: "article-images-missing-from-reader-out-2beb19b8c5d0bd09"
description: "Use X-With-Images-Summary when you want captions generated for the images that do come through. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_biX0SO6JDwDbhiUfi1f9mA"
  title: "Article images missing from Reader output - srcset and Readability stripping"
  version: "skv_Tt6cRCoPE8GOeGYxs1Z1xQ"
  updated: "2026-10-03T05:06:45.75975+00:00"
  canonical_url: "https://vectle.com/skills/skl_biX0SO6JDwDbhiUfi1f9mA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use X-With-Images-Summary when you want captions generated for the images that do come through. A maintainer found the cause: those img elements only carry a srcset attribute with no src, which the Reader ignored until it was patched. A second cause: the Readability library used for cleanup intentionally strips the image block on some pages.

## The error, verbatim

```text
If images are missing from Reader output, two things may be at play. First, images defined only via srcset on picture tags were skipped - that is fixed server-side, so retry. Second, if the image still does not show, the Readability cleanup is removing the block. Request the markdown return format instead of the default, which tells the Reader not to run Readability, and the image survives. Use X-With-Images-Summary when you want captions generated for the images that do come through.
```

## Fix

If images are missing from Reader output, two things may be at play. First, images defined only via srcset on picture tags were skipped - that is fixed server-side, so retry. Second, if the image still does not show, the Readability cleanup is removing the block. Request the markdown return format instead of the default, which tells the Reader not to run Readability, and the image survives. Use X-With-Images-Summary when you want captions generated for the images that do come through.

Context: Issue jina-ai/reader#149 (closed, 7 comments): article main images were missing from Reader output on pages that use the picture tag. A maintainer found the cause: those img elements only carry a srcset attribute with no src, which the Reader ignored until it was patched. A second cause: the Readability library used for cleanup intentionally strips the image block on some pages.

## Matched source
Source: Published skill
Original query: "Article images missing from Reader output - srcset and Readability stripping"
Key terms: article, images, missing, output, readability, reader, srcset, stripping

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_biX0SO6JDwDbhiUfi1f9mA). Version: `skv_Tt6cRCoPE8GOeGYxs1Z1xQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
