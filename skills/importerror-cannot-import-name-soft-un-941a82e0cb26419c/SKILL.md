---
name: "importerror-cannot-import-name-soft-un-941a82e0cb26419c"
description: "Fixes ImportError: cannot import name 'soft_unicode' from 'markupsafe' Use when the traceback shows an old jinja2/flask importing soft_unicode from a new markupsafe Not for: your own code imports soft_unicode (just use soft_str)"
metadata:
  skill_id: "skl_AYbOCiv8OPzOnObv3suWgw"
  title: "ImportError: cannot import name 'soft_unicode' from 'markupsafe'"
  version: "skv_MEU-4nar5Wk16uY0dX_4xQ"
  updated: "2026-10-03T04:39:15.401737+00:00"
  canonical_url: "https://vectle.com/skills/skl_AYbOCiv8OPzOnObv3suWgw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/koheron/koheron-sdk/issues/648\"]"
---

# How to fix ImportError: cannot import name 'soft_unicode' from 'markupsafe'

markupsafe 2.1 removed `soft_unicode` (renamed `soft_str`), but your jinja2/flask is old enough to still import the old name. Upgrade the stack: `pip install -U flask jinja2 markupsafe`. Quick unblock: `pip install markupsafe==2.0.1`, which still has soft_unicode.

## The exact error

```text
ImportError: cannot import name 'soft_unicode' from 'markupsafe'
```

## Fix it

1. `pip install -U flask jinja2 markupsafe`
   Expected: modern mutually-compatible versions

2. Retry the import.
   Expected: works

3. Can not upgrade the app? `pip install markupsafe==2.0.1` as a stopgap.
   Expected: old jinja2 finds soft_unicode again

## When this applies

the traceback shows an old jinja2/flask importing soft_unicode from a new markupsafe

## When this does NOT apply

your own code imports soft_unicode (just use soft_str)

## Versions

markupsafe >= 2.1 with jinja2 < 3.0 / flask < 2.0

## Why it happens

markupsafe 2.1 did the py2-cleanup rename; old jinja2 (<3.0) still asked for the old name.

## Edge cases

aws-sam-cli below 1.38.1 is another classic trigger; upgrade sam instead.


---

Source: [Vectle](https://vectle.com/skills/skl_AYbOCiv8OPzOnObv3suWgw). Version: `skv_MEU-4nar5Wk16uY0dX_4xQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
