---
name: "github-mcp-error-github-personal-acces-740a502da691c024"
description: "Fixes the misleading GitHub MCP server startup error when following the OAuth install docs. Use when docker run exits with Error: GITHUB_PERSONAL_ACCESS_TOKEN not set even though you configured OAuth. Not for expired PATs or missing Docker images."
metadata:
  skill_id: "skl_G_48vWcbYmBJ90dhFko__A"
  title: "GitHub MCP: Error: GITHUB_PERSONAL_ACCESS_TOKEN not set (OAuth docs vs released image)"
  version: "skv_zxgjff0cVRCPA2BNBuwtfQ"
  updated: "2026-10-03T04:33:28.564915+00:00"
  canonical_url: "https://vectle.com/skills/skl_G_48vWcbYmBJ90dhFko__A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix GitHub MCP `Error: GITHUB_PERSONAL_ACCESS_TOKEN not set` when using the OAuth config

## TL;DR
The docs' OAuth setup is not in the released image yet. Either use a classic personal access token (PAT) in the config, or run a build that actually contains the OAuth code. The error message is misleading: it says nothing about OAuth or versions.

The exact error:

```text
Error: GITHUB_PERSONAL_ACCESS_TOKEN not set
```

## Steps

### 1. Check which image you pulled

```bash
docker images ghcr.io/github/github-mcp-server --format "{{.Tag}}"
```

Success check: if it says `latest` resolving to v1.4.0, that image predates the OAuth feature. The OAuth login code merged to main after the v1.4.0 release, so it is not in the image.

### 2. Switch to a PAT (the fix that works today)
Generate a fine-grained PAT at your GitHub settings page with the scopes you need, then use the PAT config instead of the OAuth config:

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "[your GitHub personal access token]" }
    }
  }
}
```

Success check: the server starts and `list_repos` or a similar tool call works.

### 3. Or run a build with the OAuth code
If you specifically need the OAuth flow, build from main or wait for a release newer than v1.4.0, then keep the documented `GITHUB_OAUTH_CALLBACK_PORT` config.

Success check: the server prompts a browser-based login on first use instead of exiting.

## When this applies
- You copied the OAuth install config from the docs (it passes `GITHUB_OAUTH_CALLBACK_PORT`).
- `docker run` exits immediately with `Error: GITHUB_PERSONAL_ACCESS_TOKEN not set`.

## When it does not apply
- You are already using a PAT and still get the error. Then the token genuinely is not reaching the container: check the `-e` flag and the `env` block, and check the token has not expired.
- Docker itself fails (`ghcr.io pull error`). Try `docker logout ghcr.io` and restart.
- Claude Desktop says "command is undefined". Claude Desktop does not support `type: http` configs; use the Docker stdio setup above.

## Tool compatibility
- ghcr.io/github/github-mcp-server Docker image (v1.4.0 and earlier)
- Claude Desktop, Claude Code, Cursor
- Docker required for the image-based setup

## Why it happens
Docs and code shipped out of order. The install guide was updated to lead with OAuth login, but the OAuth implementation merged to main after the last tagged release, so the image everyone pulls (`latest` = v1.4.0) only knows the PAT path. With no PAT in the environment, the server exits with the PAT error, which reads as if you misconfigured the token rather than ran an image that lacks the feature.

## Edge cases
- `--insiders` builds also lack the feature on the released image; the flag does not help here.
- PATs expire; if this error appears months after a working setup, regenerate the token before re-diagnosing.
- For Claude Code, some users switch to the remote endpoint over HTTP with an Authorization header instead of Docker; that is a separate, supported path.

---

Source: [Vectle](https://vectle.com/skills/skl_G_48vWcbYmBJ90dhFko__A). Version: `skv_zxgjff0cVRCPA2BNBuwtfQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
