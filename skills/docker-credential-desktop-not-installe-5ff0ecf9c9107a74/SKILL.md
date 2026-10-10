---
name: "docker-credential-desktop-not-installe-5ff0ecf9c9107a74"
description: "Fixes the docker-compose error `Error: docker-credential-desktop not installed or not available in PATH`. It explains the verified fix from a real resolved case, when it applies, and what to check first. Not for unrelated docker-compose failures or different error text."
metadata:
  skill_id: "skl_Agp2dxa-8Ef2dx4nMw7ngw"
  title: "docker-credential-desktop not installed or not available in PATH"
  version: "skv_DdcTzWG-523VW2XNWw2H2Q"
  updated: "2026-10-03T06:11:44.282144+00:00"
  canonical_url: "https://vectle.com/skills/skl_Agp2dxa-8Ef2dx4nMw7ngw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix `Error: docker-credential-desktop not installed or not available in PATH` (docker-compose)

## TL;DR

Your ~/.docker/config.json points at the docker-credential-desktop helper, which is not installed on this machine. Delete the "credsStore": "desktop" line from the config and compose stops looking for the helper. Re-login with docker login if you need registry auth.

The error, verbatim:

```text
Error: docker-credential-desktop not installed or not available in PATH
```

## Steps

1. Open your docker config and look for the credsStore line:

   ```
   cat ~/.docker/config.json
   ```
   Success check: You see a line like "credsStore": "desktop" in the file.

2. Remove the credsStore line (or the whole "credsStore": "desktop", entry):

   ```
   python3 -c "import json; json.load(open('[HOME]/...'.replace('[HOME]/...', __import__('os').path.expanduser('~'))))"
   ```
   Success check: The file is still valid JSON (no trailing commas).

3. Retry the compose command that was failing:

   ```
   docker compose pull
   ```
   Success check: compose commands run without the credential error.

## When to use

You hit this exact error while using docker-compose. The trigger list below matches your situation.

## When NOT to use

If the error text differs, or the failure is in a different tool (e.g. a Docker daemon error when you only need the compose fix), find the skill for that exact error instead.

## Tool compatibility

Docker Desktop / docker-compose on Linux, macOS, Windows. Any recent compose version.

## Variant phrasings

### docker-credential-desktop not installed or not available in PATH

### Error: docker-credential-desktop not installed

## Root cause

~/.docker/config.json contains "credsStore": "desktop", which tells compose to shell out to the docker-credential-desktop helper for registry auth. That helper only ships with Docker Desktop; on a plain Linux install (or a copied config) it does not exist, so every compose command that touches the registry fails.

## Edge cases

- If you actually want a credential helper on Linux, install pass (gnupg2 + pass) and keep credsStore, instead of deleting it.
- Docker Desktop for Mac/Windows ships docker-credential-desktop; this only bites when the config is copied to a machine without it.
- After editing, docker login will rewrite the auths section; that is expected.

## Where this came from

Resolved from the public discussion at https://stackoverflow.com/questions/67642620 (so:67642620).


---

Source: [Vectle](https://vectle.com/skills/skl_Agp2dxa-8Ef2dx4nMw7ngw). Version: `skv_DdcTzWG-523VW2XNWw2H2Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
