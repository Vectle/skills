---
name: "happy-dom-vs-jsdom-vitest-environment-835140e6cdca2aae"
description: "happy-dom vs jsdom vitest environment error tests fail with window is not defined"
metadata:
  skill_id: "skl_CiKyhrZrm0g9ctsnRT_cyA"
  title: "happy-dom vs jsdom vitest environment error tests fail with window is not defined"
  version: "skv_cRbUfDemvz_ucj76EA7WQg"
  updated: "2026-11-12T13:54:48.165726+00:00"
  canonical_url: "https://vectle.com/skills/skl_CiKyhrZrm0g9ctsnRT_cyA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the Vitest config and find the test environment setting, noting whether it is set at all and what value it holds.

Confirm the happy-dom package is present in the project dependencies and installed, not only named in the config.

Set the environment to happy-dom in the config for the test run and save the config.

Check the failing test file for a per file environment comment or a project level include rule that assigns it to a different environment.

Run only the one failing test file and read the first error.

Run the full suite once the single file behaves.

---

Source: [Vectle](https://vectle.com/skills/skl_CiKyhrZrm0g9ctsnRT_cyA). Version: `skv_cRbUfDemvz_ucj76EA7WQg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
