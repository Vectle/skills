---
name: "failed-to-connect-to-local-tailscaled-0ec60c48e43176e1"
description: "Fixes Tailscale's 'failed to connect to local tailscaled' CLI error. Use when any tailscale command reports it cannot reach the local daemon, on Linux, WSL, macOS, or Synology after migration. Covers starting a stopped tailscaled, socket permission problems, and the WSL no-systemd case. Not for login failures, duplicate node keys, or machines that are connected but cannot reach peers."
metadata:
  skill_id: "skl_KWCJWvMn0oPVaQ0bVRK53A"
  title: "failed to connect to local tailscaled: how to fix the Tailscale daemon connection"
  version: "skv_-AfDoLFahmGQ0Bz72_DKOA"
  updated: "2026-10-03T04:33:49.101201+00:00"
  canonical_url: "https://vectle.com/skills/skl_KWCJWvMn0oPVaQ0bVRK53A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/7229\"]"
---

# Fix "failed to connect to local tailscaled"

**TL;DR:** This error means the `tailscale` CLI cant reach the `tailscaled` daemon on your machine. It is never a network problem. Start (or restart) the daemon, and if you are on WSL, start it by hand because there is no systemd to do it for you.

## The error

```text
failed to connect to local tailscaled
```

Often with a detail like `(which appears to be running as tailscaled, pid 147358)` or `Got error: Get "http://local-tailscaled.sock/localapi/v0/status": EOF`. Every `tailscale` subcommand fails the same way.

## Fix it

### 1. Check whether the daemon is actually running

```
ps aux | grep -v grep | grep tailscaled
```

Expected: a `tailscaled` process line. No line means the daemon is simply not running, which is the most common cause.

### 2. Start the daemon

On systemd Linux:

```
sudo systemctl enable --now tailscaled
sudo systemctl status tailscaled
```

Expected: `active (running)` in the status output.

On macOS, open the Tailscale app once; the system extension starts the daemon. On Windows, start the Tailscale service from Services.

### 3. WSL: start it by hand

WSL distros often run without systemd, so the deb package install never starts the daemon (gh:tailscale/tailscale#562). Either enable systemd in `/etc/wsl.conf`:

```
[boot]
systemd=true
```

then restart WSL, or start the daemon manually each session:

```
sudo tailscaled &
```

Expected: `tailscale status` returns your machine info instead of the error.

### 4. Rule out a wedged daemon

If the process exists but the CLI still fails with an EOF on the socket, the daemon is wedged. Restart it:

```
sudo systemctl restart tailscaled
```

then retry the command. One reporter hit exactly this after a network change; a retry after the daemon settled worked.

Expected: the second attempt connects cleanly.

## When this applies

- Any `tailscale` command prints "failed to connect to local tailscaled"
- Fresh install on WSL / Ubuntu where the daemon never started
- After migration or restore (Synology reporters hit this too)
- Daemon process exists but the socket read fails with EOF

## When it does not apply

- `tailscale up` fails during login (that is an auth/control-plane problem)
- `tailscale status` works but peers are unreachable (network/DERP/ACL problem)
- The admin console shows a duplicate node key warning (different fix)

## Tool compatibility

All Tailscale clients. The WSL variant is Linux-only; the systemd steps need Tailscale 1.x with the distro package.

## Variant phrasings

### "failed to connect to local tailscaled (which appears to be running as tailscaled, pid ...)"

Same error with a pid attached. The daemon process exists but is not answering the socket. Restart it (step 4).

### Synology after migration: "failed to connect to local tailscaled"

The package daemon did not survive the migration. Reinstall or restart the Synology package, then `tailscale up` again.

## Why it happens

The CLI is a thin client; all real work happens in the `tailscaled` daemon, reached over a local socket. Anything that stops the daemon (no init system, failed package install, a wedged process after suspend/network change) produces this exact message.

## Edge cases

- **Socket permission denied:** if the error mentions permissions on the socket instead, your user needs access to the daemon (usually just run that one command with sudo to confirm, then fix group membership).
- **It comes and goes:** transient EOFs right after boot or network changes usually clear on retry once the daemon finishes starting. If it never clears, something is crashing the daemon; check `journalctl -u tailscaled`.
- **Docker:** the container needs the tailscaled socket or its own daemon with the right privileges; a bare `tailscale` CLI in a container without a daemon always prints this.

---

Source: [Vectle](https://vectle.com/skills/skl_KWCJWvMn0oPVaQ0bVRK53A). Version: `skv_-AfDoLFahmGQ0Bz72_DKOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
