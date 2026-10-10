---
name: "v0-24-upgrade-causing-disk-space-issue-e1f8131afd6a5f89"
description: "Shows how to fix v0.24 Upgrade causing disk space issues on servers. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_tDl0veKC1Wtt2FkTaiQWtQ"
  title: "v0.24 Upgrade causing disk space issues on servers"
  version: "skv_ZfvLt3tdlddFSAbIwzHGZQ"
  updated: "2026-10-03T14:09:17.858599+00:00"
  canonical_url: "https://vectle.com/skills/skl_tDl0veKC1Wtt2FkTaiQWtQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Run a scheduled job to write to our typesense servers - the job being a bulk write to the servers and allow for the job to run several times, causing a build up of non deleted redudant files.

## Steps

1. v0.24 Upgrade causing disk space issues on servers

2. What was going on
Issue typesense/typesense#928 (closed, 15 comments): RocksDB garbage collection not clearing disk up after collections marked for deletion. This is causing the disk space on the VMs our typesense servers are running on to run out of disk within a couple of days (150gb). Image 1 below shows the data folder slowly bloating - with our /data/db directory being clogged full of .sst files (Image 2). img1 [image] img2 [image] Upgrade servers to new v0.24. Run a scheduled job to write to our typesense servers - the job being a bulk write to the servers and allow for the job to run several times, causing a build up of non deleted redudant files.

3. The fix
If disk space balloons after upgrading to Typesense 0.24 (RocksDB not compacting after collection drops), upgrade to 0.25.x. The maintainer added automatic compaction on collection drop, and the reporter confirmed their db directory shrank from 23G to 1.5G after dropping collections. Note: 0.25 upgrades RocksDB, so you cannot downgrade back to 0.24 on the same data directory.

## When to use

Use this skill when you run into "v0.24 Upgrade causing disk space issues on servers".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: v0.24. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Note: 0.25 upgrades RocksDB, so you cannot downgrade back to 0.24 on the same data directory.


---

Source: [Vectle](https://vectle.com/skills/skl_tDl0veKC1Wtt2FkTaiQWtQ). Version: `skv_ZfvLt3tdlddFSAbIwzHGZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
