---
name: "unable-to-update-elasticsearch-mapping-1913701664b882e3"
description: "Fixes Temporal failing to create custom search attributes with 'unable to update Elasticsearch mapping: elastic: Error 403' on AWS OpenSearch. Use this on self-hosted Temporal 1.20.4 in dual visibility mode, even as the OpenSearch master user. Not for real permission problems or single-store setups."
metadata:
  skill_id: "skl_CmXy0yE5c0iRchIrzPgIog"
  title: "Unable to update Elasticsearch mapping: elastic: Error 403 on Create Custom Attributes"
  version: "skv_DSv60XcUm9DSVPfk63HQKA"
  updated: "2026-10-03T04:46:57.061566+00:00"
  canonical_url: "https://vectle.com/skills/skl_CmXy0yE5c0iRchIrzPgIog"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if `temporal operator search-attribute create` fails with `unable to update Elasticsearch mapping: elastic: Error 403` even as the OpenSearch master user, check for dual visibility mode. Adding search attributes is not supported when both `visibilityStore` (Postgres) and `advancedVisibilityStore` (OpenSearch) are set; that mode exists only for migrating visibility stores. Keep only `advancedVisibilityStore` and remove the `visibilityStore` and `secondaryVisibilityStore` keys plus the `datastores.visibility` section.

```text
unable to update Elasticsearch mapping: elastic: Error 403 (Forbidden): security_exception
```

## Steps

1. Inspect your Temporal config for both `visibilityStore` and `advancedVisibilityStore` being set.

2. Remove the `visibilityStore` and `secondaryVisibilityStore` keys and the `datastores.visibility` section, keeping only `advancedVisibilityStore` pointing at OpenSearch.

3. Restart Temporal and re-run the search-attribute create.

   Expected: the attribute creates. Success check: the custom search attribute is usable in queries.

## When to use this

- Self-hosted Temporal 1.20.4 with AWS OpenSearch, 403 on attribute creation despite full cluster access.
- Dual visibility mode is configured.

## When NOT to use this

- Single visibility store already; the 403 is a real permission issue then.
- You are mid-migration and need dual mode; finish the migration first, then add attributes.

## Compatibility

- Temporal 1.20.4 with OpenSearch visibility.

## Variant phrasings

- "temporal unable to update elasticsearch mapping 403"
- "temporal search attribute dual visibility"

## Root cause

The Postgres visibility store does not support custom search attributes anyway, so the dual-mode write path rejects the mapping update with a 403 that looks like a permissions error.

## Edge cases

- Do not try to work around it with broader OpenSearch permissions; the master user already failed.

Source: https://vectle.com/threads/thr_gqbJvitEqUKtGa9gjfLBtQ

---

Source: [Vectle](https://vectle.com/skills/skl_CmXy0yE5c0iRchIrzPgIog). Version: `skv_DSv60XcUm9DSVPfk63HQKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
