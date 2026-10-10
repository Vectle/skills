---
name: "importerror-cannot-import-name-escape-d7fc03c0a143880c"
description: "Fixes ImportError: cannot import name 'escape' from 'jinja2' Use when jinja2>=3.1 with old Flask or old direct imports Not for: you want autoescaping in templates (that is a different feature)"
metadata:
  skill_id: "skl_bSfOV9aTxb0VtZbWRkbi5w"
  title: "ImportError: cannot import name 'escape' from 'jinja2'"
  version: "skv_YWkWmsDAlgAix0y7eOC6Lg"
  updated: "2026-10-03T04:51:22.990406+00:00"
  canonical_url: "https://vectle.com/skills/skl_bSfOV9aTxb0VtZbWRkbi5w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'escape' from 'jinja2'

jinja2 3.1 removed `escape`; Flask below 2.2 still imports it from jinja2. Fix: upgrade Flask (`pip install -U flask`, needs >= 2.2.2), or change your own `from jinja2 import escape` to `from markupsafe import escape`. markupsafe is already a jinja2 dependency, so no new install needed.

## The exact error

```text
ImportError: cannot import name 'escape' from 'jinja2'
```

## Fix it

1. Your code: `from jinja2 import escape` -> `from markupsafe import escape`.
   Expected: import works

2. Traceback inside flask itself: `pip install -U flask` (>= 2.2.2).
   Expected: flask imports escape from markupsafe

3. Stopgap: `pip install "jinja2<3.1"`.
   Expected: old jinja2 has escape (not recommended)

## When this applies

jinja2>=3.1 with old Flask or old direct imports

## When this does NOT apply

you want autoescaping in templates (that is a different feature)

## Versions

jinja2 >= 3.1 with Flask < 2.2

## Why it happens

jinja2 moved escape to markupsafe for separation of concerns in 3.1.

## Edge cases

Flask 2.2.2 is the minimum that handles jinja2 3.1; 2.2.0/2.2.1 still break.


---

Source: [Vectle](https://vectle.com/skills/skl_bSfOV9aTxb0VtZbWRkbi5w). Version: `skv_YWkWmsDAlgAix0y7eOC6Lg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
