---
name: "key-is-not-the-correct-length-or-forma-2590a493126e5bdd"
description: "Fixes WireGuard refusing a config with Key is not the correct length or format. Use when the PrivateKey or PublicKey value is not valid base64 of the right length. Covers placeholder keys left in the file and pasting the key file path instead of the key value. Not for handshake or routing failures."
metadata:
  skill_id: "skl_cKZH_30zoGwSDHqiYCAXXw"
  title: "Key is not the correct length or format"
  version: "skv_YeHOko5pAX0TsV11DidOKA"
  updated: "2026-10-03T06:08:41.568891+00:00"
  canonical_url: "https://vectle.com/skills/skl_cKZH_30zoGwSDHqiYCAXXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://wiki.ArchLinux.org/title/WireGuard\"]"
---

# Key is not the correct length or format

TL;DR: the key value in your config is not a valid WireGuard key. The two classic causes are a placeholder like CHANGEME left in the file, and pasting the key file's path instead of the key itself. Generate a real key with `wg genkey` and paste the key value (not the path) into the config.

```text
Key is not the correct length or format
```

## Steps

1. Generate a fresh keypair:

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

Expected: two files, each holding one 44-character base64 line.

2. Open the config and replace the bad value with the actual key contents:

```text
PrivateKey [your private key value]
```

Not the path to the file. The config wants the key itself.

3. Do the same for the peer's PublicKey, using the contents of the publickey file.

4. Bring the interface up:

```bash
sudo wg-quick up wg0
```

Expected: no key error, and `wg show` displays the interface.

## When this applies

- configs copied from a template with placeholder keys still in place
- the config contains something like `/etc/wireguard/privatekey` where the key should be
- keys truncated by an editor or wrapped across lines

## When it doesnt

- handshake never completes with valid keys — that is endpoints or firewall
- `RTNETLINK` errors — address problems, not keys
- the key parses but the peer rejects — check you shared the public half

## Compatibility

wireguard-tools on Linux, macOS, Windows; any config with PrivateKey/PublicKey.

## Other phrasings

- `wireguard invalid key format`
- `wg setconf key length`

## Why it happens

WireGuard keys are 32 raw bytes shown as 44 base64 characters. Anything else — a path, a placeholder word, a wrapped line — fails the length check before any crypto happens.

## Edge cases

- `wg genkey` output includes a trailing newline; strip it when pasting.
- Keep private keys at 600 permissions; the error is about format, but leaked keys are worse.
- The Arch wiki documents this exact mistake: the config needs the key value, not the filename.


---

Source: [Vectle](https://vectle.com/skills/skl_cKZH_30zoGwSDHqiYCAXXw). Version: `skv_YeHOko5pAX0TsV11DidOKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
