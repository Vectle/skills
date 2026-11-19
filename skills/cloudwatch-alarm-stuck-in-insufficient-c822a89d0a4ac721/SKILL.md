---
name: "cloudwatch-alarm-stuck-in-insufficient-c822a89d0a4ac721"
description: "cloudwatch alarm stuck in insufficient_data after metric stops publishing"
metadata:
  skill_id: "skl_ekMncVmyFDXANJs3t16o3w"
  title: "cloudwatch alarm stuck in insufficient_data after metric stops publishing"
  version: "skv_Qe0_baF7v0HbwFjIN0vDgQ"
  updated: "2026-11-19T13:53:17.412259+00:00"
  canonical_url: "https://vectle.com/skills/skl_ekMncVmyFDXANJs3t16o3w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the metric in CloudWatch and check the timestamp of its last datapoint.

Check the alarm history for the state change into INSUFFICIENT_DATA at that same stop time.

Decide the intended meaning of silence for this metric: alert, stay quiet, or keep the last state.

Edit the alarm and set how missing data is treated to match that choice, for example breaching for a heartbeat metric.

Fix or restart the publisher and confirm new datapoints appear and the alarm returns to OK.

---

Source: [Vectle](https://vectle.com/skills/skl_ekMncVmyFDXANJs3t16o3w). Version: `skv_Qe0_baF7v0HbwFjIN0vDgQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
