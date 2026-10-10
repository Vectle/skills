---
name: "modulenotfounderror-no-module-named-xd-20fc3dc214eee06e"
description: "Fixes ModuleNotFoundError: No module named 'xdist' by installing pytest-xdist. Use when -n flags are unrecognized or xdist cannot be imported. Not for worker import errors of your own code."
metadata:
  skill_id: "skl__iNEt2v-lEir9xAvmS-Rog"
  title: "ModuleNotFoundError: No module named 'xdist'"
  version: "skv_Co8jDNL4jH_-ZoSNBuCrBA"
  updated: "2026-10-03T05:39:55.875272+00:00"
  canonical_url: "https://vectle.com/skills/skl__iNEt2v-lEir9xAvmS-Rog"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Run `python -m pip install pytest-xdist`. The `-n` flag only exists when the xdist plugin is installed; without it, pytest does not recognize `-n auto` at all.

```text
ModuleNotFoundError: No module named 'xdist'
```

## Fix it

1. **Install the plugin.** Run `python -m pip install pytest-xdist`.
   - Expected: `Successfully installed pytest-xdist-... execnet-...`.

2. **Verify.** Run `pytest --version` and confirm `xdist` appears in the plugins list.
   - Expected: `plugins: xdist-3.x.x`.

3. **Use it.** Run `pytest -n auto`.
   - Expected: tests distribute across workers instead of `unrecognized arguments: -n`.

## When this applies
- `pytest -n auto` says `unrecognized arguments`, or something imports `xdist` directly and fails.
- A fresh environment where you installed pytest but forgot xdist.

## When it does not apply
- If `-n` is accepted but workers crash importing your own modules, that is a PYTHONPATH issue in workers, not a missing xdist.

## Tool compatibility
pytest-xdist 3.x with pytest 7/8, Python 3.8+.

## Why it happens
Parallel execution is a plugin, not core pytest. The package name is `pytest-xdist` but the import name is `xdist`.

## Edge cases
- In CI, make sure the test step installs the same requirements file that includes pytest-xdist.


---

Source: [Vectle](https://vectle.com/skills/skl__iNEt2v-lEir9xAvmS-Rog). Version: `skv_Co8jDNL4jH_-ZoSNBuCrBA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
