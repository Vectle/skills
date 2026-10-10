---
name: "pinecone-workflow-migrate-a-pod-based-b13ce35f0b97b8cd"
description: "Two steps with no in-place conversion: save the pod index as a collection, then create the serverless index from it. Pause writes first if you need zero divergence. Not the full reference manual."
metadata:
  skill_id: "skl_M2ADSYdt4p9icNB1bPauNA"
  title: "Pinecone workflow: migrate a pod-based index to serverless"
  version: "skv_6M6s1aXYnI4fsd833b8NYw"
  updated: "2026-10-03T14:03:54.607699+00:00"
  canonical_url: "https://vectle.com/skills/skl_M2ADSYdt4p9icNB1bPauNA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Two steps with no in-place conversion: save the pod index as a collection, then create the serverless index from it. Pause writes first if you need zero divergence. Migrate pod-based index to serverless There is no in-place conversion. Create the new serverless index from the collection.

# Migrate pod-based index to serverless

There is no in-place conversion. The migration is two steps, and you keep both indexes until you cut over.

## Steps

1. **Decide on downtime.** If any divergence between old and new is unacceptable, pause traffic to the pod-based index before starting. The docs call this out explicitly.
2. **Save the pod index as a collection.** A collection is a static copy of the index. Creating it takes time proportional to index size; poll until it is ready.
3. **Create the new serverless index from the collection.** Same dimension and metric (they carry over); choose the serverless region.
4. **Verify the copy.** Compare `describe_index_stats` totals between the pod index and the new serverless index. Run a sample of queries against both and compare top results.
5. **Cut over reads.** Point the application at the new index. Keep the pod index for a rollback window.
6. **Decommission.** After the rollback window with no issues, delete the pod index to stop pod-hour billing.

## Ordering constraints

Collection before index creation; verification before cutover; cutover before deletion. Skipping verification is how silent data loss ships.

## Traps

1. Writing to the pod index during migration: those writes are not in the collection. Pause writes or re-sync the delta afterward.
2. Forgetting the pod index still bills after cutover. Deletion is a deliberate final step, not an afterthought.
3. Assuming dimension or metric can change in the move. They cannot; the new index inherits them.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_M2ADSYdt4p9icNB1bPauNA). Version: `skv_6M6s1aXYnI4fsd833b8NYw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
