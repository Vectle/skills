---
name: "tenant-config-as-code-auth0-deploy-cli-8be1a17b92f3e383"
description: "Click-ops tenants drift. The deploy CLI exports tenant config to a local repo so changes are reviewed, diffed, and replayable across tenants and environments. Not the full reference manual."
metadata:
  skill_id: "skl_LXxfFnV-AH1A76OowuItOQ"
  title: "Tenant config as code: auth0-deploy-cli and the Terraform provider"
  version: "skv_pl6KEu0rAR5unUj4ULkFGA"
  updated: "2026-10-03T05:12:16.895421+00:00"
  canonical_url: "https://vectle.com/skills/skl_LXxfFnV-AH1A76OowuItOQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Click-ops tenants drift. The deploy CLI exports tenant config to a local repo so changes are reviewed, diffed, and replayable across tenants and environments. Manage them separately: Action secrets via the dashboard or Management API, and never commit client secrets.

# Config as code

## auth0-deploy-cli

`npm install -g auth0-deploy-cli` (or run via npx).

1. `a0deploy export --format=yaml --output_folder=tenant-config`: dumps actions, rules (legacy), connections, applications, APIs, email templates, etc. into a directory.
2. Commit it. Review diffs like code.
3. `a0deploy import --input_file=tenant-config`: applies to a tenant. Promote dev -> staging -> prod by importing the same directory.

## What to keep in the repo

- Actions code (also keep the source in your normal repo; the export is the deployed artifact record).
- Connection configs, application settings, API definitions and permissions.
- Email templates, branding settings.
- Tenant settings (session lifetimes, attack protection thresholds).

## Secrets

The export excludes secrets. Manage them separately: Action secrets via the dashboard or Management API, and never commit client secrets. Your CI needs a Management API token with the right scopes for the target tenant.

## Terraform provider

If the team already speaks Terraform, the Auth0 Terraform provider manages the same resources declaratively with plan/apply and state. Pick ONE tool per tenant; mixing CLI and Terraform fights over state.

## Workflow

- Change in dev tenant (dashboard or code) -> export -> diff -> PR -> import to staging -> test logins -> import to prod.
- Emergency dashboard changes get exported back the same day or they become mystery drift.

## Checklist

- Every tenant reproducible from the repo plus secrets.
- No undocumented dashboard changes older than a day.

## When to use this

- This covers exactly what the title says: Tenant config as code.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Tenant; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Tenant behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_LXxfFnV-AH1A76OowuItOQ). Version: `skv_pl6KEu0rAR5unUj4ULkFGA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
