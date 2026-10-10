---
name: "mcp-error-32603-failed-to-list-pull-re-7998ab8a411b335c"
description: "Fixes the GitHub MCP server failing every pull request or repo call with a 401 Bad credentials error. Use when the MCP GitHub server returns -32603 with a 401 from the GitHub API. Not for missing env vars, rate limits, or OAuth device flow issues."
metadata:
  skill_id: "skl_rfp_SzCDMthKG78KoJ-jJQ"
  title: "MCP error -32603: failed to list pull requests: GET https://api.github.com/repos/[owner]/[repo]/pulls: 401 (Bad"
  version: "skv_ta-TGczgCB_QgOjkeiW6SQ"
  updated: "2026-10-03T06:03:13.633059+00:00"
  canonical_url: "https://vectle.com/skills/skl_rfp_SzCDMthKG78KoJ-jJQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# MCP error -32603: failed to list pull requests: GET https://api.github.com/repos/[owner]/[repo]/pulls: 401 (Bad credentials)

**TL;DR:** Regenerate your GitHub personal access token and put the new value in the MCP config env block as GITHUB_PERSONAL_ACCESS_TOKEN. A 401 Bad credentials means the token itself is rejected: expired, revoked, or pasted with a typo. It is not a scope problem. Restart the MCP client after changing the token so the server picks up the new value.

## The error

```
MCP error -32603: failed to list pull requests: GET https://api.github.com/repos/[owner]/[repo]/pulls: 401 (Bad credentials)
```

## Fix it

1. Regenerate the token at GitHub Settings, Developer settings, Personal access tokens, and copy the new value immediately.
   Expected: GitHub shows the new token once; you have it on your clipboard.
2. In your MCP client config, set GITHUB_PERSONAL_ACCESS_TOKEN to the new token inside the server env block.
   Expected: The config file contains the new token value in the env section.
3. Restart the MCP client completely (Claude Desktop, Cursor, etc.) so the server process relaunches.
   Expected: The GitHub server appears in the tool list without the 401 on the next call.
4. Call a simple read tool like list pull requests again.
   Expected: The call returns data instead of MCP error -32603.

## When this applies

Every GitHub MCP tool call fails with -32603 and the underlying cause is a 401 Bad credentials from api.github.com. The token worked before and recently stopped, or it never worked.

## When this does NOT apply

If the error is a 403 (forbidden) or 404 on a specific repo, that is scopes or repo access, not credentials. If the env var is unset entirely, see the missing-token skill instead.

## Tool compatibility

GitHub MCP server (modelcontextprotocol/servers), recent versions

## Also seen as

- 401 Unauthorized from the GitHub API through the MCP server
- Bad credentials on every GitHub MCP tool call
- GitHub MCP server stopped working overnight with 401

## Why it happens

The MCP server sends your personal access token as a Bearer token on each API call. GitHub answers 401 Bad credentials when the token is expired, manually revoked, or malformed. The server wraps the API failure as MCP error -32603, which hides the real 401 one layer down.

## Edge cases

- Fine-grained PATs expire on the schedule you chose; classic PATs show as expired in the token list.
- If you use GitHub Enterprise Server, a token for github.com will 401 against your enterprise host; generate the token on the right host.
- A trailing newline pasted into the env value also 401s; paste into a plain text editor first to check.

---

Source: [Vectle](https://vectle.com/skills/skl_rfp_SzCDMthKG78KoJ-jJQ). Version: `skv_ta-TGczgCB_QgOjkeiW6SQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
