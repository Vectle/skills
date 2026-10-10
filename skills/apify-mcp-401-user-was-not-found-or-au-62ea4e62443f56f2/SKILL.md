---
name: "apify-mcp-401-user-was-not-found-or-au-62ea4e62443f56f2"
description: "Fixes 401 auth failures from the Apify MCP server when the token is missing its required prefix. Covers the apify_api_ prefix format, where tokens are issued, and how to tell this apart from a revoked token. Not for Standby-mode visibility errors."
metadata:
  skill_id: "skl_ifmtgdQhNiYLw7Z-Hrtl1g"
  title: "Apify MCP: 401 'User was not found or authentication token is not valid' (apify_api_ prefix)"
  version: "skv_jRChgN0_YfKuYOwIoAvJVA"
  updated: "2026-10-03T05:53:30.161487+00:00"
  canonical_url: "https://vectle.com/skills/skl_ifmtgdQhNiYLw7Z-Hrtl1g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Check the token starts with `apify_api_`. Apify API tokens carry a fixed prefix; a token pasted without it (or a truncated copy) fails auth with "User was not found or authentication token is not valid". Re-copy the full token from the Console including the prefix, update the config, restart.

```text
401: User was not found or authentication token is not valid
```

## The fix

1. Open the Apify Console token page and copy the token in full, starting with `apify_api_`.
   Expected: the copied string begins with the prefix.
2. Replace the token value in your MCP config env block.
   Expected: the config still parses as valid JSON.
3. Fully restart the MCP client.
   Expected: Actor calls authenticate; the 401 is gone.

## When this applies

- 401 on every call with a token you typed or copied by hand.
- The stored token looks shorter than the one in the Console.

## When it does NOT apply

- Full token with prefix still 401s: the token was revoked; issue a new one.
- record-or-token-not-found: visibility problem, different skill.

## Tool and version compatibility

- @apify/actors-mcp-server and direct Apify API calls; the prefix rule is API-wide.

## Variant phrasings

### Apify 401 with a token I just created
Re-copy it. Fresh tokens are usually broken by a partial copy, not by the platform.

### User was not found but the user exists
The message is about the token, not the account. Fix the token string.

## Why it happens

The API parses the token format before looking anything up; a string without the expected prefix never matches a credential and returns the generic not-found message. It reads like an account problem but is always the token string.

## Edge cases

- Some password managers strip the prefix on autofill; paste into a scratch buffer and eyeball the start first.
- Tokens shown once at creation: if you lost the full string, create a new token rather than guessing.
- Rotate tokens you pasted into shared configs; the old one stays valid until revoked.


---

Source: [Vectle](https://vectle.com/skills/skl_ifmtgdQhNiYLw7Z-Hrtl1g). Version: `skv_jRChgN0_YfKuYOwIoAvJVA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
