---
name: "clinicaltrials-gov-api-returns-404-err-5302f0681603e896"
description: "ClinicalTrials.gov API returns 404 error for NCT number lookup fails"
metadata:
  skill_id: "skl_v_XCHJ_IH2ecHAJAFcRDKA"
  title: "ClinicalTrials.gov API returns 404 error for NCT number lookup fails"
  version: "skv_9A4jIylHA4SKTJKDzWM-lw"
  updated: "2026-11-04T13:57:58.830219+00:00"
  canonical_url: "https://vectle.com/skills/skl_v_XCHJ_IH2ecHAJAFcRDKA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Validate the NCT number format: the letters NCT followed by exactly 8 digits, with no spaces or dashes.

Call the v2 single-study endpoint with the id in the path, for example the studies path followed by the NCT id, and request JSON format.

Search the same id in the ClinicalTrials.gov web interface.

If the web page exists but the API 404s, check for a transposed digit by searching the registry by the exact trial title.

Correct the stored id, or flag the record for human review if neither API nor web search finds it. Withdrawn pre-registration entries can legitimately be absent.

Re-run the matcher lookup for the corrected id and log the correction.

---

Source: [Vectle](https://vectle.com/skills/skl_v_XCHJ_IH2ecHAJAFcRDKA). Version: `skv_9A4jIylHA4SKTJKDzWM-lw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
