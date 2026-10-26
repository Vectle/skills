---
name: "diagnose-stale-body-values-sent-with-u-f7c99ab44d23623b"
description: "Guide Diagnose stale body values sent with useChat requests: Symptom: you pass dynamic values (selected model, toggle state, user id) via the transport body, but the server keeps receiving the values from page load. Use this when you hit exactly this in Diagnose. Not for different errors or different tools."
metadata:
  skill_id: "skl_P6dj7hagVfXixynybEA1Kw"
  title: "Diagnose stale body values sent with useChat requests"
  version: "skv_KBFKVHhC_d-VKC0AnTAq9A"
  updated: "2026-10-03T23:12:55.432186+00:00"
  canonical_url: "https://vectle.com/skills/skl_P6dj7hagVfXixynybEA1Kw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://ai-sdk.dev/docs/troubleshooting/use-chat-stale-body-data\",\"https://ai-sdk.dev/docs/ai-sdk-ui/chatbot\"]"
---

TL;DR: Symptom: you pass dynamic values (selected model, toggle state, user id) via the transport body, but the server keeps receiving the values from page load. Cause: the body was computed once when the transport was constructed. useChat does not re-read a static body object per request. Confirmation: 1.

## Fix
1. Symptom: you pass dynamic values (selected model, toggle state, user id) via the transport body, but the server keeps receiving the values from page load.
   Expected: this specific failure stops.
2. The transport accepts functions for per-request values; otherwise rebuild the transport when the values change, or pass the fresh values in the sendMessage options arg: sendMessage({ text }, { body: { model: currentModel } }).
   Expected: this specific failure stops.
3. Verification: change the UI control, send, and confirm the server log shows the new value on the first try.
   Expected: this specific failure stops.

## Details
Cause: the body was computed once when the transport was constructed. useChat does not re-read a static body object per request. Confirmation: 1. Find new DefaultChatTransport({ body: { ... } }). If the values come from component state but the object literal was built once, that is the bug. 2. Log the received body server-side across two sends with different UI state. Identical bodies confirm staleness. Fix: make the body dynamic. Rules: 1. Per-request overrides belong in the sendMessage second argument, not in transport construction. 2. If the value changes rarely (user id), constructing the transport inside a memo keyed on it is fine. 3. Never put secrets in body. Body crosses to the client by definition; keys stay server-side.

## When to use
You hit exactly this: Diagnose stale body values sent with useChat requests in Diagnose.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Diagnose.

---

Source: [Vectle](https://vectle.com/skills/skl_P6dj7hagVfXixynybEA1Kw). Version: `skv_KBFKVHhC_d-VKC0AnTAq9A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
