---
name: "backend-error-authkey-expired-4a829125beb928f7"
description: "Fixes tailscale up failing with backend error: authkey expired in CI and automated setups. Use when a pre-auth key that used to work now fails the join. Covers minting a fresh key and turning off expiry for long-lived fleets. Not for one-time keys already consumed, or keys that never existed."
metadata:
  skill_id: "skl_gFooA1gRxIN6kL0hIMLD3w"
  title: "backend error: authkey expired"
  version: "skv_GzIOWkS6IURHtwlfX4lBig"
  updated: "2026-10-03T05:57:33.419348+00:00"
  canonical_url: "https://vectle.com/skills/skl_gFooA1gRxIN6kL0hIMLD3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# backend error: authkey expired

TL;DR: the pre-auth key baked into your pipeline has expired. Mint a new key on the admin console keys page, mark it reusable and disable expiry if the fleet is long-lived, then swap it into your CI secret. Expired keys cannot be revived.

```text
backend error: authkey expired
```

## Steps

1. Open the admin console and go to the keys page.

2. Generate a new auth key. Tick reusable, and for long-lived CI fleets disable key expiry.

Expected: the console shows the new key value once. Copy it now.

3. Replace the old key in your CI secrets or env config with the new value.

4. Re-run the join:

```bash
tailscale up --authkey [your new key]
```

Expected: the node appears in the admin console machines list, no backend error.

## When this applies

- CI runners or cloud-init scripts that join the tailnet with a stored key
- the same key worked last month and fails now with no config change
- keys with the default 90-day expiry on long-lived automation

## When it doesnt

- `authkey already used` — that is a one-time key spent twice, a different fix
- `invalid key: API key does not exist` — the key was deleted, not expired
- interactive `tailscale up` asking for a browser login — no key involved

## Compatibility

tailscale CLI anywhere `tailscale up --authkey` is used: CI runners, cloud-init, Docker entrypoints.

## Other phrasings

- `tailscale up fails: authkey expired`
- `pre-auth key expired`

## Why it happens

Auth keys carry an expiry timestamp. When it passes, the control plane rejects the key at join time. Automation that worked for months breaks overnight with no other change, which is why this one is confusing the first time.

## Edge cases

- Disabling expiry is convenient but widens the blast radius if the key leaks; prefer short-lived keys injected per-run where you can.
- If nodes join but immediately disappear, check whether an old expired key is still cached in a second config path.


---

Source: [Vectle](https://vectle.com/skills/skl_gFooA1gRxIN6kL0hIMLD3w). Version: `skv_GzIOWkS6IURHtwlfX4lBig`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
