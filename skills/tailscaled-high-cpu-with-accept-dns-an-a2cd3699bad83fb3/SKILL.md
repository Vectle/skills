---
name: "tailscaled-high-cpu-with-accept-dns-an-a2cd3699bad83fb3"
description: "Fixes tailscaled eating CPU with 'dns udp' messages in syslog when --accept-dns is on with systemd-resolved. Use when top shows tailscaled at high CPU and the logs are full of DNS query lines on Ubuntu or similar. Covers the verified resolv.conf symlink fix from the Tailscale Linux DNS guide. Not for high CPU from serve/funnel left running or unrelated load."
metadata:
  skill_id: "skl_hLZ2jlXpfwPuE-d2eeK40A"
  title: "tailscaled high CPU with --accept-dns and systemd-resolved (resolv.conf fix)"
  version: "skv_AHljk9E-CbdpYhS-b3UnWg"
  updated: "2026-10-03T04:42:55.164703+00:00"
  canonical_url: "https://vectle.com/skills/skl_hLZ2jlXpfwPuE-d2eeK40A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix tailscaled high CPU with --accept-dns and systemd-resolved

**TL;DR:** Tailscale and systemd-resolved are fighting over `/etc/resolv.conf`, and the retry storm burns CPU. Point `/etc/resolv.conf` at the systemd stub resolver as the Tailscale Linux DNS guide describes, and CPU drops back to normal.

## The error

```text
CPU high on Ubuntu linux, --accept-dns (and systemd-resolved) related
```

Symptom level: `top` shows tailscaled chewing CPU, syslog fills with `dns udp` lines, and it correlates with `--accept-dns` being on.

## Fix it

### 1. Confirm the DNS fight

```
ls -l /etc/resolv.conf
journalctl -u tailscaled --since "10 minutes ago" | grep -c "dns udp"
```

Expected: resolv.conf is a plain file (not the systemd stub symlink), and the dns udp count is high.

### 2. Point resolv.conf at the systemd stub

```
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

This is the step from the Tailscale Linux DNS guide that fixed it for the reporter.

### 3. Restart both services

```
sudo systemctl restart systemd-resolved tailscaled
```

Expected: CPU settles within a minute; the dns udp log flood stops.

### 4. Verify

```
top -b -n1 | grep tailscaled
nslookup mymachine.mytailnet.ts.net
```

Expected: tailscaled near idle, MagicDNS still resolving.

## When this applies

- Ubuntu/Debian with systemd-resolved
- `--accept-dns` enabled (default on most installs)
- High tailscaled CPU plus `dns udp` syslog spam
- `/etc/resolv.conf` is not the stub symlink

## When it does not apply

- High CPU after running `tailscale serve` or `funnel` (reset serve instead)
- High CPU with DNS fully off (different cause)
- Non-systemd distros (no resolved to fight with)

## Tool compatibility

Tailscale 1.x on systemd Linux (Ubuntu 20.04/22.04 reported). The stub path is the same on current systemd.

## Variant phrasings

### tailscaled at 100%+ CPU, DNS queries rate-limited in logs

Same signature. Same fix.

## Why it happens

With accept-dns on, tailscaled manages DNS while systemd-resolved also manages `/etc/resolv.conf`. When the file is not the expected stub symlink, the two rewrite and re-read in a loop, and every query retries hard enough to show up as CPU.

## Edge cases

- **resolv.conf gets overwritten:** NetworkManager or DHCP hooks can replace the symlink on reboot. If the problem returns after reboot, make the symlink persistent via your network manager config.
- **You do not want Tailscale DNS:** `tailscale up --accept-dns=false` sidesteps the fight entirely, at the cost of MagicDNS.
- **Still high after the symlink:** check for the serve/funnel CPU variant; `tailscale serve status` should be empty.

---

Source: [Vectle](https://vectle.com/skills/skl_hLZ2jlXpfwPuE-d2eeK40A). Version: `skv_AHljk9E-CbdpYhS-b3UnWg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
