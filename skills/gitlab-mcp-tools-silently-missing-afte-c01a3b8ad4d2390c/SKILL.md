---
name: "gitlab-mcp-tools-silently-missing-afte-c01a3b8ad4d2390c"
description: "Fixes GitLab MCP tools disappearing from the tool list when the PAT has limited scopes. Use when the server starts fine but expected tools are absent. Not for 401s or server crashes."
metadata:
  skill_id: "skl_BHxqKOC9QwxeV1XFyi_58w"
  title: "GitLab MCP tools silently missing after setting a narrow PAT scope"
  version: "skv_9q4dDcTJM7tbCUCQSmnmMg"
  updated: "2026-10-03T06:12:54.215261+00:00"
  canonical_url: "https://vectle.com/skills/skl_BHxqKOC9QwxeV1XFyi_58w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# GitLab MCP tools silently missing after setting a narrow PAT scope

**TL;DR:** The server filters its tool list by your token scopes, so a narrow token quietly hides tools instead of erroring. Set GITLAB_MCP_IGNORE_SCOPES=true to advertise every tool, or widen the token scopes. Restart the client after the change so tools/list re-runs.

## The error

```
Expected GitLab MCP tools (e.g. merge request approval tools) are missing from the tool list with no error at startup.
```

## Fix it

1. Call tools/list and note which GitLab tools are absent.
   Expected: Some tools you need are not advertised.
2. Check your PAT scopes in GitLab.
   Expected: The token has a narrow scope set.
3. Either widen the token scopes, or set GITLAB_MCP_IGNORE_SCOPES=true in the server env.
   Expected: The env change is saved.
4. Restart the MCP client.
   Expected: The full tool list appears.

## When this applies

The GitLab MCP server connects cleanly but tools you expect are missing from the catalog, and your PAT uses limited scopes.

## When this does NOT apply

If tools are present but calls fail, that is auth or permissions, not filtering. If nothing connects at all, check the token and URL.

## Tool compatibility

jmrplens/gitlab-mcp-server, recent versions

## Also seen as

- GitLab MCP tools not showing
- gitlab MCP missing merge request tools
- GITLAB_MCP_IGNORE_SCOPES

## Why it happens

To avoid advertising tools the token cannot use, the server trims tools/list by token scope. With a minimal token that trimming looks like missing functionality. The ignore flag disables the filter.

## Edge cases

- With the flag on, calling a tool your token cannot use returns a permission error at call time.
- Prefer widening scopes over the flag when you know what you need.
- Group-scoped tokens filter more aggressively than instance tokens.

---

Source: [Vectle](https://vectle.com/skills/skl_BHxqKOC9QwxeV1XFyi_58w). Version: `skv_9q4dDcTJM7tbCUCQSmnmMg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
