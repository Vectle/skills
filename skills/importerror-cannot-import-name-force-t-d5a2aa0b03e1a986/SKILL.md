---
name: "importerror-cannot-import-name-force-t-d5a2aa0b03e1a986"
description: "Fixes ImportError: cannot import name 'force_text' from 'django.utils.encoding' Use when Django 4+ raises this from your code or a dependency Not for: Django < 4 (force_text still exists there, deprecated)"
metadata:
  skill_id: "skl_xJ6oqsh1_KwnncQQ2QWt7g"
  title: "ImportError: cannot import name 'force_text' from 'django.utils.encoding'"
  version: "skv_0f8pE5gcSExlLM-xj57yAg"
  updated: "2026-10-03T04:38:34.343927+00:00"
  canonical_url: "https://vectle.com/skills/skl_xJ6oqsh1_KwnncQQ2QWt7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'force_text' from 'django.utils.encoding'

`force_text` was renamed `force_str` in Django 3 and the old name removed in Django 4. In your code, replace `from django.utils.encoding import force_text` with `force_str`. If the traceback is inside a third-party package (graphene-django, django-elasticsearch-dsl, simplejwt...), upgrade that package instead of patching site-packages.

## The exact error

```text
ImportError: cannot import name 'force_text' from 'django.utils.encoding'
```

## Fix it

1. Find the culprit: `grep -rn "force_text" --include=*.py .` and check the traceback's file path.
   Expected: you know whether it is your code or a library

2. Your code: replace force_text with force_str (same behavior).
   Expected: import works on Django 4+

3. A library: `pip install -U [library]`.
   Expected: fixed upstream release resolves it

## When this applies

Django 4+ raises this from your code or a dependency

## When this does NOT apply

Django < 4 (force_text still exists there, deprecated)

## Versions

Django >= 4.0

## Why it happens

Django dropped the Python-2-era text/bytes naming; force_text -> force_str.

## Edge cases

smart_text -> smart_str and ugettext -> gettext were removed in the same cleanup; fix them together.


---

Source: [Vectle](https://vectle.com/skills/skl_xJ6oqsh1_KwnncQQ2QWt7g). Version: `skv_0f8pE5gcSExlLM-xj57yAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
