---
name: "ip6tables-extension-mark-revision-0-no-881408c8f7f99b14"
description: "Fixes Tailscale health-check failures with 'Extension MARK revision 0 not supported, missing kernel module' from ip6tables after upgrading to Linux 6.11.4/6.11.5 or 6.6.57/6.6.58. Use when tailscale status shows a health warning about adding a MARK rule in v6/filter/ts-forward right after a kernel update. Covers the fixed kernel versions to upgrade to. Not for IPv4 iptables errors or MARK failures on older kernels."
metadata:
  skill_id: "skl_mrVbTuhQ7s24QqqMm04U-g"
  title: "ip6tables Extension MARK revision 0 not supported after Linux 6.11.4 update"
  version: "skv_pYoZO7-Ip6G8R4KdENx8LQ"
  updated: "2026-10-03T04:38:42.084897+00:00"
  canonical_url: "https://vectle.com/skills/skl_mrVbTuhQ7s24QqqMm04U-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/13863\"]"
---

# Fix ip6tables "Extension MARK revision 0 not supported" after a kernel update

**TL;DR:** Kernels 6.11.4 and 6.6.57 broke the MARK match Tailscale uses for IPv6 forwarding rules. Upgrade to 6.11.5+ or 6.6.58+ and the health warning goes away. If you do not use IPv6, you can also just ignore it.

## The error

```text
# Health check:
#     - adding [-i tailscale0 -j MARK --set-mark 0x40000/0xff0000] in v6/filter/ts-forward: [... ip6tables -t filter -A ts-forward -i tailscale0 -j MARK --set-mark 0x40000/0xff0000 --wait]: exit status 2: Warning: Extension MARK revision 0 not supported, missing kernel module?
```

Shows up in `tailscale status` right after a kernel upgrade. IPv4 rules are fine; only the v6 chain fails.

## Fix it

### 1. Check your kernel version

```
uname -r
```

Expected: 6.11.4, 6.11.5-ish, 6.6.57, or 6.6.58-ish. The bad ones are 6.11.4 and 6.6.57.

### 2. Upgrade the kernel past the regression

- If on 6.11.4, go to 6.11.5 or newer.
- If on 6.6.57, go to 6.6.58 or newer.

Use your distro or NixOS channel update, then reboot.

Expected after reboot: `tailscale status` shows no health warnings.

### 3. Confirm the MARK rule applies cleanly

```
tailscale status | head -5
```

Expected: no `# Health check:` block. IPv6 forwarding through the tailnet works again.

## When this applies

- `tailscale status` shows the MARK / missing kernel module warning in `v6/filter/ts-forward`
- It started right after a kernel update to 6.11.4 or 6.6.57
- `modprobe` for the mark module does not help (the module is not the problem)

## When it does not apply

- IPv4 iptables errors (different chain, different cause)
- MARK errors on much older kernels (check your iptables install instead)
- Tailscale fails to start entirely (not a health-warning-only situation)

## Tool compatibility

Tailscale 1.7x on Linux with kernels 6.11.4 / 6.6.57. Reported on NixOS; any distro shipping those exact kernel builds is affected.

## Variant phrasings

### `ip6tables v1.8.x: exit status 2` on ts-forward

Same failure, shorter form. The `exit status 2` plus the MARK warning is the signature.

## Why it happens

Those two kernel releases regressed the xt_mark match revision that ip6tables 1.8.x asks for, so the rule insert fails even though the module is present. It is a kernel bug, not a Tailscale bug, which is why the fix is a kernel upgrade.

## Edge cases

- **No IPv6 in use:** the failing chain is v6-only. If your tailnet is IPv4-only you can live with the warning, but upgrading is still cleaner.
- **NixOS:** the fix PRs were tracked in nixpkgs; a channel update past the fixed kernel is all it takes.
- **Still broken after upgrade:** make sure you actually booted the new kernel (`uname -r`), not just installed it.

---

Source: [Vectle](https://vectle.com/skills/skl_mrVbTuhQ7s24QqqMm04U-g). Version: `skv_pYoZO7-Ip6G8R4KdENx8LQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
