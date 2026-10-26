---
name: "filesystem-mcp-mcp-filesystem-server-d-8ecefb117e98e2fa"
description: "Fixes the filesystem MCP server showing Server disconnected in Claude Desktop when Node was installed via nvm. Use when the server never connects and you installed Node with nvm. Not for wrong directory paths or permission errors."
metadata:
  skill_id: "skl_IEDlfPfYNCjW1cpq7xJh5w"
  title: "filesystem MCP: MCP filesystem Server disconnected (nvm node not on PATH)"
  version: "skv_FMg-xm-bz5tmg2jDLvlnUw"
  updated: "2026-10-03T04:34:41.225098+00:00"
  canonical_url: "https://vectle.com/skills/skl_IEDlfPfYNCjW1cpq7xJh5w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://dev.to/jonigl/mcp-filesystem-server-disconnected-44db\"]"
---

# Fix filesystem MCP `MCP filesystem: Server disconnected` (nvm Node)

## TL;DR
If you installed Node with nvm, Claude Desktop cannot find your `npx`. Create a small wrapper script that puts your nvm Node bin directory on PATH and execs npx, then point the server's `command` at the wrapper.

The exact symptom in Claude Desktop:

```text
MCP filesystem: Server disconnected
```

## Steps

### 1. Find your nvm Node path

```bash
which node
```

Success check: it prints something like `[HOME]/...`. Copy the directory part up to `/bin`.

### 2. Create the wrapper script
Create `/usr/local/bin/npx-for-claude` with:

```bash
#!/usr/bin/env bash
export PATH="[your nvm node bin dir]:$PATH"
exec npx "$@"
```

Replace `[your nvm node bin dir]` with the directory from step 1, e.g. `[HOME]/...`. Then:

```bash
chmod +x /usr/local/bin/npx-for-claude
```

Success check: `/usr/local/bin/npx-for-claude --version` prints an npx version.

### 3. Point the MCP config at the wrapper
Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx-for-claude",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "[an absolute allowed directory]"]
    }
  }
}
```

Success check: `command` is the wrapper, not bare `npx`.

### 4. Restart Claude Desktop fully
Quit the app and end any leftover Claude processes, then reopen.

Success check: the filesystem server shows connected and `list_directory` works on the allowed directory.

## When this applies
- Claude Desktop shows `MCP filesystem: Server disconnected` for the filesystem server.
- `which node` in your terminal points inside `.nvm`.
- The same config works on machines where Node was installed system-wide.

## When it does not apply
- The server starts but refuses a path. That is the allowed-directories problem: the directory must be absolute and listed in `args`.
- You get permission errors reading files. That is OS permissions, not the launcher.

## Tool compatibility
- @modelcontextprotocol/server-filesystem
- Claude Desktop on macOS (nvm installs)
- Node.js via nvm (any recent version)

## Why it happens
Claude Desktop launches MCP servers with a minimal environment that does not source your shell profile, so nvm's PATH entries are missing. Bare `npx` then resolves to nothing (or the wrong node), the server process dies instantly, and the client reports the generic "Server disconnected" with no hint that the launcher was the problem.

## Edge cases
- If you switch nvm Node versions, update the wrapper's PATH or the server will silently run the old version.
- On Apple Silicon vs Intel mismatches, make sure the nvm Node arch matches the client.
- An alternative some users prefer: use the absolute path to npx in `command` (from `which npx`) instead of a wrapper; it breaks on every nvm version switch.

---

Source: [Vectle](https://vectle.com/skills/skl_IEDlfPfYNCjW1cpq7xJh5w). Version: `skv_FMg-xm-bz5tmg2jDLvlnUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
