---
name: "importerror-cannot-import-name-request-ef58476fefe6fcb1"
description: "Fixes `ImportError: cannot import name '_request_ctx_stack' from 'flask'` in flask. Use when upgrading to Flask 2.3+ and the traceback names _request_ctx_stack or _app_ctx_stack imported from flask. Not for 'working outside of request context' runtime errors, which are a different problem with a different fix."
metadata:
  skill_id: "skl_oNGsgWSHpahxQ6jlf2-AIw"
  title: "ImportError: cannot import name '_request_ctx_stack' from 'flask'"
  version: "skv_c0sNO6e8eMRqzBnN8odSmQ"
  updated: "2026-10-03T05:57:49.520126+00:00"
  canonical_url: "https://vectle.com/skills/skl_oNGsgWSHpahxQ6jlf2-AIw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ImportError: cannot import name '_request_ctx_stack' from 'flask'

## TL;DR
Flask removed the private _request_ctx_stack in 2.3. Rewrite code that touches it to use the public proxies instead: flask.request, flask.g, and flask.current_app cover nearly every use. Short term, pinning Flask below 2.3 also works.

## The error
```text
ImportError: cannot import name '_request_ctx_stack' from 'flask'
```

## Fix it
1. Find usages: grep -rEn "_request_ctx_stack|_app_ctx_stack" --include=*.py .
   Expected: A small list of files touching the private stacks.
2. Replace _request_ctx_stack.top with the public equivalent. Most code wants flask.request, flask.session, or flask.g; app context access becomes flask.current_app.
   Expected: The module imports and request handling works as before.
3. If a dependency does it, upgrade the dependency; most Flask extensions released 2.3-compatible versions.
   Expected: pip show [package] lists a version from mid-2023 or later.
4. Only as a stopgap: pip install 'flask<2.3'. Then schedule the rewrite, since the private API is gone for good.
   Expected: App boots on the pinned version.

## When to use this
Use when upgrading to Flask 2.3+ and the traceback names _request_ctx_stack or _app_ctx_stack imported from flask.

## When NOT to use this
Not for 'working outside of request context' runtime errors, which are a different problem with a different fix.

## Version notes
Private context stacks removed in Flask 2.3. Public proxies (request, g, current_app, session) are stable across 2.x and 3.x.

## Why it happens
Flask 2.3 deleted its private context-stack objects as part of cleaning up the internals. Anything importing them, usually old extensions or copied snippets, fails at import time.

## Edge cases
flask.globals still exposes the proxy objects; only the underscore-private stack names were removed, so most rewrites are one-liners.


---

Source: [Vectle](https://vectle.com/skills/skl_oNGsgWSHpahxQ6jlf2-AIw). Version: `skv_c0sNO6e8eMRqzBnN8odSmQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
