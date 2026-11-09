---
name: "nextflow-run-fails-with-process-termin-11a2490458f2b8c8"
description: "Nextflow run fails with \"Process terminated with an error exit status (137)\" OOM error"
metadata:
  skill_id: "skl_oMnyYZkkTG954zSx6vgFxw"
  title: "Nextflow run fails with \"Process terminated with an error exit status (137)\" OOM error"
  version: "skv_Kf1kU2zOXmhEHMqQhWpn4w"
  updated: "2026-11-09T01:54:42.085073+00:00"
  canonical_url: "https://vectle.com/skills/skl_oMnyYZkkTG954zSx6vgFxw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Find the failed task in the Nextflow trace file and note its name, its work directory, and the memory it was given.

Open that task work directory and read its error and output files. Look for a killed message or a log that stops mid step with no application error.

Raise memory for that process in your Nextflow config using a process selector for that process name, setting a clearly higher memory value.

Add a retry error strategy for that process with a small number of retries, and make the memory request grow with the attempt number so a retry is not identical to the failed run.

Resume the run with the resume flag so completed tasks are reused, and watch the previously failing task finish.

---

Source: [Vectle](https://vectle.com/skills/skl_oMnyYZkkTG954zSx6vgFxw). Version: `skv_Kf1kU2zOXmhEHMqQhWpn4w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
