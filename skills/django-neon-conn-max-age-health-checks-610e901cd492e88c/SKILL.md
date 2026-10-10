---
name: "django-neon-conn-max-age-health-checks-610e901cd492e88c"
description: "Shows how to fix django + Neon: CONN_MAX_AGE, health checks, and no server-side cursors. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_6tnnGWhrJqFGwmNK_QIgPQ"
  title: "Django + Neon: CONN_MAX_AGE, health checks, and no server-side cursors"
  version: "skv_3RLN0pf1AVduDqGzwdZciA"
  updated: "2026-10-03T14:16:32.954749+00:00"
  canonical_url: "https://vectle.com/skills/skl_6tnnGWhrJqFGwmNK_QIgPQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

On Django 4.1+ you can use a higher CONN_MAX_AGE combined with CONN_HEALTH_CHECKS for reuse with safety. - DISABLE_SERVER_SIDE_CURSORS = True: required with the pooler. - OPTIONS: {sslmode: require}`: Neon requires SSL.

## Steps

1. Django defaults keep database connections open across requests (`CONN_MAX_AGE`), and Neon closes idle connections after 5 minutes. The result is intermittent "connection already closed" errors that only happen on quiet apps, the hardest kind to reproduce. Separately, Django's server-side cursors assume session state that PgBouncer transaction mode does not preserve.

```python
DATABASES = {
 "default": {
 "ENGINE": "django.db.backends.postgresql",
 "NAME": getenv("PGDATABASE"),
 "USER": getenv("PGUSER"),
 "PASSWORD": getenv("PGPASSWORD"),
 "HOST": getenv("PGHOST"),
 "PORT": getenv("PGPORT", 5432),
 "OPTIONS": {"sslmode": "require"},
 "DISABLE_SERVER_SIDE_CURSORS": True,
 "CONN_HEALTH_CHECKS": True,
 }
}
```

2. - `CONN_MAX_AGE = 0` (the default): close connections at the end of each request so Django never reuses one Neon already closed. On Django 4.1+ you can use a higher `CONN_MAX_AGE` combined with `CONN_HEALTH_CHECKS` for reuse with safety.
- `DISABLE_SERVER_SIDE_CURSORS = True`: required with the pooler.
- `OPTIONS: {sslmode: require}`: Neon requires SSL.

3. - Start with `CONN_MAX_AGE = 0`; only raise it with `CONN_HEALTH_CHECKS = True` on 4.1+.
- Pooled connection string for the app; direct for `migrate`.
- If you see cursor errors only under the pooler, this setting is the first thing to check.

## When to use

You are seeing this: Django defaults keep database connections open across requests (CONN\_MAX\_AGE), and Neon closes idle connections after 5 minutes. Use this skill when you run into "Django + Neon: CONN_MAX_AGE, health checks, and no server-side cursors".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_6tnnGWhrJqFGwmNK_QIgPQ). Version: `skv_3RLN0pf1AVduDqGzwdZciA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
