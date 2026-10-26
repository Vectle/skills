---
name: "mpx-cli-picks-the-conversion-from-your-1e3092d3b54ce935"
description: "Run set-api-key once to store your key in the local config; every convert after that just works. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_qDd-OwnAUK0cSlMEW0rPVw"
  title: "mpx CLI picks the conversion from your output file extension"
  version: "skv_eQbSaMFsVfFcGOMtw-Cw9w"
  updated: "2026-10-03T04:35:48.914091+00:00"
  canonical_url: "https://vectle.com/skills/skl_qDd-OwnAUK0cSlMEW0rPVw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/Mathpix/mpx-cli/blob/master/README.md\"]"
---

## TL;DR

Run set-api-key once to store your key in the local config; every convert after that just works. It also compiles Mathpix Markdown without OCR (input.mmd to output.docx) and can serve a directory of mmd files as rendered HTML. API key is stored via set-api-key in the user config file.

## Fix

With the mpx CLI you never name a format flag - the output extension decides: .mmd, .docx, .tex, .html, or .pdf. Hand it an .mmd file and it compiles straight to docx or PDF with no OCR pass, which is handy for re-rendering. Run set-api-key once to store your key in the local config; every convert after that just works.

Context: Mathpix mpx-cli README: the convert command infers the conversion from the output file extension - mpx convert input.pdf output.mmd, .docx, .tex, or .html. It also compiles Mathpix Markdown without OCR (input.mmd to output.docx) and can serve a directory of mmd files as rendered HTML. API key is stored via set-api-key in the user config file.

## Matched source
Source: Published skill
Original query: "mpx CLI picks the conversion from your output file extension"
Key terms: conversion, extension, file, output, picks, your

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_qDd-OwnAUK0cSlMEW0rPVw). Version: `skv_eQbSaMFsVfFcGOMtw-Cw9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
