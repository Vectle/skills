---
name: "wg-quick-wg0-already-exists-d100c0f2d75e80af"
description: "Fixes wg-quick refusing with wg-quick: 'wg0' already exists. Use when an interface from an earlier run is still up. Covers bringing it down before re-creating it. Not for RTNETLINK file-exists on addresses, or missing configs."
metadata:
  skill_id: "skl_X7vJTuUtdQ_HrOhgwlGYow"
  title: "wg-quick: 'wg0' already exists"
  version: "skv_GoSwXvwjodTEVB0lWTzPSg"
  updated: "2026-10-03T06:07:38.382172+00:00"
  canonical_url: "https://vectle.com/skills/skl_X7vJTuUtdQ_HrOhgwlGYow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/iot-lab-unm/dream-scalable-maas/blob/HEAD/poc-wireguard-overlay/docs/troubleshooting.md\"]"
---

# wg-quick: 'wg0' already exists

TL;DR: a wg0 interface is already up from an earlier run, so wg-quick will not create a second one. Run `sudo wg-quick down wg0` first, then `up` again. This bites when a previous `up` half-succeeded or the config was applied by hand.

```text
wg-quick: 'wg0' already exists
```

## Steps

1. Take the existing interface down:

```bash
sudo wg-quick down wg0
```

Expected: no output.

2. Confirm it is gone:

```bash
ip link show wg0
```

Expected: `Device "wg0" does not exist.`

3. Bring it up fresh:

```bash
sudo wg-quick up wg0
```

Expected: the interface is created and `wg show wg0` lists peers.

## When this applies

- re-running `wg-quick up` after it was killed midway
- scripts that call `up` without a matching `down`
- the interface was created manually and then wg-quick ran

## When it doesnt

- `RTNETLINK answers: File exists` — leftover addresses, a level deeper than this
- config file missing — different error entirely
- you actually want two tunnels — give the second a different interface name

## Compatibility

wireguard-tools wg-quick on Linux.

## Other phrasings

- `wg-quick interface already exists`
- `cannot create wg0: exists`

## Why it happens

wg-quick refuses to create an interface that already exists rather than silently reusing it, because reusing it could mean applying a new config to a live tunnel halfway.

## Edge cases

- If `down` claims the interface is not defined but `ip link` shows it, delete it directly with `ip link delete wg0`.
- Persistent interfaces managed by systemd-networkd should be restarted through the service, not wg-quick.


---

Source: [Vectle](https://vectle.com/skills/skl_X7vJTuUtdQ_HrOhgwlGYow). Version: `skv_GoSwXvwjodTEVB0lWTzPSg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
