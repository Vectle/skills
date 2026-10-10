---
name: "importerror-cannot-import-name-tavilyc-3623bc02c2bcd1e9"
description: "Fixes 'ImportError: cannot import name TavilyClient from tavily' by checking for a local file named tavily.py shadowing the installed package; rename it and the import works. Use when the import fails right after pip install tavily-python. Not for API key or network errors."
metadata:
  skill_id: "skl_ER5lip6EXDVX7avtdfgNgA"
  title: "ImportError: cannot import name 'TavilyClient' from 'tavily'"
  version: "skv_7n98D2jE13DlUTXVR5x2Wg"
  updated: "2026-10-03T04:12:48.60728+00:00"
  canonical_url: "https://vectle.com/skills/skl_ER5lip6EXDVX7avtdfgNgA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check whether your script or notebook directory contains a file named `tavily.py` (or a `tavily` folder): it shadows the installed package on the import path. Rename the local file and `from tavily import TavilyClient` works. If there is no shadowing file, upgrade with `pip install --upgrade tavily-python`.

## The error

```text
ImportError: cannot import name 'TavilyClient' from 'tavily'
```

After `pip install tavily-python`; reinstalling does not help.

## Fix it

1. Look for a shadowing file in your working directory:
   ```bash
   ls tavily.py
   ls -d tavily
   ```
   Success check: either command finds a match, confirming the shadow.

2. Rename the local file (e.g. to `tavily_demo.py`).
   Success check: `ls tavily.py` no longer finds it.

3. Retry the import:
   ```bash
   python -c "from tavily import TavilyClient; print('ok')"
   ```
   Success check: prints `ok` with no ImportError.

4. If no shadowing file exists, upgrade the package:
   ```bash
   pip install --upgrade tavily-python
   ```
   Success check: the import works after upgrading.

## When this applies

- `from tavily import TavilyClient` raises ImportError immediately after installing.
- Reinstalling the package changes nothing.

## When it does not apply

- The import works but API calls fail; that is a key or network problem.
- A different symbol is missing from the import.

## Compatibility

- tavily-python (any recent version). Python 3.8+.

## Variant phrasings

- ImportError cannot import name TavilyClient
- tavily python import error after pip install
- from tavily import TavilyClient fails

## Why it happens

Python resolves imports from the current directory before installed packages. A local `tavily.py` wins over the installed SDK, and since your file has no `TavilyClient`, the import fails. Renaming removes the shadow.

## Edge cases

- Jupyter: the notebook's directory is on the path too; check there as well.
- `__pycache__` may hold a stale `tavily` bytecode entry; clear it after renaming.
- Source: https://github.com/tavily-ai/tavily-python/issues/20


---

Source: [Vectle](https://vectle.com/skills/skl_ER5lip6EXDVX7avtdfgNgA). Version: `skv_7n98D2jE13DlUTXVR5x2Wg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
