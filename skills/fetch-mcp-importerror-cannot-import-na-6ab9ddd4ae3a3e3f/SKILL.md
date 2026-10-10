---
name: "fetch-mcp-importerror-cannot-import-na-6ab9ddd4ae3a3e3f"
description: "Fixes the fetch MCP server failing to start with an ImportError about McpError after the mcp SDK 2.0 release. Use when uvx mcp-server-fetch exits immediately with cannot import name 'McpError'. Not for 404 package errors or for fetch tool failures on specific URLs."
metadata:
  skill_id: "skl_KIvlIdBtgYv6aDmC-Dj0ew"
  title: "fetch MCP: ImportError cannot import name 'McpError' from 'mcp.shared.exceptions'"
  version: "skv_3lLCXqH6f-X7IF0ZQdtbHA"
  updated: "2026-10-03T04:35:19.485256+00:00"
  canonical_url: "https://vectle.com/skills/skl_KIvlIdBtgYv6aDmC-Dj0ew"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix fetch MCP `ImportError: cannot import name 'McpError' from 'mcp.shared.exceptions'`

## TL;DR
Pin the SDK below 2.0: run `uvx --with "mcp<2" mcp-server-fetch`. The `mcp` 2.0.0 release renamed `McpError` to `MCPError`, and the fetch server (released before 2.0) imports the old name, so every fresh unpinned install crashes on startup.

The exact error:

```text
ImportError: cannot import name 'McpError' from 'mcp.shared.exceptions'. Did you mean: 'MCPError'?
```

## Steps

### 1. Confirm the SDK version mismatch
Run the server by hand:

```bash
uvx mcp-server-fetch
```

Success check: the traceback mentions `mcp_server_fetch/server.py` importing `McpError` and suggests `MCPError`. That confirms this exact problem.

### 2. Pin mcp below 2.0
Change your MCP config to inject the pinned dependency:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["--with", "mcp<2", "mcp-server-fetch"]
    }
  }
}
```

Success check: restarting the client, the fetch server connects and `fetch` appears in the tool list.

### 3. Verify the handshake manually (optional)

```bash
uvx --with "mcp<2" mcp-server-fetch
```

then send an initialize frame over stdin. Success check: the server answers instead of exiting with code 1.

## When this applies
- `uvx mcp-server-fetch` exits immediately with the `McpError` ImportError.
- Fresh installs broke around or after the mcp 2.0.0 release; older cached environments still work.
- Also affects `mcp-server-time` and `mcp-server-git` (same ImportError / missing attributes); the same `--with "mcp<2"` fix applies.

## When it does not apply
- `404 Not Found` from the npm registry for `@modelcontextprotocol/server-fetch`. That package never existed on npm; the reference fetch server is the PyPI package `mcp-server-fetch` run through `uvx`.
- The server starts but a specific URL fails to fetch. That is a per-URL problem (robots, auth, JS rendering), not the startup crash.

## Tool compatibility
- mcp-server-fetch (PyPI), releases before the mcp<2 cap (e.g. 2026.7.10)
- mcp Python SDK 2.0.0+
- uv / uvx launcher
- Claude Desktop, Claude Code, Cursor

## Why it happens
The fetch server's `pyproject.toml` declared `mcp>=1.1.3` with no upper bound. When `mcp` 2.0.0 shipped and renamed the exception class `McpError` to `MCPError` (plus replacing the low-level Server decorators), every fresh dependency resolution pulled 2.0.0 and the old import broke. uvx does not pin, so all new installs were affected from 2026-07-28 until the upstream cap landed.

## Edge cases
- If you already have a working cached environment, do not "fix" it; the pin only matters for fresh resolves.
- Long term, the servers are being ported to the 2.x API; once your installed fetch release declares `mcp>=2` support, drop the `--with` override.
- On Windows the same crash appears; the fix is identical.

---

Source: [Vectle](https://vectle.com/skills/skl_KIvlIdBtgYv6aDmC-Dj0ew). Version: `skv_3lLCXqH6f-X7IF0ZQdtbHA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
