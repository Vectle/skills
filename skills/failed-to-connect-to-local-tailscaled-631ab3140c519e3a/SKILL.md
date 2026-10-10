---
name: "failed-to-connect-to-local-tailscaled-631ab3140c519e3a"
description: "Fixes the tailscale CLI failing with failed to connect to local tailscaled when the tailscaled daemon is not running or its socket is unreachable. Use right after install, after a reboot, or when every tailscale command fails the same way. Covers starting and enabling the daemon. Not for login, authkey, or account errors."
metadata:
  skill_id: "skl_NPwV__5cl6yMBle9m-Vebg"
  title: "failed to connect to local tailscaled"
  version: "skv_UwucBd_NwO-3Pfw2RSbDYA"
  updated: "2026-10-03T05:56:42.826476+00:00"
  canonical_url: "https://vectle.com/skills/skl_NPwV__5cl6yMBle9m-Vebg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# failed to connect to local tailscaled

TL;DR: the tailscaled daemon is not running on this machine. Start it with your init system (`sudo systemctl start tailscaled` on Linux), then retry the tailscale command. The CLI is a thin client that talks to the daemon over a local socket; no daemon means every command fails.

```text
failed to connect to local tailscaled
```

## Steps

1. Check whether the daemon is running:

```bash
systemctl status tailscaled
```

Expected: `active (running)`. If it says inactive or failed, continue.

2. Start it:

```bash
sudo systemctl start tailscaled
```

Expected: no output, and `systemctl status tailscaled` now shows active.

3. Retry your command:

```bash
tailscale status
```

Expected: your node listed with its tailnet addresses, no socket error.

4. Make it survive reboots:

```bash
sudo systemctl enable --now tailscaled
```

Expected: `Created symlink ...` and the service stays active.

## When this applies

- right after installing tailscale, before the daemon was ever enabled
- after a reboot on a box where the service was installed but never enabled
- snap installs where the service needs a nudge (see the source playbook)

## When it doesnt

- `tailscale up` opening a browser login — that is authentication, not the daemon
- `backend error: authkey ...` failures — see the authkey skills
- the daemon runs but the node cannot reach the control plane — that is network, not this

## Compatibility

tailscale CLI on Linux (systemd). On macOS and Windows the daemon ships inside the app itself.

## Other phrasings

- `can't connect to tailscaled`
- `tailscale: failed to connect to local tailscaled, it may not be running`

## Why it happens

The tailscale CLI holds no state of its own. It sends every command to tailscaled, the background daemon that owns your keys and WireGuard state, over a local socket. If the daemon never started, the socket does not exist and the CLI has nobody to talk to.

## Edge cases

- On macOS and Windows there is no systemd service; if the app is not running, start the app.
- Minimal containers may lack systemd; run `tailscaled` directly in the background instead.
- A stale socket file after a crash can also produce this error; deleting the socket and restarting the daemon clears it.


---

Source: [Vectle](https://vectle.com/skills/skl_NPwV__5cl6yMBle9m-Vebg). Version: `skv_UwucBd_NwO-3Pfw2RSbDYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
