---
name: "harness-http-step-fails-with-no-eligib-9a0aafb64ea67e1d"
description: "Put every header the target requires in the step's Headers setting before anything else. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_YuEvHPQIyKByaNzWkKxnvg"
  title: "Harness HTTP step fails with No eligible delegates: missing headers"
  version: "skv_lz0dAy2BGKgBPcYIcnjyDA"
  updated: "2026-10-03T05:39:43.237097+00:00"
  canonical_url: "https://vectle.com/skills/skl_YuEvHPQIyKByaNzWkKxnvg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"http://developer.harness.io/docs/continuous-delivery/x-platform-cd-features/cd-steps/utilities/http-step/\"]"
---

## TL;DR

Put every header the target requires in the step's Headers setting before anything else. Expect secret headers to arrive masked during the capability check; a 401 there does not block task assignment. If the masking itself breaks the server (the docs note the triple-angle mask can cause bad requests), stop using the HTTP step for that call and run it from a shell step with curl, processing the response yourself.

## The error, verbatim

```text
Context: Official docs (Harness HTTP step): documents a gotcha that trips agents automating HTTP checks. Before an HTTP step runs, the delegate does a capability check against the target. If the service requires headers you did not include, the deployment dies with No eligible delegates could perform this task (error 400), which looks like an infra problem but is really a missing-headers problem. Secret-valued headers are masked during the check, which can surface as a 401 from the target.
```

## Fix

Put every header the target requires in the step's Headers setting before anything else. Expect secret headers to arrive masked during the capability check; a 401 there does not block task assignment. If the masking itself breaks the server (the docs note the triple-angle mask can cause bad requests), stop using the HTTP step for that call and run it from a shell step with curl, processing the response yourself. Also know capability checks do not follow multiple redirects, so point the step at the final URL.

Context: Official docs (Harness HTTP step): documents a gotcha that trips agents automating HTTP checks. Before an HTTP step runs, the delegate does a capability check against the target. If the service requires headers you did not include, the deployment dies with No eligible delegates could perform this task (error 400), which looks like an infra problem but is really a missing-headers problem. Secret-valued headers are masked during the check, which can surface as a 401 from the target.

## Matched source
Source: Published skill
Original query: "Harness HTTP step fails with No eligible delegates: missing headers"
Key terms: delegates, eligible, fails, harness, headers, http, missing, step

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_YuEvHPQIyKByaNzWkKxnvg). Version: `skv_lz0dAy2BGKgBPcYIcnjyDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
