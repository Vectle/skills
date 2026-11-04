---
name: "cohort-churn-cohort-definitions-differ-91704f55fc47fb5c"
description: "cohort churn: cohort definitions differ between reports - reconcile them"
metadata:
  skill_id: "skl_qhkqMhEx0_2K66hqihLKeA"
  title: "cohort churn: cohort definitions differ between reports - reconcile them"
  version: "skv_ymccYhuAhqLim3VA7hVOGw"
  updated: "2026-11-03T23:19:38.40897+00:00"
  canonical_url: "https://vectle.com/skills/skl_qhkqMhEx0_2K66hqihLKeA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Freeze one test cell before touching any definition: pick one cohort month and one later month, and export the account-level lists behind both reports for that cell (starting accounts, retained accounts, churned accounts, with account IDs). Verify: both exports exist and can be joined on account ID; if a tool cannot export account lists, rebuild its logic in SQL from raw events or subscriptions first.

Write each report's definition on the six axes, from its actual query or tool settings, not from what its owner believes it does: anchor event (signup, first payment, first activity, activation), period grain (calendar month vs rolling 30 days), churn event (cancellation date, subscription end date, last activity plus a fixed inactivity window, failed payment), denominator (all starters vs only accounts that reached paid), trial, pause, and reactivation handling, and timezone and cutoff time. Verify: a six-row comparison table exists and at least one row differs; if no row differs, the gap is a data bug, not a definition gap, so switch to account-level data debugging.

Diff the two account lists for the frozen cell and classify every account that appears in one list but not the other, or lands in different cells, by which axis explains it: anchored a month later under first-activity than under signup, churned under an inactivity rule but still subscribed, trial accounts in one denominator only, paused accounts counted as churned in one report and retained in the other, reactivations creating a second cohort membership in one report only. Verify: every mismatched account has exactly one axis label and the counts per axis sum to the total gap.

Quantify each axis on the frozen cell by recomputing the cell under report A's definition, then flipping one axis at a time toward report B's definition. Verify: flipping the labelled axes in size order closes the gap to zero, which proves the list of causes is complete and no hidden data difference remains.

Decide the canonical definition in writing with the report consumers: one anchor event, one churn event, and explicit rules for trials, pauses, reactivations, and timezone. Record why: billing-anchored definitions suit revenue questions, activity-anchored definitions suit product engagement questions, and mixing them in one chart is what created the dispute. Verify: the definition is written down, named, dated, and owned by one person or team.

Restate both reports on the canonical definition from raw data, not by adjusting the old outputs, and validate two more cells by hand: one recent cohort and one old cohort, including at least one account from each mismatch class in step 3. Verify: all three validated cells match the restated reports exactly at account level.

Publish the restated numbers with a short note naming the definition and the axes that changed, keep the old series visible for one reporting cycle labelled with its definition, and store the definition and the queries in version control so the next dashboard inherits them instead of re-inventing them. Verify: a reader of either report can find the definition it uses in one click from the chart.

Add a standing check: a monthly reconciliation that recomputes one fresh cohort cell from raw records under the canonical definition and alerts when a report drifts from it beyond a small tolerance. Verify: the check runs on schedule and its first run passes.

---

Source: [Vectle](https://vectle.com/skills/skl_qhkqMhEx0_2K66hqihLKeA). Version: `skv_ymccYhuAhqLim3VA7hVOGw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
