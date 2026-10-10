---
name: "how-to-run-kubectl-after-docker-push-i-9c7694777a121596"
description: "Walks through run kubectl after docker push in Google Cloud Build, step by step. Use it when you need to do exactly this. Not a troubleshooting guide, so skip it if you are here because of an error."
metadata:
  skill_id: "skl_bN49hETyXwpkiryW42CREA"
  title: "How to run kubectl after docker push in Google Cloud Build"
  version: "skv_dOAMCvFqLjOJUy5GLG8Eog"
  updated: "2026-10-03T13:58:58.988563+00:00"
  canonical_url: "https://vectle.com/skills/skl_bN49hETyXwpkiryW42CREA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

How to run kubectl after pushing an image in a Cloud Build pipeline? Chain build steps explicitly: run docker push as its own build step (rather than relying only on the images: field), then add a gcr.io/cloud-builders/kubectl step that deploys the pushed image.

## Steps

1. How to run kubectl after pushing an image in a Cloud Build pipeline? The goal: build an image, test/push it to GCR, then deploy it into a GKE cluster, all in one cloudbuild.yaml. Without this, the pipeline could not do end-to-end CI/CD.

2. Chain build steps explicitly: run `docker push` as its own build step (rather than relying only on the `images:` field), then add a `gcr.io/cloud-builders/kubectl` step that deploys the pushed image. A working community pattern confirmed in the thread:

3. steps:
- name: 'gcr.io/cloud-builders/docker'
 args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-project:$TAG_NAME', '.']
- name: 'gcr.io/cloud-builders/docker'
 args: ['push', 'gcr.io/$PROJECT_ID/my-project:$TAG_NAME']
- name: 'gcr.io/cloud-builders/kubectl'
 args: ['set', 'image', 'deployment/my-deploy', 'my-container=gcr.io/$PROJECT_ID/my-project:$TAG_NAME']

4. Note the images: field pushes separately, so pushing manually avoids double pushes if you push in a step. The kubectl step needs the build service account to have the right scopes/roles to talk to the GKE cluster.

5. The thread above nails the cause, so the fix addresses that directly rather than symptoms. Adapt the version numbers and paths to your setup, then verify the behavior the thread confirmed.

## When to use

You are seeing this: The goal: build an image, test/push it to GCR, then deploy it into a GKE cluster, all in one cloudbuild.yaml. Use this skill when you run into "How to run kubectl after docker push in Google Cloud Build".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The thread above nails the cause, so the fix addresses that directly rather than symptoms.

## Sources

- https://github.com/GoogleCloudPlatform/cloud-builders/issues/22


---

Source: [Vectle](https://vectle.com/skills/skl_bN49hETyXwpkiryW42CREA). Version: `skv_dOAMCvFqLjOJUy5GLG8Eog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
