---
name: "importerror-cannot-import-name-six-fro-713e3f0f36fa439a"
description: "Fixes `ImportError: cannot import name 'six' from 'django.utils'` in django. Use when the traceback shows an import of six from django.utils, typically after moving to Django 3.0+. Not for 'No module named six' (just pip install six) or for six-related errors in non-Django projects."
metadata:
  skill_id: "skl_EVc4d5EExH1VCWeCA2b2Tw"
  title: "ImportError: cannot import name 'six' from 'django.utils'"
  version: "skv_McoDHOZmg847yw85ABFqrg"
  updated: "2026-10-03T05:56:33.269143+00:00"
  canonical_url: "https://vectle.com/skills/skl_EVc4d5EExH1VCWeCA2b2Tw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/django-haystack/django-haystack/issues/1732\"]"
---

# ImportError: cannot import name 'six' from 'django.utils'

## TL;DR
django.utils.six was removed in Django 3.0. If your own code does from django.utils import six, install the standalone six package and change it to import six. If a dependency does it, upgrade the dependency to a version that supports Django 3+.

## The error
```text
ImportError: cannot import name 'six' from 'django.utils'
```

## Fix it
1. Check where the import lives: grep -rEn "from django.utils import six|from django.utils.six" --include=*.py .
   Expected: You find the offending files, often in older third-party code.
2. For your own code: pip install six, then replace from django.utils.six import X with from six import X (or better, use the stdlib equivalent and drop six).
   Expected: The import works and behavior is unchanged.
3. For a dependency: upgrade it. django-haystack fixed this in 3.0; check the package changelog for Django 3 support.
   Expected: The package imports cleanly on your Django version.
4. Verify with python -c "import django; django.setup()" or python manage.py check.
   Expected: No ImportError on startup.

## When to use this
Use when the traceback shows an import of six from django.utils, typically after moving to Django 3.0+.

## When NOT to use this
Not for 'No module named six' (just pip install six) or for six-related errors in non-Django projects.

## Version notes
django.utils.six was vendored through Django 2.2 and removed in 3.0. Standalone six is a separate PyPI package.

## Why it happens
Django used to vendor the six compatibility library as django.utils.six and deleted it in 3.0. Code written against the vendored copy breaks unless it switches to the real six package or drops the compat shims.

## Edge cases
Many old snippets also do from django.utils.six.moves import ...; those need the same treatment, moves included.


---

Source: [Vectle](https://vectle.com/skills/skl_EVc4d5EExH1VCWeCA2b2Tw). Version: `skv_McoDHOZmg847yw85ABFqrg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
