---
name: "modulenotfounderror-no-module-named-bl-303fa5019231c459"
description: "Fixes ModuleNotFoundError: No module named 'black' by installing the Black formatter. Use when the black command or module is not found. Not for formatting crashes."
metadata:
  skill_id: "skl_6J32q44d55Smp4qZkDaP0w"
  title: "ModuleNotFoundError: No module named 'black'"
  version: "skv_g0CKx89ZormvDaDeh-qQJw"
  updated: "2026-10-03T06:06:09.710342+00:00"
  canonical_url: "https://vectle.com/skills/skl_6J32q44d55Smp4qZkDaP0w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://pypi.org/project/black/\"]"
---

## TL;DR
Run `python -m pip install black`. This error means the Black formatter is not installed in the environment running the command, or your shell is finding a different Python than the one you installed into.

```text
ModuleNotFoundError: No module named 'black'
```

## Fix it

1. **Install it.** Run `python -m pip install black`.
   - Expected: `Successfully installed black-...`.

2. **Verify.** Run `black --version`.
   - Expected: `black, version ...`.

3. **If it still fails**, check `which black` and `which python` point at the same environment.

## When this applies
- Fresh machine, new virtualenv, or CI job missing the formatter.
- pre-commit hook environment issues (see the hook's own troubleshooting).

## When it does not apply
- If black runs but crashes on a file, that is a parsing or config issue.

## Tool compatibility
black 23.x/24.x, Python 3.8+. `pip install black`.

## Why it happens
`black` the command comes from the `black` package. No package, no command, and `python -m black` fails the same way.

## Edge cases
- For `blackd` (the daemon), you need the `d` extra: `pip install "black[d]"`, which pulls in aiohttp.


---

Source: [Vectle](https://vectle.com/skills/skl_6J32q44d55Smp4qZkDaP0w). Version: `skv_g0CKx89ZormvDaDeh-qQJw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
