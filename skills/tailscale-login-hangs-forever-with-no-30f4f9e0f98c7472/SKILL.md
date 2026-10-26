---
name: "tailscale-login-hangs-forever-with-no-30f4f9e0f98c7472"
description: "Fixes 'tailscale login' hanging forever without showing a login link. Use when the command never returns and never prints a URL, on Linux hosts where the daemon state may be wedged. Covers deleting the stale state file and logging in fresh, the user-verified fix. Not for login links that error in the browser or auth-key problems."
metadata:
  skill_id: "skl_fqYIOAzmzPW2wquNRca7TQ"
  title: "tailscale login hangs forever with no login link (state file fix)"
  version: "skv_uOytjZAn2ZOJ28o0gBFMgw"
  updated: "2026-10-03T04:39:52.592706+00:00"
  canonical_url: "https://vectle.com/skills/skl_fqYIOAzmzPW2wquNRca7TQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/9514\"]"
---

# Fix `tailscale login` hanging forever

**TL;DR:** The login is stuck on wedged local state, not on the network. Delete `/var/lib/tailscale/tailscaled.state`, then run `tailscale up` and log in fresh.

## The error

```text
$ tailscale login
(hangs forever, no login link appears)
```

Logs show the client sitting in `NeedsLogin` state and going nowhere.

## Fix it

### 1. Kill any stuck login attempt

Ctrl-C the hung command.

### 2. Delete the stale state file

```
sudo rm /var/lib/tailscale/tailscaled.state
```

This wipes the local login state. Your tailnet devices and settings in the admin console are untouched.

### 3. Log in fresh

```
sudo tailscale up
```

Expected: a login URL prints within seconds. Open it, authenticate, and the command completes.

### 4. Re-apply your flags

If you normally pass flags like `--accept-dns=false`, add them back after the first successful login. One reporter found the hang only happened when the flag was passed on a wedged state; after the state wipe, everything worked with or without flags.

Expected: `tailscale status` shows connected.

## When this applies

- `tailscale login` or `tailscale up` hangs with no URL and no error
- Retrying and restarting the daemon do not help
- Logs show the client stuck in `NeedsLogin`

## When it does not apply

- A login URL appears but fails in the browser (account/auth problem)
- `tailscale up --auth-key` fails immediately (key problem)
- The daemon itself will not start (see the daemon skills)

## Tool compatibility

Tailscale on Linux with the standard state path. Reported on 1.88.x; the state-file layout is the same across 1.x.

## Variant phrasings

### `tailscale up` hangs the same way

Same root cause and same fix. `login` and `up` share the state file.

### `tailscale status` says `unexpected state: NoState`

A related symptom reporters saw alongside the hang. The state wipe fixes this too.

## Why it happens

The daemon persists login progress in the state file. If a previous attempt died mid-write or the stored credentials went stale in a way the client does not detect, every new login replays the same broken state instead of starting over.

## Edge cases

- **You will re-authenticate:** deleting state logs the machine out. Keep a browser handy.
- **Headless servers:** use `tailscale up --auth-key` with a fresh auth key after the wipe instead of the interactive flow.
- **It comes back:** if logins hang again weeks later, something is corrupting state on shutdown; check disk health and unclean reboots.

---

Source: [Vectle](https://vectle.com/skills/skl_fqYIOAzmzPW2wquNRca7TQ). Version: `skv_uOytjZAn2ZOJ28o0gBFMgw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
