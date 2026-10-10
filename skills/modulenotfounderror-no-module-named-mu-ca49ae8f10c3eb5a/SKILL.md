---
name: "modulenotfounderror-no-module-named-mu-ca49ae8f10c3eb5a"
description: "Fixes ModuleNotFoundError: No module named 'multipart' Use when FastAPI/Starlette app using UploadFile, File(...) or Form(...) raises No module named 'multipart' Not for: you are not doing file uploads (then you do not need it at all)"
metadata:
  skill_id: "skl_Vzry4zwBz-9g_ScZWfeIyw"
  title: "ModuleNotFoundError: No module named 'multipart'"
  version: "skv_VOf0w3shFlt8QQtjNcZARg"
  updated: "2026-10-03T04:40:03.333421+00:00"
  canonical_url: "https://vectle.com/skills/skl_Vzry4zwBz-9g_ScZWfeIyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ModuleNotFoundError: No module named 'multipart'

FastAPI needs the separate `python-multipart` package for File/Form uploads but does not install it. Run `python -m pip install python-multipart` and add it to requirements.txt. The import name is `multipart`, the pip name is `python-multipart`; that is the whole confusion.

## The exact error

```text
ModuleNotFoundError: No module named 'multipart'
```

## Fix it

1. `python -m pip install python-multipart`
   Expected: Successfully installed python-multipart

2. `python -c "import multipart"`
   Expected: no error

3. Add `python-multipart` to requirements.txt and redeploy.
   Expected: uploads work in the deployed env too

## When this applies

FastAPI/Starlette app using UploadFile, File(...) or Form(...) raises No module named 'multipart'

## When this does NOT apply

you are not doing file uploads (then you do not need it at all)

## Versions

FastAPI file uploads / Form data

## Why it happens

multipart parsing is an optional dependency; FastAPI raises at request time, not import time.

## Edge cases

python-multipart 0.0.18+ changed some internals; if an old pin breaks, unpin it.


---

Source: [Vectle](https://vectle.com/skills/skl_Vzry4zwBz-9g_ScZWfeIyw). Version: `skv_VOf0w3shFlt8QQtjNcZARg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
