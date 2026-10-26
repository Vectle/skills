---
name: "importerror-cannot-import-name-pillow-55327ab50392712c"
description: "Fixes ImportError: cannot import name 'PILLOW_VERSION' from 'PIL' Use when Pillow 7+ and something imports PILLOW_VERSION Not for: `No module named 'PIL'` (Pillow is not installed at all)"
metadata:
  skill_id: "skl_t1r60q95WPvFaFadRtvmNw"
  title: "ImportError: cannot import name 'PILLOW_VERSION' from 'PIL'"
  version: "skv_2Aj3AhkO6odjMr5JrRsIHg"
  updated: "2026-10-03T04:44:27.35383+00:00"
  canonical_url: "https://vectle.com/skills/skl_t1r60q95WPvFaFadRtvmNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/gregunz/invertransforms/issues/3\"]"
---

# How to fix ImportError: cannot import name 'PILLOW_VERSION' from 'PIL'

`PILLOW_VERSION` was removed from Pillow. In your own code replace `from PIL import PILLOW_VERSION` with `from PIL import __version__`. If the traceback is inside a library (old torchvision, invertransforms, etc.), upgrade that library; downgrading Pillow is only a stopgap.

## The exact error

```text
ImportError: cannot import name 'PILLOW_VERSION' from 'PIL'
```

## Fix it

1. Your code: `from PIL import PILLOW_VERSION` -> `from PIL import __version__`.
   Expected: import works on Pillow 10+

2. A library: `pip install -U [library]`.
   Expected: upstream fixed the import

3. Stopgap only: `pip install "pillow<7"`.
   Expected: old Pillow has the constant (not recommended)

## When this applies

Pillow 7+ and something imports PILLOW_VERSION

## When this does NOT apply

`No module named 'PIL'` (Pillow is not installed at all)

## Versions

Pillow >= 7 (removed), >= 10 (fully gone)

## Why it happens

Pillow deprecated the constant in 5.2, removed it in 7.0.

## Edge cases

torchvision below 0.5 is the most common carrier of this; upgrade torchvision with torch.


---

Source: [Vectle](https://vectle.com/skills/skl_t1r60q95WPvFaFadRtvmNw). Version: `skv_2Aj3AhkO6odjMr5JrRsIHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
