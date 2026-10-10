---
name: "duplicate-node-key-in-the-tailscale-ad-35250f791e605c80"
description: "Fixes the Tailscale 'Duplicate node key' warning shown in the admin console. Use when two devices appear to share one node key, usually after cloning a VM, restoring a disk image, or migrating a NAS. Covers finding the duplicate in the machines list, deleting the stale entry, and re-authenticating the cloned device so it mints a fresh key. Not for expired auth keys, login loops, or devices that fail to connect for other reasons."
metadata:
  skill_id: "skl_qmlicXbtFhGlMME7wMix7w"
  title: "Duplicate node key in the Tailscale admin console: how to fix it"
  version: "skv_1CzJesG7KCIrk1bWRieFVA"
  updated: "2026-10-03T04:29:35.573331+00:00"
  canonical_url: "https://vectle.com/skills/skl_qmlicXbtFhGlMME7wMix7w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix the Tailscale "Duplicate node key" warning

**TL;DR:** The admin console flags "Duplicate node key" when two devices share the same node key, almost always because a VM or disk image was cloned. Delete the stale duplicate in the admin console machines list, then run `tailscale logout` and `tailscale up` on the real device so it mints a fresh key. The warning clears within a minute or two.

## The error

```text
Duplicate node key
```

Shown as a warning banner on a device in the Tailscale admin console (https://login.tailscale.com/admin/machines). Sometimes flickers on refresh; that still counts.

## Fix it

### 1. Find the two machines sharing the key

Open the admin console machines page and look for the device carrying the warning. If you cloned a VM or restored from an image, the original and the clone usually show the same hostname.

Expected: you can identify which entry is the live machine (recent "last seen" time) and which is stale.

### 2. Delete the stale duplicate

On the stale entry, open the machine menu (three dots) and choose Remove. Do not remove the live one.

Expected: the entry disappears from the list.

### 3. Re-authenticate the live device for a fresh key

On the real device, run:

```
tailscale logout
tailscale up
```

Complete the browser login when prompted. This mints a brand new node key, so even a lingering duplicate reference cant collide with it.

Expected: `tailscale status` shows the machine connected with no warnings.

### 4. Confirm the warning is gone

Refresh the admin console. The banner clears within a minute or two. If it flickers once and vanishes, youre fine.

Expected: no "Duplicate node key" banner on any device.

## When this applies

- Admin console shows "Duplicate node key" on one or more machines
- You cloned a VM, duplicated a disk image, or restored a backup onto new hardware
- You migrated a NAS or server and the old entry still exists
- Android reinstall loops that keep re-registering the same key (seen in the 1.84.x Taildrop release)

## When it does not apply

- `tailscale up` fails with an auth error but there is no duplicate warning (that is an auth key problem, different fix)
- A device cant connect at all (check network/DERP, not node keys)
- The warning names a device you do not recognize at all (check for an actual unauthorized device first)

## Tool compatibility

Tailscale client 1.80 and newer, all platforms. Admin console steps are the same everywhere. The Android Taildrop variant was reported on 1.84.1.

## Variant phrasings

### "Duplicate Node key" with capital N

Same warning, older console wording. Same fix.

### Warning only flickers on page refresh

Reporters saw the banner flash for a split second on refresh. It usually means the duplicate entry was already removed but the page cached the state. Hard-refresh and re-check; if it stays gone, youre done.

## Why it happens

Every Tailscale device has a node key that identifies it to the coordination server. Cloning a disk, VM snapshot, or phone backup copies the key along with everything else, so two machines check in as the same identity. The console cant tell which is real, so it flags both.

## Edge cases

- **Fleets from one golden image:** bake `tailscale logout` into your image build, or better, provision each machine with its own one-use auth key at first boot so no two machines ever share a key.
- **Deactivate/reactivate workaround:** some users cleared the warning by deactivating the device in the console and reactivating it. Works when the duplicate is transient, not when a real clone is still checking in.
- **The clone keeps coming back:** if you delete the stale entry and it reappears, the cloned machine is still online. Find it and re-authenticate it; deleting alone wont stick.

---

Source: [Vectle](https://vectle.com/skills/skl_qmlicXbtFhGlMME7wMix7w). Version: `skv_1CzJesG7KCIrk1bWRieFVA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
