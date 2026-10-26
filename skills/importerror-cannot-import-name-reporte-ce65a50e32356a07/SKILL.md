---
name: "importerror-cannot-import-name-reporte-ce65a50e32356a07"
description: "Fixes ImportError for Reporter from coverage.report by upgrading the importing tool or pinning coverage below 7. Use when an old IDE plugin or pytest-cov meets coverage 7. Not for display_covered errors."
metadata:
  skill_id: "skl_IjXyF3WQymeaf6pR5U86uA"
  title: "ImportError: cannot import name 'Reporter' from 'coverage.report'"
  version: "skv_ijNaiaq0j6OHL9Trk4ycsw"
  updated: "2026-10-03T05:38:07.8801+00:00"
  canonical_url: "https://vectle.com/skills/skl_IjXyF3WQymeaf6pR5U86uA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/opendebates/opendebates/issues/4\"]"
---

## TL;DR
Upgrade the tool that imports `Reporter` (often an old PyCharm pytest plugin or pinned pytest-cov), or align coverage to a version that still has it. `Reporter` was removed from `coverage.report` in coverage 7.

```text
ImportError: cannot import name 'Reporter' from 'coverage.report'
```

## Fix it

1. **Find who imports it.** The traceback shows the importer, for example PyCharm's `teamcity/pytest_plugin.py` doing `from coverage.report import Reporter`.
   - Expected: the file and line are named in the traceback.

2. **Upgrade the importer.** Update PyCharm, or run `python -m pip install -U pytest-cov coverage`.
   - Expected: the new importer no longer references the removed name.

3. **If you cannot upgrade the importer**, pin coverage to 6.x: `python -m pip install "coverage<7"`.
   - Expected: `Reporter` imports fine again.

## When this applies
- Old IDE plugins (PyCharm 2020-era) or old pytest-cov with coverage 7.
- The traceback literally says `from coverage.report import Reporter`.

## When it does not apply
- If the missing name is `display_covered` from `coverage.results`, that is the sibling issue with its own fix.

## Tool compatibility
coverage 7 removed `Reporter` from `coverage.report`. PyCharm 2020.x and old pytest-cov predate the removal.

## Why it happens
coverage 7 refactored its reporting internals and dropped the `Reporter` class. Anything importing it directly breaks on upgrade.

## Edge cases
- JetBrains fixed this in later PyCharm releases; updating the IDE is the cleanest fix (see PY-40980).


---

Source: [Vectle](https://vectle.com/skills/skl_IjXyF3WQymeaf6pR5U86uA). Version: `skv_ijNaiaq0j6OHL9Trk4ycsw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
