---
name: "importerror-cannot-import-name-cached-2b55e1b684deb035"
description: "Fixes ImportError: cannot import name 'cached_path' from 'transformers.file_utils' Use when importing a transformers-based library fails on `from transformers.file_utils import cached_path` Not for: you import cached_path in your own code (just import it from huggingface_hub instead)"
metadata:
  skill_id: "skl_vpP05teT0hQg8gmAgULbNg"
  title: "ImportError: cannot import name 'cached_path' from 'transformers.file_utils'"
  version: "skv_wjPIzdYKmkykNeY1GKYX7g"
  updated: "2026-10-03T04:35:51.127845+00:00"
  canonical_url: "https://vectle.com/skills/skl_vpP05teT0hQg8gmAgULbNg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pandora-intelligence/classy-classification/issues/24\"]"
---

# How to fix ImportError: cannot import name 'cached_path' from 'transformers.file_utils'

A library you use (txtai, classy-classification, etc.) imports `cached_path` from its old home and your transformers is too new. Upgrade that library; if it has no fixed release, pin `transformers<=4.21.3`. `cached_path` was removed from transformers.file_utils (it lives in huggingface_hub now) in late 2022.

## The exact error

```text
ImportError: cannot import name 'cached_path' from 'transformers.file_utils'
```

## Fix it

1. Read the traceback to find the importing library (the frame above transformers).
   Expected: e.g. txtai, classy_classification

2. Upgrade it: `pip install -U [library]`.
   Expected: the new release imports from the new location

3. If no fixed release exists: `pip install "transformers<=4.21.3"`.
   Expected: import works again

## When this applies

importing a transformers-based library fails on `from transformers.file_utils import cached_path`

## When this does NOT apply

you import cached_path in your own code (just import it from huggingface_hub instead)

## Versions

transformers >= 4.22 with libs importing the old path

## Why it happens

transformers removed file_utils.cached_path; the canonical home is now huggingface_hub.

## Edge cases

Pinning transformers back is temporary; the library will break again on other new-transformers changes.


---

Source: [Vectle](https://vectle.com/skills/skl_vpP05teT0hQg8gmAgULbNg). Version: `skv_wjPIzdYKmkykNeY1GKYX7g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
