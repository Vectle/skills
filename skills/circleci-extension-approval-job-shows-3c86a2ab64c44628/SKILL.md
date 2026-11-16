---
name: "circleci-extension-approval-job-shows-3c86a2ab64c44628"
description: "CircleCI extension approval job shows as Queued since 2.19.0: pin to 2.18.0 to restore Pending Approval"
metadata:
  skill_id: "skl__Othya-Rq2NvV1_b_nl46A"
  title: "CircleCI extension approval job shows as Queued since 2.19.0: pin to 2.18.0 to restore Pending Approval"
  version: "skv_2OaphbpQgbbORYG9unj4IQ"
  updated: "2026-11-16T12:08:58.580048+00:00"
  canonical_url: "https://vectle.com/skills/skl__Othya-Rq2NvV1_b_nl46A"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm it is this regression and not a real queue. Check the extension version first (Extensions view, CircleCI entry) and confirm it is 2.19.0 or 2.21.1, then open the same workflow in the CircleCI web app. Success check: the web app shows the job waiting for approval while the extension shows Queued, and the job is a hold / approval job, not a normal run job waiting on concurrency.

Unblock the waiting job from the web app. Approve the hold job in the CircleCI web UI so the pipeline keeps moving while you fix the editor side. Success check: the workflow advances past the approval step in the web app.

Pin the extension to 2.18.0. In the Extensions view, open the CircleCI extension page, use the gear / dropdown next to Install or Uninstall, choose Install Another Version, and select 2.18.0. Success check: the extension page now shows version 2.18.0 as the installed version.

Turn off auto-update for this one extension so the pin survives. Use the same extension page menu and disable auto-update for CircleCI only, leaving other extensions alone. Success check: the extension stays on 2.18.0 after an editor restart instead of jumping back to 2.19.0 or newer.

Reload the editor window and re-check the Runs panel on a workflow with a fresh approval job. Success check: the hold job now shows as Pending Approval and the Approve button is present in the extension, matching the web app.

Unpin only for a fixed release. When a release newer than 2.21.1 ships and its notes mention approval or on_hold handling, update one machine first, run one approval workflow, and confirm the button appears before unpinning everywhere. Success check: the new version shows Pending Approval in the Runs panel without the pin.

---

Source: [Vectle](https://vectle.com/skills/skl__Othya-Rq2NvV1_b_nl46A). Version: `skv_2OaphbpQgbbORYG9unj4IQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
