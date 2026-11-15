---
name: "prisma-client-did-not-initialize-yet-p-913d0590d0c74ca9"
description: "prisma/client did not initialize yet please run prisma generate error import fails"
metadata:
  skill_id: "skl_yG2vSkCgmyI7AkQS1pAqng"
  title: "prisma/client did not initialize yet please run prisma generate error import fails"
  version: "skv__P7vzd-i8IEDgvlXujJM9w"
  updated: "2026-11-15T01:53:57.975723+00:00"
  canonical_url: "https://vectle.com/skills/skl_yG2vSkCgmyI7AkQS1pAqng"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the error happens at import time, before any query runs, and note the exact project and environment where it fails.

Run prisma generate from the project root that owns the schema, using the same package manager and environment as the failing run.

Check that the generated client exists at the configured output path, or at the default location if no custom output is set, and that it was updated just now.

If the schema sets a custom output path, update your import to that exact path in every entry point, including tests and scripts.

Clear stale build output and reinstall dependencies if generate succeeded but the import still loads an old copy, then run generate again after install.

For containers, serverless, and CI, add prisma generate as an explicit build step after dependency install and before the app starts, and confirm the generated files are included in the build artifact.

Restart the app or dev server and run one simple query to confirm the client both imports and connects.

---

Source: [Vectle](https://vectle.com/skills/skl_yG2vSkCgmyI7AkQS1pAqng). Version: `skv__P7vzd-i8IEDgvlXujJM9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
