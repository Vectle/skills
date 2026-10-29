---
name: "fix-discovery-pagination-timeout-error-dac22bbe59b2ed73"
description: "Fix discovery pagination, timeout errors, and provider-aware health"
metadata:
  skill_id: "skl_WhxHtd5mCrPp2pFoEBS8lg"
  title: "Fix discovery pagination, timeout errors, and provider-aware health"
  version: "skv_1ivvRD7-hQpbDUmGF2IBxg"
  updated: "2026-10-28T15:23:22.998802+00:00"
  canonical_url: "https://vectle.com/skills/skl_WhxHtd5mCrPp2pFoEBS8lg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

[jaaacki]: ## Root-cause ruling for the recurring discovery partial-results defect Read-only trace of exact head `dacee986661817f9b6d97e37b62177bb37a7f902`: timeouts were wrapped around an atomic fetch-all-then-validate-all flow. Retained partials are raw provider rows, not accepted candidates. This affects both late Brave pagination and cancellation partway through either provider's normalization. The root trace performed no implementation, tests, CI, or provider calls; the checks below must be implemented/run by the author. ### Minimum coherent fix , m2 owns implementation - `shape_candidates`: accept the one absolute deadline; bound each URL-validation await by remaining time and check between rows. On its OWN deadline expiry, return the already accepted prefix plus a small completion indicator. Preserve external cancellation and unrelated exceptions. Incomplete empty is not a completed no-match answer. Do not bypass URL/DNS validation or add grace time. - `BraveKeyPool._search_with_key`: normalize each page BEFORE requesting the next; accumulate validated candidates, deduplicate across pages, and count accepted candidates toward the requested limit. All normal/error partials must now be accepted candidates, never raw rows. Preserve accepted prefixes when a later fetch or normalization expires. - `BraveKeyPool.search`: retain request-local `(results, retry_after)` and `None` versus g

Context: GitHub issue jaaacki/web-search-tool#44 (open, 3 comments, reported 2026-10-21): ## Phase and dependency Phase 2. Coordinate with the final Firecrawl provider order; source-level correctness can be fixed before Firecrawl exists. ## Verified findings at dec8da4 - `api/app.py:869-891`: Brave offset advances by returned result count, but the API uses zero-based page indices 0..9. Page size also shrinks on later requests, changing offset meaning. - `api/app.py:672-683`: discovery timeout followed by failed/timed-out SearXNG fallback becomes `ok:true, results:[]`. - `api/app.py:534-565`: health fails solely on SearXNG even when configured Brave discovery can serve requests. Re

---

Source: [Vectle](https://vectle.com/skills/skl_WhxHtd5mCrPp2pFoEBS8lg). Version: `skv_1ivvRD7-hQpbDUmGF2IBxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
