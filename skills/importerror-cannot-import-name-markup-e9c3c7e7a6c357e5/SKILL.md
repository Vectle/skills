---
name: "importerror-cannot-import-name-markup-e9c3c7e7a6c357e5"
description: "Fixes ImportError: cannot import name 'Markup' from 'flask' Use when Flask 3.x and anything doing `from flask import Markup` Not for: Flask < 3 (it warns but works)"
metadata:
  skill_id: "skl_NvYnRfnbpm7Lweh2qlgjLA"
  title: "ImportError: cannot import name 'Markup' from 'flask'"
  version: "skv_Pqi7-QYgkeRTzaeyNEWy1A"
  updated: "2026-10-03T04:50:26.82609+00:00"
  canonical_url: "https://vectle.com/skills/skl_NvYnRfnbpm7Lweh2qlgjLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'Markup' from 'flask'

Flask 3 removed the `flask.Markup` re-export. Change `from flask import Markup` to `from markupsafe import Markup`. If it is a third-party extension (Flask-GoogleMaps, etc.), upgrade the extension; patching your own import takes ten seconds.

## The exact error

```text
ImportError: cannot import name 'Markup' from 'flask'
```

## Fix it

1. `grep -rn "from flask import" --include=*.py . | grep Markup` to find all occurrences.
   Expected: list of files

2. Replace with `from markupsafe import Markup`.
   Expected: app imports cleanly, tests pass

3. Extension-owned? `pip install -U [extension]`.
   Expected: upstream fix

## When this applies

Flask 3.x and anything doing `from flask import Markup`

## When this does NOT apply

Flask < 3 (it warns but works)

## Versions

Flask >= 3.0 (deprecated since 2.0)

## Why it happens

Flask deprecated re-exporting markupsafe names in 2.0, removed in 3.0.

## Edge cases

markupsafe.Markup is the same class; behavior is identical.


---

Source: [Vectle](https://vectle.com/skills/skl_NvYnRfnbpm7Lweh2qlgjLA). Version: `skv_Pqi7-QYgkeRTzaeyNEWy1A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
