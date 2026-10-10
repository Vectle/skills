---
name: "importerror-numpy-core-multiarray-fail-ce21df4e649bb925"
description: "Fixes ImportError: numpy.core.multiarray failed to import Use when any `import numpy` (or import of a package that needs numpy, like cv2) dies with `numpy.core.multiarray failed to import` Not for: `No module named 'numpy'` (nothing installed) or a pure-Python `cannot import name` error"
metadata:
  skill_id: "skl_AXnKt59NAUHf1OABhWL_iw"
  title: "ImportError: numpy.core.multiarray failed to import"
  version: "skv_V7F8zhvbVIy5HgQn2itQug"
  updated: "2026-10-03T04:28:46.724123+00:00"
  canonical_url: "https://vectle.com/skills/skl_AXnKt59NAUHf1OABhWL_iw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: numpy.core.multiarray failed to import

Your numpy install is broken, not your code. First check which python and numpy you are actually running, then cleanly reinstall numpy (uninstall, then install, no cache). If you mix conda and pip, reinstall numpy from the same manager that owns the environment. This error means Python found numpy's Python files but its compiled C extension failed to load.

## The exact error

```text
ImportError: numpy.core.multiarray failed to import
```

## Fix it

1. Confirm the broken env: run `python -c "import sys; print(sys.executable)"` and `python -m pip show numpy`.
   Expected: both point at the same environment; note the numpy version

2. Clean reinstall: `python -m pip uninstall -y numpy` then `python -m pip install --no-cache-dir numpy`.
   Expected: `python -c "import numpy; print(numpy.__version__)"` prints a version with no error

3. If you use conda, use `conda install -c conda-forge numpy` (or force-reinstall) instead of mixing pip into a conda env.
   Expected: import numpy works and dependent packages (pandas, opencv) import too

## When this applies

any `import numpy` (or import of a package that needs numpy, like cv2) dies with `numpy.core.multiarray failed to import`

## When this does NOT apply

`No module named 'numpy'` (nothing installed) or a pure-Python `cannot import name` error

## Versions

any numpy, usually after upgrades or mixed pip/conda installs

## Why it happens

The compiled multiarray extension does not match the interpreter or is corrupted: partial upgrades, pip-vs-conda mixes, or copying site-packages between Pythons.

## Edge cases

If reinstall fails the same way, check for multiple numpy copies on sys.path (IDE virtualenv confusion) or a 32/64-bit mismatch.


---

Source: [Vectle](https://vectle.com/skills/skl_AXnKt59NAUHf1OABhWL_iw). Version: `skv_V7F8zhvbVIy5HgQn2itQug`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
