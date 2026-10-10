---
name: "modulenotfounderror-no-module-named-at-61b113b02ed0e9b3"
description: "Fixes ModuleNotFoundError: No module named 'attrs' by installing hypothesis's missing dependency. Use when hypothesis's import chain breaks on attrs. Not for a missing hypothesis install."
metadata:
  skill_id: "skl_ghVQi-evn3ZFORcdjvbMAg"
  title: "ModuleNotFoundError: No module named 'attrs'"
  version: "skv_P4k3zKe-vIuW9IfKTWiv5A"
  updated: "2026-10-03T06:04:29.393824+00:00"
  canonical_url: "https://vectle.com/skills/skl_ghVQi-evn3ZFORcdjvbMAg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Run `python -m pip install attrs`, or reinstall hypothesis with dependencies: `python -m pip install --force-reinstall hypothesis`. Hypothesis depends on attrs; skipping deps leaves it missing.

```text
ModuleNotFoundError: No module named 'attrs'
```

## Fix it

1. **Install the missing dep.** Run `python -m pip install attrs`.
   - Expected: `Successfully installed attrs-...`.

2. **Verify.** Run `python -c "import hypothesis; print('ok')"`.
   - Expected: prints `ok`.

## When this applies
- Importing hypothesis fails naming attrs.
- Minimal installs with `--no-deps`.

## When it does not apply
- If hypothesis itself is missing, install it first.

## Tool compatibility
hypothesis 6.x requires attrs. Python 3.8+.

## Why it happens
attrs is a hard dependency of hypothesis. Dependency-skipping installs break it.

## Edge cases
- Note the package is `attrs` (plural); the classic import is `import attr` or `import attrs`. Install the package name with pip.


---

Source: [Vectle](https://vectle.com/skills/skl_ghVQi-evn3ZFORcdjvbMAg). Version: `skv_P4k3zKe-vIuW9IfKTWiv5A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
