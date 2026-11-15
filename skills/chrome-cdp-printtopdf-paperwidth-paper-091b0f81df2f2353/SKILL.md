---
name: "chrome-cdp-printtopdf-paperwidth-paper-091b0f81df2f2353"
description: "chrome cdp printtopdf paperwidth paperheight a4 settings"
metadata:
  skill_id: "skl_1lugl94Hyi-PC5xg5oquIA"
  title: "chrome cdp printtopdf paperwidth paperheight a4 settings"
  version: "skv_EVgofH1tlyUs4BHB1k_Lxw"
  updated: "2026-11-14T16:19:59.785951+00:00"
  canonical_url: "https://vectle.com/skills/skl_1lugl94Hyi-PC5xg5oquIA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Convert the paper size to inches before setting anything. A4 is 210 by 297 millimeters, which is 8.27 by 11.69 inches.

Set paperWidth to 8.27 and paperHeight to 11.69 for portrait A4 in the PrintToPDF parameters.

For landscape, swap the two values so paperWidth is 11.69 and paperHeight is 8.27, and set landscape to true if your client exposes that flag separately.

Decide between explicit size and CSS size. If your stylesheet defines an at-page size rule, set preferCSSPageSize to true and remove conflicting explicit values; otherwise leave it false and keep the explicit inches.

Set margins in inches as well, and check that margin plus content width does not exceed the paper width, which otherwise clips or scales content.

Set the scale to 1 unless you deliberately want scaling, and set printBackground to true if backgrounds are part of the design.

Generate one test page, open the PDF properties, and confirm the page size reads A4 before running the full batch.

---

Source: [Vectle](https://vectle.com/skills/skl_1lugl94Hyi-PC5xg5oquIA). Version: `skv_EVgofH1tlyUs4BHB1k_Lxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
