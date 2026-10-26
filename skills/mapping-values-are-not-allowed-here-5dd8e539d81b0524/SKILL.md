---
name: "mapping-values-are-not-allowed-here-5dd8e539d81b0524"
description: "Fixes the docker-compose error `mapping values are not allowed here`. It explains the verified fix from a real resolved case, when it applies, and what to check first. Not for unrelated docker-compose failures or different error text."
metadata:
  skill_id: "skl__CtzV2qODF_5fq7xgYNKwQ"
  title: "mapping values are not allowed here"
  version: "skv_vnsAlgp3JyrvK6Er7T3KAw"
  updated: "2026-10-03T05:53:23.693479+00:00"
  canonical_url: "https://vectle.com/skills/skl__CtzV2qODF_5fq7xgYNKwQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/39077526\"]"
---

# Fix `mapping values are not allowed here` (docker-compose)

## TL;DR

Your compose file has a tab character (or bad indentation) where YAML expects spaces. Search the file for tabs, replace them with spaces, and re-run. docker compose config tells you instantly whether the file parses now.

The error, verbatim:

```text
mapping values are not allowed here
```

## Steps

1. Find the tab characters in the compose file:

   ```
   grep -Pn "	" docker-compose.yml
   ```
   Success check: cat -A shows ^I wherever a tab hides; grep finds the lines.

2. Replace every tab with spaces (2 spaces per indent level is the compose convention):

   ```
   grep -Pn "	" docker-compose.yml
   ```
   Success check: No output means no tabs remain.

3. Validate the file parses cleanly:

   ```
   docker compose config
   ```
   Success check: The parsed file prints with no errors.

## When to use

You hit this exact error while using docker-compose. The trigger list below matches your situation.

## When NOT to use

If the error text differs, or the failure is in a different tool (e.g. a Docker daemon error when you only need the compose fix), find the skill for that exact error instead.

## Tool compatibility

docker-compose v1 and Compose v2. Any OS; common on Windows editors.

## Variant phrasings

### mapping values are not allowed here

### yaml: mapping values are not allowed here

## Root cause

YAML forbids tab characters for indentation. A tab (or a misaligned colon, like key value value split across a line break) makes the YAML parser read a mapping where it expected a scalar, and compose surfaces the parser error. It is always a whitespace problem in the compose file, never a compose bug.

## Edge cases

- A stray tab anywhere in the file breaks parsing, not just near the reported line.
- Copy-pasting from web pages can introduce non-breaking spaces that look like spaces but are not.
- After fixing, docker compose config is the fastest way to confirm the file parses.

## Where this came from

Resolved from the public discussion at https://stackoverflow.com/questions/39077526 (so:39077526).


---

Source: [Vectle](https://vectle.com/skills/skl__CtzV2qODF_5fq7xgYNKwQ). Version: `skv_vnsAlgp3JyrvK6Er7T3KAw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
