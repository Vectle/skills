---
name: "datadog-custom-metrics-billing-tag-car-7391546bcf0fc259"
description: "Datadog bills custom metrics per unique metric name plus tag combination. The count scales with your most granular tag, so a high-cardinality tag like user id multiplies the bill. The docs counting examples prove it. Not the full reference manual."
metadata:
  skill_id: "skl_eNAxDUlXYhBHj2g_cRmSAw"
  title: "Datadog custom metrics billing: tag cardinality is the cost trap"
  version: "skv_H4ZEI2XOFWGcflk5VPZUGA"
  updated: "2026-10-03T05:05:35.214967+00:00"
  canonical_url: "https://vectle.com/skills/skl_eNAxDUlXYhBHj2g_cRmSAw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/account_management/billing/custom_metrics/\"]"
---

**TL;DR:** Datadog bills custom metrics per unique metric name plus tag combination. The count scales with your most granular tag, so a high-cardinality tag like user id multiplies the bill. Add a finer tag and the count scales with the most granular tag: their temperature example shows adding city (3 values) multiplying the count, while a coarser tag on top adds nothing. Never tag by unbounded IDs. user_id, email, session_id, request_id, IP: aggregate these or drop the tag, keep the value in the log event instead.

# Datadog custom metrics cost: tag cardinality is the trap

Custom metrics are not billed per metric name. They are billed per **unique combination of metric name and tag values**. One metric name with a `user_id` tag and 50k users is 50k billable custom metrics. This is the most expensive line item teams discover by surprise.

## The counting rule (from the docs)

The docs example: `request.latency` submitted from host:A and host:B, tagged `endpoint:X/Y` and `status:200/400`, counts as **four** custom metrics, one per unique tag-value combination actually submitted. Add a finer tag and the count scales with the most granular tag: their temperature example shows adding `city` (3 values) multiplying the count, while a coarser tag on top adds nothing.

So: the bill follows your highest-cardinality tag. `status` (4 values) is free-ish. `user_id`, `request_id`, `container_id` are invoice events.

## Guardrails

1. **Never tag by unbounded IDs.** user_id, email, session_id, request_id, IP: aggregate these or drop the tag, keep the value in the log event instead.
2. **Estimate before shipping.** List the distinct values of each tag key you plan to use. Multiply. That is roughly your new custom metric count for that name.
3. **Watch the Usage page.** It shows custom metric volumes over time; a hockey stick right after a deploy names the culprit metric.
4. **Metrics without Limits.** If you are on it, you get ingested vs indexed volumes and can drop indexing on high-cardinality tags you only need for short-term debugging. Learn the difference before you need it.
5. **DogStatsD histograms vs distributions.** Distributions aggregate server-side and can carry more tag combos cheaply-ish; know which one you are emitting.

## The agent-side fix

When you find the offending tag: remove it at emission (client code), or use the agent/metrics filtering to drop the tag before submission. Fixing it in dashboards does nothing, the series are already billed at ingest.

## When to use this

- This covers exactly what the title says: Datadog custom metrics billing.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_eNAxDUlXYhBHj2g_cRmSAw). Version: `skv_H4ZEI2XOFWGcflk5VPZUGA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
