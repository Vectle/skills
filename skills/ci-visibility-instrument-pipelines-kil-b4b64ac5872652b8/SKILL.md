---
name: "ci-visibility-instrument-pipelines-kil-b4b64ac5872652b8"
description: "Shows how to fix cI Visibility: instrument pipelines, kill flaky tests, alert on duration. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_H9cidmWWWw4bVVnsiU9n4w"
  title: "CI Visibility: instrument pipelines, kill flaky tests, alert on duration"
  version: "skv_d_E_C4ugn5Sr2ZtEsgkFWw"
  updated: "2026-10-04T02:30:55.434718+00:00"
  canonical_url: "https://vectle.com/skills/skl_H9cidmWWWw4bVVnsiU9n4w"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Enable test visibility: per-test results, durations, and flakiness history. Sort by flakiness, fix or quarantine from the top.

## Steps

1. - **Flaky test list**: the single highest-value view. Sort by flakiness, fix or quarantine from the top. A flaky test suite trains developers to ignore red, which is how real breakages ship.
- **Pipeline duration trends**: alert when p95 pipeline time regresses. Slow CI is a tax on every commit; a 20-minute regression is a staffing decision in disguise.
- **Failure-to-commit correlation**: when a deploy breaks, trace back to the commit and the pipeline run that let it through. This closes the loop between CI signal and production incident.
- **Monitors on CI data**: failed pipeline rate, queue wait time. Page the platform team on the same terms as production.

## When to use

You are seeing this: CI is a production system for developers. Use this skill when you run into "CI Visibility: instrument pipelines, kill flaky tests, alert on duration".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_H9cidmWWWw4bVVnsiU9n4w). Version: `skv_d_E_C4ugn5Sr2ZtEsgkFWw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
