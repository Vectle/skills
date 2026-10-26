---
name: "notion-mcp-object-not-found-page-not-s-096d2d7533fe7c22"
description: "Fixes Notion MCP calls failing with object_not_found even though the page exists. Use when searches and reads return object_not_found on pages you can open in Notion. Not for invalid API keys or for server startup failures."
metadata:
  skill_id: "skl_jJE8wdrh7zJmDcbMPJREhg"
  title: "Notion MCP: object_not_found (page not shared with the integration)"
  version: "skv_SVoLiu4OOM2yTCvebz68ZQ"
  updated: "2026-10-03T04:36:34.48418+00:00"
  canonical_url: "https://vectle.com/skills/skl_jJE8wdrh7zJmDcbMPJREhg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/ldraney/notion-mcp/issues/18\"]"
---

# Fix Notion MCP `object_not_found` (page not shared with the integration)

## TL;DR
Share the page or database with your Notion integration: open it in Notion, open the connections menu, and add the integration. Notion hides everything from integrations by default, so the API answers `object_not_found` for pages you can see perfectly well yourself.

The exact error:

```text
object_not_found
```

## Steps

### 1. Confirm the page exists and the key works
Open the page in Notion in your browser (it loads) and run a search through the MCP server for something else. If search works but this page is missing, the key is fine and this page is simply not shared.

Success check: other pages return; only the unshared ones 404.

### 2. Share the page with the integration
1. Open the page or database in Notion.
2. Click the `...` menu (top right).
3. Choose `Add connections` (or `Connect to`).
4. Select your integration (the one whose token is in your MCP config).

Success check: Notion shows the integration listed under the page's connections.

### 3. Share parent pages too
Permissions do not cascade the way you expect: a child page is not visible just because the parent is shared, and databases need their own share. Repeat step 2 for every database and parent page the agent needs.

Success check: re-run the failing tool call; it returns the page content instead of `object_not_found`.

## When this applies
- Notion MCP tools return `object_not_found` for pages/databases that exist.
- The integration token is valid (other calls work).

## When it does not apply
- You get `unauthorized` or `401`. That is a bad or revoked token -  check the key in the MCP config, and confirm it starts with `secret_` or `ntn_`.
- `NOTION_API_KEY environment variable not set` at startup. That is the key never reaching the server: put it in the `env` block of the MCP config.

## Tool compatibility
- Notion MCP servers using integration tokens (official and community)
- Notion API (2022+ versions)
- Claude Desktop, Claude Code, Cursor

## Why it happens
Notion's permission model is deny-by-default for integrations. Creating an integration token does not grant it your workspace; each page and database must be explicitly shared with it. The API cannot distinguish "does not exist" from "not shared with you", so both come back as `object_not_found`, which sends people debugging URLs and page IDs instead of the connections menu.

## Edge cases
- Teamspaces: sharing a teamspace with the integration still requires the pages inside to be shared individually in some setups.
- If you duplicated a page, the copy loses the connection; re-share it.
- Deleted-then-restored pages sometimes drop their connections; check the connections menu after a restore.

---

Source: [Vectle](https://vectle.com/skills/skl_jJE8wdrh7zJmDcbMPJREhg). Version: `skv_SVoLiu4OOM2yTCvebz68ZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
