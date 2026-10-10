---
name: "apify-mcp-actor-not-found-wrong-actor-9b7cb67662a4c8bd"
description: "Fixes 'Actor not found' errors from the Apify MCP server caused by a mistyped Actor ID. Covers the username/actor-name vs Actor ID formats, where to copy the exact ID, and how to tell this apart from visibility errors. Not for auth failures."
metadata:
  skill_id: "skl__P1FQbyyH4TS-JHQdhmfqA"
  title: "Apify MCP: 'Actor not found' (wrong Actor ID or name)"
  version: "skv_UchBWGSqucuKxsiNC9yq2Q"
  updated: "2026-10-03T06:03:49.930131+00:00"
  canonical_url: "https://vectle.com/skills/skl__P1FQbyyH4TS-JHQdhmfqA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Copy the exact Actor ID from the Console. "Actor not found" almost always means the string you passed is not an Actor: a typo, a display name instead of the ID, or a renamed Actor. The Console's Actor page shows the canonical ID; use it verbatim.

```text
Actor not found
```

## The fix

1. Open the Actor in the Apify Console and copy the Actor ID (format like `username/actor-name` or the long ID).
   Expected: you have the exact string, case intact.
2. Replace the actor value in your tool call or server args with the copied string.
   Expected: no retyping, no guessing.
3. Retry the call.
   Expected: the Actor resolves and starts.

## When this applies

- The Actor exists in the Console but the MCP call 404s it.
- You typed the name from memory or copied it from a chat message.

## When it does NOT apply

- record-or-token-not-found: visibility/auth problem, different skill.
- The ID is right but runs fail: see the FAILED run skill.

## Tool and version compatibility

- @apify/actors-mcp-server and the Apify API; ID formats are platform-wide.

## Variant phrasings

### Apify Actor 404 but it exists
Same fix. "Exists in the Console" plus "404 from the API" equals a string mismatch.

### Renamed my Actor, now not found
Renames change the name part of the ID. Re-copy the new canonical ID.

## Why it happens

Actor identity is the exact ID string, not the display title. Humans remember titles; the API matches IDs. Any drift (case, dashes, old name after a rename) 404s.

## Edge cases

- Store Actors use IDs too; "the popular web scraper" is not an identifier.
- Some tools accept the short name only within your own account; the full `username/name` form works everywhere.
- If the Actor was deleted, the ID 404s permanently; check the Console trash/recent deletions.


---

Source: [Vectle](https://vectle.com/skills/skl__P1FQbyyH4TS-JHQdhmfqA). Version: `skv_UchBWGSqucuKxsiNC9yq2Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
