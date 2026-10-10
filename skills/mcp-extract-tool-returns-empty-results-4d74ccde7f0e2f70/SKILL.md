---
name: "mcp-extract-tool-returns-empty-results-4d74ccde7f0e2f70"
description: "Tavily MCP: MCP Extract tool returns empty results without extract_depth: \"advanced\". The verified fix is Workaround from the reporter: pass extract_depth:'advanced' when extraction returns empty. Use this when you hit the symptoms above in tavily-mcp; not for unrelated tavily-mcp errors or general setup questions."
metadata:
  skill_id: "skl_lSGCY5v7OB_upnqc0C3rrQ"
  title: "MCP Extract tool returns empty results without `extract_depth: \"advanced\"`"
  version: "skv_mJMPSh691RBrn3gD_V37NQ"
  updated: "2026-10-03T04:33:20.496421+00:00"
  canonical_url: "https://vectle.com/skills/skl_lSGCY5v7OB_upnqc0C3rrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Workaround from the reporter: pass extract_depth:'advanced' when extraction returns empty. Lesson for agents: retry an empty extract with extract_depth advanced before concluding the page has no content.

## The error

```text
The Tavily MCP extract tool returns empty results for some URLs with the default extraction depth, but works when extract_depth is set to 'advanced' - silently inconsistent behavior for AI assistants.
```

## Fix

1. Workaround from the reporter: pass extract_depth:'advanced' when extraction returns empty.
2. Lesson for agents: retry an empty extract with extract_depth advanced before concluding the page has no content.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in tavily-mcp.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in tavily-mcp, even a similar-looking one.
- General tavily-mcp setup or credential questions.

## Compatibility

- Tavily MCP (tavily-ai/tavily-mcp)

## Variant phrasings

- How to fix "MCP Extract tool returns empty results without extract_depth: "advanced"" in tavily-mcp
- tavily-mcp: MCP Extract tool returns empty results without extract_depth: "advanced"

## Source

- https://github.com/tavily-ai/tavily-mcp/issues/58

---

Source: [Vectle](https://vectle.com/skills/skl_lSGCY5v7OB_upnqc0C3rrQ). Version: `skv_mJMPSh691RBrn3gD_V37NQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
