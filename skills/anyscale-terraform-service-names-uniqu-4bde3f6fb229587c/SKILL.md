---
name: "anyscale-terraform-service-names-uniqu-4bde3f6fb229587c"
description: "Guide Anyscale Terraform: service names unique per project only, null-check canary_version (service_lookup): If two projects both have a service called my-service, the by-name lookup errors and asks you to pass project_id or cloud_id, it never guesses for you. Use this when you hit exactly this in Anyscale Terraform. Not for different errors or different tools."
metadata:
  skill_id: "skl_RBINd2DEgr7F6agGg-YvQg"
  title: "Anyscale Terraform: service names unique per project only, null-check canary_version (service_lookup)"
  version: "skv_SQ8ML1b6Wsnig3P-Zek4dQ"
  updated: "2026-10-03T05:11:34.502112+00:00"
  canonical_url: "https://vectle.com/skills/skl_RBINd2DEgr7F6agGg-YvQg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If two projects both have a service called my-service, the by-name lookup errors and asks you to pass project_id or cloud_id, it never guesses for you. canary_version is null unless a rollout is actively in progress, so null-check before reading it. [Anyscale Terraform provider service data source]: service names are unique only within a project, not org-wide.

## Fix
1. If two projects both have a service called my-service, the by-name lookup errors and asks you to pass project_id or cloud_id, it never guesses for you. canary_version is null unless a rollout is actively in progress, so null-check before reading it.
   Expected: this specific failure stops.
2. If two projects each have a service called my-service, the by-name lookup errors out asking you to set project_id or cloud_id to disambiguate; it never silently guesses. canary_version is null except while a rollout is actively in progress, so check for null before reading fields off it. error_message carries the error from the most recent API request against the service, null otherwise.
   Expected: this specific failure stops.

## Details
[Anyscale Terraform provider service data source]: service names are unique only within a project, not org-wide. And error_message holds the latest API error against the service, null when things are fine. Context: Anyscale Terraform provider service data source: service names are unique only within a project, not organization-wide.

## When to use
You hit exactly this: Anyscale Terraform: service names unique per project only, null-check canary_version (service_lookup) in Anyscale Terraform.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Anyscale Terraform.

---

Source: [Vectle](https://vectle.com/skills/skl_RBINd2DEgr7F6agGg-YvQg). Version: `skv_SQ8ML1b6Wsnig3P-Zek4dQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
