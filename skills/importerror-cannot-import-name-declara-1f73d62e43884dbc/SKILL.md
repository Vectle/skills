---
name: "importerror-cannot-import-name-declara-1f73d62e43884dbc"
description: "Fixes ImportError: cannot import name 'declarative_base' from 'sqlalchemy.ext.declarative' Use when SQLAlchemy 2.x and old `sqlalchemy.ext.declarative` imports Not for: SQLAlchemy 1.4 (both import paths work there)"
metadata:
  skill_id: "skl_z7s-5-A4_6a0KXw2k1pyVg"
  title: "ImportError: cannot import name 'declarative_base' from 'sqlalchemy.ext.declarative'"
  version: "skv_Ukc3D12yK2o30grrZ6gD4Q"
  updated: "2026-10-03T04:42:20.531644+00:00"
  canonical_url: "https://vectle.com/skills/skl_z7s-5-A4_6a0KXw2k1pyVg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'declarative_base' from 'sqlalchemy.ext.declarative'

SQLAlchemy 2.0 removed `sqlalchemy.ext.declarative.declarative_base`. Import it from `sqlalchemy.orm` instead: `from sqlalchemy.orm import declarative_base`. (Or go full 2.0 style with `class Base(DeclarativeBase)`.) One-line change, same behavior.

## The exact error

```text
ImportError: cannot import name 'declarative_base' from 'sqlalchemy.ext.declarative'
```

## Fix it

1. Replace `from sqlalchemy.ext.declarative import declarative_base` with `from sqlalchemy.orm import declarative_base`.
   Expected: import works on SQLAlchemy 2.x

2. Run your test suite and migrations.
   Expected: models load, migrations run

3. Optional modernize: `from sqlalchemy.orm import DeclarativeBase` and `class Base(DeclarativeBase): pass`.
   Expected: 2.0-native style

## When this applies

SQLAlchemy 2.x and old `sqlalchemy.ext.declarative` imports

## When this does NOT apply

SQLAlchemy 1.4 (both import paths work there)

## Versions

SQLAlchemy >= 2.0

## Why it happens

1.4 deprecated the ext.declarative location; 2.0 removed it.

## Edge cases

Some old tutorials also use `sqlalchemy.ext.declarative.api`; same fix.


---

Source: [Vectle](https://vectle.com/skills/skl_z7s-5-A4_6a0KXw2k1pyVg). Version: `skv_Ukc3D12yK2o30grrZ6gD4Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
