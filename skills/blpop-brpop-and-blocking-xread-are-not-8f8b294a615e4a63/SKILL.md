---
name: "blpop-brpop-and-blocking-xread-are-not-8f8b294a615e4a63"
description: "HTTP 400 or unsupported-command errors calling BLPOP, BRPOP, BRPOPLPUSH, BZPOPMAX, BZPOPMIN, or blocking XREAD over Upstash REST. Covers the polling replacement and when to switch to the native Redis protocol. Not for non-blocking commands or native-protocol connections."
metadata:
  skill_id: "skl_UVhwvcIXWJvwUPawKkeytQ"
  title: "BLPOP, BRPOP, and blocking XREAD are not supported over Upstash REST: poll or use RESP"
  version: "skv_0Ui7gNjSJp1iePSJWKSawQ"
  updated: "2026-10-03T04:32:24.984473+00:00"
  canonical_url: "https://vectle.com/skills/skl_UVhwvcIXWJvwUPawKkeytQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://upstash.com/docs/redis/features/restapi\"]"
---

TL;DR: Blocking Redis commands need a held connection, and REST has no connection to hold, so BLPOP, BRPOP, BRPOPLPUSH, BZPOPMAX, BZPOPMIN, and XREAD/XREADGROUP with BLOCK fail over Upstash REST with an HTTP 400 or unsupported-command error. Replace BLPOP with LPOP in a sleep loop (each poll is a billed command, so size the sleep to your latency budget), or switch to the native Redis protocol where blocking works normally. For queue consumers, the protocol path is the right call.

What you see:

```text
HTTP 400, or an unsupported-command error, when calling BLPOP, BRPOP,
BRPOPLPUSH, BZPOPMAX, BZPOPMIN, or XREAD/XREADGROUP with BLOCK.
```

Steps:

1. Decide which path fits. Polling over REST is fine for low-frequency consumers; anything queue-like wants the native protocol. Success: you picked one deliberately.
2. Polling path: replace BLPOP with LPOP in a loop that sleeps briefly between attempts. Success: the consumer picks up a pushed item within the expected poll window.
3. Protocol path: connect over RESP with a persistent connection and keep using blocking commands unchanged. Success: BLPOP behaves exactly like self-hosted Redis.
4. Streams over REST: use non-blocking XREAD (no BLOCK argument). Success: reads work without the BLOCK flag.

When to use: blocking commands fail over Upstash REST with 400/unsupported-command.

When not to use: you control the client and can open a RESP connection (just use the protocol), or the command is non-blocking (it works fine over REST already).

Compatibility: Upstash Redis REST API, any HTTP client. Native protocol path needs a RESP-capable client.

Variants:
- upstash blpop not supported
- upstash rest blocking xread
- upstash redis blocking commands rest

Root cause: blocking commands hold a connection open waiting for data. REST is request/response per call, so there is no connection to hold. The compatibility table marks all of these unsupported by design, not by bug.

Edge cases:
- Cost: polling every 100ms is 864K commands a day per consumer. At pay-as-you-go rates that is real money. Prefer the protocol path for blocking-style consumers, or lengthen the poll interval and accept the latency.
- Verify end to end: RPUSH a test item and watch the consumer pick it up.

---

Source: [Vectle](https://vectle.com/skills/skl_UVhwvcIXWJvwUPawKkeytQ). Version: `skv_0Ui7gNjSJp1iePSJWKSawQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
