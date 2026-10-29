---
name: "securityscorecard-error-vendor-domain-786a05715009a9e6"
description: "SecurityScorecard error vendor domain mapped to parent company findings"
metadata:
  skill_id: "skl_fovEj_D_S6BZc5xoXVv_lw"
  title: "SecurityScorecard error vendor domain mapped to parent company findings"
  version: "skv_fg8cS9pKrKA2VdZzwPMSkA"
  updated: "2026-10-29T01:57:25.560208+00:00"
  canonical_url: "https://vectle.com/skills/skl_fovEj_D_S6BZc5xoXVv_lw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the vendor scorecard and go to the digital footprint or domains view. Expected: you can list every domain counted toward the vendor score, and the parent company domains stand out by name or registration.

Pick one wrong finding and open its detail. Expected: the affected asset is a parent domain, which confirms an attribution problem rather than a real vendor issue.

Compare against the parent company scorecard. Expected: the same domains and findings appear there too, confirming the domain set overlaps between the two scorecards.

Remove the parent domains from the vendor view you control: if you built a custom scorecard or portfolio for the vendor, edit its domain scope to the vendor-operated domains only. Expected: the vendor score recalculates from its own footprint and the parent findings leave the assessment.

For the automatic public scorecard mapping, submit an attribution correction request with evidence the domain is operated by the parent (registration records, the parent's own site listing the domain, certificate organisation fields). Expected: the request is logged as an attribution fix, which moves the domain for all viewers rather than only your portfolio.

While the correction is pending, annotate the vendor record in your risk register: note which findings are parent-attributed so reviewers do not score the vendor on them. Expected: the current assessment shows the adjusted view and the pending correction side by side.

Recheck after the next scorecard refresh cycle. Expected: the vendor footprint no longer lists the parent domains and new parent findings stop appearing in the vendor assessment.

---

Source: [Vectle](https://vectle.com/skills/skl_fovEj_D_S6BZc5xoXVv_lw). Version: `skv_fg8cS9pKrKA2VdZzwPMSkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
