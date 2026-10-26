---
name: "keyerror-transport-from-multiservermcp-c6aac9d35f06a804"
description: "Fixes KeyError: 'transport' when calling get_tools() on LangGraph's MultiServerMCPClient. Use when the MCP client config came from a blog post or FastMCP docs and get_tools() raises KeyError 'transport'. Cause: the servers dict is wrapped in an extra \"mcpServers\" key. Fix: pass the servers dict directly. Not for connection failures to a running MCP server."
metadata:
  skill_id: "skl_ON-SWvj-iH_7oyF-UIK4Lw"
  title: "KeyError: 'transport' from MultiServerMCPClient.get_tools()"
  version: "skv_IFdVKN-orsfopwQqyym8mQ"
  updated: "2026-10-03T05:04:20.278247+00:00"
  canonical_url: "https://vectle.com/skills/skl_ON-SWvj-iH_7oyF-UIK4Lw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/79653344/error-keyerror-transport-while-trying-to-get-mcp-tools-from-multiservermcpclient\"]"
---

# KeyError: 'transport' from MultiServerMCPClient.get_tools()

TL;DR: your server config is wrapped in an extra `"mcpServers"` key that `MultiServerMCPClient` does not expect. Pass the servers dict directly: `MultiServerMCPClient({"airbnb": {"transport": "stdio", ...}})`. The client iterates the dict you give it, so one extra nesting level breaks the `"transport"` lookup.

```text
KeyError: 'transport'
# raised by await client.get_tools() when the config dict has the wrong shape.
```

## When this applies

- You use `MultiServerMCPClient` from `langchain_mcp_adapters` to load MCP tools into a LangGraph agent.
- `get_tools()` raises `KeyError: 'transport'` immediately, before any server starts.
- Your config looks like `{"mcpServers": {"airbnb": {...}}}` (copied from a blog post or the FastMCP multi-server docs).

## When it does not

- Timeouts or connection refused mean the server config is right but the server is not reachable. Different fix.
- `get_tools()` returning an empty list means the server started but exposed no tools.

## Fix it

### 1. Drop the wrapper key

```python
# wrong: extra "mcpServers" nesting
client = MultiServerMCPClient(connections={"mcpServers": {"airbnb": {...}}})

# right: servers dict directly
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({
    "airbnb": {
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@openbnb/mcp-server-airbnb"],
    }
})
tools = await client.get_tools()
```

Expected: `get_tools()` returns the tool list instead of raising KeyError.

### 2. Every server entry needs a transport

```python
# stdio servers
"my_server": {"transport": "stdio", "command": "npx", "args": [...]}

# HTTP servers
"other": {"transport": "streamable_http", "url": "YOUR_HOST:4001/mcp"}
```

Expected: the client knows how to reach each server. A missing `"transport"` key on ANY entry raises the same KeyError, so check all of them.

### 3. Then wire the tools into your agent

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools)
```

Expected: the agent lists the MCP tools and can call them.

## Why it happens

`MultiServerMCPClient` expects `{server_name: server_config}` and reads `server_config["transport"]` for each entry. When you wrap everything in `"mcpServers"`, it iterates one entry named `"mcpServers"` whose value is the whole servers dict, and that dict has no `"transport"` key. The blog-post shape comes from a different client (FastMCP's multi-server config), not this one.

## Edge cases

- `connections=` vs positional: both spellings appear in examples. The SHAPE of the dict matters, not the kwarg name.
- npx-based servers need node installed where the agent runs. In Docker, that means node in the image, not just on your laptop.
- On Windows, stdio servers often need `shell: True` or a `.cmd` shim for npx.

## Compatibility

`langchain-mcp-adapters` (Python), used with langgraph's `create_react_agent` / `ToolNode`.

---

Source: [Vectle](https://vectle.com/skills/skl_ON-SWvj-iH_7oyF-UIK4Lw). Version: `skv_IFdVKN-orsfopwQqyym8mQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
