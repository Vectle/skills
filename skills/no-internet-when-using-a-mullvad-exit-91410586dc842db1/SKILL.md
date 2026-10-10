---
name: "no-internet-when-using-a-mullvad-exit-91410586dc842db1"
description: "Fixes losing all internet connectivity when selecting a Mullvad exit node in Tailscale. Use when everything works without an exit node but enabling a Mullvad exit node kills browsing and DNS. Covers the verified admin-console DNS override fix plus allowing LAN access. Not for self-hosted exit nodes or Mullvad nodes that are down for everyone."
metadata:
  skill_id: "skl_Kx4JCVReQ2zVfAAGIzsjxg"
  title: "No internet when using a Mullvad exit node (disable the DNS override)"
  version: "skv_Cd_GWJ-n0kLMDHzq1-FOGQ"
  updated: "2026-10-03T04:41:26.933234+00:00"
  canonical_url: "https://vectle.com/skills/skl_Kx4JCVReQ2zVfAAGIzsjxg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix no internet with a Mullvad exit node

**TL;DR:** Turn OFF the "override DNS servers" option in the admin console and enable `--exit-node-allow-lan-access`. The DNS override is only needed on ancient Tailscale versions; on current ones it breaks Mullvad exit nodes.

## The error

```text
No internet connectivity when using Mullvad as exit node
```

`tailscale status` shows the Mullvad node as `active; exit node`, but nothing loads. Turning the exit node off fixes it instantly.

## Fix it

### 1. Disable the DNS override

In the admin console, open DNS settings and turn OFF "override DNS servers" (override local DNS).

Expected: no more forced DNS override for the tailnet.

### 2. Allow LAN access on the client

```
sudo tailscale up --exit-node-allow-lan-access
```

(re-run with whatever other flags you normally use).

Expected: local network still reachable while on the exit node.

### 3. Check the Mullvad server itself

Look up the specific server (e.g. ca-tor-wg-001) on the Mullvad server list and confirm it is online. Try a different Mullvad exit node if yours is down.

Expected: `tailscale exit-node list` shows candidates; pick a healthy one.

### 4. Re-test

```
tailscale status
curl -sI https://example.com | head -1
```

Expected: status shows the exit node active, and the curl returns HTTP/2 200 through it.

## When this applies

- Internet dies only when a Mullvad exit node is selected
- `tailscale status` shows the exit node as active
- You followed old guides that said to override DNS for Mullvad

## When it does not apply

- Self-hosted exit nodes broken (different checklist: IP forwarding, firewall)
- No exit node works at all (client or tailnet problem)
- The Mullvad node is down for everyone (pick another server)

## Tool compatibility

Tailscale 1.5x and newer with the Mullvad integration. The DNS-override advice changed across versions; current clients do not need it.

## Variant phrasings

### Timeouts opening connections "to node" via the Mullvad peer

The log form: `open-conn-track: timeout opening (TCP ... => 1.1.1.1:443) to node`. Same fix.

## Why it happens

Old docs told users to override DNS when using Mullvad exit nodes. Current Tailscale handles DNS through the exit node correctly on its own, and the forced override conflicts with it, so name resolution (and everything after it) dies.

## Edge cases

- **Docker on NixOS:** one reporter needed the host's routing features set to client mode and the container on host networking for exit-node traffic to flow. Container networking adds its own layer.
- **Still broken:** re-read the current Mullvad exit-node docs page; the recommended settings have changed more than once.
- **Per-node flakiness:** Mullvad servers do go down. Rule out the server before rebuilding your config.

---

Source: [Vectle](https://vectle.com/skills/skl_Kx4JCVReQ2zVfAAGIzsjxg). Version: `skv_Cd_GWJ-n0kLMDHzq1-FOGQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
