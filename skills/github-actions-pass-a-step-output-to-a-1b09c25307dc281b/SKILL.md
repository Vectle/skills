---
name: "github-actions-pass-a-step-output-to-a-1b09c25307dc281b"
description: "Shows how to fix gitHub Actions: pass a step output to a later step with GITHUB_OUTPUT. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_3-Qp4cNCE362i3aespgQdA"
  title: "GitHub Actions: pass a step output to a later step with GITHUB_OUTPUT"
  version: "skv_DmAiJJaQ9FPOxOzS8UNAkA"
  updated: "2026-10-03T14:07:48.966148+00:00"
  canonical_url: "https://vectle.com/skills/skl_3-Qp4cNCE362i3aespgQdA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

First, add an id to the producing step. Second, inside its run script, append lines like echo "result=$(my-command)" >> $GITHUB_OUTPUT (multiline values need the heredoc form).

## Steps

1. Three steps. First, add an id to the producing step. Second, inside its run script, append lines like echo "result=$(my-command)" >> $GITHUB_OUTPUT (multiline values need the heredoc form). Third, consume it later as ${{ steps.[id].outputs.result }}. Do not use the old ::set-output command; it is deprecated and disabled. Outputs must be set in the same step that declares the id, and a step cannot read its own outputs.

## When to use

You are seeing this: Third, consume it later as ${{ steps.[id].outputs.result }}. Use this skill when you run into "GitHub Actions: pass a step output to a later step with GITHUB_OUTPUT".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_3-Qp4cNCE362i3aespgQdA). Version: `skv_DmAiJJaQ9FPOxOzS8UNAkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
