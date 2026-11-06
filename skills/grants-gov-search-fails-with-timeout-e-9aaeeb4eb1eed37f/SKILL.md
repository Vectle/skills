---
name: "grants-gov-search-fails-with-timeout-e-9aaeeb4eb1eed37f"
description: "Grants.gov search fails with timeout error funding opportunity lookup broken"
metadata:
  skill_id: "skl_z2MgOA2q-hY8gKO3hD_4kA"
  title: "Grants.gov search fails with timeout error funding opportunity lookup broken"
  version: "skv_XIEvO_E8TIEsWoEk_ku3ew"
  updated: "2026-11-06T01:54:28.97568+00:00"
  canonical_url: "https://vectle.com/skills/skl_z2MgOA2q-hY8gKO3hD_4kA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Search by opportunity number first if you have one.** Enter the exact opportunity number with no keywords. Expected: the single opportunity opens directly, proving the lookup path works and the problem is query breadth, not the service.

**Cut the keyword list to one term.** Replace a multi word phrase with the single most specific noun, for example the program name. Success check: results return within a few seconds instead of timing out.

**Limit the opportunity status.** Select posted and forecasted only, and clear closed and archived. Expected: the result count drops sharply and the page loads.

**Limit the date range.** Set a posted date window such as the last 90 days when the tracker only needs current calls. Success check: older, irrelevant opportunities no longer inflate the search.

**Save the working search instead of rebuilding it.** Once a narrow search works, save it and reuse it for the daily tracker check. Expected: the same filters load each time and the timeout does not recur from a rebuilt broad query.

**Retry a service side timeout once, later.** If even an opportunity number search times out, note the time, wait, and retry the same exact search. Success check: the same query succeeds without changes, confirming a transient service slowdown rather than a query problem.

---

Source: [Vectle](https://vectle.com/skills/skl_z2MgOA2q-hY8gKO3hD_4kA). Version: `skv_XIEvO_E8TIEsWoEk_ku3ew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
