---
name: "linksquares-clause-error-compare-view-989a0c22e4f002a4"
description: "LinkSquares clause error compare view fails to highlight changed wording"
metadata:
  skill_id: "skl_gKzqIM542SLiGuHXGGGGSQ"
  title: "LinkSquares clause error compare view fails to highlight changed wording"
  version: "skv_6jE1sAEKZe05-sXCNPd7JA"
  updated: "2026-10-30T01:54:23.357104+00:00"
  canonical_url: "https://vectle.com/skills/skl_gKzqIM542SLiGuHXGGGGSQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the failure on one named agreement and record the full problem text plus the versions involved. Verify: the compare view opens, both versions load, and a clause you know changed shows no highlight, so the miss is reproduced on demand, not only seen in a report.

Check the source versions before changing anything. Verify: one version is not a scanned or flattened copy, both have selectable text, and the pair is the prior draft against the latest draft rather than the executed copy compared to itself.

Check the compare and highlight settings for that agreement. Verify: change highlighting is turned on, the comparison is set to wording changes and not only formatting, and no filter is hiding clause level changes.

Apply the specific fix described in the TL;DR on that single agreement first, using a clean native copy if one version was flattened. Verify: the single failing compare now highlights the known changed clause, or the corrected output is visible on the record.

Check neighbouring agreements from the same template or upload batch, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.

Rerun compare on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the task completes and changed wording is highlighted and the original problem does not appear.

Record the fix, the triggering versions and the verification result on the run log so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the rerun result, and it is saved with the run.

---

Source: [Vectle](https://vectle.com/skills/skl_gKzqIM542SLiGuHXGGGGSQ). Version: `skv_6jE1sAEKZe05-sXCNPd7JA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
