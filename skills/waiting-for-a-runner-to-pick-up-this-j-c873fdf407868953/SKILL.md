---
name: "waiting-for-a-runner-to-pick-up-this-j-c873fdf407868953"
description: "Fixes jobs stuck at 'Waiting for a runner to pick up this job'. Use when a workflow job never starts and stays queued. Not for jobs that fail fast or for GitHub-wide outages."
metadata:
  skill_id: "skl__tLRN0mnXr_QzmgRlKOCCA"
  title: "Waiting for a runner to pick up this job in GitHub Actions"
  version: "skv_MctXV4XjxjAjMJ7HIzaLgA"
  updated: "2026-10-03T05:29:42.550089+00:00"
  canonical_url: "https://vectle.com/skills/skl__tLRN0mnXr_QzmgRlKOCCA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Make the runs-on labels match a runner that is actually online and idle: check Settings, Actions, Runners for a green idle runner carrying every label you listed. The job is queued, not broken; no runner with that exact label set is picking it up, so it waits forever.

```text
Waiting for a runner to pick up this job
```

## The fix

1. Open the repo or org Settings, Actions, Runners page and look for an Idle runner.
   Expected: You see which runners are online and their labels.

2. Compare the runner labels with your workflow's runs-on. A self-hosted runner only takes jobs whose labels are a subset of its own.
   Expected: You spot the mismatch, e.g. runs-on: [self-hosted, gpu] but the runner only has self-hosted.

3. Fix the mismatch: relabel the runner (./config.sh --labels) or change runs-on to labels that exist. On GitHub-hosted runners, verify the label name spelling (ubuntu-latest, not ubuntu_latest) and check status.github.com for an outage.
   Expected: The job starts within a minute of the next push or re-run.

## When this applies

- a job sits queued showing Waiting for a runner to pick up this job
- you use self-hosted runners or custom labels

## When it does NOT apply

- the job fails immediately (that is a workflow error, not a runner shortage)
- all jobs are queued including ubuntu-latest (likely a GitHub incident; check the status page)

## Compatibility

GitHub Actions with self-hosted runners (all OSes) and GitHub-hosted runners. Runner application 2.2xx and later.

## Why it happens

The scheduler matches jobs to runners purely by label set. One wrong label, an offline runner, or a busy runner pool means the job never gets assigned; GitHub shows the waiting message instead of failing so transient capacity dips recover on their own.

## Edge cases and pitfalls

- Ephemeral runners that failed to register leave no trace; check the runner logs on the host.
- Org-level runners are only visible to jobs in that org; repo runners only to that repo.
- A runner stuck on a zombie job shows busy forever; restart the runner service on the host.

---

Source: [Vectle](https://vectle.com/skills/skl__tLRN0mnXr_QzmgRlKOCCA). Version: `skv_MctXV4XjxjAjMJ7HIzaLgA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
