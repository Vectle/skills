---
name: "ibm-cloud-importing-a-gen2-ibm-databas-4e5f99bdec2ee920"
description: "Explains the misleading 'database instance was not found in the region' error when importing a Gen2 ibm_database with the IBM Cloud Terraform provider. It is a Gen1/Gen2 backend dispatch bug, not a region problem; upgrade to a provider release containing the fix. Use when terraform import of a standard-gen2 database fails despite correct region and CRN. Not for actual region mismatches or Gen1 databases."
metadata:
  skill_id: "skl_MaaGDws7S6r1tN0YHmvLPw"
  title: "IBM Cloud: importing a Gen2 ibm_database fails with false \"not found in the region\" error"
  version: "skv_LHx_W0ty0U-gP8G1Y12__A"
  updated: "2026-10-03T05:58:21.713287+00:00"
  canonical_url: "https://vectle.com/skills/skl_MaaGDws7S6r1tN0YHmvLPw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if importing a Gen2 `ibm_database` fails with "not found in the region" even though the instance genuinely exists in the right region, do not chase your region config. It is a Gen1/Gen2 backend dispatch bug in the provider. The maintainer linked a fix PR (IBM-Cloud/terraform-provider-ibm#7000); upgrade to a provider release containing that fix.

The error, verbatim:

```text
Error: [ERROR] The database instance was not found in the region set for the Provider, or the default of us-south
```

## Steps

1. Confirm the setup: you are importing a Gen2 instance (`plan = "standard-gen2"`) via an `import {}` block or `terraform import`, and the instance really exists in the configured region.

2. Check your provider version against the fix PR (IBM-Cloud/terraform-provider-ibm#7000). Expected: if your version predates it, you are on the buggy dispatch path.

3. Upgrade the provider to a release containing the fix, then re-run the import. Success check: the import completes and the instance shows in state.

4. On an affected version with no upgrade available, know the failure is expected regardless of how correctly your region and CRN are set; do not burn time re-checking them.

## When to use this

- `terraform import` of a `standard-gen2` `ibm_database` fails with the "not found in the region" error.
- The instance exists in the correct region; region config is not the problem.

## When NOT to use this

- Gen1 (classic) databases; the dispatch bug is Gen2-specific.
- The instance genuinely is in a different region; fix the region instead.

## Compatibility

- terraform-provider-ibm versions before the #7000 fix, Gen2 `standard-gen2` plan databases. Issue is closed with the fix linked.

## Variant phrasings

- ibm_database import fails not found in region gen2
- terraform import ibm cloud database not found in region
- standard-gen2 import "not found in the region set for the Provider"

## Root cause

`pickResourceBackend` in resource_ibm_database.go dispatches on `d.Get("plan")`, but during import-driven Read the plan field is not yet populated, so it always falls through to the Gen1 (classic) backend. The Gen1 backend's `GetDeploymentInfo` 404s on a Gen2 deployment, and that 404 surfaces as the misleading region error.

## Edge cases

- Normal (non-import) create/read of Gen2 databases was unaffected because the plan field is populated in that path.
- The error message names the provider's region default (us-south); that string is a red herring on every region.

Source: https://github.com/IBM-Cloud/terraform-provider-ibm/issues/6996

---

Source: [Vectle](https://vectle.com/skills/skl_MaaGDws7S6r1tN0YHmvLPw). Version: `skv_LHx_W0ty0U-gP8G1Y12__A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
