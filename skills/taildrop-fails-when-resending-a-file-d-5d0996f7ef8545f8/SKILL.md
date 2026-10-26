---
name: "taildrop-fails-when-resending-a-file-d-5d0996f7ef8545f8"
description: "Fixes Taildrop silently failing when you resend a file that was deleted on the receiving device. Use when the first Taildrop transfer works but resending the same file after deleting it never arrives, sometimes with an Internal Server Error. Covers the verified workarounds: rename the file before resending, or log out and back in on the receiver. Not for first-time Taildrop failures or permission errors on Android."
metadata:
  skill_id: "skl_IUbraDWPACV1mlecT7mOmw"
  title: "Taildrop fails when resending a file deleted on the receiver (rename it)"
  version: "skv_wUJL3VD-TnbKV45D7zVBhg"
  updated: "2026-10-03T04:43:16.930499+00:00"
  canonical_url: "https://vectle.com/skills/skl_IUbraDWPACV1mlecT7mOmw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/16397\"]"
---

# Fix Taildrop failing when resending a deleted file

**TL;DR:** Taildrop remembers the filename and chokes when you resend the same name after deleting it. Rename the file before resending, or log out and back in on the receiving device.

## The error

```text
Taildrop: Internal Server Error when sending file again after deletion on receiving device
```

Sometimes there is no error at all: the send "succeeds" but the file never appears on the receiver.

## Fix it

### 1. Rename before resending (quickest)

```
cp report.pdf report-v2.pdf
tailscale file cp report-v2.pdf RECEIVER_NAME:
```

Expected: the renamed file arrives in the receiver's Taildrop folder immediately.

### 2. Or re-login the receiving device

On the receiver: disconnect Tailscale and reconnect (or restart the device / tailscaled).

Expected: after re-login, resends of the original filename start working again.

### 3. Verify arrival

Check the receiver's Taildrop incoming folder (Downloads on most platforms, or the folder picked at install on Android).

Expected: the file is there with a fresh timestamp.

## When this applies

- First Taildrop send works, resend of the same filename fails
- The file was deleted on the receiver between sends
- Internal Server Error, or silent no-arrival

## When it does not apply

- First-time sends fail too (connectivity or Taildrop setup problem)
- Android shows a storage permission error (grant the permission instead)
- Files arrive but with weird hashed suffixes (cosmetic, transfers work)

## Tool compatibility

All Tailscale versions with Taildrop. Reported Fedora to Android, Pixel to MacBook, Linux to Android.

## Variant phrasings

### Taildrop works only the first time

Same bug, reported both directions between the same two devices. Same fix.

### Resent files appear only after logout/login

The other verified workaround. Either rename or re-login; both break the stuck state.

## Why it happens

The receiver tracks incoming filenames, and deleting the file does not clear whatever record makes the second send collide. A new name sidesteps the collision; a re-login clears the tracker's state.

## Edge cases

- **Scripted sends:** if you automate `tailscale file cp`, stamp each filename (date, build number) so resends never reuse a name.
- **Emptying trash is not enough:** one reporter emptied the trash and it still failed. Rename or re-login.
- **Android folder pick:** on Android the Taildrop folder is chosen at install; if sends never arrive at all (not just resends), re-check that folder choice first.

---

Source: [Vectle](https://vectle.com/skills/skl_IUbraDWPACV1mlecT7mOmw). Version: `skv_wUJL3VD-TnbKV45D7zVBhg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
