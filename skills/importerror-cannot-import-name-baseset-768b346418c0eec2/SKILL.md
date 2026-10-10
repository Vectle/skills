---
name: "importerror-cannot-import-name-baseset-768b346418c0eec2"
description: "Fixes ImportError: cannot import name 'BaseSettings' from 'pydantic' Use when pydantic v2 installed and code does `from pydantic import BaseSettings` Not for: pydantic v1 (BaseSettings is right there; do not add pydantic-settings)"
metadata:
  skill_id: "skl_FBcmk90TU-iJONlHrqoMgQ"
  title: "ImportError: cannot import name 'BaseSettings' from 'pydantic'"
  version: "skv_Q5bcK2SS2Yg8o4rp2QjFEg"
  updated: "2026-10-03T04:43:02.766577+00:00"
  canonical_url: "https://vectle.com/skills/skl_FBcmk90TU-iJONlHrqoMgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'BaseSettings' from 'pydantic'

Pydantic v2 moved settings out of the main package. Install `pydantic-settings` and change the import to `from pydantic_settings import BaseSettings`. Keep `from pydantic import Field` as-is. That is the whole migration for this error.

## The exact error

```text
ImportError: cannot import name 'BaseSettings' from 'pydantic'
```

## Fix it

1. `python -m pip install pydantic-settings`
   Expected: installed

2. Change `from pydantic import BaseSettings` to `from pydantic_settings import BaseSettings`.
   Expected: import works

3. Add `pydantic-settings` to requirements.txt / pyproject.
   Expected: deploys stop breaking

## When this applies

pydantic v2 installed and code does `from pydantic import BaseSettings`

## When this does NOT apply

pydantic v1 (BaseSettings is right there; do not add pydantic-settings)

## Versions

pydantic v2

## Why it happens

v2 split settings into its own distribution to slim the core.

## Edge cases

pydantic-settings v1 is the v1-compat line; v2 line up with pydantic v2.


---

Source: [Vectle](https://vectle.com/skills/skl_FBcmk90TU-iJONlHrqoMgQ). Version: `skv_Q5bcK2SS2Yg8o4rp2QjFEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
