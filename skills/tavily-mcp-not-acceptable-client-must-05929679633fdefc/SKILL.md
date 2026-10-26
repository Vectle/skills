---
name: "tavily-mcp-not-acceptable-client-must-05929679633fdefc"
description: "Fixes Tavily MCP authentication failures when using an HTTP client config, where every tool call returns an auth error. Use when the remote Tavily MCP endpoint rejects requests with an Accept-header or authentication error. Not for stdio npx installs that fail to start or for invalid API keys."
metadata:
  skill_id: "skl_PxhX435xsgk85uce8iddMA"
  title: "Tavily MCP: Not Acceptable, client must accept application/json and text/event-stream"
  version: "skv_ALj3eCKLcLg-qfonxO4s2A"
  updated: "2026-10-03T04:27:28.872522+00:00"
  canonical_url: "https://vectle.com/skills/skl_PxhX435xsgk85uce8iddMA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tavily-ai/tavily-mcp/issues/121\"]"
---

# Fix Tavily MCP `Not Acceptable: Client must accept both application/json and text/event-stream`

## TL;DR
Switch from the `type: http` config to the stdio config (`npx -y tavily-mcp@latest` with your key in `env`). The hosted Tavily MCP endpoint requires an `Accept: application/json, text/event-stream` header that Claude Code's HTTP client does not send, so every call fails with what looks like an authentication error.

What the failure looks like:

```json
{"error":"Search failed","detail":"Authentication required"}
```

and at the raw HTTP level:

```text
Not Acceptable: Client must accept both application/json and text/event-stream
```

## Steps

### 1. Confirm the header is the problem
Run a raw request without the special Accept header:

```bash
curl -X POST "https://mcp.tavily.com/mcp/?tavilyApiKey [your value] Tavily API key]" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

Success check: you get the `Not Acceptable` response, which proves the header (not your key) is the issue. With the right header it works:

```bash
curl -X POST "https://mcp.tavily.com/mcp/?tavilyApiKey [your value] Tavily API key]" \
  -H "Accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

### 2. Replace the HTTP config with stdio
In your MCP config, drop the `type: http` entry and use:

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": { "TAVILY_API_KEY": "[your Tavily API key]" }
    }
  }
}
```

Success check: restart the client; `tavily-search` and `tavily-extract` appear and searches return results.

### 3. Validate the key separately if it still fails
If the stdio route also fails, verify the key itself:

```bash
curl -s "https://api.tavily.com/search" -H "Content-Type: application/json" \
  -d '{"api_key":"[your Tavily API key]","query":"test","max_results":1}' | head -c 300
```

Success check: valid JSON with results means the key is fine and the problem is the transport.

## When this applies
- You configured Tavily with `"type": "http"` and `"url": "https://mcp.tavily.com/mcp/?tavilyApiKey [your value] and every tool call returns an authentication error.
- Raw curl shows the `Not Acceptable` message about `text/event-stream`.

## When it does not apply
- The stdio `npx tavily-mcp` server fails to start at all (check Node and npx first).
- The key is actually invalid or missing; the API check in step 3 returns a 401. Regenerate the key instead.

## Tool compatibility
- tavily-mcp npm package (latest)
- Tavily hosted MCP at mcp.tavily.com
- Claude Code (the `type: http` client is the one affected), also relevant to any client that cannot set custom Accept headers

## Why it happens
The Tavily MCP server streams responses over SSE, so it requires clients to send `Accept: application/json, text/event-stream`. Claude Code's `type: http` client sends a default Accept header without the SSE part, the server rejects the request as Not Acceptable, and the client surfaces that as an authentication failure, which sends you chasing the API key instead of the header.

## Edge cases
- Do not paste the key with quotes or trailing spaces in the URL parameter; the `type: http` setup passes it verbatim in the query string.
- If you need the remote endpoint (no local node), use `mcp-remote` with the URL as an npx stdio wrapper instead of `type: http`.
- API rate limits on the free tier return HTTP 429, not auth errors; treat those as usage limits, not this problem.

---

Source: [Vectle](https://vectle.com/skills/skl_PxhX435xsgk85uce8iddMA). Version: `skv_ALj3eCKLcLg-qfonxO4s2A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
