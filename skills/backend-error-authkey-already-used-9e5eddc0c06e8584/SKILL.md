---
name: "backend-error-authkey-already-used-9e5eddc0c06e8584"
description: "Fixes tailscale up failing with backend error: authkey already used when containers or ephemeral nodes re-register. Use when a one-time key worked once and the next boot fails. Covers making the key reusable and persisting the state directory. Not for expired or deleted keys."
metadata:
  skill_id: "skl_-F0dAil1VJooP2K9eHra2A"
  title: "backend error: authkey already used"
  version: "skv_I4sxokFW1hw0EKDUoxu6SA"
  updated: "2026-10-03T05:58:26.568918+00:00"
  canonical_url: "https://vectle.com/skills/skl_-F0dAil1VJooP2K9eHra2A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# backend error: authkey already used

TL;DR: your auth key is single-use and something already spent it — usually a container that registered, restarted, and tried to register again. Make the key reusable on the admin console keys page, or persist the tailscale state directory so restarts reuse the node's identity instead of re-registering.

```text
backend error: authkey already used
```

## Steps

1. Open the admin console keys page and edit the key. Enable reusable.

Expected: the key can now register more than one node.

2. For containers, persist the state so a restart does not look like a new node. Mount a volume at the state dir and set the env var, for example:

```bash
TS_STATE_DIR=/var/lib/tailscale
```

Expected: after a restart, `tailscale status` shows the same node name, not a -1 suffixed duplicate.

3. Clean up any duplicate nodes the failed retries created in the admin console.

Expected: one machine entry per real node.

## When this applies

- Docker or VM images that run `tailscale up --authkey` on every boot
- one-time keys used in auto-scaling groups or CI fleets
- the first node joined fine and every later one fails

## When it doesnt

- `authkey expired` — the key aged out, make a new one
- `invalid key: API key does not exist` — the key was deleted server-side
- nodes joining fine but traffic not flowing — that is routing, not auth

## Compatibility

tailscale CLI on Linux containers and VMs using pre-auth keys.

## Other phrasings

- `tailscale authkey already used on second boot`
- `backend error: authkey has already been used`

## Why it happens

A non-reusable auth key is consumed by the first successful registration. The second boot looks like a brand-new node asking to spend the same key, and the control plane refuses. Persisting state avoids the second registration entirely.

## Edge cases

- Reusable keys let anyone with the value join your tailnet; scope them with tags and short expiry where possible.
- If you persist state, also persist across image rebuilds or the -1 duplicate problem returns.


---

Source: [Vectle](https://vectle.com/skills/skl_-F0dAil1VJooP2K9eHra2A). Version: `skv_I4sxokFW1hw0EKDUoxu6SA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
