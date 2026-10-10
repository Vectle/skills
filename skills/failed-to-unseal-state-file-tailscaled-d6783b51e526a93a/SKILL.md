---
name: "failed-to-unseal-state-file-tailscaled-d6783b51e526a93a"
description: "Fixes tailscaled failing to start with 'failed to unseal state file' or TPM_RC_INTEGRITY errors after an upgrade or firmware change. Use when the tailscaled service will not start on Linux and the logs mention unsealing the state file or tpm2.Load integrity failures. Covers disabling TPM state encryption as the verified workaround. Not for duplicate node keys, login failures, or the daemon failing for unrelated reasons."
metadata:
  skill_id: "skl_xwz9jVKWfGGOd7uoO3zfcg"
  title: "failed to unseal state file: tailscaled wont start after upgrade (TPM fix)"
  version: "skv_Yzxbhb9xbOIbznThBWgu_g"
  updated: "2026-10-03T04:37:47.405134+00:00"
  canonical_url: "https://vectle.com/skills/skl_xwz9jVKWfGGOd7uoO3zfcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix tailscaled "failed to unseal state file" after an upgrade

**TL;DR:** Tailscale 1.90.x encrypts its state file with the TPM, and a firmware or upgrade change can make the TPM refuse to unseal it. Disable state encryption with `--encrypt-state=false` in `/etc/default/tailscaled`, restart the daemon, and it starts cleanly.

## The error

```text
failed to unseal state file
```

In the logs it looks like:

```text
getLocalBackend error: ipnlocal.NewLocalBackend: failed to load profile prefs: parsing saved prefs: tpm2.Load: TPM_RC_INTEGRITY (parameter 1): integrity check failed
```

`systemctl status tailscaled` shows the service failed right after start.

## Fix it

### 1. Confirm this is the TPM state problem

```
journalctl -u tailscaled --since "1 hour ago" | grep -i -m2 -E "unseal|tpm2"
```

Expected: lines mentioning unseal or tpm2.Load failures. If you see something else, this skill is not your fix.

### 2. Disable state encryption

```
sudo bash -c 'cat > /etc/default/tailscaled <<EOF
PORT=0
FLAGS="--encrypt-state=false"
EOF'
```

### 3. Verify the daemon picks up the flag, then restart

```
sudo systemctl restart tailscaled
sudo systemctl status tailscaled
```

Expected: the status output shows the daemon running with your flags line present, and `active (running)`.

### 4. Re-authenticate if needed

If the old encrypted state is unreadable, the daemon starts fresh and you may need to log in again:

```
tailscale up
```

Expected: `tailscale status` shows connected.

## When this applies

- tailscaled fails to start right after a Tailscale 1.90.x upgrade
- A BIOS/firmware upgrade happened around the same time
- Logs mention `tpm2.Load`, `TPM_RC_INTEGRITY`, or "failed to unseal"

## When it does not apply

- tailscaled fails with no TPM mentions (check the actual error)
- The TPM lockout variant `TPM_RC_LOCKOUT` (different skill: upgrade to 1.92.1+)
- `tailscale up` login failures on a running daemon

## Tool compatibility

Tailscale 1.90.x on Linux with TPM2 (reported on Arch; also seen on Debian/Ubuntu). The `/etc/default/tailscaled` path is Debian/Ubuntu/Arch packaging; adjust for your distro.

## Variant phrasings

### `tpm2.Load: TPM_RC_INTEGRITY (parameter 1): integrity check failed`

Same root cause, fuller log line. Same fix.

### State migration failure on upgrade (1.90.2)

A sibling issue (gh#17622) covered TPM state migration failing on upgrade; if the `--encrypt-state=false` workaround from there did not help, this is the next step (full reinstall + the flag).

## Why it happens

Starting with 1.90.x, tailscaled can seal its state file to the TPM. If the TPM state changes out from under it (firmware upgrade, PCR changes), the unseal fails integrity checks and the daemon refuses to start rather than run with unreadable state.

## Edge cases

- **Security tradeoff:** `--encrypt-state=false` stores the state unencrypted on disk. On a single-user laptop that is usually acceptable; on shared hardware, prefer re-sealing to the TPM after a firmware update instead.
- **Verify the flag stuck:** reporters had to double-check with `systemctl status tailscaled` that the daemon really launched with the flag; a stale override file can silently win.
- **Still failing:** a full uninstall/reinstall before applying the flag cleared leftover encrypted state for the reporter.

---

Source: [Vectle](https://vectle.com/skills/skl_xwz9jVKWfGGOd7uoO3zfcg). Version: `skv_Yzxbhb9xbOIbznThBWgu_g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
