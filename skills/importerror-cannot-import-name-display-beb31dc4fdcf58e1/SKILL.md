---
name: "importerror-cannot-import-name-display-beb31dc4fdcf58e1"
description: "Fixes ImportError for display_covered from coverage.results by upgrading pytest-cov and coverage together. Use when old pytest-cov meets new coverage. Not for a missing pytest-cov install."
metadata:
  skill_id: "skl_po0ufpXdkJHxdtYDUSvxxQ"
  title: "ImportError: cannot import name 'display_covered' from 'coverage.results'"
  version: "skv_KlR9GvSJVDCUJ4ttk_n0Gg"
  updated: "2026-10-03T05:35:54.160708+00:00"
  canonical_url: "https://vectle.com/skills/skl_po0ufpXdkJHxdtYDUSvxxQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Align your coverage and pytest-cov versions: `python -m pip install -U pytest-cov coverage`. Old pytest-cov imports `display_covered` from `coverage.results`, which newer coverage versions removed.

```text
ImportError: cannot import name 'display_covered' from 'coverage.results'
```

## Fix it

1. **Check versions.** Run `python -m pip show pytest-cov coverage`.
   - Expected: you will see an old pytest-cov (for example 3.x/4.x) next to a new coverage (7.x).

2. **Upgrade both together.** Run `python -m pip install -U pytest-cov coverage`.
   - Expected: `Successfully installed pytest-cov-6.x coverage-7.x` (or current).

3. **Re-run.** The plugin import should succeed now.
   - Expected: `pytest --cov` starts without the ImportError.

## When this applies
- The traceback points at `pytest_cov/plugin.py` line doing `from coverage.results import display_covered`.
- You pinned one of the two packages and let the other float.

## When it does not apply
- If the error is about `coverage.report.Reporter`, that is a different removed name.
- If pytest-cov is not installed at all, install it first.

## Tool compatibility
pytest-cov 5+ with coverage 7.x. Python 3.8+.

## Why it happens
pytest-cov reaches into coverage's internals. When coverage refactors those internals (removing `display_covered`), old pytest-cov releases break. Upgrading pytest-cov gets the fixed import.

## Edge cases
- If you must pin coverage (for example `coverage==6.5.0`), pin a contemporary pytest-cov instead (4.x era).


---

Source: [Vectle](https://vectle.com/skills/skl_po0ufpXdkJHxdtYDUSvxxQ). Version: `skv_KlR9GvSJVDCUJ4ttk_n0Gg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
