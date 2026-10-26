---
name: "pscale-ci-auth-planetscale-service-tok-52aa810ca4a02328"
description: "Configures PlanetScale CLI auth in CI with service-token env vars. Use when setting up pipelines, GitHub Actions, or any non-interactive job that needs pscale. Exports PLANETSCALE_SERVICE_TOKEN_ID and PLANETSCALE_SERVICE_TOKEN as secrets so the CLI authenticates without a browser. Not for local interactive login."
metadata:
  skill_id: "skl_EQuJhazdYMs_l1b_0s84BQ"
  title: "pscale CI auth: PLANETSCALE_SERVICE_TOKEN_ID and PLANETSCALE_SERVICE_TOKEN"
  version: "skv_TfzShQ2IiL74pJEeLd_2-g"
  updated: "2026-10-03T05:58:43.45718+00:00"
  canonical_url: "https://vectle.com/skills/skl_EQuJhazdYMs_l1b_0s84BQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://planetscale.com/docs/cli\"]"
---

# pscale CI auth: PLANETSCALE_SERVICE_TOKEN_ID and PLANETSCALE_SERVICE_TOKEN

TL;DR: the CLI reads service-token credentials from the environment when the browser flow is unavailable. Create a service token in the dashboard with the needed grants, store the token id and token as CI secrets under exactly those variable names, and export them before any pscale call. The CLI then authenticates non-interactively.

```text
pscale commands need non-interactive auth in CI
```

## Steps

1. Create a service token in the PlanetScale dashboard with grants for the databases and branches the job touches.

2. Add two CI secrets: one holding the token id, one holding the token value. Name them exactly PLANETSCALE_SERVICE_TOKEN_ID and PLANETSCALE_SERVICE_TOKEN.

3. Export both before the pscale step (or set them as job-level env). Run a read-only command like `pscale database list`. Expected: it lists databases with no login prompt.

4. If auth fails, re-check the names character by character and confirm the secrets are actually injected into the job, not just defined.

## When this applies

- GitHub Actions, GitLab CI, or any runner needing pscale
- scheduled jobs and deploy pipelines
- Docker builds that call pscale

## When it doesn't

- local development — use `pscale auth login` there
- auth failures with the vars already set — check the token grants next
- interactive troubleshooting sessions

## Compatibility

pscale CLI; PLANETSCALE_SERVICE_TOKEN_ID / PLANETSCALE_SERVICE_TOKEN env vars; CI secret stores. Verified against the official PlanetScale CLI docs.

## Variant phrasings

- pscale CI authentication service token
- PLANETSCALE_SERVICE_TOKEN_ID env var
- planetscale github actions auth

## Root cause

The CLI checks these two env vars before attempting interactive login, so a correctly named pair silently converts every pscale invocation into an authenticated one. A single typo in either name drops back to the browser flow, which is why the names must be exact.

## Edge cases

- mark both as secret/masked; build logs must never show the token value
- scope the token to the branches the pipeline needs, not the whole org
- service tokens do not expire on password change, which is why they suit CI

---

Source: [Vectle](https://vectle.com/skills/skl_EQuJhazdYMs_l1b_0s84BQ). Version: `skv_TfzShQ2IiL74pJEeLd_2-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
