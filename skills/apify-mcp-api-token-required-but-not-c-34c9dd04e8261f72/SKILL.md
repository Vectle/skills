---
name: "apify-mcp-api-token-required-but-not-c-34c9dd04e8261f72"
description: "Fixes the Apify MCP server erroring that an API token is required when none is configured. Covers the env variable name, the config env block shape, and the full restart. Not for malformed-token 401s or Actor visibility errors."
metadata:
  skill_id: "skl_RnsL7n-eaeZ5F4X1rThyvQ"
  title: "Apify MCP: API token required but not configured (set it in the env block)"
  version: "skv_FjCEWapyIPQw2TWnyPWPqw"
  updated: "2026-10-03T06:01:01.630434+00:00"
  canonical_url: "https://vectle.com/skills/skl_RnsL7n-eaeZ5F4X1rThyvQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/apify/actors-mcp-server\"]"
---

Set the token in the config's `env` block. The server needs an API token for private Actors and higher limits, and it only reads the env its config declares; a shell export never reaches it. Add the variable, restart the client fully, and the requirement error clears.

```text
APIFY_API_TOKEN is required / API token required
```

## The fix

1. Create a token in the Apify Console (My profile, Integrations) and copy it whole.
   Expected: the string starts with the apify_api_ prefix.
2. Add it to your apify server entry:
   ```json
   "apify": {
     "command": "npx",
     "args": ["-y", "@apify/actors-mcp-server"],
     "env": { "APIFY_TOKEN": "[your Apify API token]" }
   }
   ```
   Expected: the config still parses as valid JSON.
3. Fully quit and relaunch the client.
   Expected: the server starts without the token error; private Actors resolve.

## When this applies

- Fresh install hitting a token-required error on startup or first Actor call.
- The token works in the Console but the server claims it is missing.

## When it does NOT apply

- Token set but 401: malformed or revoked token (see those skills).
- Public Actors work but private ones 404: visibility, see the Standby skill.

## Tool and version compatibility

- @apify/actors-mcp-server (npm). Check the README for the exact variable name your version reads; older docs use APIFY_TOKEN.

## Variant phrasings

### Apify MCP says no API token
Same fix. It means the server process env, not your shell.

### I exported APIFY_TOKEN, why does the server not see it
MCP servers do not inherit shell env. The config env block is the only channel.

## Why it happens

Same stdio isolation as every MCP server: the client spawns the process with env built from the config file. Shell exports, .bashrc, and IDE terminals are all invisible to it.

## Edge cases

- Variable naming drift: if one name does not work, check the server README for the current expected name and set exactly that.
- JSON trailing commas break the whole config; validate after editing.
- On shared machines, keep the config file permissions tight since it now holds a credential.


---

Source: [Vectle](https://vectle.com/skills/skl_RnsL7n-eaeZ5F4X1rThyvQ). Version: `skv_FjCEWapyIPQw2TWnyPWPqw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
