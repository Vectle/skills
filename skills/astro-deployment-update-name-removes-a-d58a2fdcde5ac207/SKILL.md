---
name: "astro-deployment-update-name-removes-a-d58a2fdcde5ac207"
description: "Shows how to fix astro deployment update name removes all dags. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_stJ615Ini5Anv7ZE7fLjSw"
  title: "astro deployment update name removes all dags"
  version: "skv_cWWbYFA1SMcURN-N6QzTWQ"
  updated: "2026-10-04T04:46:21.683541+00:00"
  canonical_url: "https://vectle.com/skills/skl_stJ615Ini5Anv7ZE7fLjSw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade the Astro CLI to 1.21.0 or newer. Run `bash astro deployment update --deployment-name SRC\_NAME --name DST\_NAME `` 4.

## Steps

1. How to astro deployment update name removes all dags.

2. Issue astronomer/astro-cli#1458 (closed, 8 comments): **Describe the bug**

```bash astro deployment update --deployment-name SRC_NAME --name DST_NAME ```

3. Will rename the deployment but lose all its dags, the only one left is astronomer_monitoring_dag **What CLI Version did you experience this bug?** 1.20.1 **This CLI bug is related to which Astronomer Platform?** - [x] Astro - [ ] Software - [ ] None/Unknown **What Operating System is the above CLI installed on?** MacOS Sonoma 14.1.1 **🪜 Steps To Reproduce** 1. Create a deployment 2. Deploy some dags 3. Run

```bash astro deployment update --deployment-name SRC_NAME --name DST_NAME ```

4. Upgrade the Astro CLI to 1.21.0 or newer. The regression in the reported CLI version was fixed there, and the reporter confirmed the failure went away after upgrading. If you installed via a package manager, re-run the install to pull the fixed release before retrying the failing command.

## When to use

You are seeing this: MacOS Sonoma 14.1.1 🪜 Steps To Reproduce 1. Use this skill when you run into "astro deployment update name removes all dags".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: bug 1.20.1, Sonoma 14.1.1, 1.21.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/astronomer/astro-cli/issues/1458


---

Source: [Vectle](https://vectle.com/skills/skl_stJ615Ini5Anv7ZE7fLjSw). Version: `skv_cWWbYFA1SMcURN-N6QzTWQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
