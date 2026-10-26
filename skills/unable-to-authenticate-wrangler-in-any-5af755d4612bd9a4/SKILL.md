---
name: "unable-to-authenticate-wrangler-in-any-5af755d4612bd9a4"
description: "Shows how to fix unable to Authenticate Wrangler in any Remote Development Environment. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_7YuyHoHFla5-lHiL5QMixQ"
  title: "Unable to Authenticate Wrangler in any Remote Development Environment"
  version: "skv_N7_jKXYag8nFnAUSZIHYqA"
  updated: "2026-10-03T23:19:57.053556+00:00"
  canonical_url: "https://vectle.com/skills/skl_7YuyHoHFla5-lHiL5QMixQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/cloudflare/workers-sdk/issues/2874\"]"
---

## TL;DR

[tkalejaiye (commenter)]: If wrangler login fails on a remote dev environment (Gitpod, Codespaces, Stackblitz) with "Received query string parameter doesn't match the one sent!", forward port 8976 to your local machine when you ssh in, e.g. ssh -L 8976:YOUR_HOST:8976 user@remote.

## Steps

1. [tkalejaiye (commenter)]: If wrangler login fails on a remote dev environment (Gitpod, Codespaces, Stackblitz) with "Received query string parameter doesn't match the one sent!", forward port 8976 to your local machine when you ssh in, e.g. ssh -L 8976:YOUR_HOST:8976 user@remote. The OAuth callback needs that port reachable locally.

2. https://github.com/cloudflare/workers-sdk/issues/2874: Issue cloudflare/workers-sdk#2874 (closed, 28 comments): [https://developers.cloudflare.com/workers/wrangler/commands/#using-wrangler-login-on-a-remote-machine](https://developers.cloudflare.com/workers/wrangler/commands/#using-wrangler-login-on-a-remote-machine) outlines how to authenticate the Wrangler CLI when using a remote development environment (e.g. Codespaces).

3. However it doesn't seem to work. The original shell always puts out this error message at the end

```bash
Received query string parameter doesn't match the one sent! Possible malicious activity somewhere.
```

4. I've seen this on Gitpod, Codespaces, Stackblitz, and...

## When to use

You are seeing this: https://github.com/cloudflare/workers-sdk/issues/2874: Issue cloudflare/workers-sdk#2874 (closed, 28 comments): https://developers.cloudflare.com/workers/wrangler/commands/#using-wrangler-login-on-a-remote-machine outlines how to authenticate the Wrangler... Use this skill when you run into "Unable to Authenticate Wrangler in any Remote Development Environment".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/cloudflare/workers-sdk/issues/2874:

- https://developers.cloudflare.com/workers/wrangler/commands/#using-wrangler-login-on-a-remote-machine


---

Source: [Vectle](https://vectle.com/skills/skl_7YuyHoHFla5-lHiL5QMixQ). Version: `skv_N7_jKXYag8nFnAUSZIHYqA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
