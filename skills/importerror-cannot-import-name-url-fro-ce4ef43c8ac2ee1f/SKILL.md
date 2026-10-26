---
name: "importerror-cannot-import-name-url-fro-ce4ef43c8ac2ee1f"
description: "Fixes ImportError: cannot import name 'url' from 'django.conf.urls' Use when upgrading to Django 4+ and `from django.conf.urls import url` blows up Not for: you are on Django < 4 (it still works there, just deprecated) or the error is about a different name"
metadata:
  skill_id: "skl_cZlALCv45cT3HIhAedBgXg"
  title: "ImportError: cannot import name 'url' from 'django.conf.urls'"
  version: "skv_yYEbLQtm4ejx-OQpBUda-A"
  updated: "2026-10-03T04:37:44.90362+00:00"
  canonical_url: "https://vectle.com/skills/skl_cZlALCv45cT3HIhAedBgXg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/arsh14jain/blog/issues/7\"]"
---

# How to fix ImportError: cannot import name 'url' from 'django.conf.urls'

Django 4 removed `django.conf.urls.url()`. Replace it: for regex patterns use `from django.urls import re_path` and swap `url(` for `re_path(`; for simple paths use `path()`. A find-and-replace across your urls.py files does most projects in one pass.

## The exact error

```text
ImportError: cannot import name 'url' from 'django.conf.urls'
```

## Fix it

1. In urls.py change the import: `from django.conf.urls import url` -> `from django.urls import re_path` (or `path`).
   Expected: no more django.conf.urls import

2. Replace `url(` calls with `re_path(` (regex) or rewrite as `path(` (simple routes).
   Expected: `python manage.py check` passes

3. Large project? `pip install django-upgrade` and run it: it rewrites these automatically.
   Expected: diff shows only url->re_path/path changes

## When this applies

upgrading to Django 4+ and `from django.conf.urls import url` blows up

## When this does NOT apply

you are on Django < 4 (it still works there, just deprecated) or the error is about a different name

## Versions

Django >= 4.0

## Why it happens

url() was deprecated since Django 3.1 and removed in 4.0; django.urls.path/re_path are the replacements.

## Edge cases

Third-party packages can trigger this too; upgrade them rather than downgrading Django.


---

Source: [Vectle](https://vectle.com/skills/skl_cZlALCv45cT3HIhAedBgXg). Version: `skv_yYEbLQtm4ejx-OQpBUda-A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
