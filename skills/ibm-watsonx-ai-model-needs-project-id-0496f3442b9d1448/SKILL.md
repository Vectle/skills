---
name: "ibm-watsonx-ai-model-needs-project-id-0496f3442b9d1448"
description: "Guide ibm-watsonx-ai: Model needs project_id or space_id, one is required: If your ibm-watsonx-ai Model or ModelInference call fails at construction, check that you passed exactly one of project_id or space_id; one of the two is required, not optional. Use this when you hit exactly this in ibm-watsonx-ai. Not for different errors or different tools."
metadata:
  skill_id: "skl_Vbh04zWmcl8PihOP1dxp3w"
  title: "ibm-watsonx-ai: Model needs project_id or space_id, one is required"
  version: "skv_JHeG5v0MIzabpEQejf9nZQ"
  updated: "2026-10-03T05:05:46.029759+00:00"
  canonical_url: "https://vectle.com/skills/skl_Vbh04zWmcl8PihOP1dxp3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/fm_model.html\"]"
---

TL;DR: If your ibm-watsonx-ai Model or ModelInference call fails at construction, check that you passed exactly one of project_id or space_id; one of the two is required, not optional. You can copy the project_id from the Project's Manage tab (Project -> Manage -> General -> Details). Set params as a dict of GenTextParamsMetaNames (call GenParams().get_example_values() to see examples).

## Fix
1. If your ibm-watsonx-ai Model or ModelInference call fails at construction, check that you passed exactly one of project_id or space_id; one of the two is required, not optional.
   Expected: this specific failure stops.
2. You can copy the project_id from the Project's Manage tab (Project -> Manage -> General -> Details).
   Expected: this specific failure stops.
3. Set params as a dict of GenTextParamsMetaNames (call GenParams().get_example_values() to see examples).
   Expected: this specific failure stops.
4. If a valid model id is rejected, the validate=True default may be at fault; pass validate=False for brand-new or custom model ids.
   Expected: this specific failure stops.

## When to use
You hit exactly this: ibm-watsonx-ai: Model needs project_id or space_id, one is required in ibm-watsonx-ai.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
ibm-watsonx-ai.

---

Source: [Vectle](https://vectle.com/skills/skl_Vbh04zWmcl8PihOP1dxp3w). Version: `skv_JHeG5v0MIzabpEQejf9nZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
