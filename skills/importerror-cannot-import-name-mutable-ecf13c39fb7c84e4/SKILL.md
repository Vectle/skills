---
name: "importerror-cannot-import-name-mutable-ecf13c39fb7c84e4"
description: "Fixes ImportError: cannot import name 'MutableMapping' from 'collections' Use when Python 3.10+ and `from collections import [ABC]` Not for: Python < 3.10 (it works there, with a deprecation warning)"
metadata:
  skill_id: "skl_qNftJLkL2e2uUBlVNZ_BhQ"
  title: "ImportError: cannot import name 'MutableMapping' from 'collections'"
  version: "skv_17gDZjDXyV2n6hvTQRzzfw"
  updated: "2026-10-03T04:52:29.66484+00:00"
  canonical_url: "https://vectle.com/skills/skl_qNftJLkL2e2uUBlVNZ_BhQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'MutableMapping' from 'collections'

Python 3.10 removed the abstract base classes from the top-level `collections` module. Change `from collections import MutableMapping` to `from collections.abc import MutableMapping`. Same for Iterable, Mapping, Sequence, Callable. If it is a library doing this, upgrade the library; `collections.abc` has been the right home since Python 3.3.

## The exact error

```text
ImportError: cannot import name 'MutableMapping' from 'collections'
```

## Fix it

1. Find it: `grep -rn "from collections import" --include=*.py .`.
   Expected: the offending lines

2. Change to `from collections.abc import MutableMapping` (etc.).
   Expected: works on 3.10+ and all the way back to 3.3

3. Library-owned: upgrade the library.
   Expected: upstream fixed long ago

## When this applies

Python 3.10+ and `from collections import [ABC]`

## When this does NOT apply

Python < 3.10 (it works there, with a deprecation warning)

## Versions

Python >= 3.10

## Why it happens

The ABCs lived in collections.abc since 3.3; the 3.10 cleanup removed the aliases.

## Edge cases

collections.abc has existed since 3.3, so the fix is back-compatible; no version guard needed.


---

Source: [Vectle](https://vectle.com/skills/skl_qNftJLkL2e2uUBlVNZ_BhQ). Version: `skv_17gDZjDXyV2n6hvTQRzzfw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
