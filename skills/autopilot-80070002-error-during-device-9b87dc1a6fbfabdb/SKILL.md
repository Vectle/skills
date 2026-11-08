---
name: "autopilot-80070002-error-during-device-9b87dc1a6fbfabdb"
description: "autopilot 80070002 error during device setup"
metadata:
  skill_id: "skl_Mrty155XZKrmQAL3avgUwA"
  title: "autopilot 80070002 error during device setup"
  version: "skv_UjYZ_SPICtlhGbKfe1aIBA"
  updated: "2026-11-08T13:53:38.63638+00:00"
  canonical_url: "https://vectle.com/skills/skl_Mrty155XZKrmQAL3avgUwA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

On the failed device, open the Autopilot diagnostics from the ESP failure screen and note the exact app or script listed as failed.

In the Intune admin center, open that app or script and check its install command and source file name match exactly, including the file extension.

If the item is a PowerShell script, check it does not call a second file that was never uploaded with it.

Check the assignment targets the device group the test device is in, and that no required app was deleted or replaced after the profile was built.

Fix the package, wait for the new version to show as available, then reset one test device and run provisioning again.

---

Source: [Vectle](https://vectle.com/skills/skl_Mrty155XZKrmQAL3avgUwA). Version: `skv_UjYZ_SPICtlhGbKfe1aIBA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
