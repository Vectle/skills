---
name: "stream-error-after-5-minutes-connectio-2400d30e321b7028"
description: "Fixes streamed OpenAI completions dying at exactly the 5-minute mark with 'Connection broken: InvalidChunkLength'. Use this when long streamed responses always cut out at ~5 minutes but non-streaming requests with longer timeouts go further. Not for immediate connection failures."
metadata:
  skill_id: "skl_ATLNcCeCxDoJdP4ZHFUcSA"
  title: "Stream error after 5 minutes: Connection broken InvalidChunkLength"
  version: "skv_4hLIgUSmMWu95FPxHJ7X8A"
  updated: "2026-10-03T04:45:06.050746+00:00"
  canonical_url: "https://vectle.com/skills/skl_ATLNcCeCxDoJdP4ZHFUcSA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_4HWfpbTuq_Hs-viPYdECbQ\",\"https://github.com/openai/openai-python/issues/399\"]"
---

TL;DR: if your streamed completions die at almost exactly 5 minutes with `Connection broken: InvalidChunkLength(got length b'', 0 bytes read)`, you are hitting a streaming timeout that existed in the v0 client. Upgrade to v1 of the openai python library, where the client side was fixed. The server-side limit was improved too, so recent reports hit the wall closer to 10 minutes instead.

```text
Connection broken: InvalidChunkLength(got length b'', 0 bytes read)
```

## Steps

1. Upgrade the client:

```sh
pip install --upgrade openai
```

   Expected: v1 of the library.

2. Re-run the long streaming request.

   Expected: the stream survives past 5 minutes. Success check: the full document rewrite completes.

3. If it still fails on v1, note where it dies; the wall moved toward 10 minutes after the server-side improvement, so check the new mark before digging into your own socket code.

## When to use this

- Streamed responses reproducibly die at ~5 minutes; non-streaming with a 10-minute timeout only fails at 10 minutes.
- You run the v0 client.

## When NOT to use this

- Connections fail immediately; that is networking or auth.
- Short responses fail; this timeout only bites long streams.

## Compatibility

- openai python library v1+ (client fix); server-side limit also improved.

## Variant phrasings

- "openai stream dies 5 minutes InvalidChunkLength"
- "openai python streaming timeout long response"

## Root cause

The v0 client had a streaming-specific timeout the non-streaming path did not share, so long streams always cut out at the same mark.

## Edge cases

- A longer server-side wall (~10 minutes) still exists; truly huge generations need chunking regardless.

---

Source: [Vectle](https://vectle.com/skills/skl_ATLNcCeCxDoJdP4ZHFUcSA). Version: `skv_4hLIgUSmMWu95FPxHJ7X8A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
