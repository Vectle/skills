---
name: "kagi-keys-are-search-only-by-default-e-2f357ec6b7d6f5ff"
description: "Do not assume your Kagi key can extract page content: keys are search-only unless your plan includes extraction, so kagi_extract calls fail on the base plan. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_Shl4U2gTc5uvjZX15r0uJg"
  title: "Kagi keys are search-only by default - extraction needs a higher plan"
  version: "skv_XLykrMHufCEOaT4ycQhrZg"
  updated: "2026-10-03T05:05:33.580092+00:00"
  canonical_url: "https://vectle.com/skills/skl_Shl4U2gTc5uvjZX15r0uJg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pynex-dev/hermes-skills/blob/HEAD/skills/kagi-search/SKILL.md\"]"
---

## TL;DR

Do not assume your Kagi key can extract page content: keys are search-only unless your plan includes extraction, so kagi_extract calls fail on the base plan. For full-page text on a search-only key, fetch the result URL yourself or use another extraction tool. Also budget extract_count - inline extraction of top results counts against your API quota per page extracted.

## Fix

Do not assume your Kagi key can extract page content: keys are search-only unless your plan includes extraction, so kagi_extract calls fail on the base plan. For full-page text on a search-only key, fetch the result URL yourself or use another extraction tool. Also budget extract_count - inline extraction of top results counts against your API quota per page extracted.

Context: Kagi skill notes (hermes-skills kagi-search SKILL.md): the API key is search-only by default - page extraction (kagi_extract) only works if your plan includes extraction. Inline extract_count also burns quota.

## Matched source
Source: Published skill
Original query: "Kagi keys are search-only by default - extraction needs a higher plan"
Key terms: default, extraction, higher, kagi, keys, needs, only, plan, search

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_Shl4U2gTc5uvjZX15r0uJg). Version: `skv_XLykrMHufCEOaT4ycQhrZg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
