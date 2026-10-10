---
name: "tailscale-funnel-works-only-within-tai-11a0f53770597377"
description: "Fixes Tailscale Funnel being reachable only inside the tailnet instead of publicly. Use when tailscale funnel serves fine to tailnet peers but external visitors get nothing or a TLS stall. Covers the userspace-networking cause found by reporters: funnel needs kernel WireGuard mode for public ingress. Not for funnel setup errors or serve path mistakes."
metadata:
  skill_id: "skl_Fb6zfu72VOrYSnaEvDBhUw"
  title: "Tailscale funnel works only within tailnet, not publicly (userspace mode fix)"
  version: "skv_d7gp8STpl-PDyJLSrqJtwA"
  updated: "2026-10-03T04:41:03.855085+00:00"
  canonical_url: "https://vectle.com/skills/skl_Fb6zfu72VOrYSnaEvDBhUw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Tailscale Funnel reachable only inside the tailnet

**TL;DR:** If `tailscale funnel` works for tailnet peers but not the public internet, you are probably running in userspace networking mode. Funnel's public ingress needs kernel WireGuard mode. Run tailscaled normally (no userspace flag) and the public URL starts working.

## The error

```text
Funnel works only within tailnet
```

No CLI error: `tailscale funnel 8080` says it is live, tailnet devices reach it, but external browsers time out or stall on TLS.

## Fix it

### 1. Check for userspace networking

```
tailscale debug --help 2>/dev/null | head -2
ps aux | grep tailscaled | grep -o "tun=[a-z]*"
```

Simpler: recall how you started it. Docker setups often pass userspace mode; check for `TS_USERSPACE` in your container env or `--tun=userspace-netstack` in the daemon flags.

Expected: you find userspace networking in play.

### 2. Switch to kernel WireGuard mode

Remove the userspace setting (unset `TS_USERSPACE`, drop `--tun=userspace-netstack`) and restart the daemon or container.

```
sudo systemctl restart tailscaled
```

Expected: `tailscale status` still connected, now via kernel mode.

### 3. Re-enable funnel and test externally

```
tailscale funnel 8080
```

Then visit the public funnel URL from a device NOT on your tailnet (phone with wifi, not VPN).

Expected: the page loads publicly.

## When this applies

- Funnel URL works on tailnet, fails externally
- Tailscale runs in a container or with userspace networking
- No funnel config errors; the dashboard shows funnel live

## When it does not apply

- Funnel fails for tailnet peers too (serve/funnel config problem)
- `tailscale funnel` prints an error immediately (read the error)
- You need userspace mode for other reasons (then public funnel is not available; use serve inside the tailnet instead)

## Tool compatibility

Tailscale 1.x on Linux, especially Docker deployments. Kernel mode needs TUN device access.

## Variant phrasings

### External clients get ERR_SSL_PROTOCOL_ERROR from funnel

Same family: the public edge cannot complete TLS to a userspace-mode node. Same fix.

### Funnel status says on but public CDN edges stall on TLS handshake

Same root cause, observed at the edge. Same fix.

## Why it happens

Funnel's public ingress terminates at Tailscale's edge and needs to reach your node over a real WireGuard path. In userspace networking mode the node's ingress path does not behave the way the funnel edge expects, so tailnet traffic (which uses a different path) works while public traffic stalls.

## Edge cases

- **Docker without TUN:** kernel mode needs `/dev/net/tun`. If your container cannot get it, public funnel is off the table; keep funnel tailnet-only via `tailscale serve`.
- **Intermittent external stalls:** some reporters saw external funnel break for hours then recover with no changes. If kernel mode is already on, wait it out before rebuilding.
- **Confirm the mode stuck:** after restart, `tailscale status` should not show userspace indicators; re-check your env/flags if the problem persists.

---

Source: [Vectle](https://vectle.com/skills/skl_Fb6zfu72VOrYSnaEvDBhUw). Version: `skv_d7gp8STpl-PDyJLSrqJtwA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
