---
name: "importerror-cannot-import-name-user-fr-6f5360e0e1806133"
description: "Fixes ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular import) Use when the error says 'partially initialized module' and 'most likely due to a circular import' Not for: the module truly lacks the name (typo) - then it is a plain ImportError"
metadata:
  skill_id: "skl_8aX2B_QLd0YvTLmzquQ-gw"
  title: "ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular"
  version: "skv_4Evx0cb7GN_CCB-1fj5sNA"
  updated: "2026-10-03T04:54:00.503987+00:00"
  canonical_url: "https://vectle.com/skills/skl_8aX2B_QLd0YvTLmzquQ-gw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular import)

Two modules import each other at the top level, so one of them is not finished when the other asks for a name. Break the cycle: move the shared name into a third module both import, or move one import inside the function that uses it, or `import models` and use `models.User` (attribute lookup happens at call time, after init). Restructuring beats the local-import band-aid.

## The exact error

```text
ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular import)
```

## Fix it

1. Map the cycle: read the traceback's import chain (a imports b imports a).
   Expected: you see the loop

2. Best: extract the shared class/function into a third module both import.
   Expected: no cycle, imports clean

3. Quick: move one import inside the function using it, or switch to `import models` + `models.User`.
   Expected: works; revisit the structure later

## When this applies

the error says 'partially initialized module' and 'most likely due to a circular import'

## When this does NOT apply

the module truly lacks the name (typo) - then it is a plain ImportError

## Versions

any Python 3

## Why it happens

Python executes module top-level code on first import; a cycle means someone reads names from a half-executed module.

## Edge cases

TYPE_CHECKING imports dodge runtime cycles for annotations; `import x` plus attribute access is the idiomatic runtime dodge.


---

Source: [Vectle](https://vectle.com/skills/skl_8aX2B_QLd0YvTLmzquQ-gw). Version: `skv_4Evx0cb7GN_CCB-1fj5sNA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
