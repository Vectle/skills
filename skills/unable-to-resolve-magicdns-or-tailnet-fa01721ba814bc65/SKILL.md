---
name: "unable-to-resolve-magicdns-or-tailnet-fa01721ba814bc65"
description: "Fixes MagicDNS and tailnet FQDNs failing to resolve on macOS with OSS tailscaled 1.74 through 1.101. Use when dig or ping of machine names and .ts.net addresses returns 'no such host' on macOS while other platforms resolve fine. Covers the fixed release to upgrade to and the DNS-settings workaround. Not for split-DNS domains or global DNS outages."
metadata:
  skill_id: "skl_pTwNmKeNTv30-fUt4bCl_A"
  title: "Unable to resolve MagicDNS or tailnet names on macOS (fix: upgrade to 1.102+)"
  version: "skv_QKvRbRclHT7yK6NQyifkgg"
  updated: "2026-10-03T04:40:14.933661+00:00"
  canonical_url: "https://vectle.com/skills/skl_pTwNmKeNTv30-fUt4bCl_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix MagicDNS not resolving on macOS (OSS tailscaled)

**TL;DR:** OSS tailscaled 1.74 through 1.101 mishandles macOS DNS config. Upgrade to 1.102 or newer, which fixes it properly. As a workaround, turn on "Use Tailscale DNS settings" or run with `--accept-dns=true`.

## The error

```text
$ dig mymachine.mytailnet.ts.net
;; status: NXDOMAIN
$ ping mymachine
ping: cannot resolve mymachine: Unknown host
```

Other devices on the tailnet resolve the same names fine. Only the Mac is broken.

## Fix it

### 1. Upgrade to the fixed release

Install Tailscale 1.102 or newer on the Mac. That release configures macOS DNS via scutil correctly, matching the app clients.

Expected: `tailscale version` shows 1.102+.

### 2. Verify resolution

```
dig mymachine.mytailnet.ts.net
ping -c2 mymachine
```

Expected: the dig returns a 100.x address; ping resolves and replies.

### 3. Workaround if you cannot upgrade yet

Turn on "Use Tailscale DNS settings" in the macOS app, or for the standalone daemon:

```
sudo tailscale up --accept-dns=true
```

Expected: MagicDNS starts resolving immediately.

### 4. Check for a conflicting VPN

One reporter traced the same symptom to NordVPN running alongside Tailscale. Disconnect any other VPN and retest.

Expected: resolution works with the other VPN off.

## When this applies

- macOS only, OSS tailscaled 1.74 to 1.101
- MagicDNS short names and .ts.net FQDNs both fail
- `dig @100.100.100.100 name.ts.net` works (the DNS server is fine; the OS just is not using it)

## When it does not apply

- All platforms fail to resolve (check tailnet DNS settings in the admin console)
- Only external/split-DNS domains fail (split DNS config problem)
- The Mac app client with default settings (that path always worked)

## Tool compatibility

Tailscale 1.74.0 through 1.101.x on macOS, OSS tailscaled builds. Fixed in 1.102.

## Variant phrasings

### `no such host` for tailnet names on macOS

Same symptom, different wording from Go tooling. Same fix.

### Worked on 1.72.1, broke on 1.74.0

The exact regression window from the issue. If that matches your history, this is your bug.

## Why it happens

The 1.74.0 changelog reworked DNS handling, and the OSS daemon stopped programming macOS resolvers correctly when Tailscale DNS was off. The 1.102 fix shells out to scutil like the app clients do.

## Edge cases

- **scutil check:** `scutil --dns` should show a resolver entry for your tailnet domain pointing at 100.100.100.100. If it is missing, DNS was never programmed.
- **Accept-dns=false users:** if you deliberately keep Tailscale DNS off, you need manual resolver entries for the tailnet domain; MagicDNS will not just work.
- **VPN conflicts:** any VPN that grabs DNS (Nord, Proton, corporate clients) can shadow Tailscale's resolvers. Test with them disconnected before blaming Tailscale.

---

Source: [Vectle](https://vectle.com/skills/skl_pTwNmKeNTv30-fUt4bCl_A). Version: `skv_QKvRbRclHT7yK6NQyifkgg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
