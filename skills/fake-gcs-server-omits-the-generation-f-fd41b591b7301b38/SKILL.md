---
name: "fake-gcs-server-omits-the-generation-f-fd41b591b7301b38"
description: "Shows how to fix fake-gcs-server omits the generation field, breaking the official PHP storage client. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_jvn6fW1tVaWFnPpvbZfeXQ"
  title: "fake-gcs-server omits the generation field, breaking the official PHP storage client"
  version: "skv_sGf0thl8DtQjJ-5rhKy7yw"
  updated: "2026-10-03T13:54:35.483539+00:00"
  canonical_url: "https://vectle.com/skills/skl_jvn6fW1tVaWFnPpvbZfeXQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade fake-gcs-server to a build containing the #812 fix and update the Docker image. Uploading a file to fake-gcs-server with the official Google PHP storage client broke because the upload response omitted the generation field entirely.

## Steps

1. Uploading a file to fake-gcs-server with the official Google PHP storage client broke because the upload response omitted the `generation` field entirely. The PHP client's Bucket.php expects `generation` in the response, so a missing field caused failures. The real GCS API always returns a generation number (epoch in microseconds matching upload time) whether versioning is enabled or not.

2. The filesystem backend did not serialize a `generation` field when none was set. The maintainer fixed it in PR #812 so the fake server always returns a generation number (based on the current time), matching the real GCS API, and the reporter confirmed uploads now work with the PHP client. Upgrade fake-gcs-server to a build containing the #812 fix and update the Docker image.

3. The thread above nails the cause, so the fix addresses that directly rather than symptoms. Adapt the version numbers and paths to your setup, then verify the behavior the thread confirmed.

## When to use

You are seeing this: The PHP client's Bucket.php expects generation in the response, so a missing field caused failures. Use this skill when you run into "fake-gcs-server omits the generation field, breaking the official PHP storage client".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The thread above nails the cause, so the fix addresses that directly rather than symptoms.

## Sources

- https://github.com/fsouza/fake-gcs-server/issues/701


---

Source: [Vectle](https://vectle.com/skills/skl_jvn6fW1tVaWFnPpvbZfeXQ). Version: `skv_sGf0thl8DtQjJ-5rhKy7yw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
