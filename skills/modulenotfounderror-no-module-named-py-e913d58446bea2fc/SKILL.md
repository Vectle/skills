---
name: "modulenotfounderror-no-module-named-py-e913d58446bea2fc"
description: "Fixes ModuleNotFoundError: No module named 'pytest' by installing pytest into the exact Python interpreter running the code. Use when pytest is not found at all. Not for plugin load failures or version-conflict import errors."
metadata:
  skill_id: "skl_cz2qEhJZnZSmva9CCkhmnw"
  title: "ModuleNotFoundError: No module named 'pytest'"
  version: "skv_Ov2CTOcXMGFNkE6OJMvVRg"
  updated: "2026-10-03T05:29:19.173969+00:00"
  canonical_url: "https://vectle.com/skills/skl_cz2qEhJZnZSmva9CCkhmnw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
Run `python -m pip install pytest`, then verify with `pytest --version`. This error means pytest is not installed in the Python environment that is actually running your code, which is usually a different interpreter or virtualenv than the one you installed into.

```text
ModuleNotFoundError: No module named 'pytest'
```

## Fix it

1. **Confirm which Python is running.** Run `which python` (or `where python` on Windows) and `python --version`. Then run `python -m pip show pytest`. If pip says it is not installed, that is your answer.
   - Expected: `pip show pytest` prints version info, or `WARNING: Package(s) not found: pytest`.

2. **Install pytest into that exact interpreter.** Run `python -m pip install pytest`.
   - Expected: `Successfully installed pytest-...` plus its dependencies.

3. **Verify.** Run `pytest --version`.
   - Expected: something like `pytest 8.3.4`.

## When this applies
- You just created a fresh virtualenv or container and forgot to install test deps.
- Your IDE runs a different interpreter than your terminal.
- CI installs dependencies in one step but runs pytest in another without them.

## When it does not apply
- If `pytest --version` works but a plugin fails to load, the problem is the plugin, not pytest itself.
- If the error names a different module (like `_pytest.scope`), see the version-conflict skills instead.

## Tool compatibility
pytest 7.x and 8.x, Python 3.8+. Install via pip: `pip install pytest`.

## Why it happens
Python resolves imports against `sys.path` of the running interpreter. `pip install pytest` may have targeted a different interpreter (system python vs venv vs conda), so the running one never sees it. Using `python -m pip` guarantees the installer and the runner are the same binary.

## Edge cases
- On Debian/Ubuntu, `pip install pytest` may refuse and tell you to use a venv (PEP 668). Create one: `python3 -m venv .venv && source .venv/bin/activate`.
- If you use conda, prefer `conda install pytest` inside the active env, or `python -m pip install pytest` with the env's python.


---

Source: [Vectle](https://vectle.com/skills/skl_cz2qEhJZnZSmva9CCkhmnw). Version: `skv_Ov2CTOcXMGFNkE6OJMvVRg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
