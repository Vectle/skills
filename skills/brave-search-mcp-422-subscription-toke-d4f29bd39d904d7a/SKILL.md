---
name: "brave-search-mcp-422-subscription-toke-d4f29bd39d904d7a"
description: "Fixes the Brave Search MCP server failing every query with a 422 subscription token error. Use when searches return 422 SUBSCRIPTION_TOKEN_INVALID, which means the BRAVE_API_KEY is missing, wrong, or not reaching the server. Not for wrong package name errors or MCP transport failures."
metadata:
  skill_id: "skl_mk62vX_6cnx87yWCq-QgPA"
  title: "Brave Search MCP: 422 SUBSCRIPTION_TOKEN_INVALID"
  version: "skv_Zcy_k81gSB1tqdXKLbFqAw"
  updated: "2026-10-03T04:32:30.146229+00:00"
  canonical_url: "https://vectle.com/skills/skl_mk62vX_6cnx87yWCq-QgPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Brave Search MCP `422 SUBSCRIPTION_TOKEN_INVALID`

## TL;DR
Your Brave API key is missing, wrong, or not reaching the server. Put `BRAVE_API_KEY` in the `env` block of the MCP config (not in HTTP headers), verify the key is valid in the Brave dashboard, and restart. The 422 is Brave's way of saying the subscription token is invalid.

The exact error:

```text
422 SUBSCRIPTION_TOKEN_INVALID
```

## Steps

### 1. Confirm the key is actually set in env
Open your MCP config and check the entry looks like this:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server"],
      "env": { "BRAVE_API_KEY": "[your Brave API key]" }
    }
  }
}
```

Success check: the key sits under `env`, not in `headers`, not in `args`. Keys in headers or args never reach the server process.

### 2. Verify the key itself
Log in to the Brave Search API dashboard and check:

- the key exists and is not expired
- the key has no leading or trailing spaces when pasted
- you have not exceeded the free monthly credits (the Search plan includes $5 in free credits)

Success check: a test search from the dashboard works with the same key.

### 3. Restart and retest
Fully quit the client (Claude Desktop needs all processes ended, not just the window closed) and reopen it. Ask it to run a brave search.

Success check: results come back instead of the 422.

## When this applies
- Every brave_search call fails with `422 SUBSCRIPTION_TOKEN_INVALID`.
- You recently registered, reinstalled, or moved the config between clients.

## When it does not apply
- The server fails to start with "package not found" or a module error. That is the wrong package name problem: it must be `@brave/brave-search-mcp-server`.
- The server starts but Codex says it is "not logged in". Do not try to log in; Brave MCP takes an API key, not OAuth. Use `--brave-api-key` or the env var.

## Tool compatibility
- @brave/brave-search-mcp-server npm package
- Claude Desktop, Claude Code, Cursor, Codex
- Node.js 18+

## Why it happens
The server sends your key to Brave's API as the `X-Subscription-Token` header. When the key is absent or wrong, Brave answers 422 SUBSCRIPTION_TOKEN_INVALID, which the server surfaces verbatim. The most common cause is putting the key somewhere the server never reads: HTTP headers in a remote config, a quoted empty string, or an `env` block that a registry UI silently dropped.

## Edge cases
- Registry UIs (SlashMCP and similar) sometimes preprocess configs; if the key looks right but the 422 persists, re-register the server from scratch with the corrected package name and key.
- Smithery-installed servers can overwrite your manual config; check the config file after any reinstall.
- A key that worked yesterday and 422s today usually means it expired or hit the credit cap; regenerate it in the dashboard.

---

Source: [Vectle](https://vectle.com/skills/skl_mk62vX_6cnx87yWCq-QgPA). Version: `skv_Zcy_k81gSB1tqdXKLbFqAw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
