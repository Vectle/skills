---
name: "importerror-cannot-import-name-ugettex-ea348323f6d9c7c7"
description: "Fixes `ImportError: cannot import name 'ugettext' from 'django.utils.translation'` in django. Use when upgrading to Django 4.0+ and the traceback names ugettext, ugettext_lazy, or ungettext from django.utils.translation. Not for missing .po/.mo translation files, untranslated strings, or LocaleMiddleware misconfiguration."
metadata:
  skill_id: "skl_oXFEo1CD-EiIts44v1_t2A"
  title: "ImportError: cannot import name 'ugettext' from 'django.utils.translation'"
  version: "skv_LrMHnjLz3uEEgXzt6KI3Cg"
  updated: "2026-10-03T05:55:16.573139+00:00"
  canonical_url: "https://vectle.com/skills/skl_oXFEo1CD-EiIts44v1_t2A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/etianen/django-reversion/issues/907\"]"
---

# ImportError: cannot import name 'ugettext' from 'django.utils.translation'

## TL;DR
ugettext was removed from Django in 4.0 (use gettext instead). Change from django.utils.translation import ugettext to from django.utils.translation import gettext. If the import is inside django-reversion or another package, upgrade that package past the version that fixed it.

## The error
```text
ImportError: cannot import name 'ugettext' from 'django.utils.translation'
```

## Fix it
1. Search your code: grep -rn "ugettext" --include=*.py . Look for both ugettext and ugettext_lazy.
   Expected: You see every file still using the old aliases.
2. Swap the aliases: ugettext becomes gettext, ugettext_lazy becomes gettext_lazy, ungettext becomes ngettext. The call signatures are identical.
   Expected: Imports succeed and translations behave exactly as before.
3. If the traceback leads into site-packages, upgrade the package. django-reversion fixed this in 4.0.0; most maintained packages have equivalent fixes.
   Expected: pip show [package] reports a version whose changelog mentions Django 4 support.
4. Run python manage.py check and your test suite to catch any remaining old alias in a corner of the codebase.
   Expected: No ImportError anywhere and tests pass.

## When to use this
Use when upgrading to Django 4.0+ and the traceback names ugettext, ugettext_lazy, or ungettext from django.utils.translation.

## When NOT to use this
Not for missing .po/.mo translation files, untranslated strings, or LocaleMiddleware misconfiguration.

## Version notes
ugettext aliases deprecated in Django 3.0, removed in 4.0. Code using them needs Django < 4.0 or the gettext rename.

## Why it happens
Django dropped the u-prefixed translation aliases in 4.0 after a long deprecation. Anything still importing them, your code or a stale dependency, fails at import time on Django 4+.

## Edge cases
Third-party packages are the usual culprit; pinning Django below 4.0 only postpones the rename, which is mechanical and safe.


---

Source: [Vectle](https://vectle.com/skills/skl_oXFEo1CD-EiIts44v1_t2A). Version: `skv_LrMHnjLz3uEEgXzt6KI3Cg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
