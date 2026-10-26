---
name: "android-showing-duplicate-node-key-aft-43eff66d03903934"
description: "Fixes the 'Duplicate Node key' warning on Android after updating Tailscale by upgrading the Android app to version 1.86 or newer, which defers the taildrop directory picker until a file is actually received. Use when the Tailscale admin console shows duplicate node key entries for an Android device after an update. Not for duplicate keys caused by cloned device identities or multiple installs sharing state."
metadata:
  skill_id: "skl_BSAw2RUixtuGO-vDLW_h7A"
  title: "Android: Showing duplicate node key after recent update"
  version: "skv_STHcuUOv4P70fjeICmYXkw"
  updated: "2026-10-03T04:06:19.59732+00:00"
  canonical_url: "https://vectle.com/skills/skl_BSAw2RUixtuGO-vDLW_h7A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/16366\"]"
---

## TL;DR

Update the Tailscale Android app to version 1.86 or newer. Version 1.84 introduced a taildrop directory picker that registered a second node key; 1.86 defers the picker until you actually receive a file, which stops the duplicate key warning.

## The error

```text
Duplicate Node key
```

Shown in the Tailscale admin console for the Android device after updating the app.

## Fix it

1. Open the Google Play Store on the Android device and check the installed Tailscale version.
   Success check: the version is below 1.86, confirming you are affected.

2. Update Tailscale to 1.86 or newer.
   Success check: the Play Store shows the update installed with no errors.

3. Open the Tailscale admin console and find the Android device.
   Success check: only one node key entry remains; the duplicate warning is gone.

4. If a stale duplicate entry lingers, remove the old machine entry from the admin console.
   Success check: the device list shows a single entry for the phone.

## When this applies

- Tailscale on Android, app version 1.84 or 1.85, admin console shows 'Duplicate Node key' after an update.
- The duplicate appeared right after the taildrop directory picker prompt.

## When it does not apply

- The duplicate key comes from cloning a device image or restoring a backup onto a second phone; that needs key rotation, not an upgrade.
- You are on iOS, macOS, Windows, or Linux; this was an Android-only regression.
- You are already on 1.86+ and still see duplicates; investigate stale machine entries instead.

## Compatibility

- Tailscale Android app: affected in 1.84 and 1.85, fixed in 1.86 and newer.
- Tailscale admin console (any version).

## Variant phrasings

- Android showing duplicate node key after recent update
- Tailscale duplicate node key warning on Android
- taildrop duplicate machine entry Android

## Why it happens

Tailscale 1.84 added a prompt asking Android users to pick a taildrop directory at startup. Accepting it registered a second node identity for the same device, so the admin console listed two keys. In 1.86 the picker only appears when a file is actually incoming via taildrop, so no second key is created. This was maintainer-confirmed in the Tailscale issue thread.

## Edge cases

- If the Play Store has no update yet in your region, sideloading is not recommended; the duplicate entry is cosmetic until 1.86 arrives.
- Devices enrolled via MDM may need the admin to push the update.


---

Source: [Vectle](https://vectle.com/skills/skl_BSAw2RUixtuGO-vDLW_h7A). Version: `skv_STHcuUOv4P70fjeICmYXkw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
