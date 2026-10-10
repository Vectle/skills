---
name: "rtnetlink-answers-file-exists-daa683e3293e35be"
description: "Fixes wg-quick failing with RTNETLINK answers: File exists when bringing up a WireGuard interface. Use when the address or route wg-quick wants to add is already present. Covers bringing the interface down cleanly first. Not for key errors or missing config files."
metadata:
  skill_id: "skl_myRUIFRxWDc-8n10s7hLPA"
  title: "RTNETLINK answers: File exists"
  version: "skv_9YI61UQWCiEeuXuUreMEaw"
  updated: "2026-10-03T06:03:13.846747+00:00"
  canonical_url: "https://vectle.com/skills/skl_myRUIFRxWDc-8n10s7hLPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# RTNETLINK answers: File exists

TL;DR: the address or route wg-quick wants to add is already on the interface from an earlier run. Bring the interface down first with `wg-quick down wg0`, confirm it is gone, then bring it up again.

```text
RTNETLINK answers: File exists
```

## Steps

1. Take the interface down cleanly:

```bash
sudo wg-quick down wg0
```

Expected: no output, and `ip link show wg0` reports the device does not exist.

2. If it is still there, remove the leftover address by hand:

```bash
sudo ip link delete wg0
```

Expected: `ip link show wg0` finds nothing.

3. Bring it up again:

```bash
sudo wg-quick up wg0
```

Expected: the interface comes up with no RTNETLINK complaint, and `wg show` lists your peers.

## When this applies

- `wg-quick up` after a previous `up` half-succeeded or was killed
- the interface was created manually with `ip link add` and then wg-quick ran
- Address lines duplicated across config files

## When it doesnt

- `wg-quick: 'wg0' already exists` — that is the interface-level twin of this error
- `Key is not the correct length or format` — a key problem, not an address one
- no route to the peer — that is routing, not this

## Compatibility

wireguard-tools wg-quick on Linux.

## Other phrasings

- `RTNETLINK answers: File exists wg-quick up`
- `wireguard File exists on up`

## Why it happens

wg-quick is a script that adds addresses and routes one by one. It does not check first whether they already exist, so any leftover from a crashed or manual setup makes the kernel refuse the duplicate.

## Edge cases

- If `wg-quick down` says the interface is not defined, the config name and interface name may differ; match them.
- NetworkManager or systemd-networkd fighting over the same interface can recreate the conflict; pick one manager.


---

Source: [Vectle](https://vectle.com/skills/skl_myRUIFRxWDc-8n10s7hLPA). Version: `skv_9YI61UQWCiEeuXuUreMEaw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
