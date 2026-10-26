---
name: "modulenotfounderror-no-module-named-py-0007975a8f40ea6f"
description: "Fixes ModuleNotFoundError: No module named 'pytest_cov' by installing the pytest-cov plugin. Use when --cov flags fail because the plugin is missing. Not for coverage/pytest-cov version mismatch errors."
metadata:
  skill_id: "skl_tfHYerRCN3eomtWMv0DiPg"
  title: "ModuleNotFoundError: No module named 'pytest_cov'"
  version: "skv_D8-JdWQoFp3TSgkwnTVtmg"
  updated: "2026-10-03T05:34:31.657126+00:00"
  canonical_url: "https://vectle.com/skills/skl_tfHYerRCN3eomtWMv0DiPg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://pypi.org/project/pytest-cov/\"]"
---

## TL;DR
Run `python -m pip install pytest-cov`. The import name is `pytest_cov` (underscore) while the package is `pytest-cov` (dash). This error means the plugin is not installed in the environment running pytest.

```text
ModuleNotFoundError: No module named 'pytest_cov'
```

## Fix it

1. **Install the plugin.** Run `python -m pip install pytest-cov`.
   - Expected: `Successfully installed pytest-cov-...`.

2. **Verify it loads.** Run `pytest --version` and look for the `cov` plugin in the plugins list, or run `pytest --cov --collect-only -q`.
   - Expected: no ModuleNotFoundError; coverage options are accepted.

## When this applies
- You use `--cov` flags but never installed the plugin in this environment.
- CI installs pytest but the coverage step assumes pytest-cov is present.

## When it does not apply
- If `--cov` is accepted but coverage import errors mention `coverage.results` or `coverage.report`, that is a version mismatch, not a missing install.

## Tool compatibility
pytest-cov 4.x/5.x/6.x with pytest 7/8, Python 3.8+.

## Why it happens
`--cov` is not built into pytest; it comes from the pytest-cov plugin. Without the plugin installed, anything importing `pytest_cov` fails.

## Edge cases
- Remember the dash/underscore split: `pip install pytest-cov`, `import pytest_cov`.


---

Source: [Vectle](https://vectle.com/skills/skl_tfHYerRCN3eomtWMv0DiPg). Version: `skv_D8-JdWQoFp3TSgkwnTVtmg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
