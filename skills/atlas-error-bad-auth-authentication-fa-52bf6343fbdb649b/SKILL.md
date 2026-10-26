---
name: "atlas-error-bad-auth-authentication-fa-52bf6343fbdb649b"
description: "Shows how to fix atlas error: bad auth, authentication failed (code 18). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_40SG640P5KFArq0xrSHnRQ"
  title: "Atlas error: bad auth, authentication failed (code 18)"
  version: "skv_DEsnNwK_oW_vWXz-Pw0vnw"
  updated: "2026-10-03T13:55:31.305671+00:00"
  canonical_url: "https://vectle.com/skills/skl_40SG640P5KFArq0xrSHnRQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.mongodb.com/docs/atlas/troubleshoot-connection/\",\"https://www.mongodb.com/docs/manual/reference/connection-string/\"]"
---

## TL;DR

For "MongoServerError: bad auth : Authentication failed.": add authSource=admin explicitly. If the network were the problem you would see a timeout instead.

```text
MongoServerError: bad auth : Authentication failed.
```

## Steps

1. Full text looks like: `MongoServerError: bad auth : Authentication failed.` This is always credentials, never the network. If the network were the problem you would see a timeout instead.

2. Correct the piece that is wrong, update the stored secret, and re-run the startup ping. Do not "fix" it by widening the IP access list or recreating the cluster.

## When to use

You are seeing this: Full text looks like: MongoServerError: bad auth : Authentication failed. Use this skill when you run into "Atlas error: bad auth, authentication failed (code 18)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_40SG640P5KFArq0xrSHnRQ). Version: `skv_DEsnNwK_oW_vWXz-Pw0vnw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
