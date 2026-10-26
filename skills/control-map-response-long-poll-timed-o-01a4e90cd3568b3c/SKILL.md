---
name: "control-map-response-long-poll-timed-o-01a4e90cd3568b3c"
description: "Fixes Tailscale losing connectivity with 'control: map response long-poll timed out!' in the logs and never reconnecting. Use when a node (often in a container) goes dark, the log shows the long-poll timeout, and only a manual restart of tailscaled brings it back. Covers the restart plus a watchdog that restarts the daemon when the message appears. Not for DERP failures or login problems."
metadata:
  skill_id: "skl_OzMotb2Iz2Qcqtwqto07ug"
  title: "control: map response long-poll timed out and Tailscale never reconnects"
  version: "skv_ICPmEckP2P8K2cJUnPkYyA"
  updated: "2026-10-03T04:39:30.908082+00:00"
  canonical_url: "https://vectle.com/skills/skl_OzMotb2Iz2Qcqtwqto07ug"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/12021\"]"
---

# Fix "control: map response long-poll timed out" with no reconnect

**TL;DR:** When Tailscale logs this, the control-plane connection is dead and the daemon sometimes never notices. Restart `tailscaled` to recover, then add a tiny watchdog that restarts it automatically next time.

## The error

```text
control: map response long-poll timed out!
```

The node stops passing traffic and never recovers on its own. Common in containers, where nothing restarts the daemon for you.

## Fix it

### 1. Recover right now

```
sudo systemctl restart tailscaled
tailscale status
```

Expected: status shows connected and traffic flows again.

In a container without systemd, restart the container or re-run the tailscaled process.

### 2. Add a watchdog so it self-heals

A simple approach: a cron job every few minutes that looks for the message and restarts the service.

```
#!/bin/bash
if journalctl -u tailscaled --since "10 minutes ago" | grep -q "map response long-poll timed out"; then
  systemctl restart tailscaled
fi
```

Expected: the next stall clears itself within minutes instead of waiting for you.

### 3. For containers: make the failure visible

If your orchestrator can restart on failure, have the watchdog exit nonzero instead of restarting in place, so the container gets recycled:

```
#!/bin/bash
if journalctl -u tailscaled --since "10 minutes ago" | grep -q "map response long-poll timed out"; then
  exit 1
fi
```

Expected: orchestrator restarts the container, Tailscale reconnects fresh.

## When this applies

- Logs show `control: map response long-poll timed out!`
- The node stops working and stays broken until manual restart
- Especially containers and always-on appliances

## When it does not apply

- Occasional long-poll timeouts that recover on their own (normal on flaky networks)
- DERP relay errors (different subsystem)
- Login or auth failures

## Tool compatibility

All Tailscale versions; reported on Linux containers and Debian hosts. The journalctl watchdog needs systemd; adapt the log source for other setups.

## Variant phrasings

### Node goes dark after WAN/IP change, only restart helps

Same family. One reporter found nothing but a restart recovered the DERP path after an ISP IP change. The watchdog covers this too.

## Why it happens

The long-poll is how the client hears about network updates. If the underlying TCP connection stalls silently (middleboxes, NAT timeouts), the client can sit forever waiting on a dead socket instead of reconnecting.

## Edge cases

- **Do not watchdog too aggressively:** checking every minute and restarting on any single timeout can flap a node that would have recovered. Five to ten minute windows are saner.
- **Stalled TCP variant:** one reporter instead watched for unsent bytes piling up on the control-plane connection and killed just that connection. If restarts feel heavy, that is the lighter scalpel.
- **This is a known upstream gap:** the issue asks for self-detection; until that lands, the watchdog is the supported-by-experience answer.

---

Source: [Vectle](https://vectle.com/skills/skl_OzMotb2Iz2Qcqtwqto07ug). Version: `skv_ICPmEckP2P8K2cJUnPkYyA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
