---
name: "same-options-same-output-the-48h-docum-5302b2172d9539aa"
description: "If tweaking parsing_instruction or options changes nothing in the output, you are reading the cached result. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_bDi2JmFqVVXBr3lWYeOKSw"
  title: "Same options, same output? The 48h document cache is serving stale parses"
  version: "skv_uMnGAgad5ni9BYQ4Q83WPQ"
  updated: "2026-10-03T04:41:39.413112+00:00"
  canonical_url: "https://vectle.com/skills/skl_bDi2JmFqVVXBr3lWYeOKSw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/lizo-roadtown/tapestry/blob/HEAD/integrations/claude-code/tapestry-patterns/skills/document-parsing/SKILL.md\"]"
---

## TL;DR

If tweaking parsing_instruction or options changes nothing in the output, you are reading the cached result. LlamaParse caches by document hash for ~48h, so re-submitting the same file returns the old parse for free. Force a fresh parse with the invalidate-cache option when iterating on instructions.

## Fix

If tweaking parsing_instruction or options changes nothing in the output, you are reading the cached result. LlamaParse caches by document hash for ~48h, so re-submitting the same file returns the old parse for free. Force a fresh parse with the invalidate-cache option when iterating on instructions. Conversely, lean on the cache deliberately: re-running a pipeline over unchanged documents costs nothing.

Context: LlamaParse field notes (document-parsing SKILL.md): parse results are cached server-side for about 48 hours keyed by document hash, so re-parsing the same document is free - but it also means changed parsing options will not take effect on a re-parse unless you invalidate the cache.

## Matched source
Source: Published skill
Original query: "Same options, same output? The 48h document cache is serving stale parses"
Key terms: cache, document, options, output, parses, same, serving, stale

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_bDi2JmFqVVXBr3lWYeOKSw). Version: `skv_uMnGAgad5ni9BYQ4Q83WPQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
