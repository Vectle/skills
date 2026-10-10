---
name: "dbt-cloud-cli-dbt-cloud-yml-not-found-fd90f836f1774f04"
description: "Fixes the dbt Cloud CLI failing because dbt_cloud.yml is missing or its credentials are rejected. Use when the dbt Cloud CLI (dbt-cloud) errors about a missing config file or says you are not authenticated before running. Generates a valid dbt_cloud.yml from the dbt Cloud UI and places it where the CLI looks. Not for dbt Core profiles.yml issues or warehouse connection errors."
metadata:
  skill_id: "skl_ziOctZSLKDU_zmNSarCj3Q"
  title: "dbt Cloud CLI: dbt_cloud.yml not found / not authenticated"
  version: "skv_QzCLYsCJhkwlGFSKar8Erw"
  updated: "2026-10-03T05:35:23.278407+00:00"
  canonical_url: "https://vectle.com/skills/skl_ziOctZSLKDU_zmNSarCj3Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# dbt Cloud CLI: dbt_cloud.yml not found / not authenticated

TL;DR: the CLI reads its credentials from dbt_cloud.yml, which lives in your project dir and must contain a valid api key plus the right account, project, and environment ids. Regenerate it from the dbt Cloud UI (Develop > configure the IDE / download dbt_cloud.yml), drop it in the project root, and rerun from that directory. If the file exists but auth still fails, the api key or ids are stale.

```text
dbt_cloud.yml not found / not authenticated
```

## Steps

1. In the dbt Cloud UI, go to your profile settings and generate a fresh api key. Then download or copy the generated dbt_cloud.yml for your environment.

2. Place dbt_cloud.yml in the root of the project you run the CLI from. The CLI looks in the current directory, not ~/.dbt.

3. Run `dbt-cloud --version` or a lightweight command from that directory. Expected: it authenticates instead of complaining about the config file.

4. Still failing: verify account_id, project_id, and environment_id in the file match the dbt Cloud URL you log into, and that the api key has not been revoked.

## When this applies

- the dbt Cloud CLI (the `dbt-cloud` binary) reporting a missing or invalid dbt_cloud.yml
- `not authenticated` errors before any dbt command runs against dbt Cloud
- a fresh machine where the CLI was installed but never configured

## When it doesn't

- dbt Core's profiles.yml — the Cloud CLI does not read it
- warehouse credential errors inside a run (the Cloud auth already succeeded)
- SSO browser flows for the dbt Cloud web UI itself

## Compatibility

dbt Cloud CLI; dbt_cloud.yml format from the official dbt Cloud CLI configuration docs.

## Variant phrasings

- dbt cloud cli dbt_cloud.yml not found
- dbt cloud cli not authenticated
- dbt-cloud configure authentication

## Root cause

Unlike dbt Core, the Cloud CLI authenticates to the dbt Cloud API, not to your warehouse directly. dbt_cloud.yml is the whole credential bundle (host, ids, api key), so a missing file or a revoked key fails every command up front.

## Edge cases

- running from a subdirectory means the CLI cannot find dbt_cloud.yml; cd to the project root first
- revoked api keys after a team member leaves produce the same `not authenticated` message
- the generated file embeds your personal api key; do not commit it to git

---

Source: [Vectle](https://vectle.com/skills/skl_ziOctZSLKDU_zmNSarCj3Q). Version: `skv_QzCLYsCJhkwlGFSKar8Erw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
