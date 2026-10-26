---
name: "apify-mcp-record-or-token-not-found-in-b2cef253b1bd7468"
description: "Fixes the Apify Actors MCP server failing with record-or-token-not-found when running in Standby mode. Covers why private Actors are invisible to the server, the two fixes (make the Actor public or sign the server in with an API token), and when each applies. Not for wrong Actor IDs or bad tokens."
metadata:
  skill_id: "skl_NAy2N4sXyXVU79C6PhqJmg"
  title: "Apify MCP: record-or-token-not-found in Standby mode (public Actor or logged-in token)"
  version: "skv_3Hc2pYUp-o071QP7KnjxJw"
  updated: "2026-10-03T05:58:28.837899+00:00"
  canonical_url: "https://vectle.com/skills/skl_NAy2N4sXyXVU79C6PhqJmg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/apify/actors-mcp-server\"]"
---

Give the server a way to see the Actor. In Standby mode the Actors MCP server loads Actors it can read; a private Actor with no API token is invisible and every call fails with record-or-token-not-found. Either make the Actor public or add your API token to the server config.

```text
record-or-token-not-found
```

## The fix

1. Decide: public Actor or private with token. Public is fine for shared utilities; keep business Actors private and use the token.
2. Option A (public): in the Apify Console, open the Actor's settings and set it public.
   Expected: the Actor page loads without login.
3. Option B (private): add your API token to the MCP server config env:
   `"env": { "APIFY_TOKEN": "[your Apify API token]" }`.
   Expected: the config still parses as valid JSON.
4. Restart the MCP client and retry the Actor call.
   Expected: the Actor resolves and runs instead of record-or-token-not-found.

## When this applies

- The error names the Actor you are sure exists in your account.
- You run the Actors MCP server in Standby mode (the persistent mode), not one-shot.

## When it does NOT apply

- "Actor not found" with no record-or-token wording: the ID itself is wrong (see that skill).
- 401 on the token -  the token value is bad (see the 401 skill).

## Tool and version compatibility

- @apify/actors-mcp-server in Standby mode; one-shot mode takes the Actor list differently.

## Variant phrasings

### Apify MCP cannot find my private Actor
Same fix. Private Actors need the token; the server runs logged-out by default.

### record-or-token-not-found but the Actor exists
Existence is not visibility. The server needs read access via public status or your token.

## Why it happens

Standby mode keeps one server process serving many Actors, and it resolves each Actor through the API as whatever identity the server has. With no token that identity is anonymous, and anonymous callers cannot see private Actors, so the API returns record-or-token-not-found.

## Edge cases

- Tokens inherit your account permissions; a token from a teammate's account cannot see your private Actors.
- Making an Actor public is irreversible in the sense that scrapes get cached and indexed; prefer the token for anything sensitive.
- After adding the token, restart fully; the server caches Actor resolution from its logged-out phase.


---

Source: [Vectle](https://vectle.com/skills/skl_NAy2N4sXyXVU79C6PhqJmg). Version: `skv_3Hc2pYUp-o071QP7KnjxJw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
