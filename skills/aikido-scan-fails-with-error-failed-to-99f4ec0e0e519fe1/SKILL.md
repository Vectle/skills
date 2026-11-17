---
name: "aikido-scan-fails-with-error-failed-to-99f4ec0e0e519fe1"
description: "aikido scan fails with error failed to clone repository"
metadata:
  skill_id: "skl_cCgNLBgp8hNVPDBccObRyw"
  title: "aikido scan fails with error failed to clone repository"
  version: "skv_ZaOVQee_-gDc08R9AlGnSA"
  updated: "2026-11-17T13:52:21.895451+00:00"
  canonical_url: "https://vectle.com/skills/skl_cCgNLBgp8hNVPDBccObRyw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the failed scan details and note the exact repository and branch the scan tried to clone.

Check that the scanner integration still has read access to that repository in your code host.

Confirm the repository has not been renamed, moved, or made private since the integration was connected.

If the repository uses branch protection or an allowlist, confirm the scanner is allowed to fetch the target branch.

Reconnect or refresh the code host integration if access was revoked, then trigger a fresh scan instead of retrying the old one.

Open the completed scan and confirm findings or a clean result are shown for the expected commit.

---

Source: [Vectle](https://vectle.com/skills/skl_cCgNLBgp8hNVPDBccObRyw). Version: `skv_ZaOVQee_-gDc08R9AlGnSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
