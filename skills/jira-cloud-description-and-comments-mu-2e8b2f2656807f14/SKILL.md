---
name: "jira-cloud-description-and-comments-mu-2e8b2f2656807f14"
description: "Wrap your text builder so every write path produces ADF. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_sKaWTRYKvabpdq9D3CFkig"
  title: "Jira Cloud: description and comments must be Atlassian Document Format"
  version: "skv_QhFVMsHaZvezhBKINTQlog"
  updated: "2026-10-03T05:01:57.938362+00:00"
  canonical_url: "https://vectle.com/skills/skl_sKaWTRYKvabpdq9D3CFkig"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/anthropics/claude-tag-plugins/blob/HEAD/jira/skills/jira-api/SKILL.md\"]"
---

## TL;DR

Wrap your text builder so every write path produces ADF. Sending a plain string returns 400. The minimal shape wraps text in a doc with a paragraph node.

## Fix

When you create Jira Cloud issues or comments via the API, build the description as an ADF document: type doc, version 1, content with a paragraph node holding text nodes. Plain strings and Markdown get a 400. Wrap your text builder so every write path produces ADF.

Context: Jira API skill (anthropics/claude-tag-plugins): body text fields like description and comment bodies are Atlassian Document Format, a JSON tree, not plain text or Markdown. Sending a plain string returns 400. The minimal shape wraps text in a doc with a paragraph node.

## Matched source
Source: Published skill
Original query: "Jira Cloud: description and comments must be Atlassian Document Format"
Key terms: atlassian, cloud, comments, description, document, format, jira, must

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_sKaWTRYKvabpdq9D3CFkig). Version: `skv_QhFVMsHaZvezhBKINTQlog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
