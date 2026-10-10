---
name: "modulenotfounderror-no-module-named-hy-20fd59cd936bda10"
description: "Fixes ModuleNotFoundError: No module named 'hypothesis' by installing the Hypothesis library. Use when property-based tests cannot import hypothesis at all. Not for strategy usage errors."
metadata:
  skill_id: "skl_yBZ_bz9CgshDiIvL9uM1DA"
  title: "ModuleNotFoundError: No module named 'hypothesis'"
  version: "skv_-iOkCg0YcfW87TOrkOWGxQ"
  updated: "2026-10-03T05:57:51.90115+00:00"
  canonical_url: "https://vectle.com/skills/skl_yBZ_bz9CgshDiIvL9uM1DA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Run `python -m pip install hypothesis`. This error means the Hypothesis property-testing library is not installed in the environment running your tests.

```text
ModuleNotFoundError: No module named 'hypothesis'
```

## Fix it

1. **Install it.** Run `python -m pip install hypothesis`.
   - Expected: `Successfully installed hypothesis-...`.

2. **Verify.** Run `python -c "import hypothesis; print(hypothesis.__version__)"`.
   - Expected: a version number prints.

## When this applies
- Tests use `@given` or hypothesis strategies but the env lacks the package.
- Fresh CI image or new virtualenv.

## When it does not apply
- If hypothesis imports but strategies fail, that is a usage error, not a missing install.

## Tool compatibility
hypothesis 6.x, Python 3.8+. `pip install hypothesis`.

## Why it happens
Hypothesis is a third-party package, not stdlib. It must be installed per environment.

## Edge cases
- The `.hypothesis` example database directory is created automatically; you do not need to create it.


---

Source: [Vectle](https://vectle.com/skills/skl_yBZ_bz9CgshDiIvL9uM1DA). Version: `skv_-iOkCg0YcfW87TOrkOWGxQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
