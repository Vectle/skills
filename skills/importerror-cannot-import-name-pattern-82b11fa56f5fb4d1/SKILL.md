---
name: "importerror-cannot-import-name-pattern-82b11fa56f5fb4d1"
description: "Fixes `ImportError: cannot import name 'patterns' from 'django.conf.urls'` in django. Use when the traceback points at django.conf.urls and names patterns, usually right after a Django upgrade. Not for 404s, reversed-URL NoReverseMatch errors, or 'No module named django' (that is a missing install)."
metadata:
  skill_id: "skl_6bBqrZtOXww7wyFPG_Jwpw"
  title: "ImportError: cannot import name 'patterns' from 'django.conf.urls'"
  version: "skv_cJ_eSaZEiczdmtbDVWfjmQ"
  updated: "2026-10-03T05:54:04.005682+00:00"
  canonical_url: "https://vectle.com/skills/skl_6bBqrZtOXww7wyFPG_Jwpw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ImportError: cannot import name 'patterns' from 'django.conf.urls'

## TL;DR
Your code (or a dependency) still imports patterns from django.conf.urls, which Django removed in 1.10. Replace patterns('', ...) with a plain Python list of url() entries. If the import lives in a third-party package, upgrade that package to a version that supports your Django.

## The error
```text
ImportError: cannot import name 'patterns' from 'django.conf.urls'
```

## Fix it
1. Find every import of patterns: run grep -rn "from django.conf.urls import" --include=*.py . and note each file that pulls in patterns.
   Expected: You get a short list of files, usually urls.py files and maybe an old third-party package.
2. In your own code, replace the old call: patterns('', url(r'^$', view)) becomes a plain list [url(r'^$', view)]. The first string argument (the prefix) is simply dropped.
   Expected: urls.py imports cleanly and python manage.py check runs without the ImportError.
3. If the import is inside site-packages (a dependency), upgrade it: pip install -U [package]. Waliki, for example, fixed this in a later release.
   Expected: The dependency imports fine against your Django version.
4. As a last resort for an unmaintained package, pin Django below 1.10, but plan the migration since that Django is long out of support.
   Expected: App boots, with a note to revisit the pin.

## When to use this
Use when the traceback points at django.conf.urls and names patterns, usually right after a Django upgrade.

## When NOT to use this
Not for 404s, reversed-URL NoReverseMatch errors, or 'No module named django' (that is a missing install).

## Version notes
patterns() existed up to Django 1.8, deprecated in 1.8, removed in 1.10. Any code importing it needs Django < 1.10 or a rewrite.

## Why it happens
Django 1.10 deleted the patterns() helper along with the old string-view-prefix style. Old tutorials and old packages still import it, so upgrading Django past 1.9 breaks them at import time.

## Edge cases
Some packages import patterns conditionally; a grep that finds nothing in your code means the culprit is a dependency, check pip freeze and the full traceback.


---

Source: [Vectle](https://vectle.com/skills/skl_6bBqrZtOXww7wyFPG_Jwpw). Version: `skv_cJ_eSaZEiczdmtbDVWfjmQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
