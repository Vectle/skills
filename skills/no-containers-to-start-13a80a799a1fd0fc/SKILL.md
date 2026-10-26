---
name: "no-containers-to-start-13a80a799a1fd0fc"
description: "Fixes the docker-compose error `ERROR: No containers to start`. It explains the verified fix from a real resolved case, when it applies, and what to check first. Not for unrelated docker-compose failures or different error text."
metadata:
  skill_id: "skl_mwqThb3hgKhz-w3WpTFQjQ"
  title: "No containers to start"
  version: "skv_uIgLzK-OT03KOK3xdvEq5Q"
  updated: "2026-10-03T05:38:55.369104+00:00"
  canonical_url: "https://vectle.com/skills/skl_mwqThb3hgKhz-w3WpTFQjQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/39562748\"]"
---

# Fix `ERROR: No containers to start` (docker-compose)

## TL;DR

You ran docker-compose start but the containers were never created. start only starts containers that already exist, it never creates them. Run docker-compose up -d once to create and start everything; after that, start, stop, and restart work as expected.

The error, verbatim:

```text
ERROR: No containers to start
```

## Steps

1. Check whether any containers exist for the project:

   ```
   docker-compose ps
   ```
   Success check: The list is empty or shows no containers, which confirms nothing was created yet.

2. Create and start everything with up instead of start:

   ```
   docker-compose up -d
   ```
   Success check: Compose prints Creating ... done / Started for each service.

3. Verify the services are running:

   ```
   docker-compose ps
   ```
   Success check: Each service shows Up in the state column.

## When to use

You hit this exact error while using docker-compose. The trigger list below matches your situation.

## When NOT to use

If the error text differs, or the failure is in a different tool (e.g. a Docker daemon error when you only need the compose fix), find the skill for that exact error instead.

## Tool compatibility

docker-compose v1 and Compose v2 (docker compose). Any OS.

## Variant phrasings

### ERROR: No containers to start

### no containers to start

## Root cause

docker-compose start and restart operate on already-created containers. If you never ran up (or ran down, which removes containers), there is nothing to start, so compose errors out instead of silently doing nothing. In Compose v2 the same message can appear when a service is scaled to 0 replicas.

## Edge cases

- After docker-compose down, you must run up again; start alone will fail the same way.
- If only one service errors, check that service for a scale: 0 or a profiles entry that was not enabled.
- docker compose (v2, no hyphen) behaves the same; the fix is identical.

## Where this came from

Resolved from the public discussion at https://stackoverflow.com/questions/39562748 (so:39562748).


---

Source: [Vectle](https://vectle.com/skills/skl_mwqThb3hgKhz-w3WpTFQjQ). Version: `skv_uIgLzK-OT03KOK3xdvEq5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
