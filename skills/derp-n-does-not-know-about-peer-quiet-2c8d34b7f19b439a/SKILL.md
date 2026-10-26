---
name: "derp-n-does-not-know-about-peer-quiet-2c8d34b7f19b439a"
description: "Explains and quiets Tailscale's 'derp-N does not know about peer' log spam. Use when journalctl or syslog fills with magicsock messages about derp not knowing a peer and removing routes, usually naming peers that are offline or no longer in tailscale status. Covers the verified systemd override that silences the noise. Not for actual connectivity loss or DERP connection failures."
metadata:
  skill_id: "skl_nJ_In4WtRalTOMj5PRLFXw"
  title: "derp-N does not know about peer: quiet the Tailscale log spam"
  version: "skv_uRUnDOv6sEcRIKlhMPffmg"
  updated: "2026-10-03T04:39:06.516072+00:00"
  canonical_url: "https://vectle.com/skills/skl_nJ_In4WtRalTOMj5PRLFXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/14623\"]"
---

# Quiet "derp-N does not know about peer" log spam

**TL;DR:** That message is Tailscale noticing an offline peer and cleaning up a route. It is noise, not an outage. Cap the daemon log level with a systemd override and your logs go quiet.

## The error

```text
[unexpected] magicsock: derp-10 does not know about peer [0uI/W], removing route
```

Repeats every few seconds in `journalctl -u tailscaled`, with `[RATELIMIT]` lines noting dropped duplicates. The peer ID in brackets usually is not in your `tailscale status` output.

## Fix it

### 1. Confirm it is just offline-peer noise

```
tailscale status
```

Expected: your online peers look fine. The spam names devices that are offline or long gone. If real peers are unreachable, this skill is not your fix.

### 2. Quiet the logs with a systemd override

```
sudo mkdir -p /etc/systemd/system/tailscaled.service.d
printf "[Service]\nLogLevelMax=notice\n" | sudo tee -a /etc/systemd/system/tailscaled.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart tailscaled
```

Expected: the derp-peer messages stop; normal notices still log.

### 3. Optional: remove the dead devices

If the peer IDs belong to devices you retired, delete them in the admin console machines list. Fewer offline peers means fewer messages at the source.

Expected: spam volume drops even without the log-level cap.

## When this applies

- Logs repeat `derp-N does not know about peer ... removing route`
- The named peers are offline or unknown
- Everything actually works; it is just log volume

## When it does not apply

- Peers you need are unreachable (that is a connectivity problem)
- DERP connection errors on startup (different failure)
- Log spam about something other than unknown peers

## Tool compatibility

All Tailscale versions on systemd Linux. The override path is systemd-specific; other init systems need their own log filtering.

## Variant phrasings

### `[RATELIMIT] format("[unexpected] magicsock: derp-%d does not know about peer %s, removing route") (N dropped)`

Same messages, rate-limited. Same fix.

## Why it happens

When a peer goes offline, the DERP relay server tells your node it no longer knows that peer, and your node logs the route removal at a chatty level. With several offline devices it loops forever, which is why central log collectors notice it first.

## Edge cases

- **Subnet routers see it most:** reporters on pfSense and always-on routers hit this hardest because they never sleep and collect logs centrally.
- **LogLevelMax=notice is safe:** it only raises the floor; warnings and errors still log. Do not set it to `err` or you will miss real problems.
- **The messages will return** if you remove the override file, e.g. on a full reinstall. Keep the drop-in; it survives package upgrades.

---

Source: [Vectle](https://vectle.com/skills/skl_nJ_In4WtRalTOMj5PRLFXw). Version: `skv_uRUnDOv6sEcRIKlhMPffmg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
