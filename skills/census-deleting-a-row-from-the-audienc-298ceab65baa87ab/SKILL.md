---
name: "census-deleting-a-row-from-the-audienc-298ceab65baa87ab"
description: "Fix for Census: deleting a row from the audiences table invalidates the audience and fails syncs: But the audience list itself refreshes on a 15-minute background job: adding a row creates a new audience at the next refresh, updating a row renames it, and removing a row marks the audience. Use this when you hit exactly this in Census. Not for different errors or different tools."
metadata:
  skill_id: "skl_5BFc1pG9ANsjK6Z81hsGiA"
  title: "Census: deleting a row from the audiences table invalidates the audience and fails syncs"
  version: "skv_emDBpejMteTV8pSufF7NVw"
  updated: "2026-10-03T04:48:55.907103+00:00"
  canonical_url: "https://vectle.com/skills/skl_5BFc1pG9ANsjK6Z81hsGiA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.getcensus.com/audience-hub/getting-started/warehouse-managed-audiences\"]"
---

TL;DR: But the audience list itself refreshes on a 15-minute background job: adding a row creates a new audience at the next refresh, updating a row renames it, and removing a row marks the audience invalid, at which point any related syncs begin to fail. [Official Census docs (warehouse-managed audiences)]: Audience membership lives in your warehouse's audience membership table, and Census queries it just-in-time, so adding or removing rows updates membership on the next sync.

```text
Census: deleting a row from the audiences table invalidates the audience and fails syncs
```

[Official Census docs (warehouse-managed audiences)]: Audience membership lives in your warehouse's audience membership table, and Census queries it just-in-time, so adding or removing rows updates membership on the next sync. But the audience list itself refreshes on a 15-minute background job: adding a row creates a new audience at the next refresh, updating a row renames it, and removing a row marks the audience invalid, at which point any related syncs begin to fail. You can manually delete the invalid audience or re-add the row. Never delete rows from the audiences table casually; that single change can break downstream syncs.

Context: Official docs (Census/Activations warehouse-managed audiences): documents the audience lifecycle gotcha that trips agents. Census refreshes warehouse-managed audiences on a 15-minute background job, and deleting a row from the audiences table marks the audience invalid, which makes related syncs start failing.

## When to use
You hit exactly this: Census: deleting a row from the audiences table invalidates the audience and fails syncs in Census.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Census.

## Edge cases
- Context: Official docs (Census/Activations warehouse-managed audiences): documents the audience lifecycle gotcha that trips agents.

---

Source: [Vectle](https://vectle.com/skills/skl_5BFc1pG9ANsjK6Z81hsGiA). Version: `skv_emDBpejMteTV8pSufF7NVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
