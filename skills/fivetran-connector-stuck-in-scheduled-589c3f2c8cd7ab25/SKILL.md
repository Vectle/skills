---
name: "fivetran-connector-stuck-in-scheduled-589c3f2c8cd7ab25"
description: "fivetran connector stuck in scheduled state, sync never starts error"
metadata:
  skill_id: "skl_7mmVwSdFWbOhDXob2cZVVQ"
  title: "fivetran connector stuck in scheduled state, sync never starts error"
  version: "skv_K6gBHHBSvO7nvjLEUbtj5w"
  updated: "2026-11-21T13:53:13.048044+00:00"
  canonical_url: "https://vectle.com/skills/skl_7mmVwSdFWbOhDXob2cZVVQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the connector details page and check the pause toggle and the schema change handling state.

Re-run the setup tests from the connector setup page.

Check the destination status on the destination page.

Look for a schedule collision: a very long-running sync of the same connector, or a resync still in progress.

Trigger a manual sync with the sync now action and watch the sync history tab.

---

Source: [Vectle](https://vectle.com/skills/skl_7mmVwSdFWbOhDXob2cZVVQ). Version: `skv_K6gBHHBSvO7nvjLEUbtj5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
