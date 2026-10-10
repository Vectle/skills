---
name: "no-configuration-file-provided-not-fou-84937d60e8a9dcfc"
description: "Fixes the docker-compose error `no configuration file provided: not found`. It explains the verified fix from a real resolved case, when it applies, and what to check first. Not for unrelated docker-compose failures or different error text."
metadata:
  skill_id: "skl_4Kjp0obDVHAxEgW5aOYg3w"
  title: "no configuration file provided: not found"
  version: "skv_rXU2bHLofRv0j335CIumAg"
  updated: "2026-10-03T06:06:13.229311+00:00"
  canonical_url: "https://vectle.com/skills/skl_4Kjp0obDVHAxEgW5aOYg3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix `no configuration file provided: not found` (docker-compose)

## TL;DR

You ran compose from a directory that has no compose file. cd into the directory containing docker-compose.yml, or point compose at it explicitly with docker compose -f /path/to/docker-compose.yml ps. That is the whole fix.

The error, verbatim:

```text
no configuration file provided: not found
```

## Steps

1. Confirm you are in the wrong directory:

   ```
   pwd && ls docker-compose.yml compose.yaml 2>/dev/null
   ```
   Success check: pwd prints the directory; ls shows whether a compose file is there.

2. Change into the directory that holds the compose file:

   ```
   cd /path/to/project
   ```
   Success check: ls lists the compose file in the new directory.

3. Re-run your compose command and verify:

   ```
   docker compose ps
   ```
   Success check: Services are listed with their state; no error.

## When to use

You hit this exact error while using docker-compose. The trigger list below matches your situation.

## When NOT to use

If the error text differs, or the failure is in a different tool (e.g. a Docker daemon error when you only need the compose fix), find the skill for that exact error instead.

## Tool compatibility

Compose v2 (docker compose) and docker-compose v1. Any OS.

## Variant phrasings

### no configuration file provided: not found

### docker compose ps returns no configuration file provided

## Root cause

Compose looks for docker-compose.yml / compose.yaml in the current working directory (or the paths given by -f / COMPOSE_FILE). When you run it from anywhere else, it finds nothing and reports this instead of guessing.

## Edge cases

- Check the file is not saved with a hidden extension like docker-compose.yml.txt on Windows.
- If you use multiple files, every -f flag must point at a real file; one bad path gives the same error.
- COMPOSE_FILE env var overrides the default search; an empty or wrong COMPOSE_FILE causes this too.

## Where this came from

Resolved from the public discussion at https://stackoverflow.com/questions/70256928 (so:70256928).


---

Source: [Vectle](https://vectle.com/skills/skl_4Kjp0obDVHAxEgW5aOYg3w). Version: `skv_rXU2bHLofRv0j335CIumAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
