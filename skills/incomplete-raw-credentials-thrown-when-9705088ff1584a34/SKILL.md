---
name: "incomplete-raw-credentials-thrown-when-9705088ff1584a34"
description: "Fixes Nango throwing incomplete_raw_credentials when requesting a Slack user token via authorization_params. Use this when the connection only returns the bot token and user scopes fail. Not for Slack OAuth config errors or for bot-token-only integrations."
metadata:
  skill_id: "skl_CJg73SkxzOhYPBmIEt3TTg"
  title: "incomplete_raw_credentials thrown when requesting a Slack user token"
  version: "skv_MDxhWj56Ib3mdrBTE-ce6w"
  updated: "2026-10-03T04:46:24.96014+00:00"
  canonical_url: "https://vectle.com/skills/skl_CJg73SkxzOhYPBmIEt3TTg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_ZNoHdXOVNo-5obCHTIQOIw\",\"https://github.com/NangoHQ/nango/issues/3561\"]"
---

TL;DR: if triggering a Nango connection for Slack with user scopes throws `incomplete_raw_credentials`, the SDK only handled the bot token path and dropped the user token. Update Nango to a version containing PR #4025; user-scope connections then return the user token properly.

```text
incomplete_raw_credentials
```

## Steps

1. Update Nango past the PR #4025 fix.

2. Re-trigger the Slack connection with user scopes via authorization_params.

   Expected: the connection completes with the user token from oauth.v2.access. Success check: you can read the user token off the connection.

## When to use this

- Slack connections with user scopes fail with incomplete_raw_credentials.
- You need the Slack user token, not just the bot token.

## When NOT to use this

- Bot-token connections work and that is all you need; this fix is user-token-specific.
- Slack OAuth itself errors; check the Slack app config.

## Compatibility

- Nango with the PR #4025 fix.

## Variant phrasings

- "nango slack incomplete_raw_credentials"
- "nango slack user token missing"

## Root cause

The SDK only handled the bot token path, so the user token from the OAuth response was dropped before it reached the connection.

## Edge cases

- None reported; the upstream fix covers the user-scope path.

---

Source: [Vectle](https://vectle.com/skills/skl_CJg73SkxzOhYPBmIEt3TTg). Version: `skv_MDxhWj56Ib3mdrBTE-ce6w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
