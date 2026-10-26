---
name: "partitionkey-value-must-be-supplied-fo-d14eb9317a5e9aec"
description: "Diagnoses the Cosmos DB error 'PartitionKey value must be supplied for this operation' when calling stored procedures or operations on a partitioned collection. Use when an agent sees this from the .NET SDK or any DocumentDB client. Covers passing RequestOptions with the partition key and making sure the document carries the partition key property. Not for throughput or auth errors."
metadata:
  skill_id: "skl_I1EMh1evHph4qEVN8B5CYA"
  title: "PartitionKey value must be supplied for this operation"
  version: "skv_ZMRacpiWUFluuxSt6Gdztw"
  updated: "2026-10-03T04:49:17.344808+00:00"
  canonical_url: "https://vectle.com/skills/skl_I1EMh1evHph4qEVN8B5CYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://exchangetuts.com/how-do-you-pass-a-partitionkey-to-execute-a-storedprocedure-in-azure-documentdb-net-sdk-1636373616892807\"]"
---

# PartitionKey value must be supplied for this operation

## TL;DR
You are calling a stored procedure (or another partition-scoped operation) without saying which partition it belongs to. Pass the partition key in the request options, and make sure your documents actually carry the partition key property. One of those two is missing.

## The error
```
PartitionKey value must be supplied for this operation.
```

## Fix it
1. Pass the partition key with the call. In the .NET SDK that means RequestOptions carrying the key: `new RequestOptions { PartitionKey = new PartitionKey("[your-partition-key-value]") }`. Expected: the stored procedure executes against the right partition.
2. Check that the document you are writing includes the partition key property the collection is partitioned on. Expected: the document has the property with a non-null value.
3. Confirm the partition key path on the collection matches what your code sends. A collection partitioned on `/tenantId` needs `tenantId` in the document, not `tenant_id`. Expected: the paths match exactly.
4. For stored procedures, remember they run inside one partition. There is no cross-partition stored procedure call. Expected: the procedure logic stays within a single partition key value.
5. Retry the operation. Expected: it succeeds.

## When to use this
- An agent sees "PartitionKey value must be supplied for this operation" from Cosmos DB or the DocumentDB SDK.
- Stored procedure calls against a partitioned collection.

## When NOT to use this
- 429 throttling or RequestRateTooLarge. Those are throughput, not partition keys.
- 401 or 403 auth errors. Those are keys and permissions.

## Compatibility
- Azure Cosmos DB (SQL API), DocumentDB .NET SDK and equivalents.

### Variant phrasings
- "PartitionKey value must be supplied"
- Stored procedure failures on partitioned collections

## Root cause
Partitioned collections route every operation by the partition key. A stored procedure executes transactionally inside one partition, so the service refuses to run it without knowing which partition you mean. The two classic misses are forgetting the RequestOptions and writing documents that lack the partition key property entirely.

## Edge cases
- Migrating from a single-partition (old DocumentDB) collection to partitioned: old code has no partition key anywhere and every call needs updating.
- The partition key value is case-sensitive. "TenantA" and "tenanta" are different partitions.


---

Source: [Vectle](https://vectle.com/skills/skl_I1EMh1evHph4qEVN8B5CYA). Version: `skv_ZMRacpiWUFluuxSt6Gdztw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
