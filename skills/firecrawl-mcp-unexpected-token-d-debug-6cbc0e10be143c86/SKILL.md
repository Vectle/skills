---
name: "firecrawl-mcp-unexpected-token-d-debug-6cbc0e10be143c86"
description: "Fixes the firecrawl MCP server failing in Claude Desktop with a JSON parse error caused by debug log lines on stdout. Use when the server shows connected but immediately errors with Unexpected token 'D' and a [DEBUG] prefix. Not for missing API keys or fetch tool errors."
metadata:
  skill_id: "skl_q1Wggk_kXSZRinsVus8xtQ"
  title: "firecrawl-mcp: Unexpected token 'D', \"[DEBUG] 202\"... is not valid JSON"
  version: "skv_elXQMcR8E5FgsIro6g3A3A"
  updated: "2026-10-03T04:28:06.110494+00:00"
  canonical_url: "https://vectle.com/skills/skl_q1Wggk_kXSZRinsVus8xtQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Firecrawl MCP `Unexpected token 'D', "[DEBUG] 202"... is not valid JSON`

## TL;DR
Stop the server from writing log lines to stdout: switch its logging to stderr or turn debug logging off. The `[DEBUG]` lines pollute the same pipe the MCP protocol uses, so the client chokes trying to parse a log line as JSON.

The exact error in the Claude Desktop log:

```text
[error] Unexpected token 'D', "[DEBUG] 202"... is not valid JSON
```

## Steps

### 1. Confirm stdout pollution in the logs
Open the Claude Desktop MCP log for firecrawl and look for log lines interleaved with protocol messages, like:

```text
[mcp-server-firecrawl] [info] Server started and connected successfully
[mcp-server-firecrawl] [error] Unexpected token 'D', "[DEBUG] 202"... is not valid JSON
```

Success check: the error mentions `[DEBUG]` and the quoted fragment starts with `[DEBUG] 202` (a timestamp). That confirms log output, not protocol output.

### 2. Redirect logging to stderr or disable debug logging
In your `claude_desktop_config.json`, set the server's log level so debug output does not go to stdout:

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "[your Firecrawl API key]",
        "LOG_LEVEL": "error"
      }
    }
  }
}
```

Success check: no more `[DEBUG]` lines in the log after a restart.

### 3. Restart and verify the handshake
Fully quit Claude Desktop (kill leftover processes) and reopen it. Check the log for:

```text
[mcp-server-firecrawl] [info] Server started and connected successfully
```

with no `[error] Unexpected token` after it. Success check: `firecrawl_scrape` and `firecrawl_search` appear in the tool list.

## When this applies
- The firecrawl MCP server starts (you see the "connected successfully" line) but immediately errors with `Unexpected token 'D'` quoting a `[DEBUG]` fragment.
- Affects Claude Desktop and any stdio client; the JSON-RPC transport requires stdout to carry only protocol messages.

## When it does not apply
- You see `FIRECRAWL_API_KEY` missing or 401 errors. That is an auth problem; set the key in `env`.
- The scrape/search tools run but return bad data. That is an API-side issue, not the transport.

## Tool compatibility
- firecrawl-mcp npm package
- Claude Desktop (any recent version), also Cursor and other stdio MCP clients
- Node.js 18+

## Why it happens
MCP over stdio uses stdout as the JSON-RPC message channel. Any server process that prints logs to stdout breaks the framing: the client reads a log line, calls JSON.parse on it, and dies with `Unexpected token`. Debug-level logging is the usual culprit because it is the noisiest and includes timestamps, which is why the error quotes `[DEBUG] 202...`.

## Edge cases
- `dotenv` banner lines (`[dotenv@...]`) cause the sibling error `Unexpected token 'd'`; the same fix (keep stdout clean) applies.
- If the env var for the log level is ignored by your package version, wrap the command in a small script that redirects stdout: run the server with its stdout filtered so only lines starting with `{` pass through.
- On Windows, leftover `Claude.exe` processes hold the old config; use Task Manager to end them all before retesting.

---

Source: [Vectle](https://vectle.com/skills/skl_q1Wggk_kXSZRinsVus8xtQ). Version: `skv_elXQMcR8E5FgsIro6g3A3A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
