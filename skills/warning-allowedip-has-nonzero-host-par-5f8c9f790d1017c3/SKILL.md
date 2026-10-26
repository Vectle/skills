---
name: "warning-allowedip-has-nonzero-host-par-5f8c9f790d1017c3"
description: "Fixes the WireGuard warning AllowedIP has nonzero host part on wg-quick up. Use when an AllowedIPs line sets host bits outside the network mask, like CONTAINER_IP/24. Covers correcting the CIDR to the network address or a /32. Not for key or interface-exists errors."
metadata:
  skill_id: "skl_lLxN14-HomWoow_IstdEZg"
  title: "Warning: AllowedIP has nonzero host part"
  version: "skv_E8beN5HhUQSQcxRjKTqMQg"
  updated: "2026-10-03T06:04:11.992317+00:00"
  canonical_url: "https://vectle.com/skills/skl_lLxN14-HomWoow_IstdEZg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/knightmare2600/example_music_infra/blob/HEAD/docs/wireguard/wireguard-troubleshooting.md\"]"
---

# Warning: AllowedIP has nonzero host part

TL;DR: your AllowedIPs line has host bits set outside the network mask, for example CONTAINER_IP/24. WireGuard warns and may route oddly. Change it to the network address (CONTAINER_IP/24) or use a /32 when you mean a single host.

```text
Warning: AllowedIP has nonzero host part
```

## Steps

1. Open the interface config:

```bash
sudo nano /etc/wireguard/wg0.conf
```

2. Find the offending line, something like:

```text
AllowedIPs = CONTAINER_IP/24
```

Change it to the network address:

```text
AllowedIPs = CONTAINER_IP/24
```

Or, if you meant exactly one host:

```text
AllowedIPs = CONTAINER_IP/32
```

3. Re-apply:

```bash
sudo wg-quick down wg0 && sudo wg-quick up wg0
```

Expected: the interface comes up with no warning, and `wg show` displays the peer.

## When this applies

- the warning appears on `wg-quick up`
- traffic to some hosts in the range behaves strangely
- configs copied from examples with a host address left in a /24

## When it doesnt

- `RTNETLINK answers: File exists` — an address conflict, not a mask issue
- handshake never completes — that is keys or endpoints, not this
- you intentionally want the whole subnet — then use the .0/24 form

## Compatibility

wireguard-tools on Linux, any peer config with AllowedIPs.

## Other phrasings

- `wg-quick warns nonzero host part`
- `AllowedIPs host bits set`

## Why it happens

A /24 network address must have the last octet zeroed. CONTAINER_IP/24 describes host .5 inside network CONTAINER_IP/24, so the kernel-facing route is ambiguous and WireGuard flags it.

## Edge cases

- the all-interfaces address/0 (full tunnel) never triggers this; only masked ranges with stray host bits do.
- Both sides should agree on the intended range or return traffic may take a different path.


---

Source: [Vectle](https://vectle.com/skills/skl_lLxN14-HomWoow_IstdEZg). Version: `skv_E8beN5HhUQSQcxRjKTqMQg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
