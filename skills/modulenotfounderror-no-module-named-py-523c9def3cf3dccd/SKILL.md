---
name: "modulenotfounderror-no-module-named-py-523c9def3cf3dccd"
description: "Fixes ModuleNotFoundError: No module named 'pytest_xdist' by importing xdist, the real module name. Use when code guesses the import from the PyPI name. Not for a genuinely missing install."
metadata:
  skill_id: "skl_MgUKAFDQW86gsHnGTkeaTg"
  title: "ModuleNotFoundError: No module named 'pytest_xdist'"
  version: "skv_jCXNL_EsbL75OOXMcowcwg"
  updated: "2026-10-03T05:56:20.815589+00:00"
  canonical_url: "https://vectle.com/skills/skl_MgUKAFDQW86gsHnGTkeaTg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Import `xdist`, not `pytest_xdist`. The package is called `pytest-xdist` on PyPI but the importable module is just `xdist`. If you actually need the plugin, `pip install pytest-xdist` is the fix.

```text
ModuleNotFoundError: No module named 'pytest_xdist'
```

## Fix it

1. **Fix the import.** Change `import pytest_xdist` to `import xdist`.
   - Expected: the import succeeds (if pytest-xdist is installed).

2. **If it still fails**, install the package: `python -m pip install pytest-xdist`.
   - Expected: `Successfully installed pytest-xdist-...`.

## When this applies
- You guessed the module name from the PyPI package name.
- Code or docs you copied use the wrong import.

## When it does not apply
- If `import xdist` also fails, the package is genuinely not installed.

## Tool compatibility
pytest-xdist 2.x/3.x. The module has always been `xdist`.

## Why it happens
PyPI package names and import names often differ. The `pytest-` prefix is a naming convention for plugins; the module drops it.

## Edge cases
- Same trap as `pytest-cov` (module `pytest_cov`, which keeps the prefix) versus `pytest-xdist` (module `xdist`, which drops it). Check each plugin's docs.


---

Source: [Vectle](https://vectle.com/skills/skl_MgUKAFDQW86gsHnGTkeaTg). Version: `skv_jCXNL_EsbL75OOXMcowcwg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
