---
name: "modulenotfounderror-no-module-named-py-65673f8276a0cac7"
description: "Fixes ModuleNotFoundError: No module named '_pytest.scope' by upgrading pytest to 8.x, which introduced that internal module. Use when a pytest plugin imports _pytest.scope on an old pytest. Not for a missing pytest install."
metadata:
  skill_id: "skl_CzvQwcP-NYl4StKSx3xHpQ"
  title: "ModuleNotFoundError: No module named '_pytest.scope'"
  version: "skv_DPloeauYh1mhgev_oUWTBQ"
  updated: "2026-10-03T05:31:15.365106+00:00"
  canonical_url: "https://vectle.com/skills/skl_CzvQwcP-NYl4StKSx3xHpQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Upgrade pytest to 8.x: `python -m pip install -U pytest`. The `_pytest.scope` module was added in pytest 8.0, so any plugin or tool importing it (like newer anyio) breaks on pytest 7.x and older with this exact error.

```text
ModuleNotFoundError: No module named '_pytest.scope'
```

## Fix it

1. **Check your pytest version.** Run `pytest --version` or `python -m pip show pytest`.
   - Expected: you will see pytest 7.x or older.

2. **Upgrade pytest.** Run `python -m pip install -U pytest`.
   - Expected: `Successfully installed pytest-8.x.x`.

3. **Re-run your tests.** The importing plugin (often anyio's pytest plugin) should now load cleanly.
   - Expected: no ModuleNotFoundError, tests collect normally.

4. **If you cannot upgrade pytest**, pin the plugin to a version that supports your pytest. For anyio, that means staying on anyio 3.x with pytest 7.x.

## When this applies
- The traceback shows a plugin (anyio, or similar) doing `from _pytest.scope import ...` or `import _pytest.scope`.
- You recently upgraded a pytest plugin but not pytest itself.

## When it does not apply
- If the missing module is `pytest` itself (not `_pytest.scope`), pytest is simply not installed.
- If the error names a hook (like `pytest_namespace`), that is a plugin validation error, a different problem.

## Tool compatibility
pytest 8.0+ provides `_pytest.scope`. anyio 4.x requires it. Python 3.8+.

## Why it happens
`_pytest.scope` is an internal pytest module introduced in pytest 8.0. Plugins written against pytest 8 import it at load time. If your environment pins pytest 7.x (common in CI images or libraries with upper bounds), the import fails even though everything else works.

## Edge cases
- Some distributions pin pytest via constraints files; check `pip freeze | grep -i pytest` and any constraints files.
- If you must stay on pytest 7, downgrade the plugin instead: `pip install "anyio<4"`.


---

Source: [Vectle](https://vectle.com/skills/skl_CzvQwcP-NYl4StKSx3xHpQ). Version: `skv_DPloeauYh1mhgev_oUWTBQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
