---
name: "investigate-performance-degradation-of-ba8b66ec1d915924"
description: "Guide Investigate performance degradation of pgvector 0.8.0 at neon: We need to investigate and fix the issue before merging the PR. https://github.com/neondatabase/neon/pull/9733 The pgvector 0.8. Use this when you hit exactly this in Investigate. Not for different errors or different tools."
metadata:
  skill_id: "skl_oHXrBgNFY_c6HY2KzcFFAQ"
  title: "Investigate performance degradation of pgvector 0.8.0 at neon"
  version: "skv_MTVn7oBsZfLGHngEQVashg"
  updated: "2026-10-03T04:43:39.275352+00:00"
  canonical_url: "https://vectle.com/skills/skl_oHXrBgNFY_c6HY2KzcFFAQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: We need to investigate and fix the issue before merging the PR. https://github.com/neondatabase/neon/pull/9733 The pgvector 0.8.0 bench has run to completion successfully but pgvector indexing time in this run has been 1h47m while prior run with 0.7.4 was 1h12 minutes. - pgvector 0.8.0 Run 1 1h47 https://github.com/neondatabase/neon/actions/runs/11804399332/job/32884522153 Run 2 - 5h53 (!!) https://github.com/neondatabase/neon/actions/runs/11809885891/job/32900971252 - pgvector 0.7.4: 1h12 https:/

[hlinnaka (maintainer)]: per slack discussion, this was an issue with autoscaling, not pgvector. Latest benchmark runs with 0.8.0 don't show a regression anymore.

Context:
GitHub issue neondatabase/neon#9892 (closed, 1 comments): New version of the extension is available, but it shows performance degradation in our benchmark. We need to investigate and fix the issue before merging the PR. https://github.com/neondatabase/neon/pull/9733 The pgvector 0.8.0 bench has run to completion successfully but pgvector indexing time in this run has been 1h47m while prior run with 0.7.4 was 1h12 minutes. - pgvector 0.8.0 Run 1 1h47 https://github.com/neondatabase/neon/actions/runs/11804399332/job/32884522153 Run 2 - 5h53 (!!) https://github.com/neondatabase/neon/actions/runs/11809885891/job/32900971252 - pgvector 0.7.4: 1h12 https:/

## When to use
You hit exactly this: Investigate performance degradation of pgvector 0.8.0 at neon in Investigate.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Investigate (versions mentioned here: 0.8.0, 0.7.4).

---

Source: [Vectle](https://vectle.com/skills/skl_oHXrBgNFY_c6HY2KzcFFAQ). Version: `skv_MTVn7oBsZfLGHngEQVashg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
