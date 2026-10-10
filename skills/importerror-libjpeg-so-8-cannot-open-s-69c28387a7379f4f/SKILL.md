---
name: "importerror-libjpeg-so-8-cannot-open-s-69c28387a7379f4f"
description: "Fixes ImportError: libjpeg.so.8: cannot open shared object file: No such file or directory Use when Pillow import or JPEG open fails on libjpeg.so.8 missing (WSL, Docker, minimal images) Not for: Pillow not installed at all"
metadata:
  skill_id: "skl_SM4KZ7Pdks56ilcGRhFcBg"
  title: "ImportError: libjpeg.so.8: cannot open shared object file: No such file or directory"
  version: "skv_wAQzkVE-ti2SzBmLNziVcA"
  updated: "2026-10-03T04:45:16.502932+00:00"
  canonical_url: "https://vectle.com/skills/skl_SM4KZ7Pdks56ilcGRhFcBg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: libjpeg.so.8: cannot open shared object file: No such file or directory

The system JPEG library Pillow was built against is missing. On Debian/Ubuntu: `sudo apt-get install libjpeg-turbo8` (or libjpeg8). Easiest robust fix: reinstall Pillow from a wheel so it bundles its own libs: `pip install --force-reinstall --no-cache-dir pillow`.

## The exact error

```text
ImportError: libjpeg.so.8: cannot open shared object file: No such file or directory
```

## Fix it

1. `sudo apt-get install libjpeg-turbo8` (Debian/Ubuntu) or the equivalent libjpeg package.
   Expected: libjpeg.so.8 exists on the system

2. Or reinstall Pillow as a wheel: `pip install --force-reinstall --no-cache-dir pillow`.
   Expected: Pillow bundles its own libs

3. Verify: open a JPEG with PIL and call .load() on it.
   Expected: image loads, prints ok

## When this applies

Pillow import or JPEG open fails on libjpeg.so.8 missing (WSL, Docker, minimal images)

## When this does NOT apply

Pillow not installed at all

## Versions

Linux, Pillow built from source / minimal envs

## Why it happens

Source-built Pillow links the system libjpeg; the runtime image lacks it.

## Edge cases

Alpine/musl needs the apk libjpeg-turbo package; prefer musl wheels when available.


---

Source: [Vectle](https://vectle.com/skills/skl_SM4KZ7Pdks56ilcGRhFcBg). Version: `skv_wAQzkVE-ti2SzBmLNziVcA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
