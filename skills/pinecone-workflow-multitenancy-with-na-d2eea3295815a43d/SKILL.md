---
name: "pinecone-workflow-multitenancy-with-na-d2eea3295815a43d"
description: "One index, one namespace per tenant: isolated reads, writes, and deletes with a single dimension and bill. Enforce the namespace at the data-access layer, never trust caller input."
metadata:
  skill_id: "skl_6CuHWzS4cjtK8lu9LaDwmg"
  title: "Pinecone workflow: multitenancy with namespaces"
  version: "skv_AgBmmjBpD29nkbgUPwnyVg"
  updated: "2026-10-03T14:01:20.062544+00:00"
  canonical_url: "https://vectle.com/skills/skl_6CuHWzS4cjtK8lu9LaDwmg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** One index, one namespace per tenant: isolated reads, writes, and deletes with a single dimension and bill. Enforce the namespace at the data-access layer, never trust caller input. Create one index with the shared embedding dimension and metric. All tenants must use the same embedding model.

# Multitenancy on namespaces

## The pattern

One index serves all tenants; each tenant's vectors live in its namespace. Every data-plane call carries the tenant's namespace. Deletes are per-tenant (`delete_all` in the namespace). Stats break down per namespace for per-tenant observability.

## Steps

1. **Create one index** with the shared embedding dimension and metric. All tenants must use the same embedding model.
2. **Derive the namespace server-side** from the authenticated tenant id. Never accept a namespace from client input; that is a cross-tenant read vulnerability.
3. **Write a data-access wrapper** that takes `tenant_id`, maps it to a namespace string, and passes it to every upsert, query, fetch, delete, and stats call. No raw index calls outside the wrapper.
4. **Onboard tenants** by upserting into their namespace; namespaces auto-create.
5. **Offboard tenants** with `delete(delete_all=True, namespace=...)`. Verify the namespace count hits zero in stats.
6. **Monitor per namespace** with `describe_index_stats` filtering, and alert on per-tenant growth anomalies.

## Traps

1. Forgetting the namespace on one call site: that site reads or writes the default namespace, leaking data across tenants or losing writes.
2. Tenant ids with dots, uppercase, or spaces as namespace strings: sanitize to the same charset rules as index names.
3. Tenants needing different dimensions or models: namespaces share the index config, so this needs separate indexes per cohort, not per tenant.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_6CuHWzS4cjtK8lu9LaDwmg). Version: `skv_AgBmmjBpD29nkbgUPwnyVg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
