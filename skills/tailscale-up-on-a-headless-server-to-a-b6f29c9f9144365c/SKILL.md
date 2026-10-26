---
name: "tailscale-up-on-a-headless-server-to-a-b6f29c9f9144365c"
description: "Connects a headless Linux server to Tailscale without a browser. Use when sudo tailscale up prints a login URL and waits forever on a machine with no browser. Covers approving the printed URL from another device, and the unattended path with tailscale up --authkey using a reusable auth key. Not for tailscaled not running or firewall issues."
metadata:
  skill_id: "skl_RqENuhopBsY-tKOM-lFSmQ"
  title: "tailscale up on a headless server: \"To authenticate, visit: https://login.tailscale.com/a/...\""
  version: "skv_xF0SaFTQEAJ25dESPzapSw"
  updated: "2026-10-03T04:44:47.865653+00:00"
  canonical_url: "https://vectle.com/skills/skl_RqENuhopBsY-tKOM-lFSmQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tech-drew/home-lab-mini-rack/blob/HEAD/v1-lego-infrastructure-prototype/docs/networking/tailscale-setup.md\"]"
---

# tailscale up on a headless server: "To authenticate, visit: https://login.tailscale.com/a/..."

TL;DR: on a headless box `tailscale up` cant open a browser, so it prints a login URL and waits. Either open that URL on your phone or laptop and approve the device, or skip the dance entirely with `tailscale up --authkey [your auth key]` using a reusable auth key from the admin console.

```text
To authenticate, visit: https://login.tailscale.com/a/[code]
```

## Steps

1. Start the join:

```bash
sudo tailscale up
```

Expected output includes the login URL shown above.

2. Open that URL on any device with a browser, sign in, and approve the machine. The command returns on its own once you approve.

3. Verify:

```bash
tailscale status
```

Expected: your node listed with a 100.x.x.x address.

4. Unattended path (scripts, rebuilds, containers): in the Tailscale admin console generate a reusable auth key, then:

```bash
sudo tailscale up --authkey [your auth key]
```

Expected: the node joins immediately, no URL printed.

## When this applies

- headless servers, VMs, and containers where `tailscale up` prints the URL and waits
- first-time joins with no browser on the box
- automated provisioning where nobody can click approve

## When it doesnt

- `failed to connect to local tailscaled` — the daemon isnt running; start the service first
- `invalid key` on --authkey — the key was single-use and already consumed; generate a reusable one
- nodes showing Logged out later — check key expiry in the admin console

## Compatibility

Tailscale 1.x, Linux, macOS, Windows.

## Why it happens

The CLI delegates identity to the browser-based control-plane login. With no browser the out-of-band approval URL is the only channel, and auth keys exist precisely for the no-human case.

## Edge cases

- keys expire: set a long expiry for servers or rotate on a schedule
- in Docker, pass the key as the TS_AUTHKEY env var instead of baking it into the image
- after `tailscale up --reset` you may need to re-approve the device

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=tailscale+up+headless+authenticate+visit'
```


---

Source: [Vectle](https://vectle.com/skills/skl_RqENuhopBsY-tKOM-lFSmQ). Version: `skv_xF0SaFTQEAJ25dESPzapSw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
