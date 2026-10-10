---
name: "renovate-lockfiles-not-being-updated-i-dff28bf5ae7a784d"
description: "Shows how to fix renovate lockfiles not being updated in dependency PRs. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl__ZtvxgcGJGjUrhZPy5oW6A"
  title: "Renovate lockfiles not being updated in dependency PRs"
  version: "skv_kUpgKM7VEAfXhdUlSGa6iA"
  updated: "2026-10-03T13:53:17.101551+00:00"
  canonical_url: "https://vectle.com/skills/skl__ZtvxgcGJGjUrhZPy5oW6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

This was a Renovate regression fixed in version 23.70.1, upgrade to that release or later. If you self-host, update the Renovate image or package to 23.70.1+; on the hosted app the fix rolled out automatically.

## Steps

1. Renovate PRs changed package.json but left yarn.lock untouched, breaking yarn install --frozen-lockfile in CI. Reported against the hosted WhiteSource Renovate app on GitHub.com after a sudden behavior change. Maintainers traced it to a regression in the lockfile maintenance flow.

2. This was a Renovate regression fixed in version 23.70.1, upgrade to that release or later. After the fix, jobs ran regularly and PRs included updated lockfiles with no unnecessary force-pushes. If you self-host, update the Renovate image or package to 23.70.1+; on the hosted app the fix rolled out automatically.

## When to use

You are seeing this: Maintainers traced it to a regression in the lockfile maintenance flow. Use this skill when you run into "Renovate lockfiles not being updated in dependency PRs".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 23.70.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl__ZtvxgcGJGjUrhZPy5oW6A). Version: `skv_kUpgKM7VEAfXhdUlSGa6iA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
