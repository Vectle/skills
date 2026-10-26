---
name: "dagster-webserver-and-daemon-memory-us-fdcb2e01c6a24c3e"
description: "Shows how to fix dagster webserver and daemon memory usage grows fast until OOM. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_lM-T11fxjh32IXgxnyMzmA"
  title: "Dagster webserver and daemon memory usage grows fast until OOM"
  version: "skv_ESuNzsTlXKEBdaO7bXjfJA"
  updated: "2026-10-03T05:12:46.082812+00:00"
  canonical_url: "https://vectle.com/skills/skl_lM-T11fxjh32IXgxnyMzmA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_NnekL9-MHEUe8gaW7vepTA\",\"https://github.com/dagster-io/dagster/issues/18997\"]"
---

## TL;DR

A user narrowed it down by pinning dependencies and found grpcio was the culprit: with grpcio 1.57.1 or newer installed, memory climbed fast; pinned to 1.57.0, the leak disappeared. A later user reported that upgrading to grpcio 1.68+ also fixed it, with a month of stable operation.

## Steps

1. Dagster's webserver and daemon steadily grew in memory until containers were OOM-killed, even on small deployments. A user narrowed it down by pinning dependencies and found grpcio was the culprit: with grpcio 1.57.1 or newer installed, memory climbed fast; pinned to 1.57.0, the leak disappeared. A Dagster maintainer confirmed the finding and added a grpcio pin to the Helm chart's user-deployment images so fresh installs wouldn't pull the bad version. A later user reported that upgrading to grpcio 1.68+ also fixed it, with a month of stable operation. The reporter who found the pin confirmed two weeks of flat memory on the pinned version.

2. This memory leak was traced to grpcio, not Dagster itself: grpcio versions after 1.57.0 leak in Dagster's webserver/daemon setup. Short-term fix: pin `grpcio==1.57.0` (1.59.5 was also reported stable) in your Dagster deployment image. Durable fix: upgrade to `grpcio>=1.68`, which one user ran for a month with stable memory. Dagster also added a grpcio pin to the Helm chart images, so current chart installs pull a safe version. The original reporter confirmed flat memory for two weeks on the pinned version.

Expected: A Dagster maintainer confirmed the finding and added a grpcio pin to the Helm chart's user-deployment images so fresh installs wouldn't pull the bad version.

## When to use

You are seeing this: Dagster's webserver and daemon steadily grew in memory until containers were OOM-killed, even on small deployments. Use this skill when you run into "Dagster webserver and daemon memory usage grows fast until OOM".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: grpcio 1.57.1, 1.57.0, 1.59.5. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_lM-T11fxjh32IXgxnyMzmA). Version: `skv_ESuNzsTlXKEBdaO7bXjfJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
