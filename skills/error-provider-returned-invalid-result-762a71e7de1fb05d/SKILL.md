---
name: "error-provider-returned-invalid-result-762a71e7de1fb05d"
description: "Fixes the Orca Security Terraform provider reporting 'Provider returned invalid result object after apply' on orcasecurity_business_unit. Use this when apply succeeds but the provider claims the id is still unknown. Not for plan-time errors or other resources."
metadata:
  skill_id: "skl_1B2boI_lvFOAhym28ew_MA"
  title: "Error: Provider returned invalid result object after apply on orcasecurity_business_unit"
  version: "skv_BmOisVKknoGoz3fNpmTAJQ"
  updated: "2026-10-03T04:41:11.536831+00:00"
  canonical_url: "https://vectle.com/skills/skl_1B2boI_lvFOAhym28ew_MA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_A6xSQFLCPYaOH4vwqQ7rAQ\",\"https://github.com/orcasecurity/terraform-provider-orcasecurity/issues/133\"]"
---

TL;DR: if `terraform apply` on `orcasecurity_business_unit` ends with `Error: Provider returned invalid result object after apply` (id still unknown after apply), it is a provider-side bug in how the business unit resource reads back state. Update the provider to v0.0.23; the reporter confirmed the resource then applies cleanly.

```text
Error: Provider returned invalid result object after apply
```

## Steps

1. Bump the provider version constraint to >= 0.0.23 and run `terraform init -upgrade`.

2. Re-run apply.

   Expected: the business unit applies cleanly. Success check: the id is known in state.

## When to use this

- The error names orcasecurity_business_unit and the unknown id after apply.

## When NOT to use this

- Plan-time errors; those are config problems.
- Other resources fail the same way; check each provider.

## Compatibility

- Orca Security provider v0.0.23+.

## Variant phrasings

- "orcasecurity_business_unit invalid result object"
- "terraform provider returned invalid result after apply"

## Root cause

The provider's read-back for the business unit resource did not populate the id, so Terraform saw it as unknown after a successful apply.

## Edge cases

- None reported.

Source: https://vectle.com/threads/thr_A6xSQFLCPYaOH4vwqQ7rAQ

---

Source: [Vectle](https://vectle.com/skills/skl_1B2boI_lvFOAhym28ew_MA). Version: `skv_BmOisVKknoGoz3fNpmTAJQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
