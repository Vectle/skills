---
name: "android-14-crash-exception-receiver-ex-3583372dd6bf7523"
description: "Fixes the Android 14 crash 'One of RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED should be specified' by upgrading React Native Purchases to 6.2.1 or newer. Use when your app crashes on Android 14 after targeting SDK 34. Not for crashes on older Android versions, or for receivers you register in your own code."
metadata:
  skill_id: "skl_XlWGaPKQJ05lXoBdsiTHUQ"
  title: "[Android 14] Crash Exception - RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED is required"
  version: "skv_xVerwwtSbK19GjKUKKjZeA"
  updated: "2026-10-03T04:35:03.728906+00:00"
  canonical_url: "https://vectle.com/skills/skl_XlWGaPKQJ05lXoBdsiTHUQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: upgrade React Native Purchases to 6.2.1 or newer. Android 14 requires RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED when registering a broadcast receiver, and the SDK fixed it at 6.2.1.

```text
Fatal Exception: java.lang.SecurityException: com.my-test-app.app:
One of RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED should be specified
when a receiver isn't being registered exclusively for system broadcasts
```

1. Upgrade react-native-purchases to 6.2.1 or newer.
2. Ship it and watch crash reports. Expected: the SecurityException crashes stop on Android 14 devices.

When to use: your crash reporter shows this SecurityException on Android 14 after you updated your target SDK to 34.

When not to use: crashes on Android 13 and below, or broadcast receivers registered in your own native code (that flag is yours to add, not the SDK's).

Compatibility: React Native Purchases 6.2.1+, Android 14 (SDK 34).

Variants:
- "RECEIVER_EXPORTED React Native Purchases"
- "android 14 purchases crash SecurityException"
- "one of RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED should be specified react native"

Root cause: Android 14 made the exported flag mandatory for broadcast receivers, and the older Purchases SDK registered receivers without it.

Edge cases: if you register your own receivers in native code, you need to add the flag there yourself. The SDK upgrade only fixes the SDK's own receivers.

---

Source: [Vectle](https://vectle.com/skills/skl_XlWGaPKQJ05lXoBdsiTHUQ). Version: `skv_xVerwwtSbK19GjKUKKjZeA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
