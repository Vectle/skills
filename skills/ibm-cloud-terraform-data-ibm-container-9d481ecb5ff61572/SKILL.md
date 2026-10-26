---
name: "ibm-cloud-terraform-data-ibm-container-9d481ecb5ff61572"
description: "Fixes the IBM Cloud Terraform data source ibm_container_vpc_cluster returning the cluster ID from the .name attribute. Use this when you need the actual cluster name in config. Not for other data sources."
metadata:
  skill_id: "skl_4yK98krawLhMt_qEN-JTKw"
  title: "IBM Cloud Terraform: data ibm_container_vpc_cluster name returns the ID"
  version: "skv_Jko-l6CKLPonjgdqvVqBSA"
  updated: "2026-10-03T05:11:24.02362+00:00"
  canonical_url: "https://vectle.com/skills/skl_4yK98krawLhMt_qEN-JTKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_KO-KVa2nMVdfwcGKFLIW6A\",\"https://github.com/IBM-Cloud/terraform-provider-ibm/issues/4485\"]"
---

TL;DR: if `data "ibm_container_vpc_cluster"` looked up by ID returns the cluster ID (not the name) from the `.name` attribute, and the deprecated `cluster_name_id` field returns null, that is the provider's current behavior. Do not copy the reporter's workaround of parsing the name out of the ingress hostname with a regex; it is fragile and undocumented. Track the upstream issue for a proper fix or look up the name through the IBM Cloud API/CLI instead.

## Steps

1. Avoid the ingress-hostname regex parsing; it will break.

2. Get the cluster name from the IBM Cloud API or CLI and pass it in as a variable.

   Expected: a stable name value. Success check: config no longer depends on hostname parsing.

## When to use this

- You need the actual cluster name from the ibm_container_vpc_cluster data source.

## When NOT to use this

- Other data sources; check each one's attributes.

## Compatibility

- IBM Cloud Terraform provider (behavior as reported).

## Variant phrasings

- "ibm_container_vpc_cluster name returns ID"
- "terraform ibm cluster name data source"

## Root cause

The data source populates `.name` with the ID when looked up by ID.

## Edge cases

- The regex workaround is explicitly discouraged; do not copy it.

---

Source: [Vectle](https://vectle.com/skills/skl_4yK98krawLhMt_qEN-JTKw). Version: `skv_Jko-l6CKLPonjgdqvVqBSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
