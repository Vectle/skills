---
name: "aikido-ignore-rule-not-working-finding-8188805557a2a818"
description: "aikido ignore rule not working: finding still reported after aikido ignore comment fails"
metadata:
  skill_id: "skl_Dg5Z2scrYip9LJaDRyOpfA"
  title: "aikido ignore rule not working: finding still reported after aikido ignore comment fails"
  version: "skv_lOuHsoK59B7QzqUjGxlLUw"
  updated: "2026-11-08T01:52:10.124366+00:00"
  canonical_url: "https://vectle.com/skills/skl_Dg5Z2scrYip9LJaDRyOpfA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the finding in Aikido and copy its exact rule ID and file path.

Put the ignore comment on the same line as the flagged code, or the line directly above it if your scanner version requires that placement, using that exact rule ID.

Commit the file and push it so the scanner sees the change on the scanned branch.

Trigger a new scan and wait for it to finish.

If it still reports, check for a second copy of the same code in another file or a generated file that is also scanned.

---

Source: [Vectle](https://vectle.com/skills/skl_Dg5Z2scrYip9LJaDRyOpfA). Version: `skv_lOuHsoK59B7QzqUjGxlLUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
