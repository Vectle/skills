---
name: "deactivated-stream-chat-user-still-rec-9521c469e5a41d79"
description: "Shows how to fix deactivated Stream Chat user still receiving messages. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_O7HztWSYuRmsN7QBuf98RA"
  title: "Deactivated Stream Chat user still receiving messages"
  version: "skv_nWXDlvWAu_4THaZEwkCT3Q"
  updated: "2026-10-03T14:12:04.101531+00:00"
  canonical_url: "https://vectle.com/skills/skl_O7HztWSYuRmsN7QBuf98RA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_PHkE2VHsTnoQGfDBdypLAQ\",\"https://github.com/GetStream/stream-chat-js/issues/642\"]"
---

## TL;DR

What fixed it This was a backend bug on Stream's side: deactivation stopped the user from sending but did not cut off their websocket event stream. The Stream team fixed it server-side; no SDK upgrade is required.

## Steps

1. What was going on
After deactivating a user via `deactivate_user(user_id)` (stream-chat-ruby gem, stream-chat-js 1.7.2), the deactivated user correctly fails when trying to send messages, but still receives messages and other realtime information from active users. The deactivation only blocked the send path, not the receive path. The reporter verified the deactivate call succeeded since sends were rejected as expected.

2. What fixed it
This was a backend bug on Stream's side: deactivation stopped the user from sending but did not cut off their websocket event stream. The Stream team fixed it server-side; no SDK upgrade is required. If you still observe deactivated users receiving events, re-run `deactivate_user` and make sure their user token is revoked/regenerated, and contact Stream support if the behavior persists.

## When to use

You are seeing this: What was going on After deactivating a user via deactivate\_user(user\_id) (stream-chat-ruby gem, stream-chat-js 1.7.2), the deactivated user correctly fails when trying to send messages, but still receives messages and other realtime information from... Use this skill when you run into "Deactivated Stream Chat user still receiving messages".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: stream-chat-js 1.7.2. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_O7HztWSYuRmsN7QBuf98RA). Version: `skv_nWXDlvWAu_4THaZEwkCT3Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
