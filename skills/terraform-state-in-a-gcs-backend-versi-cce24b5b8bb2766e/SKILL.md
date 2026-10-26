---
name: "terraform-state-in-a-gcs-backend-versi-cce24b5b8bb2766e"
description: "Shows how to fix terraform state in a GCS backend: versioning, locking, and per-env separation. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_kXzpb68u7PVBeAz5g4wcjA"
  title: "Terraform state in a GCS backend: versioning, locking, and per-env separation"
  version: "skv_Ee-rRktLWiiOCh-NRkWXOA"
  updated: "2026-10-03T14:09:47.3328+00:00"
  canonical_url: "https://vectle.com/skills/skl_kXzpb68u7PVBeAz5g4wcjA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developer.hashicorp.com/terraform/language/backend/gcs\",\"https://cloud.google.com/storage/docs/lifecycle\"]"
---

## TL;DR

Enable versioning on the state bucket: gcloud storage buckets update gs://[BUCKET] --versioning. Backend config: ``hcl terraform { backend "gcs" { bucket = "[STATE-BUCKET]" prefix = "envs/prod" } } ` Setup order: 1. Enable uniform bucket-level access and public access prevention on the state bucket. If a lock sticks after a crashed apply, terraform force-unlock [LOCK-ID] deliberately, after confirming no apply is running.

## When to use

You are seeing this: Goal: shared, safe terraform state for a team. Use this skill when you run into "Terraform state in a GCS backend: versioning, locking, and per-env separation".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

Goal: shared, safe terraform state for a team.

Backend config:

```hcl
terraform {
  backend "gcs" {
    bucket = "[STATE-BUCKET]"
    prefix = "envs/prod"
  }
}
```

Setup order:
1. Create the state bucket FIRST, outside the terraform that uses it (bootstrap by hand or a separate tiny config). Chicken-and-egg otherwise.
2. Enable versioning on the state bucket: `gcloud storage buckets update gs://[BUCKET] --versioning`. Corrupted state is recoverable from a prior version.
3. Enable uniform bucket-level access and public access prevention on the state bucket. State files contain secrets.
4. Grant the CI/human identities storage.objectAdmin on the bucket (terraform needs read/write, and locking).

Locking: the GCS backend handles state locking natively. Do not disable it. If a lock sticks after a crashed apply, `terraform force-unlock [LOCK-ID]` deliberately, after confirming no apply is running.

Environment separation: prefix per env (envs/dev, envs/prod) or workspaces. Never share one state file across environments; a bad apply then touches everything.

Traps:
- State bucket in the SAME terraform config that uses it: the backend needs the bucket before init. Bootstrap separately.
- No versioning: one bad apply corrupts state with no recovery. This is the most expensive terraform mistake on GCP.
- Storing the backend config with credentials in it: use ADC in the environment, not credentials blocks in checked-in files.
- `terraform init -migrate-state` when moving from local to GCS: back up local state first.

Verify: init succeeds from a fresh clone, plan shows no diff, and a prior state version exists in the bucket.


---

Source: [Vectle](https://vectle.com/skills/skl_kXzpb68u7PVBeAz5g4wcjA). Version: `skv_Ee-rRktLWiiOCh-NRkWXOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
