---
name: "importerror-cannot-import-name-safe-st-c9ded322dec9ca1c"
description: "Fixes ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security' Use when werkzeug>=2.1 and an old flask extension imports safe_str_cmp Not for: your own code (use hmac.compare_digest directly)"
metadata:
  skill_id: "skl_nQyep9XJsyUh3YBtjehOCQ"
  title: "ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security'"
  version: "skv_70XrgcHdaKEcwiROMImjTg"
  updated: "2026-10-03T04:49:33.160161+00:00"
  canonical_url: "https://vectle.com/skills/skl_nQyep9XJsyUh3YBtjehOCQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pgadmin-org/pgadmin4/issues/5285\"]"
---

# How to fix ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security'

Werkzeug 2.1 removed `safe_str_cmp`; the library importing it (flask-login, flask-jwt-extended, pgadmin4's deps) is too old. Upgrade that library (`pip install -U flask-login` etc.). Stopgap: `pip install "werkzeug<2.1"`, but that just postpones the upgrade.

## The exact error

```text
ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security'
```

## Fix it

1. Find the importer from the traceback (e.g. flask_login/utils.py).
   Expected: you know which package is stale

2. `pip install -U [that package]` (flask-login>=0.6.2 fixed it).
   Expected: it uses hmac.compare_digest now

3. Re-run your app.
   Expected: no ImportError

## When this applies

werkzeug>=2.1 and an old flask extension imports safe_str_cmp

## When this does NOT apply

your own code (use hmac.compare_digest directly)

## Versions

werkzeug >= 2.1 with old flask extensions

## Why it happens

Werkzeug removed the helper; its own docs point at hmac.compare_digest.

## Edge cases

Pinning werkzeug[2.1 can conflict with Flask]=2.2 requirements; upgrade the extension instead.


---

Source: [Vectle](https://vectle.com/skills/skl_nQyep9XJsyUh3YBtjehOCQ). Version: `skv_70XrgcHdaKEcwiROMImjTg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
