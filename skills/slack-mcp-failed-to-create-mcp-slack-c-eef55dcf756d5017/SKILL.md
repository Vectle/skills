---
name: "slack-mcp-failed-to-create-mcp-slack-c-eef55dcf756d5017"
description: "Fixes the korotovsky Slack MCP server failing to start with an invalid_auth error from Slack's API. Use when the log shows Failed to create MCP Slack client with error invalid_auth. Not for token-type routing errors or for channels the bot was never invited to."
metadata:
  skill_id: "skl_4BoC792y8ryavZ7tlcse_A"
  title: "Slack MCP: Failed to create MCP Slack client, error invalid_auth"
  version: "skv_oD57_T0Fa0j4JI_YhiD40g"
  updated: "2026-10-03T04:37:07.572427+00:00"
  canonical_url: "https://vectle.com/skills/skl_4BoC792y8ryavZ7tlcse_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/korotovsky/slack-mcp-server/issues/105\"]"
---

# Fix Slack MCP `Failed to create MCP Slack client: invalid_auth`

## TL;DR
Your Slack tokens are stale or mismatched. Re-copy fresh token values from your active browser session, set the user agent to match that browser, and enable custom TLS. The server validates the token at startup, so a dead token kills it before any tool runs.

The exact error in the log:

```text
"message":"Failed to create MCP Slack client","app":"slack-mcp-server","error":"invalid_auth"
```

## Steps

### 1. Confirm the token type you configured
Check which auth method your config uses: `xoxb` (bot token), `xoxp` (user OAuth token), or `xoxc`/`xoxd` (browser session tokens). Each has its own env var (`SLACK_MCP_XOXB_TOKEN`, `SLACK_MCP_XOXP_TOKEN`, or the xoxc/xoxd pair).

Success check: you know which variable the server is reading.

### 2. Refresh the token values
- For `xoxc`/`xoxd`: open Slack in your browser, open devtools, and copy fresh `xoxc` and `xoxd` cookie values. These rotate; running some tools invalidates the session, which is why a setup that worked yesterday dies today.
- For `xoxb`/`xoxp`: regenerate or re-copy the token from your Slack app config; check it was not revoked or rotated.

Success check: the values in your config are the current ones, with no truncation.

### 3. Match the user agent and enable custom TLS
Set `SLACK_MCP_USER_AGENT` to the user agent string of the browser you copied the tokens from (find it at a what-is-my-user-agent page), and set `SLACK_MCP_CUSTOM_TLS` to `1` or `true`.

```json
{
  "mcpServers": {
    "slack": {
      "command": "slack-mcp-server",
      "env": {
        "SLACK_MCP_XOXC_TOKEN": "[fresh xoxc value]",
        "SLACK_MCP_XOXD_TOKEN": "[fresh xoxd value]",
        "SLACK_MCP_USER_AGENT": "[your browser user agent]",
        "SLACK_MCP_CUSTOM_TLS": "1"
      }
    }
  }
}
```

Success check: the server log shows successful authentication instead of `invalid_auth`.

### 4. Restart the client and test
Restart the MCP client and call `channels_list`.

Success check: channel list returns; no `invalid_auth` in the log.

## When this applies
- The slack-mcp-server log shows `Failed to create MCP Slack client` with `error: invalid_auth` at startup.
- It worked before and broke after you used Slack in the browser (session tokens rotated).

## When it does not apply
- Tools run but return `not_allowed_token_type` or empty results for unreads. That is token-type routing (xoxb vs xoxp vs xoxc capabilities), not a dead token.
- `channels_list` works but a specific channel is missing. The bot was never invited to that channel; invite it.

## Tool compatibility
- korotovsky/slack-mcp-server (Go binary, npm wrapper, or DXT extension)
- Slack workspaces with xoxb, xoxp, or xoxc/xoxd auth
- Claude Desktop, Claude Code, Cursor, Cline

## Why it happens
`invalid_auth` is Slack's API saying the token is not valid right now. Browser-session tokens (xoxc/xoxd) are the fragile ones: Slack rotates them, and actions like running searches can invalidate the session the token was copied from. The server checks the token once at startup and refuses to run at all rather than failing per-call, so one stale value takes down every tool.

## Edge cases
- DXT installs have a known bug where an empty `xoxb_token` field is passed as the literal template string, which breaks auth when you meant xoxc/xoxd; update to a release with the workaround or clear the field properly.
- On very large workspaces the server can also time out during startup caching; if auth succeeds but the client drops the server, pre-warm the cache by running the binary once first.
- Enterprise Grid workspaces may need a custom user agent to match; the default one can be rejected.

---

Source: [Vectle](https://vectle.com/skills/skl_4BoC792y8ryavZ7tlcse_A). Version: `skv_oD57_T0Fa0j4JI_YhiD40g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
