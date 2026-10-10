---
name: "importerror-cannot-import-name-googles-40811a1fb6356a11"
description: "Fixes 'ImportError: cannot import name GoogleSearch from serpapi' by installing the correct package: pip install google-search-results (not pip install serpapi, which is a different library). Use when the SerpAPI Python client fails to import after installation. Not for API key or quota errors."
metadata:
  skill_id: "skl_YasvGupOXmm_tQZJepusnQ"
  title: "ImportError: cannot import name 'GoogleSearch' from 'serpapi'"
  version: "skv_4TjJsE_GInfpJLzZLzOZFA"
  updated: "2026-10-03T04:09:42.762568+00:00"
  canonical_url: "https://vectle.com/skills/skl_YasvGupOXmm_tQZJepusnQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

You installed the wrong package. `pip install serpapi` gives you an unrelated library; the SerpAPI client lives in `google-search-results`. Fix: `pip install google-search-results`, then `from serpapi import GoogleSearch` works.

## The error

```text
ImportError: cannot import name 'GoogleSearch' from 'serpapi'
```

## Fix it

1. Uninstall the wrong package:
   ```bash
   pip uninstall serpapi
   ```
   Success check: `pip show serpapi` reports the package is not installed.

2. Install the correct SerpAPI client:
   ```bash
   pip install google-search-results
   ```
   Success check: install completes with no errors.

3. Verify the import:
   ```bash
   python -c "from serpapi import GoogleSearch; print('ok')"
   ```
   Success check: prints `ok` with no ImportError.

## When this applies

- `from serpapi import GoogleSearch` raises ImportError right after installing what you thought was the SerpAPI client.
- You ran `pip install serpapi` (the wrong package).

## When it does not apply

- The import works but API calls fail; that is an API key or quota problem, not a packaging problem.
- You are using the Node.js SerpAPI client (`serpapi` on npm is correct there).
- The error names a different symbol than `GoogleSearch`.

## Compatibility

- Python 3.8+. Package `google-search-results` (the official SerpAPI Python client).
- The unrelated PyPI package named `serpapi` is a different library entirely.

## Variant phrasings

- ImportError cannot import name GoogleSearch from serpapi
- pip install serpapi wrong package
- serpapi python client import error

## Why it happens

Two different libraries share a confusingly similar name on PyPI. `pip install serpapi` installs an unrelated package that has no `GoogleSearch` export. The official SerpAPI client is published as `google-search-results`, which provides the `serpapi` import namespace with `GoogleSearch`.

## Edge cases

- If both packages are installed, uninstall `serpapi` first to avoid namespace shadowing.
- In requirements files, pin `google-search-results`, never `serpapi`.
- Source: https://github.com/serpapi/google-search-results-python/issues/63


---

Source: [Vectle](https://vectle.com/skills/skl_YasvGupOXmm_tQZJepusnQ). Version: `skv_4TjJsE_GInfpJLzZLzOZFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
