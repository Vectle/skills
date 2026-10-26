---
name: "finding-what-keeps-changing-your-infra-97f7e56738cb6533"
description: "Drift on every plan means an external writer. The procedure identifies the writer from change patterns, audit logs, and resource metadata instead of adding ignore_changes blindly. Not the full reference manual."
metadata:
  skill_id: "skl_0GTCKtDKH4NTCpN1U5jDNA"
  title: "Finding what keeps changing your infra outside Terraform: \"Objects have changed\" every run"
  version: "skv_FHt4ILy7Z9QL5lcBnnwRXA"
  updated: "2026-10-03T15:21:55.331393+00:00"
  canonical_url: "https://vectle.com/skills/skl_0GTCKtDKH4NTCpN1U5jDNA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/plan/\",\"https://developer.hashicorp.com/terraform/docs/language/meta-arguments/lifecycle\"]"
---

**TL;DR:** Drift on every plan means an external writer. The procedure identifies the writer from change patterns, audit logs, and resource metadata instead of adding ignore_changes blindly. Read the drift note: which attributes change? Check cloud audit logs (CloudTrail, Activity Log, Audit Logs) for the resource ARN around the drift window.

## The fix

**TL;DR:** Drift on every plan means an external writer. The procedure identifies the writer from change patterns, audit logs, and resource metadata instead of adding ignore_changes blindly. Read the drift note: which attributes change? Check cloud audit logs (CloudTrail, Activity Log, Audit Logs) for the resource ARN around the drift window.

# Finding what keeps changing your infra outside Terraform

## Symptom

Every `terraform plan` reports `Objects have changed outside of Terraform` on the same resources, even right after a clean apply.

## Cause

Something with API access is mutating the resources: an autoscaler, a Kubernetes controller, a console user, another IaC tool, or a provider-side defaulting behavior.

## Confirmation

1. Read the drift note: which attributes change? Scaling counts point at autoscalers; tags point at humans or policy tools; timestamps/version fields point at controllers.
2. Check cloud audit logs (CloudTrail, Activity Log, Audit Logs) for the resource ARN around the drift window. The `userIdentity` field names the writer.
3. Check for controllers: does a Kubernetes operator, ASG, or external system own this resource? Resource tags and descriptions often name the owner.
4. Rule out Terraform itself: `terraform plan` immediately after `terraform apply` should be clean. If it is not clean even with no external actor, the provider is defaulting something (see the inconsistent-result diagnostic).

## Fix

1. Human writers: move their workflow into Terraform or into the config. Console hotfixes during incidents should be codified afterwards.
2. Controllers/autoscalers: either manage the resource entirely outside Terraform (remove it, use a data source), or add a scoped `ignore_changes` on exactly the controller-managed attributes, with a comment naming the controller.
3. Another IaC tool: split ownership clearly. Two writers for one resource is the bug; decide who owns it.

## Verification

1. Apply, wait a full controller cycle (or a day for human-driven drift), then plan. Clean means the writer is handled.
2. `ignore_changes` should name specific attributes, never whole resources. Verify the plan still catches changes to the non-ignored attributes.

## When to use this

- This covers exactly what the title says: Finding what keeps changing your infra outside Terraform.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Finding; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_0GTCKtDKH4NTCpN1U5jDNA). Version: `skv_FHt4ILy7Z9QL5lcBnnwRXA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
