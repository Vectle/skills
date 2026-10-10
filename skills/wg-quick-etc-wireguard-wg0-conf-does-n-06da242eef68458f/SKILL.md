---
name: "wg-quick-etc-wireguard-wg0-conf-does-n-06da242eef68458f"
description: "Fixes wg-quick failing because the config file does not exist at the expected path. Use when wg-quick names a .conf that was never created, often on a fresh install. Covers creating the config with Interface and Peer sections and correct permissions. Not for syntax errors inside an existing file."
metadata:
  skill_id: "skl_IAfbwRjiECS7z_23IMLQdA"
  title: "wg-quick: '/etc/wireguard/wg0.conf' does not exist"
  version: "skv_ZA0XQUV9cbxI6qFa0ZJGRw"
  updated: "2026-10-03T06:09:54.073784+00:00"
  canonical_url: "https://vectle.com/skills/skl_IAfbwRjiECS7z_23IMLQdA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# wg-quick: '/etc/wireguard/wg0.conf' does not exist

TL;DR: there is no config file where wg-quick expects one. Create /etc/wireguard/wg0.conf with Interface and Peer sections, set permissions to 600, then run `wg-quick up wg0` again.

```text
wg-quick: '/etc/wireguard/wg0.conf' does not exist
```

## Steps

1. Create the config file:

```bash
sudo nano /etc/wireguard/wg0.conf
```

2. Fill in Interface and Peer sections:

```text
[Interface]
PrivateKey [your private key value]
Address = CONTAINER_IP/24

[Peer]
PublicKey [the peer public key value]
AllowedIPs = CONTAINER_IP/24
Endpoint = vpn.example.com:51820
```

3. Lock down permissions (WireGuard refuses world-readable key files):

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
```

4. Bring it up:

```bash
sudo wg-quick up wg0
```

Expected: the interface comes up; `wg show` lists the peer.

## When this applies

- fresh installs where only the tools were installed, no config written
- the interface name in the command does not match any file in /etc/wireguard
- configs stored elsewhere and never copied into place

## When it doesnt

- the file exists but wg-quick complains about its contents — that is a syntax or key error
- `wg-quick: 'wg0' already exists` — the opposite problem
- permission denied reading the file — check ownership, not existence

## Compatibility

wireguard-tools wg-quick on Linux.

## Other phrasings

- `wg-quick config file not found`
- `/etc/wireguard/wg0.conf: No such file or directory`

## Why it happens

wg-quick maps the interface name directly to a file path: `up wg0` reads /etc/wireguard/wg0.conf. No file, no tunnel. Package installs ship the tools but never your config.

## Edge cases

- Use `wg-quick up ./myconfig.conf`... actually wg-quick accepts a full path, so configs can live elsewhere if you pass the path.
- Keep keys out of version control; 600 permissions are the minimum.


---

Source: [Vectle](https://vectle.com/skills/skl_IAfbwRjiECS7z_23IMLQdA). Version: `skv_ZA0XQUV9cbxI6qFa0ZJGRw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
