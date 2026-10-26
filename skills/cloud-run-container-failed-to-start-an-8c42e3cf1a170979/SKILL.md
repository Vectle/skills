---
name: "cloud-run-container-failed-to-start-an-8c42e3cf1a170979"
description: "Shows how to fix cloud Run: Container failed to start and then listen on the port. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_sXZ3D4qQKIq7YRTKBoEgCQ"
  title: "Cloud Run: Container failed to start and then listen on the port"
  version: "skv_E-YCEyzkKmb0Xc932bQjJg"
  updated: "2026-10-03T14:20:18.145836+00:00"
  canonical_url: "https://vectle.com/skills/skl_sXZ3D4qQKIq7YRTKBoEgCQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/run/docs/troubleshooting\",\"https://cloud.google.com/run/docs/deploying\"]"
---

## TL;DR

For "Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable.": check the container logs: gcloud run services logs read [SERVICE] --region [REGION]. Failed to start and then listen on the port defined by the PORT environment variable." Meaning: Cloud Run started your container, waited, and nothing accepted connections on $PORT (default 8080).

```text
Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable.
```

## Steps

1. Full error: "Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable."

2. Meaning: Cloud Run started your container, waited, and nothing accepted connections on $PORT (default 8080). The container may have crashed instantly or bound the wrong port.

3. Fix checklist, in order:
1. Read PORT from the environment in your code. Never hardcode 3000/5000/8000. In Node: `process.env.PORT || 8080`. In Python: `os.environ.get("PORT", 8080)`. In Go: `os.Getenv("PORT")`.
2. Bind the all-interfaces address, not YOUR_HOST. Binding the loopback address inside the container is unreachable from Cloud Run's perspective.
3. Reproduce locally: `docker run -e PORT=8080 -p 8080:8080 [IMAGE]` then curl YOUR_HOST:8080. If it fails locally, it is your image, not Cloud Run.
4. Check the container logs: `gcloud run services logs read [SERVICE] --region [REGION]`. A crash traceback here means fix the crash first.
5. Startup time: if the app takes longer than the startup probe allows, it gets killed before listening. Optimize startup or raise CPU.

4. Not this error: "Revision is not ready" with a crash log means the container died; the PORT error specifically means it stayed alive but never listened. Different fix.

5. Verify: local docker run with PORT set responds to curl, then redeploy and watch the revision become ready.

## When to use

You are seeing this: Full error: "Container failed to start. Use this skill when you run into "Cloud Run: Container failed to start and then listen on the port".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_sXZ3D4qQKIq7YRTKBoEgCQ). Version: `skv_E-YCEyzkKmb0Xc932bQjJg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
