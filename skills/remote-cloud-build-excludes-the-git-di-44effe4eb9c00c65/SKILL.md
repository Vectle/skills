---
name: "remote-cloud-build-excludes-the-git-di-44effe4eb9c00c65"
description: "Shows how to fix remote Cloud Build excludes the .git directory from the build context. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_oh7sBH7PmWVJzV7-Gh7u_A"
  title: "Remote Cloud Build excludes the .git directory from the build context"
  version: "skv_Z_Os_ICMSrlrA4MSvAH0Qw"
  updated: "2026-10-03T05:33:57.012482+00:00"
  canonical_url: "https://vectle.com/skills/skl_oh7sBH7PmWVJzV7-Gh7u_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

To include it, override the ignore rules: create an empty.gcloudignore (touch.gcloudignore), write a.gcloudignore that does not ignore.git, add an explicit !.git line to.gcloudignore, or disable the ignore behavior entirely with gcloud config set gcloudignore/enabled false.

## Steps

1. gcloud's default ignore behavior always excludes .git from the upload tarball, and it does so silently. To include it, override the ignore rules: create an empty .gcloudignore (`touch .gcloudignore`), write a .gcloudignore that does not ignore .git, add an explicit `!.git` line to .gcloudignore, or disable the ignore behavior entirely with `gcloud config set gcloudignore/enabled false`. The reporter confirmed one of these got their remote build working.

## When to use

You are seeing this: Submitting a remote build with gcloud container builds submit --config cloudbuild.yaml, the.git directory never showed up in the build context even though there was no.dockerignore, no.gitignore, no.gcloudignore, and no "Some files were not included" message. Use this skill when you run into "Remote Cloud Build excludes the .git directory from the build context".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_oh7sBH7PmWVJzV7-Gh7u_A). Version: `skv_Z_Os_ICMSrlrA4MSvAH0Qw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
