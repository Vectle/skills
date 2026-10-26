---
name: "npm-error-could-not-determine-executab-01e3a383bb5edd71"
description: "Fixes the exa-mcp-server install failure where npx reports it cannot determine an executable to run. Use when the Exa MCP server will not start locally and the npx command exits with the executable-resolution error. Not for missing API key errors or remote hosted MCP setup."
metadata:
  skill_id: "skl_nH81GD_WnK-Zq0zMGzgzqw"
  title: "npm error could not determine executable to run (exa-mcp-server)"
  version: "skv_neyU-30V_5RjwFiumO6WCg"
  updated: "2026-10-03T04:26:49.985506+00:00"
  canonical_url: "https://vectle.com/skills/skl_nH81GD_WnK-Zq0zMGzgzqw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/exa-labs/exa-mcp-server/issues/107\"]"
---

# Fix `npm error could not determine executable to run` for exa-mcp-server

## TL;DR
Point your MCP config at the server file with `node` directly instead of `npx`, or switch to the hosted remote server at `https://mcp.exa.ai/mcp`. The npx wrapper cannot resolve the package's entry point because the published `bin` field points inside a hidden `.smithery` directory, which npm refuses to execute.

The exact error:

```text
npm error could not determine executable to run
```

## Steps

### 1. Confirm this is the error
Run the package by hand in a terminal:

```bash
npx -y exa-mcp-server
```

Success check: if you see `npm error could not determine executable to run`, this skill applies. If instead you see a missing API key error, that is a different problem.

### 2. Find where npm installed the package

```bash
npm root -g
```

Success check: it prints a directory. Append `/exa-mcp-server/.smithery/stdio/index.cjs` to it. Verify the file exists:

```bash
ls "$(npm root -g)/exa-mcp-server/.smithery/stdio/index.cjs"
```

### 3. Point the MCP config at node directly
Edit `claude_desktop_config.json` (or your client's MCP config) and replace the npx entry with a direct node call:

```json
{
  "mcpServers": {
    "exa": {
      "command": "node",
      "args": ["[global npm root]/exa-mcp-server/.smithery/stdio/index.cjs"],
      "env": { "EXA_API_KEY": "[your Exa API key]" }
    }
  }
}
```

Success check: save the file, fully restart the client. The exa server should start and its tools (web search, code context) appear in the tool list.

### 4. Alternative: use the hosted remote server instead
If you would rather skip the local install entirely, use the remote endpoint. For Claude Code:

```bash
claude mcp add exa -e EXA_API_KEY [your value] Exa API key] -- npx -y mcp-remote https://mcp.exa.ai/mcp
```

Success check: `claude mcp list` shows exa connected, and no local package install is needed.

## When this applies
- You followed the standard `npx -y exa-mcp-server` setup for Claude Desktop, Cursor, or another MCP client and the server never starts.
- The terminal reproduces `npm error could not determine executable to run` for the package.

## When it does not apply
- You get `EXA_API_KEY environment variable is not set` instead. That is an auth problem: put your key in the `env` block.
- You are using the remote `https://mcp.exa.ai/mcp` URL already. Do not mix the remote URL and the npx package in one entry; they are separate setups.

## Tool compatibility
- exa-mcp-server npm package, versions publishing the `.smithery/stdio/index.cjs` layout
- npx / npm (Node.js 18+)
- Claude Desktop, Claude Code, Cursor, KiloCode

## Why it happens
The published package's `bin` field points at `.smithery/stdio/index.cjs`, a path inside a hidden dot-directory. npm/npx will not resolve an executable out of a hidden directory, so it exits with the "could not determine executable" error even though the file is present and valid.

## Edge cases
- `bunx exa-mcp-server` hits a related startup crash (`SyntaxError` at line 2 of the same file) on some versions; the node-direct workaround avoids that path too.
- If npm installed the package in a user-local prefix (`.npm-global`), the args path must use that prefix, not the system one. `npm root -g` tells you which.
- Some users report success pinning an older package version (e.g. `[recipient email]`) as a stopgap; the remote server option is the cleaner long-term move.

---

Source: [Vectle](https://vectle.com/skills/skl_nH81GD_WnK-Zq0zMGzgzqw). Version: `skv_neyU-30V_5RjwFiumO6WCg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
