---
name: "multiple-shebang-lines-in-smithery-ind-410704538d469bdb"
description: "Exa MCP Server: multiple shebang lines in .smithery/index.cjs breaks stdio transport. The verified fix is Fix: Collaborator theishangoswami: the broken npm build was fixed; exa-mcp-server@3.0.5 works. Use this when you hit the symptoms above in exa-mcp-server; not for unrelated exa-mcp-server errors or general setup questions."
metadata:
  skill_id: "skl_QsXqv5ckimO5nuvZxNKeEQ"
  title: "Multiple shebang lines in .smithery/index.cjs breaks stdio transport"
  version: "skv_BYgAoN_0f3x6i3vEsvqa5Q"
  updated: "2026-10-03T05:10:11.106307+00:00"
  canonical_url: "https://vectle.com/skills/skl_QsXqv5ckimO5nuvZxNKeEQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/exa-labs/exa-mcp-server/issues/65\"]"
---

## TL;DR

Fix: Collaborator theishangoswami: the broken npm build was fixed; exa-mcp-server@3.0.5 works. Community workaround before the fix: pin to 2.0.9, or switch to the remote MCP (mcp-remote https://mcp.exa.ai/mcp). Lesson: a SyntaxError on the shebang line of a published MCP package means a bad build - pin a known-good version or use the remote server.

## The error

```text
The npm package exa-mcp-server fails to start via stdio with 'SyntaxError: Invalid or unexpected token' pointing at a second '#!/usr/bin/env node' shebang line inside .smithery/index.cjs.
```

## Fix

1. Collaborator theishangoswami: the broken npm build was fixed; exa-mcp-server@3.0.5 works.
2. Community workaround before the fix: pin to 2.0.9, or switch to the remote MCP (mcp-remote https://mcp.exa.ai/mcp).
3. Lesson: a SyntaxError on the shebang line of a published MCP package means a bad build - pin a known-good version or use the remote server.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in exa-mcp-server.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in exa-mcp-server, even a similar-looking one.
- General exa-mcp-server setup or credential questions.

## Compatibility

- Exa MCP Server (exa-labs/exa-mcp-server)

## Variant phrasings

- How to fix "multiple shebang lines in .smithery/index.cjs breaks stdio transport" in exa-mcp-server
- exa-mcp-server: multiple shebang lines in .smithery/index.cjs breaks stdio transport

## Source

- https://github.com/exa-labs/exa-mcp-server/issues/65

---

Source: [Vectle](https://vectle.com/skills/skl_QsXqv5ckimO5nuvZxNKeEQ). Version: `skv_BYgAoN_0f3x6i3vEsvqa5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
