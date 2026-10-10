---
name: "backend-error-invalid-key-api-key-does-2ebea8678e6d9d19"
description: "Fixes tailscale failing with backend error: invalid key: API key does not exist after a key rotation or expiry. Use when a previously working key is rejected as nonexistent, commonly after Docker restarts past the 90-day expiry. Covers minting a replacement key. Not for expired-but-present keys."
metadata:
  skill_id: "skl_Hqaow1cfq0SwITFP2e52Cw"
  title: "backend error: invalid key: API key does not exist"
  version: "skv_6zQ3YZrKxBZ2p5LaJWIyUQ"
  updated: "2026-10-03T05:59:21.834133+00:00"
  canonical_url: "https://vectle.com/skills/skl_Hqaow1cfq0SwITFP2e52Cw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# backend error: invalid key: API key does not exist

TL;DR: the key in your config no longer exists server-side. The usual story is the 90-day expiry silently deleting it, then a container restart surfacing the failure. Create a fresh key in the admin console and update the config. The old key cannot be resurrected.

```text
backend error: invalid key: API key does not exist
```

## Steps

1. Open the admin console keys page and confirm the old key is gone.

Expected: it is not listed, or shows as expired and removed.

2. Generate a new auth key. For automation, tick reusable and consider disabling expiry.

Expected: the console shows the new key value once.

3. Update the key everywhere it is referenced: compose files, env files, CI secrets.

4. Restart the service:

```bash
docker compose up -d
```

Expected: the container joins the tailnet with no backend error.

## When this applies

- Docker setups that ran fine for months then fail after a restart
- keys created with the default 90-day expiry on long-lived automation
- the error appears immediately at startup, not mid-session

## When it doesnt

- `authkey expired` — that key still exists but aged out
- `authkey already used` — one-time key spent twice
- login or OAuth browser flows — no API key involved

## Compatibility

Any tailscale deployment using auth keys: Docker, CI, cloud-init.

## Other phrasings

- `tailscale API key does not exist after restart`
- `invalid key after 90 days tailscale`

## Why it happens

Expired keys are eventually removed server-side. The local config still references the old value, so the first join attempt after the deletion fails with this error. Docker restarts are the classic trigger because the container only reads the key at startup.

## Edge cases

- If you use a secrets manager, rotate the secret there rather than editing compose files by hand.
- After replacing the key, remove the stale node entry in the admin console to avoid confusion.


---

Source: [Vectle](https://vectle.com/skills/skl_Hqaow1cfq0SwITFP2e52Cw). Version: `skv_6zQ3YZrKxBZ2p5LaJWIyUQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
