---
name: "serverless-job-stuck-in-in-progress-af-a7d6b66def60529c"
description: "Shows how to fix serverless job stuck in IN_PROGRESS after calling progress_update. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_dGLyqduWW51Lc8A5JAvzkQ"
  title: "Serverless job stuck in IN_PROGRESS after calling progress_update"
  version: "skv_q9OikPll111O-AbNdfQfUA"
  updated: "2026-10-03T14:15:27.292187+00:00"
  canonical_url: "https://vectle.com/skills/skl_dGLyqduWW51Lc8A5JAvzkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_uTov_VcVVTA8fLGru5u9mg\",\"https://github.com/runpod/runpod-python/issues/250\"]"
---

## TL;DR

Keep your progress updates away from the very end of the handler where possible. What was going on Calling runpod.serverless.progress\_update(job,...) near the end of a handler left the job stuck in IN_PROGRESS even after the handler returned.

## Steps

1. What was going on
Calling `runpod.serverless.progress_update(job, ...)` near the end of a handler left the job stuck in IN_PROGRESS even after the handler returned. The reporter confirmed it was a race condition by adding a one-second sleep before the return, which let the async progress update finish first. Maintainer justinmerrell dug in, deployed a production-side fix, and confirmed that once jobs are marked done they can no longer revert to in-progress status.

2. What fixed it
If your job stays IN_PROGRESS after the handler returns, the async `progress_update` call is racing with the completion signal. The platform-side fix is deployed, so jobs marked done now stay done, but if you are on an older flow the one-second sleep before returning from your handler is the confirmed workaround. Keep your progress updates away from the very end of the handler where possible. The maintainer confirmed the production fix after reproducing the race.

Expected: The maintainer confirmed the production fix after reproducing the race.

## When to use

Use this skill when you run into "Serverless job stuck in IN_PROGRESS after calling progress_update".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_dGLyqduWW51Lc8A5JAvzkQ). Version: `skv_q9OikPll111O-AbNdfQfUA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
