---
name: "importerror-cannot-import-name-contain-d97aca62f4b15db8"
description: "Fixes ImportError: cannot import name 'container_abcs' from 'torch._six' Use when the traceback shows `from torch._six import container_abcs` failing on torch 1.9+ Not for: torch itself fails to import (DLL/shared-library errors) - that is an install problem, not this"
metadata:
  skill_id: "skl_fjo3IMXmKjSS3P8K-aUcyA"
  title: "ImportError: cannot import name 'container_abcs' from 'torch._six'"
  version: "skv_mbsR3CmSEMcPJqKNuEU0xw"
  updated: "2026-10-03T04:32:16.14626+00:00"
  canonical_url: "https://vectle.com/skills/skl_fjo3IMXmKjSS3P8K-aUcyA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'container_abcs' from 'torch._six'

The library importing torch._six is too old for your torch. `torch._six.container_abcs` was removed in torch 1.9; the modern equivalent is `collections.abc`. Upgrade the offending package (apex, pytorch-lightning, mmcv), or patch its import to `import collections.abc as container_abcs`. Your torch is fine; the caller is stale.

## The exact error

```text
ImportError: cannot import name 'container_abcs' from 'torch._six'
```

## Fix it

1. Read the traceback: find which file does `from torch._six import container_abcs` (often apex/amp/_amp_state.py or pytorch_lightning).
   Expected: you have the stale file path

2. Preferred: upgrade the stale package (`pip install -U [package]`, or reinstall apex from current master).
   Expected: the import line is gone or fixed upstream

3. If you must patch: replace `from torch._six import container_abcs` with `import collections.abc as container_abcs` and reinstall that package.
   Expected: import works on torch>=1.9

## When this applies

the traceback shows `from torch._six import container_abcs` failing on torch 1.9+

## When this does NOT apply

torch itself fails to import (DLL/shared-library errors) - that is an install problem, not this

## Versions

torch >= 1.9 with old apex / pytorch-lightning / mmcv

## Why it happens

torch removed the private _six compat module in 1.9; downstream libs pinned to the old private API.

## Edge cases

Downgrading torch below 1.9 'fixes' it too, but breaks everything else modern; upgrade the caller instead.


---

Source: [Vectle](https://vectle.com/skills/skl_fjo3IMXmKjSS3P8K-aUcyA). Version: `skv_mbsR3CmSEMcPJqKNuEU0xw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
