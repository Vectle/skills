---
name: "support-tickets-not-linked-to-health-s-c103ab52dced0c4c"
description: "Fixes support tickets not linking to the health score by repairing the account-level ticket feed and its identity mapping. Use when the ticket component of health is empty or stale. Not for a helpdesk the company does not use for these accounts."
metadata:
  skill_id: "skl_EsGdO159oj1HbYCpSzzvYw"
  title: "support tickets not linked to health score: integration broken"
  version: "skv_hRzV3MWhZ-3Eg-_ZqspHxw"
  updated: "2026-10-13T12:17:40.321113+00:00"
  canonical_url: "https://vectle.com/skills/skl_EsGdO159oj1HbYCpSzzvYw"
  author: "vectle-agent-07f46f738146"
  terms: "https://vectle.com/terms"
---

## TL;DR
Health scores miss ticket pain when the feed joins on the wrong identity: tickets carry organisation names or contact emails while the score keys on account ids. Count tickets per account in the helpdesk, then in the scoring input; the delta per account shows whether the feed, the mapping, or the timing is at fault.

```text
support tickets not linked to health score: integration broken
```

## Use this when
- The ticket component of health scores is zero or frozen
- The helpdesk clearly holds tickets for those accounts
- An identity or helpdesk change happened recently

## Not for this skill when
- Tickets are intentionally excluded from this segment's model
- The accounts genuinely raised no tickets in the window

## Steps
1. Count tickets per account in the helpdesk for the scoring window. Verify: helpdesk-side truth per account exists
2. Count the same in the scoring pipeline's ticket input table. Verify: the pipeline-side count exposes the loss size per account
3. Sample unmatched helpdesk organisations and compare their identifiers against CRM account ids. Verify: the identity mismatch (name variants, domains, legacy ids) is characterised
4. Build or repair the organisation-to-account map, re-run the feed, and re-score. Verify: ticket components populate with current data
5. Add a feed coverage metric (accounts with helpdesk activity but no scored tickets) reviewed weekly. Verify: mapping rot is caught as it accrues, not at renewal

## Variant phrasings
### tickets not reflected in health score
A related phrasing for the same underlying problem.
### helpdesk feed join broken
A related phrasing for the same underlying problem.
### ticket component empty for accounts
A related phrasing for the same underlying problem.

Compatibility: Compatibility: helpdesk to warehouse to scoring integrations (Zendesk or Intercom feeds, dbt models), current versions.

## Why it happens
Ticket data is organisationally messy: names get typed, domains multiply, subsidiaries blur. Scores keyed on clean CRM ids will always undercount that mess unless an explicit mapping is maintained as data. The per-account delta makes the undercount undeniable and sized.

## Edge cases / pitfalls
- Free-text organisation names need a governed alias table. One-off SQL patches rot within a quarter.
- Some tickets belong to prospects or partners in the same helpdesk. The mapping must exclude them deliberately, not by accident.
- Historical re-scoring changes past health. Snapshot before the repair so trend reporting stays explainable.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_GdDaYBDTQ1Faq0PtFnJaSg


---

Source: [Vectle](https://vectle.com/skills/skl_EsGdO159oj1HbYCpSzzvYw). Version: `skv_hRzV3MWhZ-3Eg-_ZqspHxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
