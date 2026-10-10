---
name: "pluggy-manager-pluginvalidationerror-u-3b6c02ba33128e35"
description: "Fixes pluggy PluginValidationError for unknown hook 'pytest_namespace' by upgrading the stale plugin or replacing the removed hook with pytest_configure. Use when an old pytest plugin breaks on pytest 4.1+. Not for missing installs."
metadata:
  skill_id: "skl_aHWv5iA7VHRopdBHLPLWNw"
  title: "pluggy.manager.PluginValidationError: unknown hook 'pytest_namespace' in plugin"
  version: "skv_aqcgyTOgIZFdpa1Qa6-W_g"
  updated: "2026-10-03T05:33:01.527504+00:00"
  canonical_url: "https://vectle.com/skills/skl_aHWv5iA7VHRopdBHLPLWNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Update the offending plugin to a version that supports your pytest, or downgrade pytest below 4.1. The `pytest_namespace` hook was removed in pytest 4.0/4.1, so any old plugin or conftest.py still defining it fails validation at startup.

```text
pluggy.manager.PluginValidationError: unknown hook 'pytest_namespace' in plugin <module '...' from '...'>
```

## Fix it

1. **Find the culprit.** The error names the plugin module (for example `allure.pytest_plugin`, `pytest_quickcheck.plugin`, or your own `conftest.py`).
   - Expected: the module path in the error message points at the file defining `pytest_namespace`.

2. **Upgrade the plugin.** Run `python -m pip install -U [plugin-name]`.
   - Expected: the new version no longer implements `pytest_namespace`.

3. **If it is your own conftest.py**, replace the hook:
   ```python
   # before
   def pytest_namespace():
       return {"my_thing": my_thing}
   # after
   def pytest_configure(config):
       import pytest
       pytest.my_thing = my_thing
   ```
   - Expected: `pytest --collect-only` runs without the PluginValidationError.

4. **Last resort:** pin `pytest<4.1`. This keeps the old hook working but forgoes years of fixes.

## When this applies
- You upgraded pytest to 4.1+ and an old plugin (allure, pytest-quickcheck, nose2pytest, old conftest) now fails at startup.
- The error message names `pytest_namespace` specifically.

## When it does not apply
- If the unknown hook is a different name, the same logic applies but the plugin at fault differs.
- If pytest itself is not installed, that is a different error.

## Tool compatibility
pytest 4.1+ removed `pytest_namespace` (deprecated since 3.7). Affects plugins written for pytest 3.x.

## Why it happens
pluggy validates every hook implementation against the hook specifications pytest registers. `pytest_namespace` was deprecated in pytest 3.7 and removed in 4.1, so pluggy rejects any plugin still implementing it with `unknown hook`.

## Edge cases
- `-p no:[plugin]` on the command line can disable the offending plugin to confirm the diagnosis.
- Some plugins fixed this in a minor release; check the plugin changelog before rewriting anything.


---

Source: [Vectle](https://vectle.com/skills/skl_aHWv5iA7VHRopdBHLPLWNw). Version: `skv_aqcgyTOgIZFdpa1Qa6-W_g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
