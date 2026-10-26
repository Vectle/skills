---
name: "importerror-attempted-relative-import-be5fa1e82c521f5e"
description: "Fixes ImportError: attempted relative import with no known parent package Use when running a module file directly that contains `from .` / `from ..` imports Not for: absolute imports failing (that is ModuleNotFoundError, different fix)"
metadata:
  skill_id: "skl_rzXUzOPXS07jETxJbR7Chg"
  title: "ImportError: attempted relative import with no known parent package"
  version: "skv_kE_mArVlgohMaDQsB0AtkA"
  updated: "2026-10-03T04:53:21.65108+00:00"
  canonical_url: "https://vectle.com/skills/skl_rzXUzOPXS07jETxJbR7Chg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.pythonpool.com/importerror-attempted-relative-import-with-no-known-parent-package/\"]"
---

# How to fix ImportError: attempted relative import with no known parent package

You ran a file that uses relative imports (`from . import x`) directly as a script, so Python does not know its package. Run it as a module from the project root: `python -m package.module` instead of `python package/module.py`. Or convert the relative imports to absolute ones.

## The exact error

```text
ImportError: attempted relative import with no known parent package
```

## Fix it

1. From the project root (where the top package dir lives), run `python -m package.module`.
   Expected: relative imports resolve

2. Alternative: rewrite `from .helpers import f` as `from package.helpers import f`.
   Expected: works however it is launched

3. Check every package dir has an __init__.py (namespace packages aside).
   Expected: package structure recognized

## When this applies

running a module file directly that contains `from .` / `from ..` imports

## When this does NOT apply

absolute imports failing (that is ModuleNotFoundError, different fix)

## Versions

any Python 3

## Why it happens

Relative imports need the module's package context; direct script execution leaves __package__ unset.

## Edge cases

`python -m` adds the CWD to sys.path; running from the wrong directory still fails.


---

Source: [Vectle](https://vectle.com/skills/skl_rzXUzOPXS07jETxJbR7Chg). Version: `skv_kE_mArVlgohMaDQsB0AtkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
