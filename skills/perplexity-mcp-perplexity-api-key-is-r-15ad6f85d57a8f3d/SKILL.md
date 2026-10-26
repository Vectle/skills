---
name: "perplexity-mcp-perplexity-api-key-is-r-15ad6f85d57a8f3d"
description: "Fixes the Perplexity MCP server refusing to start with a missing-key error. Use when the server exits immediately with PERPLEXITY_API_KEY is required, which means the key never reached the server process. Not for 401 errors from Perplexity's API or for tool-call failures after a successful start."
metadata:
  skill_id: "skl_2cOfvch1WWj7tVsXaDmhyw"
  title: "Perplexity MCP: PERPLEXITY_API_KEY is required"
  version: "skv_82pCqVIKs2xM19Sx7pULvQ"
  updated: "2026-10-03T04:32:48.443113+00:00"
  canonical_url: "https://vectle.com/skills/skl_2cOfvch1WWj7tVsXaDmhyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/jschuller/perplexity-mcp\"]"
---

# Fix Perplexity MCP `PERPLEXITY_API_KEY is required`

## TL;DR
Put `PERPLEXITY_API_KEY` in the `env` block of your MCP config. The server reads it from its own process environment, and clients do not inherit your shell's exports, so a key that works in your terminal is invisible to the server until you declare it there.

The exact error:

```text
PERPLEXITY_API_KEY is required
```

## Steps

### 1. Add the key to the MCP config
Edit your MCP config (`claude_desktop_config.json` for Claude Desktop) so the entry looks like this:

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@jschuller/perplexity-mcp"],
      "env": { "PERPLEXITY_API_KEY": "[your Perplexity API key]" }
    }
  }
}
```

Success check: the JSON is valid (run it through a JSON linter if unsure) and the key has no surrounding spaces or quotes.

### 2. Check the key format
Perplexity API keys start with `pplx-`. If yours does not, you probably copied the wrong token (for example a browser session value).

Success check: the key starts with `pplx-`.

### 3. Restart the client completely
Quit the client fully. On macOS, Claude Desktop keeps helper processes alive after the window closes; end them or the old config stays loaded.

Success check: the perplexity tools (`search_web`, `search_academic`, etc.) appear in the tool list and a test query returns an answer.

## When this applies
- The Perplexity MCP server fails to start and the log or client shows `PERPLEXITY_API_KEY is required`.
- You set the key in your shell or `.env` but never put it in the MCP client config.

## When it does not apply
- The server starts but calls fail with `401 Unauthorized`. That means the key reached the server but Perplexity rejected it: check for extra spaces, an expired key, or a key from the wrong account.
- You get `400 invalid_request_error` on tool calls. Update the package to v2.1.0 or newer; older versions ship a schema Claude Code rejects.
- `No module named 'fastmcp'` on a Python-based variant. That is a missing dependency; reinstall requirements in the venv.

## Tool compatibility
- @jschuller/perplexity-mcp npm package (npx)
- Python-based Perplexity MCP variants that read PERPLEXITY_API_KEY from the environment
- Claude Desktop, Claude Code, Cursor

## Why it happens
MCP servers spawn as child processes of the client. A child process only sees the environment the client gives it, which is the `env` block in the config. Keys exported in your shell profile, set in a project `.env`, or typed into a terminal never cross that boundary, so the server exits with the "is required" error even though the key "is set" from your point of view.

## Edge cases
- On Windows, some clients need the machine restarted (not just the app) before the new config is picked up.
- If you run the server via `uvx` or a custom script instead of npx, the same rule holds: the key must be in the environment of the spawned process.
- Storing the key in the config file is fine on a personal machine; on shared machines prefer a secrets manager that injects env vars for the client.

---

Source: [Vectle](https://vectle.com/skills/skl_2cOfvch1WWj7tVsXaDmhyw). Version: `skv_82pCqVIKs2xM19Sx7pULvQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
