---
name: "apideck-list-endpoints-use-cursor-pagi-61deda980a9ecd6f"
description: "Guide Apideck list endpoints use cursor pagination, not page numbers: Use the SDK helpers (for await...of in Node, .next() in Python/Go/.NET) instead of hand-rolling cursors. Use this when you hit exactly this in Apideck. Not for different errors or different tools."
metadata:
  skill_id: "skl_r1eLSxHeb4lWPloPBBvTfw"
  title: "Apideck list endpoints use cursor pagination, not page numbers"
  version: "skv_puJj7f-2AOkqb6KODMDcCA"
  updated: "2026-10-03T04:44:53.288071+00:00"
  canonical_url: "https://vectle.com/skills/skl_r1eLSxHeb4lWPloPBBvTfw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Use the SDK helpers (for await...of in Node, .next() in Python/Go/.NET) instead of hand-rolling cursors. Web (Apideck official best-practices skill, apideck-libraries/api-skills): documents pagination gotchas agents hit. Apideck uses cursor-based pagination on all list endpoints: iterate until meta.cursors.next is null, never assume one page returns everything. limit is 1-200 with default 20, so large syncs need bigger pages.

Web (Apideck official best-practices skill, apideck-libraries/api-skills): documents pagination gotchas agents hit. Apideck uses cursor-based pagination on all list endpoints: iterate until meta.cursors.next is null, never assume one page returns everything. limit is 1-200 with default 20, so large syncs need bigger pages. Use the SDK helpers (for await...of in Node, .next() in Python/Go/.NET) instead of hand-rolling cursors. For incremental sync, use filter[updated_since] with an ISO 8601 timestamp to fetch only changed records. Narrow server-side with filter and fields params; do not fetch everything and filter client-side.

## What to do
Paginating Apideck list calls: always loop on meta.cursors.next until it is null, and set limit up to 200 so you are not crawling at 20 records a page. Use the SDK pagination helpers instead of manual cursor plumbing. For sync jobs, combine filter[updated_since] with a stored timestamp so each run only pulls changed records, and pass fields to request only the columns you need. Fetching full records and filtering client-side wastes quota and breaks at scale.

## When to use
You hit exactly this: Apideck list endpoints use cursor pagination, not page numbers in Apideck.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Apideck.

---

Source: [Vectle](https://vectle.com/skills/skl_r1eLSxHeb4lWPloPBBvTfw). Version: `skv_puJj7f-2AOkqb6KODMDcCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
