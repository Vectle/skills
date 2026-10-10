---
name: "importerror-cannot-import-name-bool-fr-2c26618763c0e1bf"
description: "Fixes ImportError: cannot import name 'bool' from 'numpy' Use when the traceback shows `from numpy import bool` (or int, float, complex, object, unicode, str) and you run numpy 1.24 or newer Not for: the error is `ModuleNotFoundError: No module named 'numpy'` (numpy is not installed) or a binary/ABI mismatch error"
metadata:
  skill_id: "skl_I2H8wX2kW66ZVbdC_uw-9g"
  title: "ImportError: cannot import name 'bool' from 'numpy'"
  version: "skv_92ythR1ylA_tJhNFZl5qBw"
  updated: "2026-10-03T04:27:43.638473+00:00"
  canonical_url: "https://vectle.com/skills/skl_I2H8wX2kW66ZVbdC_uw-9g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'bool' from 'numpy'

Stop importing the alias. In your own code replace `from numpy import bool` with the builtin `bool` (or `np.bool_` if you need the numpy scalar type). If the error comes from a library you do not own (chumpy is the classic carrier), upgrade that library, or pin `numpy<1.24` as a stopgap. numpy 1.24 removed the old aliases np.bool, np.int, np.float and friends for good.

## The exact error

```text
ImportError: cannot import name 'bool' from 'numpy'
```

## Fix it

1. Find the bad import: `grep -rn "from numpy import" --include=*.py .` and look for bool, int, float, complex, object, unicode, str.
   Expected: you see the exact line raising the error

2. In your own code, swap the alias for the builtin: `from numpy import bool` goes away, just use `bool`. Only keep numpy's `np.bool_` if you truly need the numpy scalar.
   Expected: import succeeds on numpy>=1.24

3. If the traceback points inside a third-party package (chumpy is the classic), upgrade that package; if no fixed release exists, pin `numpy<1.24` in your requirements.
   Expected: pip shows numpy 1.23.x and the import works

## When this applies

the traceback shows `from numpy import bool` (or int, float, complex, object, unicode, str) and you run numpy 1.24 or newer

## When this does NOT apply

the error is `ModuleNotFoundError: No module named 'numpy'` (numpy is not installed) or a binary/ABI mismatch error

## Versions

numpy >= 1.24, Python 3.8+

## Why it happens

numpy deprecated these aliases in 1.20 and removed them in 1.24. Old code and old libraries still import them.

## Edge cases

np.bool_ still exists and is fine to use. Pinning numpy<1.24 is a band-aid; the real fix is updating the importing code.


---

Source: [Vectle](https://vectle.com/skills/skl_I2H8wX2kW66ZVbdC_uw-9g). Version: `skv_92ythR1ylA_tJhNFZl5qBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
