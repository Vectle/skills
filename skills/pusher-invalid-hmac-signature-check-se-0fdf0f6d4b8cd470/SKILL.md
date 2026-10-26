---
name: "pusher-invalid-hmac-signature-check-se-0fdf0f6d4b8cd470"
description: "When a private/presence subscription fails with \"Invalid signature: Expected HMAC SHA256 hex digest\": 1."
metadata:
  skill_id: "skl_qwOC59P3x0BWa8L-LQE-eA"
  title: "Pusher invalid HMAC signature: check secret, channel name, and socket id, not the key"
  version: "skv_ISDcSEhWKwR5yyrWybnijg"
  updated: "2026-10-03T05:40:02.809616+00:00"
  canonical_url: "https://vectle.com/skills/skl_qwOC59P3x0BWa8L-LQE-eA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.bird.com/pusher/channels/channels/troubleshooting/why-am-i-receiving-the-invalid-signature-expected-hmac-sha256-error\"]"
---

# Pusher invalid HMAC signature: check secret, channel name, and socket id, not the key

## TL;DR

When a private/presence subscription fails with "Invalid signature: Expected HMAC SHA256 hex digest": 1. Context: Docs (Pusher troubleshooting, mirrored at docs.bird.com): subscribing to a private or presence channel fails with "Invalid signature: Expected HMAC SHA256 hex digest" when the auth token from your endpoint is wrong. Three variables make the signature: the app secret, the channel name, and the socket id.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

2. Verify your /pusher/auth endpoint returns { "auth": "APP_KEY -signature" } signed with the same secret shown in your dashboard. 3. Verify the channel name the client subscribes to is byte-identical to what the server signed (private- and presence- prefixes included). 4. Check that the endpoint reads socket_id and channel_name from the request the client actually sent (pusher-js POSTs them as form params by default). One benign case: if the client reconnects between requesting the token and subscribing, it gets a new socket id, the stale token emits this error once, and the automatic retry with the fresh socket id succeeds. A single occurrence followed by a successful subscription is normal; repeated occurrences mean a real signing mismatch.

Context: Docs (Pusher troubleshooting, mirrored at docs.bird.com): subscribing to a private or presence channel fails with "Invalid signature: Expected HMAC SHA256 hex digest" when the auth token from your endpoint is wrong. Three variables make the signature: the app secret, the channel name, and the socket id. If any one differs between what the server signed and what the client sends, the token is invalid. Debugging steps: confirm the endpoint returns { auth: "key -signature" }, confirm the server signs with the same app secret as the dashboard, and confirm the channel name matches exactly. Edge case: if the client reconnects mid-auth (new socket id issued after the token was requested), the stale token emits this error once and the retry with the new socket id succeeds, so a single transient occurrence that then subscribes fine is expected, not a bug.


---

Source: [Vectle](https://vectle.com/skills/skl_qwOC59P3x0BWa8L-LQE-eA). Version: `skv_ISDcSEhWKwR5yyrWybnijg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
