---
name: "qualtrics-export-fails-with-error-surv-5e5b9de1e024dac2"
description: "Qualtrics export fails with error survey response data is corrupt"
metadata:
  skill_id: "skl_ONe_mP5uYDIDkSLyENW05A"
  title: "Qualtrics export fails with error survey response data is corrupt"
  version: "skv_ee189qZQJt6j7Yhvrazm-w"
  updated: "2026-11-16T01:53:45.740821+00:00"
  canonical_url: "https://vectle.com/skills/skl_ONe_mP5uYDIDkSLyENW05A"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Retry the export once with the same settings.

Export a narrow recent date range that you know contains clean test responses.

Widen the range in halves until the export fails again.

Within that window, export without file-upload questions and without embedded data fields.

Inspect the responses in the failing window in the data viewer and look for a response with missing answers, a broken attachment, or embedded values with control characters.

Delete that test or malformed response, or clear its broken attachment, with the survey owner approval if it is a real response.

Rerun the full export.

---

Source: [Vectle](https://vectle.com/skills/skl_ONe_mP5uYDIDkSLyENW05A). Version: `skv_ee189qZQJt6j7Yhvrazm-w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
