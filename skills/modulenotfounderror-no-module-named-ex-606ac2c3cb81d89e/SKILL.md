---
name: "modulenotfounderror-no-module-named-ex-606ac2c3cb81d89e"
description: "Fixes ModuleNotFoundError: No module named 'execnet' by installing xdist's missing worker dependency. Use when pytest-xdist is present but execnet is not. Not for a missing xdist install."
metadata:
  skill_id: "skl_ix43RQSGTD0_SXo-Q2N2eQ"
  title: "ModuleNotFoundError: No module named 'execnet'"
  version: "skv_BQw4zQiICJkNrnXC9U0PHA"
  updated: "2026-10-03T05:41:01.180626+00:00"
  canonical_url: "https://vectle.com/skills/skl_ix43RQSGTD0_SXo-Q2N2eQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Run `python -m pip install execnet`, or reinstall pytest-xdist cleanly: `python -m pip install --force-reinstall pytest-xdist`. execnet is xdist's worker-communication dependency; a partial or `--no-deps` install leaves it missing.

```text
ModuleNotFoundError: No module named 'execnet'
```

## Fix it

1. **Install the missing dependency.** Run `python -m pip install execnet`.
   - Expected: `Successfully installed execnet-...`.

2. **Or reinstall the plugin with deps.** Run `python -m pip install --force-reinstall pytest-xdist`.
   - Expected: both pytest-xdist and execnet installed.

3. **Verify.** Run `pytest -n 2 --collect-only -q`.
   - Expected: collection succeeds, workers spawn.

## When this applies
- xdist is installed but workers fail immediately importing execnet.
- You installed with `--no-deps` or copied site-packages by hand.

## When it does not apply
- If xdist itself is missing, install pytest-xdist first.

## Tool compatibility
pytest-xdist 3.x requires execnet. Python 3.8+.

## Why it happens
pip normally installs dependencies automatically, but `--no-deps`, `--target` hacks, or vendored environments can skip execnet while keeping xdist.

## Edge cases
- Some minimal Docker images strip deps; add execnet explicitly to requirements.


---

Source: [Vectle](https://vectle.com/skills/skl_ix43RQSGTD0_SXo-Q2N2eQ). Version: `skv_BQw4zQiICJkNrnXC9U0PHA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
