---
name: "failed-to-execute-subscribe-on-pushman-283f4290ae8f3c43"
description: "Fixes 'Failed to execute subscribe on PushManager: Subscription failed - no active Service Worker' from Firebase messaging getToken by upgrading the Firebase JS SDK to 11.1.0 or later. Use when getToken intermittently throws this in Next.js or other setups. Not for permission-denied or VAPID key errors."
metadata:
  skill_id: "skl_Ht0oIR_aAvDBfs-JmsEYkA"
  title: "Failed to execute 'subscribe' on 'PushManager': Subscription failed - no active Service Worker"
  version: "skv_YH0qRTBAwDdgL9OLK1EkRQ"
  updated: "2026-10-03T04:15:30.350451+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ht0oIR_aAvDBfs-JmsEYkA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade the Firebase JS SDK to 11.1.0 or later. That release fixed the service-worker subscription race for the reporters in the thread.

## The error

```text
Failed to execute 'subscribe' on 'PushManager': Subscription failed - no active Service Worker
```

Intermittent when calling `getToken` from Firebase Cloud Messaging.

## Fix it

1. Check your Firebase JS SDK version:
   ```bash
   npm ls firebase
   ```
   Success check: the version is below 11.1.0, confirming you are affected.

2. Upgrade to 11.1.0 or later:
   ```bash
   npm install firebase@^11.1.0
   ```
   Success check: `npm ls firebase` shows 11.1.0+.

3. Retry `getToken`.
   Success check: the token resolves with no PushManager error.

## When this applies

- Firebase JS SDK below 11.1.0, `getToken` intermittently throws the PushManager error.
- Next.js (pages or app router) or any setup where the service worker registration races the token call.

## When it does not apply

- Permission denied; the user blocked notifications (different error).
- VAPID key misconfiguration.
- The service worker file itself fails to register (check the SW scope and file path).

## Compatibility

- firebase JS SDK 11.1.0+ (fixed). Affects all browsers; reported on macOS with Next.js 13.

## Variant phrasings

- Failed to execute subscribe on PushManager no active Service Worker
- firebase getToken PushManager subscription failed
- FCM getToken no active service worker

## Why it happens

`getToken` called `pushManager.subscribe` before the messaging service worker was active, a race in older SDK versions. 11.1.0 waits for the worker to be ready before subscribing.

## Edge cases

- If it persists on 11.1.0+, ensure only one messaging service worker is registered and the SW file is served from the app root.
- Source: https://github.com/firebase/firebase-js-sdk/issues/7575


---

Source: [Vectle](https://vectle.com/skills/skl_Ht0oIR_aAvDBfs-JmsEYkA). Version: `skv_YH0qRTBAwDdgL9OLK1EkRQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
