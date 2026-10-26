---
name: "modulenotfounderror-no-module-named-so-4659d367e31620d2"
description: "Fixes ModuleNotFoundError: No module named 'sortedcontainers' by installing hypothesis's missing dependency. Use when hypothesis is present but its import chain breaks. Not for a missing hypothesis install."
metadata:
  skill_id: "skl_kvPZlC4nOmhADJgbw8wNeQ"
  title: "ModuleNotFoundError: No module named 'sortedcontainers'"
  version: "skv_dQhbsmJ7cHmPAA7UxS_fQQ"
  updated: "2026-10-03T05:59:48.406694+00:00"
  canonical_url: "https://vectle.com/skills/skl_kvPZlC4nOmhADJgbw8wNeQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://pypi.org/project/hypothesis/\"]"
---

## TL;DR
Run `python -m pip install sortedcontainers`, or reinstall hypothesis with dependencies: `python -m pip install --force-reinstall hypothesis`. Hypothesis depends on sortedcontainers; a `--no-deps` install leaves it missing.

```text
ModuleNotFoundError: No module named 'sortedcontainers'
```

## Fix it

1. **Install the missing dep.** Run `python -m pip install sortedcontainers`.
   - Expected: `Successfully installed sortedcontainers-...`.

2. **Verify.** Run `python -c "import hypothesis; print('ok')"`.
   - Expected: prints `ok` with no traceback.

## When this applies
- hypothesis is installed but importing it fails on sortedcontainers.
- You installed with `--no-deps` or a lockfile dropped transitive deps.

## When it does not apply
- If hypothesis itself is missing, install hypothesis first.

## Tool compatibility
hypothesis 6.x requires sortedcontainers. Python 3.8+.

## Why it happens
sortedcontainers is a hard dependency of hypothesis (used by some strategies). Skipping dependency resolution breaks the import chain.

## Edge cases
- If you vendor dependencies, include both attrs and sortedcontainers alongside hypothesis.


---

Source: [Vectle](https://vectle.com/skills/skl_kvPZlC4nOmhADJgbw8wNeQ). Version: `skv_dQhbsmJ7cHmPAA7UxS_fQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
