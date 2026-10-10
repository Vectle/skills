---
name: "getting-whole-page-images-instead-of-e-07fef362a0481d9a"
description: "Check the JSON image objects first; that is where the extracted figures and their descriptions are. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_zZ0L5fcKdGCUCsaZr4u3OA"
  title: "Getting whole-page images instead of embedded figures - use JSON mode"
  version: "skv_McqqLqBvYvCrrUiqYrS2mw"
  updated: "2026-10-03T04:42:51.551001+00:00"
  canonical_url: "https://vectle.com/skills/skl_zZ0L5fcKdGCUCsaZr4u3OA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check the JSON image objects first; that is where the extracted figures and their descriptions are. A working solution was posted in the thread and confirmed by another user.

## Fix

If LlamaParse gives you whole-page images instead of the embedded figures, do not fight the default markdown output - use JSON mode and dig into the image objects in the returned JSON, which is where the per-image results live. In markdown mode you can also get image descriptions by stating in the parsing instructions which images to describe. Check the JSON image objects first; that is where the extracted figures and their descriptions are.

Context: Issue run-llama/llama_cloud_services#317 (closed, 9 comments): a user calling get_json_result() wanted the individual embedded images from each PDF page, but kept getting one whole-page image per page instead. A working solution was posted in the thread and confirmed by another user.

## Matched source
Source: Published skill
Original query: "Getting whole-page images instead of embedded figures - use JSON mode"
Key terms: embedded, figures, getting, images, instead, json, mode, page, whole

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_zZ0L5fcKdGCUCsaZr4u3OA). Version: `skv_McqqLqBvYvCrrUiqYrS2mw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
