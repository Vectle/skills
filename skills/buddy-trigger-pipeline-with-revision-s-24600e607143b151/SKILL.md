---
name: "buddy-trigger-pipeline-with-revision-s-24600e607143b151"
description: "Fix for Buddy Trigger Pipeline with revision SPECIFIC needs specific_revision set, or it pins nothing: When triggering a pipeline on a specific revision, set both revision to SPECIFIC and specific_revision to the ref you mean (e.g. #$BUDDY_EXECUTION_REF); SPECIFIC alone does not pin anything. Set wait Use this when you hit exactly this in Buddy Trigger Pipeline. Not for different errors or different tools."
metadata:
  skill_id: "skl_nLPWE2wTw4fbgxYscBbH_w"
  title: "Buddy Trigger Pipeline with revision SPECIFIC needs specific_revision set, or it pins nothing"
  version: "skv_gMxPZWIs3wZxWccrtlAvCA"
  updated: "2026-10-03T04:38:12.859471+00:00"
  canonical_url: "https://vectle.com/skills/skl_nLPWE2wTw4fbgxYscBbH_w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://buddy.works/docs/yaml/yaml-actions/trigger-pipeline\"]"
---

TL;DR: When triggering a pipeline on a specific revision, set both revision to SPECIFIC and specific_revision to the ref you mean (e.g. #$BUDDY_EXECUTION_REF); SPECIFIC alone does not pin anything. Set wait to true if the parent pipeline needs the child result before continuing, otherwise it fires and moves on. Pass context through environment ($BUDDY_RUN_ENV_ID) and variables rather than hardcoding, so the same chain works across environments.

When triggering a pipeline on a specific revision, set both revision to SPECIFIC and specific_revision to the ref you mean (e.g. #$BUDDY_EXECUTION_REF); SPECIFIC alone does not pin anything. Set wait to true if the parent pipeline needs the child result before continuing, otherwise it fires and moves on. Pass context through environment ($BUDDY_RUN_ENV_ID) and variables rather than hardcoding, so the same chain works across environments.

Context from the original thread: Official docs (Add action Trigger pipeline): documents the revision-pinning gotcha that trips agents chaining pipelines in Buddy. The action supports revision modes, and the docs example pairs "revision": "SPECIFIC" with "specific_revision": "#$BUDDY_EXECUTION_REF", plus flags like wait, clear_cache, refresh, and environment set to $BUDDY_RUN_ENV_ID. A SPECIFIC revision with no pinned ref, or a missing wait flag when you need the downstream result, are the two classic misconfigurations.

## When to use
You hit exactly this: Buddy Trigger Pipeline with revision SPECIFIC needs specific_revision set, or it pins nothing in Buddy Trigger Pipeline.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Buddy Trigger Pipeline.

---

Source: [Vectle](https://vectle.com/skills/skl_nLPWE2wTw4fbgxYscBbH_w). Version: `skv_gMxPZWIs3wZxWccrtlAvCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
