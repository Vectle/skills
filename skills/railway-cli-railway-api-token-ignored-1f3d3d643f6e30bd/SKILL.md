---
name: "railway-cli-railway-api-token-ignored-1f3d3d643f6e30bd"
description: "Shows how to fix railway CLI: RAILWAY_API_TOKEN ignored by \"railway link\" - \"Unauthorized. Please login with railway login\". Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_EPHwnX7noE63MTSib1-rKg"
  title: "Railway CLI: RAILWAY_API_TOKEN ignored by \"railway link\" - \"Unauthorized. Please login with railway login\""
  version: "skv_zZ1UJLvwUpOiVy6UrU3NVg"
  updated: "2026-10-03T05:04:54.066311+00:00"
  canonical_url: "https://vectle.com/skills/skl_EPHwnX7noE63MTSib1-rKg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

After CLI v3.14.0, running railway link -p... with RAILWAY_API_TOKEN set always failed with "Unauthorized. This was a CLI regression fixed in a later release - upgrade to the latest railway CLI and railway link works with RAILWAY_API_TOKEN again (a maintainer verified the fix with a screenshot).

## When to use

You are seeing this: Please login with railway login", breaking CI pipelines that relied on token auth. Use this skill when you run into "Railway CLI: RAILWAY_API_TOKEN ignored by "railway link" - "Unauthorized. Please login with railway login"".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: CLI v3.14.0. If you are on something much newer or older, the details may have shifted.

## Steps

1. After CLI v3.14.0, running railway link -p ... with RAILWAY_API_TOKEN set always failed with "Unauthorized. Please login with `railway login`", breaking CI pipelines that relied on token auth. Part of the confusion in the thread was the two token types: RAILWAY_API_TOKEN is an account token, while RAILWAY_TOKEN is a project token scoped to a single environment.

2. This was a CLI regression fixed in a later release - upgrade to the latest railway CLI and railway link works with RAILWAY_API_TOKEN again (a maintainer verified the fix with a screenshot). Also use the right token for the job: RAILWAY_API_TOKEN is an account token and is what railway link needs; RAILWAY_TOKEN is a project token scoped to one environment and is intended for railway up / railway run, not for linking. If you are on the latest CLI and link still fails, double-check you are exporting an account token, not a project token. Source: https://github.com/railwayapp/cli/issues/575

## Edge cases

- Also use the right token for the job: RAILWAY_API_TOKEN is an account token and is what railway link needs; RAILWAY_TOKEN is a project token scoped to one environment and is intended for railway up / railway run, not for linking.


---

Source: [Vectle](https://vectle.com/skills/skl_EPHwnX7noE63MTSib1-rKg). Version: `skv_zZ1UJLvwUpOiVy6UrU3NVg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
