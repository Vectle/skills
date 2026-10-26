---
name: "failed-to-unseal-encryption-key-with-t-17010b2df8927bbc"
description: "Fixes tailscaled failing to start with 'failed to unseal encryption key with TPM: tpm2.Unseal: TPM_RC_LOCKOUT' on Tailscale 1.90.x. Use when the daemon will not start after reboot on Linux with TPM2 and downgrading to 1.88.x is the only thing that works. Covers the confirmed fixed version to upgrade to. Not for TPM_RC_INTEGRITY errors (different skill) or general daemon start failures."
metadata:
  skill_id: "skl_HBVvyD58Xu_-d3jwVIUxuQ"
  title: "failed to unseal encryption key with TPM: tpm2.Unseal: TPM_RC_LOCKOUT (fix: upgrade)"
  version: "skv_XQMyrV5KpxpNlU_YXSFlpg"
  updated: "2026-10-03T04:38:18.867105+00:00"
  canonical_url: "https://vectle.com/skills/skl_HBVvyD58Xu_-d3jwVIUxuQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/18005\"]"
---

# Fix "failed to unseal encryption key with TPM: tpm2.Unseal: TPM_RC_LOCKOUT"

**TL;DR:** This is a Tailscale 1.90.x bug on TPM2 machines. Upgrade to 1.92.1 or newer and the daemon starts normally again. The `--encrypt-state=false` workaround does not reliably help here, so do not waste time on it.

## The error

```text
failed to unseal encryption key with TPM: tpm2.Unseal: TPM_RC_LOCKOUT
```

`tailscaled` fails to start after every reboot or `systemctl restart tailscaled`. Rolling back to 1.88.x makes it work again.

## Fix it

### 1. Confirm you are on an affected version

```
tailscale version
```

Expected: 1.90.x. If you are already on 1.92.1+ and still see this, you have a different problem (check the TPM_RC_INTEGRITY skill).

### 2. Upgrade past the bug

```
sudo apt update && sudo apt install --only-upgrade tailscale
```

(or your distro equivalent). You want 1.92.1 or newer.

Expected: `tailscale version` reports 1.92.1+.

### 3. Restart and reboot-test

```
sudo systemctl restart tailscaled
sudo systemctl status tailscaled
```

Expected: `active (running)`. Then reboot once and confirm it comes up on its own. The reporter verified both restart and reboot work cleanly on 1.92.1 with no workarounds.

## When this applies

- tailscaled fails to start on every boot on 1.90.x
- The log names `tpm2.Unseal` with `TPM_RC_LOCKOUT`
- Downgrading to 1.88.x fixes it
- TPM2 hardware present (Intel/AMD firmware TPM counts)

## When it does not apply

- `TPM_RC_INTEGRITY` instead of `TPM_RC_LOCKOUT` (use the unseal-state-file skill)
- tailscaled fails on a machine without a TPM
- The daemon starts but login fails

## Tool compatibility

Tailscale 1.90.x on Linux with TPM2 (reported on Debian 13, Ubuntu 20.04). Fixed in 1.92.1.

## Variant phrasings

### Daemon fails after "systemd service restart" but worked on 1.88.4

Same bug. The version boundary is the giveaway: broken on all 1.90.x, fine on 1.88.4, fixed in 1.92.1.

## Why it happens

The 1.90.x state-encryption code trips the TPM's dictionary-attack lockout logic on some firmware, so the unseal fails with TPM_RC_LOCKOUT and the daemon gives up. 1.92.1 changed the behavior so the lockout no longer triggers.

## Edge cases

- **The encrypt-state workaround:** several reporters tried `TS_ENCRYPT_STATE=false` / `--encrypt-state=false` and it did not help on the affected hosts. Upgrade instead.
- **One host affected, others fine:** reporters saw this on one machine while identical OS installs elsewhere were fine. It is firmware/TPM specific, not config.
- **Secure Boot:** the reporter ran with Secure Boot disabled; the bug hit regardless.

---

Source: [Vectle](https://vectle.com/skills/skl_HBVvyD58Xu_-d3jwVIUxuQ). Version: `skv_XQMyrV5KpxpNlU_YXSFlpg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
