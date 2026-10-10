---
name: "dbt-could-not-find-profile-named-jaffl-0653b789c08f3bc4"
description: "Fixes dbt failing with Could not find profile named 'jaffle_shop'. Use when dbt run, dbt test, or any dbt command exits because the profile name in dbt_project.yml has no matching entry in profiles.yml. Confirms the profile name match, checks the profiles dir, and fixes the mismatch. Not for warehouse connection failures after the profile is found."
metadata:
  skill_id: "skl_T7BDuFBkXakTHo_u1tCRwQ"
  title: "dbt: Could not find profile named 'jaffle_shop'"
  version: "skv_7gWAChcehbtlE4tSI8okHg"
  updated: "2026-10-03T05:33:31.877692+00:00"
  canonical_url: "https://vectle.com/skills/skl_T7BDuFBkXakTHo_u1tCRwQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# dbt: Could not find profile named 'jaffle_shop'

TL;DR: the name in dbt_project.yml has no matching profile block in profiles.yml, or dbt is reading a different profiles.yml than you think. Open ~/.dbt/profiles.yml, add (or rename) the block so its name matches the `profile:` value in dbt_project.yml exactly, or point dbt at the right file with --profiles-dir.

```text
Could not find profile named 'jaffle_shop'
```

## Steps

1. Check the profile name your project expects: open dbt_project.yml and read the `profile:` line.

2. Open the profiles file dbt is actually reading, usually ~/.dbt/profiles.yml, and look for a top-level block with that exact name. Expected: the block exists and the spelling, underscores, and case match exactly.

3. If dbt uses a custom profiles dir, either set DBT_PROFILES_DIR to that directory or pass --profiles-dir [path]. Verify with `dbt debug --profiles-dir [path]`, which prints the path it read.

4. Rename the block or the `profile:` value so they agree, save, and rerun `dbt debug`. Expected: `dbt debug` reports the connection instead of the not-found error.

## When this applies

- the exact `Could not find profile named` error on dbt run, dbt test, or dbt debug
- a project that worked on another machine but not this one (different ~/.dbt/profiles.yml)
- CI runs where the profiles file is generated at build time

## When it doesn't

- warehouse auth failures like wrong password or host unreachable — the profile was found, the connection is the problem
- dbt Cloud CLI errors about dbt_cloud.yml, which uses a different auth file
- Jinja/env_var errors inside a profile that already resolves

## Compatibility

dbt Core and dbt Fusion CLIs; profiles.yml in ~/.dbt (or DBT_PROFILES_DIR / --profiles-dir). Verified against the dbt troubleshooting FAQ.

## Variant phrasings

- dbt could not find profile named
- dbt profile not found error
- dbt debug profile named error

## Root cause

dbt resolves the project name to a profile name via dbt_project.yml, then looks that name up in profiles.yml. Any typo, renamed project, or wrong profiles dir breaks the lookup before any connection attempt.

## Edge cases

- DBT_PROFILES_DIR pointing at an empty dir in CI gives this error with zero hint about the path; print it in the failing step
- profiles.yml with a `.bak` extension or YAML syntax error can also surface as not-found rather than parse-failed
- dbt Cloud CLI ignores profiles.yml entirely; this skill is Core-only

---

Source: [Vectle](https://vectle.com/skills/skl_T7BDuFBkXakTHo_u1tCRwQ). Version: `skv_7gWAChcehbtlE4tSI8okHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
