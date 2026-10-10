---
name: "gitlab-mcp-server-returns-401-unauthor-cee979f2230f8e55"
description: "Fixes the GitLab MCP server answering 401 on every call even though a token is configured. Use when the token is present but rejected. Not for 403s or permission refusals on single endpoints."
metadata:
  skill_id: "skl_a3rnjv8rhAbDtltDwcGtYA"
  title: "GitLab MCP server returns 401 Unauthorized with a personal access token"
  version: "skv_zDUsiBheM8Q89seS4xergA"
  updated: "2026-10-03T06:11:47.711726+00:00"
  canonical_url: "https://vectle.com/skills/skl_a3rnjv8rhAbDtltDwcGtYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# GitLab MCP server returns 401 Unauthorized with a personal access token

**TL;DR:** Check the token scope and expiry first: the MCP server needs api or read_api scope on a live token. A 401 means GitLab rejected the credential itself, not that you lack one permission. Regenerate the token with the right scopes and update MCP_PAT in the server env.

## The error

```
401 Unauthorized from the GitLab API on MCP tool calls (authentication failed: GitLab rejected the token (GITLAB_TOKEN) itself as invalid, expired, revoked or without the api or read_api scope)
```

## Fix it

1. In GitLab, open your personal access token list and check the token expiry and scopes.
   Expected: You find it expired, revoked, or missing api/read_api.
2. Create a new token with api scope (or read_api for read-only use).
   Expected: GitLab shows the new token once.
3. Set MCP_PAT to the new token in the MCP server env and restart the client.
   Expected: Tool calls succeed without 401.
4. Test with one simple call like listing projects.
   Expected: Results return normally.

## When this applies

Every GitLab MCP tool call returns 401 and the same token may also fail a direct curl to the GitLab API.

## When this does NOT apply

If the token works for some calls but 401s on specific ones (approve, merge), that is a permission refusal, not a bad token. See the permission-refusal skill.

## Tool compatibility

jmrplens/gitlab-mcp-server, recent versions

## Also seen as

- GitLab MCP 401 invalid token
- GITLAB_TOKEN rejected
- GitLab MCP authentication failed

## Why it happens

The server passes MCP_PAT as the API credential. GitLab answers 401 when that credential is expired, revoked, or lacks the api/read_api scope, and the server surfaces the refusal directly.

## Edge cases

- Group and project access tokens also expire; check the token type.
- Self-managed instances may disable personal access tokens entirely; use the instance setting.
- Rotating tokens on a schedule prevents surprise 401s.

---

Source: [Vectle](https://vectle.com/skills/skl_a3rnjv8rhAbDtltDwcGtYA). Version: `skv_zDUsiBheM8Q89seS4xergA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
