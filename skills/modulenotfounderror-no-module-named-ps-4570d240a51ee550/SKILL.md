---
name: "modulenotfounderror-no-module-named-ps-4570d240a51ee550"
description: "Fixes ModuleNotFoundError: No module named 'psycopg2' Use when `create_engine('postgresql://...')` raises No module named 'psycopg2' Not for: `NoSuchModuleError: Can't load plugin` for a different dialect (that is a URL/dialect mismatch)"
metadata:
  skill_id: "skl_-pcOHEU_FXVlYdDhfAX-sQ"
  title: "ModuleNotFoundError: No module named 'psycopg2'"
  version: "skv_aG98OEtXHXS10r97krABJA"
  updated: "2026-10-03T04:41:32.71658+00:00"
  canonical_url: "https://vectle.com/skills/skl_-pcOHEU_FXVlYdDhfAX-sQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ModuleNotFoundError: No module named 'psycopg2'

SQLAlchemy does not ship a Postgres driver; a bare `postgresql://` URL defaults to psycopg2. Install it: `pip install psycopg2-binary` (no compiler needed), or switch the URL to the v3 driver you do have: `postgresql+psycopg://...` with `pip install "psycopg[binary]"`. The driver name in the URL must match the installed package.

## The exact error

```text
ModuleNotFoundError: No module named 'psycopg2'
```

## Fix it

1. Check which driver you have: `python -m pip show psycopg2-binary psycopg`.
   Expected: you see which (if any) is installed

2. Easiest: `python -m pip install psycopg2-binary` and keep `postgresql://`.
   Expected: create_engine connects

3. Or go v3: `python -m pip install "psycopg[binary]"` and change the URL to `postgresql+psycopg://host/db`.
   Expected: connects via psycopg3

## When this applies

`create_engine('postgresql://...')` raises No module named 'psycopg2'

## When this does NOT apply

`NoSuchModuleError: Can't load plugin` for a different dialect (that is a URL/dialect mismatch)

## Versions

SQLAlchemy with postgresql:// URLs

## Why it happens

DBAPI drivers are separate packages by design; SQLAlchemy only knows the dialect name.

## Edge cases

psycopg2 from source needs pg_config/libpq headers to build; psycopg2-binary avoids that. Keep the password in env vars, not code.


---

Source: [Vectle](https://vectle.com/skills/skl_-pcOHEU_FXVlYdDhfAX-sQ). Version: `skv_aG98OEtXHXS10r97krABJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
