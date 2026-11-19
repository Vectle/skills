---
name: "bunny-storage-replication-fails-with-z-bd37b8488ecafc6a"
description: "bunny storage replication fails with zone not replicated error"
metadata:
  skill_id: "skl_pqWQ20MX91eT1-pgC_YK_Q"
  title: "bunny storage replication fails with zone not replicated error"
  version: "skv_9jKwHCJs_WAwcNEioEeKlg"
  updated: "2026-11-19T01:52:46.15903+00:00"
  canonical_url: "https://vectle.com/skills/skl_pqWQ20MX91eT1-pgC_YK_Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open both storage zones in the dashboard and check the replication setting on the main zone.

Confirm the replica zone was created as a replica of the main zone, not as an independent zone.

Upload a small unique test file to the main zone and wait a few minutes.

Check that both zones use the same access path and that the test file name has no special characters that sync tools skip.

If a new replica was just created, wait for the initial replication of existing files to finish before judging it broken.

---

Source: [Vectle](https://vectle.com/skills/skl_pqWQ20MX91eT1-pgC_YK_Q). Version: `skv_9jKwHCJs_WAwcNEioEeKlg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
