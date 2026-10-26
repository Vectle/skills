---
name: "importerror-c-extension-no-module-name-71eb7371357d2bc6"
description: "Fixes ImportError: C extension: No module named 'pandas._libs.tslibs.conversion' not built Use when `import pandas` raises the 'C extension ... not built' ImportError naming a pandas._libs module Not for: plain `No module named 'pandas'` or a missing optional dependency like openpyxl"
metadata:
  skill_id: "skl_9OVeWNoLo78Pb2-3NZRE-w"
  title: "ImportError: C extension: No module named 'pandas._libs.tslibs.conversion' not built"
  version: "skv_8XdmEOe5tUh3N17KUyi_tA"
  updated: "2026-10-03T04:30:06.322981+00:00"
  canonical_url: "https://vectle.com/skills/skl_9OVeWNoLo78Pb2-3NZRE-w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pandas-dev/pandas/issues/27867\"]"
---

# How to fix ImportError: C extension: No module named 'pandas._libs.tslibs.conversion' not built

You are importing pandas from a source checkout whose C extensions were never built. Either build them or just install a binary wheel with pip. Most people hitting this should do the pip reinstall: the error only appears when a source directory shadows a working install.

## The exact error

```text
ImportError: C extension: No module named 'pandas._libs.tslibs.conversion' not built
```

## Fix it

1. Check whether you are inside the pandas source dir: `pwd` and look for setup.py. If yes, cd out.
   Expected: you know whether the source tree is shadowing the install

2. Simplest fix: `python -m pip install --force-reinstall pandas`.
   Expected: `python -c "import pandas; print(pandas.__version__)"` works from any directory

3. If you actually develop pandas: build the extensions in place, then import again.
   Expected: the C extensions build and import succeeds

## When this applies

`import pandas` raises the 'C extension ... not built' ImportError naming a pandas._libs module

## When this does NOT apply

plain `No module named 'pandas'` or a missing optional dependency like openpyxl

## Versions

pandas built from source / dev installs, any version

## Why it happens

pandas ships compiled Cython extensions. A source checkout (or a copied pandas folder) without built extensions cannot import.

## Edge cases

Do not run your scripts from inside the pandas repo directory; the local pandas/ folder shadows site-packages.


---

Source: [Vectle](https://vectle.com/skills/skl_9OVeWNoLo78Pb2-3NZRE-w). Version: `skv_8XdmEOe5tUh3N17KUyi_tA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
