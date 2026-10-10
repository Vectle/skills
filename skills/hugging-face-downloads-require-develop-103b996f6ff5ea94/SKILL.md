---
name: "hugging-face-downloads-require-develop-103b996f6ff5ea94"
description: "Shows how to fix hugging Face downloads require Developer Mode on Windows. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_2PpXyoyzdvrJVcMfEyJofg"
  title: "Hugging Face downloads require Developer Mode on Windows"
  version: "skv_mJnpqBljycJ5_IuVO_PtUw"
  updated: "2026-10-04T04:35:20.902937+00:00"
  canonical_url: "https://vectle.com/skills/skl_2PpXyoyzdvrJVcMfEyJofg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

This was fixed in huggingface_hub v0.10: the download code now checks whether symlinks are supported, and when they are not, like on Windows without developer mode or admin rights, it falls back to copying the files instead of failing.

## Steps

1. On Windows, snapshot_download and hf_hub_download fail unless I enable Developer Mode or run as admin, because they use symlinks. Regular users will not enable developer mode just to download a model. Is there a workaround?

2. You are right, requiring developer mode was a bad experience. This was fixed in huggingface_hub v0.10: the download code now checks whether symlinks are supported, and when they are not, like on Windows without developer mode or admin rights, it falls back to copying the files instead of failing. So just upgrade huggingface_hub and the downloads will work for regular users with no special settings. Source: https://github.com/huggingface/huggingface_hub/issues/1062

3. Take the question above and check if it matches what you're seeing. If it does, work through the verified fix step by step. Start with the cause described first, because that's what tells you the fix applies to your setup, then apply the changes in the order given. Verify by re-running whatever failed before, and expect the same behavior the thread author reported.

## When to use

You are seeing this: You are right, requiring developer mode was a bad experience. Use this skill when you run into "Hugging Face downloads require Developer Mode on Windows".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: huggingface_hub v0.10. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/huggingface/huggingface_hub/issues/1062


---

Source: [Vectle](https://vectle.com/skills/skl_2PpXyoyzdvrJVcMfEyJofg). Version: `skv_mJnpqBljycJ5_IuVO_PtUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
