---
name: "exa-api-returns-empty-results-array-de-d63f56b26282b098"
description: "Exa MCP Server: exa API Returns Empty Results Array Despite Successful Connection. The verified fix is Fix: Collaborator theishangoswami: 'there was an issue with our api, it is now fixed' - it was an Exa-side outage, not a client misconfiguration; reporters confirmed it started working with no changes. Use this when you hit the symptoms above in exa-mcp-server; not for unrelated exa-mcp-server errors or general setup questions."
metadata:
  skill_id: "skl_3EqlEqLwLhUIoVEfjDf0Nw"
  title: "Exa API Returns Empty Results Array Despite Successful Connection"
  version: "skv_QwkH4kg69jsyu-fJoy6wiw"
  updated: "2026-10-03T05:54:50.608132+00:00"
  canonical_url: "https://vectle.com/skills/skl_3EqlEqLwLhUIoVEfjDf0Nw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/exa-labs/exa-mcp-server/issues/34\"]"
---

## TL;DR

Fix: Collaborator theishangoswami: 'there was an issue with our api, it is now fixed' - it was an Exa-side outage, not a client misconfiguration; reporters confirmed it started working with no changes. Related lesson from the same thread: the npm package can lag the repo (0.3.10 on npm vs 2.0.0 in repo), so update the package before debugging.

## The error

```text
The Exa API returns empty results arrays for all queries despite successful HTTP responses (valid requestId, zero cost) through the MCP server on Claude Desktop and Claude Code.
```

## Fix

1. Collaborator theishangoswami: 'there was an issue with our api, it is now fixed' - it was an Exa-side outage, not a client misconfiguration; reporters confirmed it started working with no changes.
2. Related lesson from the same thread: the npm package can lag the repo (0.3.10 on npm vs 2.0.0 in repo), so update the package before debugging.

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

- How to fix "exa API Returns Empty Results Array Despite Successful Connection" in exa-mcp-server
- exa-mcp-server: exa API Returns Empty Results Array Despite Successful Connection

## Source

- https://github.com/exa-labs/exa-mcp-server/issues/34

---

Source: [Vectle](https://vectle.com/skills/skl_3EqlEqLwLhUIoVEfjDf0Nw). Version: `skv_QwkH4kg69jsyu-fJoy6wiw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
