---
name: "github-mcp-server-fails-to-connect-ins-dba5427b04de8b4a"
description: "Fixes the GitHub MCP server failing to reach api.github.com from inside Docker on networks with TLS interception. Use when the server works on the host but fails in a container with TLS or certificate errors. Not for bad tokens or DNS issues."
metadata:
  skill_id: "skl_VH_zsIj5Hnw62eBDTzK9QQ"
  title: "GitHub MCP server fails to connect inside Docker behind a corporate TLS proxy"
  version: "skv_OJiYPRcm0-O2F80pnzaVOg"
  updated: "2026-10-03T06:07:52.221121+00:00"
  canonical_url: "https://vectle.com/skills/skl_VH_zsIj5Hnw62eBDTzK9QQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[]"
---

# GitHub MCP server fails to connect inside Docker behind a corporate TLS proxy

**TL;DR:** Run the prebuilt release binary on the host instead of the Docker image; that sidesteps the container TLS stack entirely. The failure is your corporate proxy re-signing TLS inside the container, where the proxy CA is not trusted. If you must use Docker, mount your corporate CA bundle into the container trust store and rebuild.

## The error

```
There was an error connecting to GitHub server. Please check your server URL and network connection, then try again.
```

## Fix it

1. Download the GitHub MCP server release binary for your OS and run it directly on the host.
   Expected: The server starts and reaches api.github.com without TLS errors.
2. Point your MCP client config at the binary instead of the docker run command.
   Expected: Tool calls succeed from the host network.
3. If Docker is required, copy the corporate CA cert into the image and update the trust store, then rebuild.
   Expected: TLS verification passes inside the container.

## When this applies

The GitHub MCP server cannot reach GitHub only when run in Docker, on a corporate network with TLS-intercepting proxies, while the host itself connects fine.

## When this does NOT apply

If the host also fails, it is a general network or proxy config issue, not Docker TLS. Token errors look different (401).

## Tool compatibility

GitHub MCP server (modelcontextprotocol/servers), Docker deployments

## Also seen as

- GitHub MCP docker certificate verify failed
- GitHub MCP server TLS error in container
- corporate proxy breaks GitHub MCP in Docker

## Why it happens

Corporate proxies terminate TLS and re-sign with an internal CA. The host trusts that CA, but the minimal Docker image does not, so every HTTPS call from the server fails verification. Release binaries on the host inherit the host trust store.

## Edge cases

- Some proxies also block the npm registry, which breaks docker build; the release binary avoids that too.
- VPN split-tunnel changes can move you on and off the intercepting proxy; retest after network changes.
- Mounting the CA is fragile across base image updates; prefer the binary.

---

Source: [Vectle](https://vectle.com/skills/skl_VH_zsIj5Hnw62eBDTzK9QQ). Version: `skv_OJiYPRcm0-O2F80pnzaVOg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
