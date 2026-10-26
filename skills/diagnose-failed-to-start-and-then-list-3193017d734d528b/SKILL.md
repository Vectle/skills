---
name: "diagnose-failed-to-start-and-then-list-3193017d734d528b"
description: "Shows how to fix diagnose: Failed to start and then listen on the port defined by PORT. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_C_DAfOYRFgE1qT1-zIzlqA"
  title: "Diagnose: Failed to start and then listen on the port defined by PORT"
  version: "skv_6kzSv5EjlgmW-F85qEakBw"
  updated: "2026-10-03T14:09:05.322923+00:00"
  canonical_url: "https://vectle.com/skills/skl_C_DAfOYRFgE1qT1-zIzlqA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/run/docs/troubleshooting\",\"https://cloud.google.com/run/docs/deploying\"]"
---

## TL;DR

For "Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable.": cause: one of three: wrong port (hardcoded instead of $PORT), wrong bind address (YOUR_HOST instead of the all-interfaces address), or the app crashed before listening. Local repro: docker run -e PORT=8080 -p 8080:8080 [IMAGE], then curl YOUR_HOST:8080.

```text
Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable.
```

## Steps

1. Symptom: "Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable." Revision never becomes ready.

2. Cause: one of three: wrong port (hardcoded instead of $PORT), wrong bind address (YOUR_HOST instead of the all-interfaces address), or the app crashed before listening.

3. Confirm in order:
1. Local repro: `docker run -e PORT=8080 -p 8080:8080 [IMAGE]`, then curl YOUR_HOST:8080. Fails here means it is the image, full stop.
2. Grep your code for the listen call. Is it reading the PORT env var? Is it binding the all-interfaces address? `app.listen(process.env.PORT)` in Node binds all interfaces by default in most frameworks, but explicit 'YOUR_HOST' binds break it.
3. `gcloud run services logs read [SERVICE] --region [R]` - a crash traceback here means fix the crash, not the port.

4. Fix:
- Read PORT at startup with a sane default for local dev.
- Bind the all-interfaces address explicitly if your framework defaults to YOUR_HOST.
- If startup is slow (model loading, migrations), the container can be killed before it listens: optimize startup or raise CPU so it boots faster.

5. Not this: "Revision is not ready" WITH a crash log is a crash diagnosis. The PORT error with NO crash log is a listen diagnosis. Check the logs to tell them apart.

6. Verify: local docker run with PORT set answers curl, then redeploy and watch the revision reach Ready.

## When to use

You are seeing this: Symptom: "Container failed to start. Use this skill when you run into "Diagnose: Failed to start and then listen on the port defined by PORT".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_C_DAfOYRFgE1qT1-zIzlqA). Version: `skv_6kzSv5EjlgmW-F85qEakBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
