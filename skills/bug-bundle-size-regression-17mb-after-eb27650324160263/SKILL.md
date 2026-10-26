---
name: "bug-bundle-size-regression-17mb-after-eb27650324160263"
description: "Fixes the +17 MB bundle size regression blocking Cloudflare Workers deployments by upgrading mastra packages past the release containing the fix. The cause was @mastra/rag pulled in as a dependency of @mastra/memory just for its chunking utils. Use when a Mastra update bloats your bundle. Not for bundle issues unrelated to Mastra."
metadata:
  skill_id: "skl_GCUPJwrhsw4TvRog-gnRqA"
  title: "[BUG] Bundle size regression (+17mb) after update is blocking cloudflare workers deployments"
  version: "skv_F7CInYDtmvI96ItttMN48A"
  updated: "2026-10-03T04:45:52.230973+00:00"
  canonical_url: "https://vectle.com/skills/skl_GCUPJwrhsw4TvRog-gnRqA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/mastra-ai/mastra/issues/3309\"]"
---

Fix first: upgrade your mastra packages past the release containing the fix. If you are pinned on an alpha, move to a newer alpha.

```text
[BUG] Bundle size regression (+17mb) after update is blocking cloudflare workers deployments
```

1. Upgrade @mastra/memory (and the rest of your mastra packages) past the fixed release.
2. Rebuild and check the bundle size. Expected: back under the Cloudflare Workers limit, deploys unblocked.

When to use: a Mastra update suddenly adds ~17 MB to your bundle and Workers deployments start failing.

When not to use: bundle bloat that has nothing to do with Mastra.

Compatibility: Mastra (@mastra/memory, @mastra/rag). Fixed in the PR linked on the issue; the maintainers also added bundle size tests to prevent a repeat.

Variants:
- "mastra bundle size regression"
- "mastra cloudflare workers deployment blocked"
- "@mastra/memory bundle too large"

Root cause: @mastra/rag was added as a dependency of @mastra/memory just to use its chunking utils, dragging the whole package into every bundle.

Edge cases: if you are pinned on an alpha for other reasons, a newer alpha has the fix; you dont need to jump to stable.

---

Source: [Vectle](https://vectle.com/skills/skl_GCUPJwrhsw4TvRog-gnRqA). Version: `skv_F7CInYDtmvI96ItttMN48A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
