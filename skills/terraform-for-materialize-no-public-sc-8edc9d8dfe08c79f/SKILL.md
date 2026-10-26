---
name: "terraform-for-materialize-no-public-sc-8edc9d8dfe08c79f"
description: "Guide Terraform for Materialize, no public schema and legacy webhook resources: Do not build new webhook ingestion on materialize_source_webhook, it is legacy; use materialize_table with webhook support. Use this when you hit exactly this in Terraform. Not for different errors or different tools."
metadata:
  skill_id: "skl_JN8gmlO3KsJ8ykY9g242BA"
  title: "Terraform for Materialize, no public schema and legacy webhook resources"
  version: "skv_TWrp4KojHLYBHksRH8iOCA"
  updated: "2026-10-03T04:41:11.291254+00:00"
  canonical_url: "https://vectle.com/skills/skl_JN8gmlO3KsJ8ykY9g242BA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/materializeinc/agent-skills/blob/HEAD/skills/materialize-terraform-provider/SKILL.md\"]"
---

TL;DR: Do not build new webhook ingestion on materialize_source_webhook, it is legacy; use materialize_table with webhook support. When automating Materialize with Terraform, expect these: no public schema is created with a new database, so create it explicitly. Size clusters through materialize_cluster rather than the deprecated replica resources.

When automating Materialize with Terraform, expect these: no public schema is created with a new database, so create it explicitly. Do not build new webhook ingestion on materialize_source_webhook, it is legacy; use materialize_table with webhook support. Size clusters through materialize_cluster rather than the deprecated replica resources. And identity resources tied to Frontegg (users, SSO, SCIM, app passwords) only work on Materialize Cloud, not self-managed.

Context: Materialize terraform provider skill (materializeinc/agent-skills skills/materialize-terraform-provider/SKILL.md), Common Gotchas: materialize_database does not auto-create a public schema, create one explicitly. materialize_source_webhook is legacy; new webhooks go through materialize_table. Cluster replicas are deprecated in favor of materialize_cluster with a size. Frontegg-dependent resources (users, SSO, SCIM, app passwords) fail against self-managed instances.

## When to use
You hit exactly this: Terraform for Materialize, no public schema and legacy webhook resources in Terraform.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Terraform.

---

Source: [Vectle](https://vectle.com/skills/skl_JN8gmlO3KsJ8ykY9g242BA). Version: `skv_TWrp4KojHLYBHksRH8iOCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
