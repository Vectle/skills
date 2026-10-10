---
name: "dbt-env-var-required-but-not-provided-be86b8abc7a675a9"
description: "Fixes dbt's Env var required but not provided error from profiles.yml. Use when dbt debug or dbt run fails because an env_var() call in profiles.yml references an environment variable that is not set in the shell. Exports the missing variable or gives env_var a fallback default. Not for variables set correctly but misspelled in profiles.yml or for --vars CLI overrides."
metadata:
  skill_id: "skl_K-P5kpNoRR2-gCH3mPLK1w"
  title: "dbt: Env var required but not provided"
  version: "skv_gNXO8A8E6BpZlioO7LzYbg"
  updated: "2026-10-03T05:34:30.891353+00:00"
  canonical_url: "https://vectle.com/skills/skl_K-P5kpNoRR2-gCH3mPLK1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# dbt: Env var required but not provided

TL;DR: profiles.yml calls env_var() with a variable you never exported. Export it in the shell before running dbt, or add a fallback default in the env_var() call. Also make sure the variable is actually exported (not just assigned) and that CI injects it into the dbt step.

```text
Env var required but not provided
```

## Steps

1. Rerun with the full error; dbt names the missing variable. Note its exact spelling.

2. Export it in the current shell, for example `export DBT_PASSWORD` with your value assigned, then rerun. Expected: the error moves past this variable to the next one or disappears.

3. For a durable fix, add a fallback in profiles.yml: `env_var('DBT_PASSWORD', 'fallback')`. Expected: dbt runs without the variable set, using the fallback.

4. In CI, add the variable to the job's env block so the dbt step inherits it. Expected: `printenv DBT_PASSWORD` (redacted) in the failing step shows it present.

## When this applies

- the exact `Env var required but not provided` error on dbt debug, dbt run, or dbt compile
- profiles.yml that uses env_var() for passwords, hosts, or schemas
- CI pipelines where secrets are injected per-job

## When it doesn't

- a variable that IS exported but spelled differently in profiles.yml — that's a typo, not a missing var
- dbt Cloud CLI env-var handling, which is configured in the dbt Cloud UI
- --vars values, which never touch env_var()

## Compatibility

dbt Core and Fusion CLIs; profiles.yml with env_var() calls. Verified against the dbt environment-variables community guide.

## Variant phrasings

- dbt env var required but not provided fix
- dbt profiles.yml env_var error
- dbt export environment variable profiles

## Root cause

env_var() without a default raises at parse time when the variable is absent from the process environment. Shells only pass variables marked for export to child processes, so a plain assignment in a script is invisible to dbt.

## Edge cases

- on Windows, `set` does not persist across terminal sessions; use the system environment settings or a persistent profile
- a fallback default still prints the value into logs; prefer real secret injection for passwords
- dbt Cloud CLI reads env vars from the environment settings UI, not your laptop's shell

---

Source: [Vectle](https://vectle.com/skills/skl_K-P5kpNoRR2-gCH3mPLK1w). Version: `skv_gNXO8A8E6BpZlioO7LzYbg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
