---
name: "only-materialize-the-topmost-serving-v-ffe072eecfa576d0"
description: "Guide Only materialize the topmost serving view, not the whole stack: Materialize only the topmost view that serves results, and keep the intermediate views plain. Do not materialize every view in a stacked definition. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_NKV1wgWyWDV5kkx1eu6h1w"
  title: "Only materialize the topmost serving view, not the whole stack"
  version: "skv_77Ip1plsFnaUt75oLdapdw"
  updated: "2026-10-03T05:07:38.286695+00:00"
  canonical_url: "https://vectle.com/skills/skl_NKV1wgWyWDV5kkx1eu6h1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/materializeinc/agent-skills/blob/HEAD/.agents/skills/materialize-docs/concepts/views/index.md\"]"
---

TL;DR: Materialize only the topmost view that serves results, and keep the intermediate views plain. Do not materialize every view in a stacked definition. If your cluster does both transform and serving, use an indexed view instead of a materialized view; a materialized view in that setup just burns memory for no isolation.

## Fix
1. Materialize only the topmost view that serves results, and keep the intermediate views plain.
   Expected: this specific failure stops.
2. If your cluster does both transform and serving, use an indexed view instead of a materialized view; a materialized view in that setup just burns memory for no isolation.
   Expected: this specific failure stops.
3. Context: Materialize docs Views concept (materializeinc/agent-skills .agents/skills/materialize-docs/concepts/views/index.md): Use a materialized view only for the topmost view whose results will be served; stacked views underneath that exist only to reduce SQL complexity should stay plain views.
   Expected: this specific failure stops.

## Details
Do not materialize every view in a stacked definition. The exception is when the view feeds a sink or SUBSCRIBE, where a materialized view is the right shape. On a shared cluster used for both transform and serving, indexed views beat materialized views; materialized views belong on the compute cluster feeding a sink or SUBSCRIBE, or in a 3-tier setup with the index in the serving cluster.

## When to use
You hit exactly this: Only materialize the topmost serving view, not the whole stack.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title.

---

Source: [Vectle](https://vectle.com/skills/skl_NKV1wgWyWDV5kkx1eu6h1w). Version: `skv_77Ip1plsFnaUt75oLdapdw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
