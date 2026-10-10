---
name: "pinecone-workflow-blue-green-index-dep-2b4de2cbaa32c4bb"
description: "Build the new embedding version in a fresh index or namespace, verify recall parity, flip readers, then delete the old. Never re-embed in place on a serving index."
metadata:
  skill_id: "skl_q38hHekysQZR22FF3zaHsQ"
  title: "Pinecone workflow: blue-green index deploys for re-embeds"
  version: "skv_wRXeTr9InEXA9StWmcaSaA"
  updated: "2026-10-03T14:16:02.485285+00:00"
  canonical_url: "https://vectle.com/skills/skl_q38hHekysQZR22FF3zaHsQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Build the new embedding version in a fresh index or namespace, verify recall parity, flip readers, then delete the old. Never re-embed in place on a serving index. Build green. Create docs-v2 (new index) or a v2 namespace with the new dimension and metric.

## The fix

1. **Build green.** Create `docs-v2` (new index) or a `v2` namespace with the new dimension and metric. Ingest the full corpus there.

2. **Verify green.** Stats totals match the corpus; sample queries return sane results; run your recall eval set against green and compare to blue's baseline.

3. **Dual-read briefly.** Send a slice of production queries to green and log both result sets. Investigate divergences before full cutover.

4. **Flip.** Update the serving config to the green index or namespace. One config value, one deploy.

5. **Hold blue.** Keep the old index for a rollback window (days, not hours). Rollback is a config flip back.

6. **Delete blue.** After the window, delete to stop billing. Confirm no code still references the old name.

7. Flipping before the ingest finished: green serves partial data and nobody notices for a week. Gate the flip on stats totals.

8. Two writers during dual-read: writes must go to both or to green only with a backfill; pick one and enforce it.

9. Forgetting blue bills: set a calendar reminder at flip time for the deletion. Pod indexes especially.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_q38hHekysQZR22FF3zaHsQ). Version: `skv_wRXeTr9InEXA9StWmcaSaA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
