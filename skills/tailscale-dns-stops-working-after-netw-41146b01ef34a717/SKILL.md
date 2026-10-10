---
name: "tailscale-dns-stops-working-after-netw-41146b01ef34a717"
description: "Fixes DNS queries dying on a Tailscale device after network link changes, with 'dns udp query' timeouts in the logs. Use when MagicDNS worked, then stops after wifi reconnects, suspend/resume, or other link changes, while other devices are fine. Covers the verified restart workaround for tailscaled plus systemd-resolved. Not for DNS that never worked or tailnet-wide DNS outages."
metadata:
  skill_id: "skl_Ve3UDdUBT6xid4fdtFrcaQ"
  title: "Tailscale DNS stops working after network changes (restart tailscaled + resolved)"
  version: "skv_TpWF9E7rrK8zcYslBJvBdA"
  updated: "2026-10-03T04:40:38.070089+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ve3UDdUBT6xid4fdtFrcaQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Tailscale DNS dying after network changes

**TL;DR:** After wifi reconnects or a link change, the local DNS path can wedge while everything else keeps working. Restart both `tailscaled` and `systemd-resolved` and DNS comes back.

## The error

```text
tailscaled[94666]: [RATELIMIT] format("dns udp query: %v") (15 dropped)
```

Symptom level: `ping mymachine` and `dig` time out, but `tailscale status` looks healthy and direct-IP traffic works.

## Fix it

### 1. Confirm it is the DNS path, not the tailnet

```
nslookup mymachine.mytailnet.ts.net
tailscale status
```

Expected: status is fine, name lookups time out. That isolates it to local DNS.

### 2. Restart both services

```
sudo systemctl restart tailscaled systemd-resolved
```

Expected: DNS works again within seconds. This is the workaround multiple reporters verified.

### 3. If it is wifi-only, try resolved alone

```
sudo systemctl restart systemd-resolved
```

One reporter on a Raspberry Pi found wifi triggered it while ethernet never did, and restarting just systemd-resolved was enough there.

Expected: lookups succeed without touching Tailscale.

## When this applies

- DNS worked, then broke after suspend, wifi roam, or link change
- Only one device affected
- Logs show `dns udp query` rate-limit messages
- Restarting fixes it temporarily

## When it does not apply

- DNS never worked on the device (initial config problem)
- All devices fail (check admin console DNS settings)
- Non-DNS traffic is also broken (network problem, not DNS)

## Tool compatibility

Tailscale on Linux with systemd-resolved (Ubuntu, Kubuntu, Raspberry Pi OS). Reported on 1.56 through recent 1.x.

## Variant phrasings

### MagicDNS stops working after a while

Same bug. The "after a while" is usually "after the first link change".

### `dns udp query` rate-limit spam in logs

The log signature. Same fix.

## Why it happens

After a link change, the DNS forwarder and systemd-resolved can disagree about which upstream to use, and queries black-hole. Restarting both re-syncs the resolver chain.

## Edge cases

- **It recurs:** if it happens on every roam, consider pinning the device to ethernet where possible, or scripting the resolved restart on link changes.
- **Non-systemd setups:** restart whatever provides local DNS (NetworkManager, dnsmasq) alongside tailscaled.
- **Heavy wifi use:** the Pi reporter feeding ADS-B data hit it most; busy wireless interfaces seem to trigger it more often.

---

Source: [Vectle](https://vectle.com/skills/skl_Ve3UDdUBT6xid4fdtFrcaQ). Version: `skv_TpWF9E7rrK8zcYslBJvBdA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
