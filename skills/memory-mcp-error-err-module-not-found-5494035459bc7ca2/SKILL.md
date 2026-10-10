---
name: "memory-mcp-error-err-module-not-found-5494035459bc7ca2"
description: "Fixes the memory MCP server crashing on startup with a missing zod module error. Use when @modelcontextprotocol/server-memory exits immediately with Cannot find package 'zod'. Not for knowledge-graph schema errors or for the server starting but tools misbehaving."
metadata:
  skill_id: "skl_vhfT6jmSTIVNnQ7jigxn1Q"
  title: "memory MCP: Error [ERR_MODULE_NOT_FOUND] Cannot find package 'zod'"
  version: "skv_9dcxEsk3wTjK-PuAVpjDxg"
  updated: "2026-10-03T04:35:54.742944+00:00"
  canonical_url: "https://vectle.com/skills/skl_vhfT6jmSTIVNnQ7jigxn1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix memory MCP `Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'zod'`

## TL;DR
The published package forgot to declare `zod` as a dependency. Install `zod` next to it (or wait for a fixed release). The server imports zod at startup, so the missing module kills it before the MCP handshake.

The exact error:

```text
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'zod' imported from .../dist/index.js
```

## Steps

### 1. Confirm the missing dependency
Run the server by hand:

```bash
npx -y @modelcontextprotocol/server-memory
```

Success check: it exits immediately with the `Cannot find package 'zod'` error, and nothing else. That confirms a packaging bug, not your config.

### 2. Install zod alongside the package

```bash
npm install -g zod @modelcontextprotocol/server-memory
```

or with pnpm:

```bash
pnpm add -g zod @modelcontextprotocol/server-memory
```

Success check: rerunning the server no longer mentions zod; it waits on stdin for the MCP handshake.

### 3. Restart the client
Fully restart Claude Desktop / Claude Code / Cursor so the server relaunches with zod resolvable.

Success check: the memory tools (`create_entities`, `read_graph`, `search_nodes`) appear and work.

## When this applies
- `@modelcontextprotocol/server-memory` (or `server-sequential-thinking`) exits instantly with the zod module-not-found error.
- Fresh installs are affected; the published `dependencies` list only `@modelcontextprotocol/sdk`.

## When it does not apply
- The server starts but `read_graph` fails with `Structured content does not match the tool's output schema: data/entities/0 must NOT have additional properties`. That is a schema-validation issue with extra fields in memory.jsonl; strip the non-standard properties from the stored entities.
- Tools fail with JSON parsing errors on Windows. Check the server version; that is a different bug.

## Tool compatibility
- @modelcontextprotocol/server-memory npm package (affected published versions)
- @modelcontextprotocol/server-sequential-thinking (same bug)
- Node.js 18+, npx / pnpm dlx launchers
- Claude Desktop, Claude Code, Cursor, Continue

## Why it happens
The package's bundled `dist/index.js` contains `import { z } from "zod"`, but `zod` was never added to the published `dependencies` in package.json. npm/pnpm only install declared dependencies, so a fresh install has no zod to resolve and Node throws ERR_MODULE_NOT_FOUND at import time, before any MCP code runs.

## Edge cases
- If you install with `npx -y` (ephemeral cache), the manual zod install can be wiped on cache eviction; a global install of both packages is more durable.
- Do not confuse with the sibling startup failure from the mcp 2.0 SDK rename; that one names `McpError`, not zod.
- Once a release declares zod properly, the manual install becomes unnecessary; check the changelog before scripting it permanently.

---

Source: [Vectle](https://vectle.com/skills/skl_vhfT6jmSTIVNnQ7jigxn1Q). Version: `skv_9dcxEsk3wTjK-PuAVpjDxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
