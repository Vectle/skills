---
name: "connection-failed-no-connection-to-the-ff035cd86fff80a7"
description: "Cognitive Services Speech SDK: connection failed (no connection to the remote host) WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED. The verified fix is Fix: If Azure speech recognition suddenly starts failing with 'Connection failed (no connection to the remote host) / WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED' and your code did not change, check the network path first. Use this when you hit the symptoms above in cognitive-services-speech-sdk; not for unrelated cognitive-services-speech-sdk errors or gen"
metadata:
  skill_id: "skl_frAthOLTjLbySGutnp-_Vw"
  title: "Connection failed (no connection to the remote host) WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED"
  version: "skv_ZUIiK81BZTaDvEnqx3I9xQ"
  updated: "2026-10-03T05:34:55.73731+00:00"
  canonical_url: "https://vectle.com/skills/skl_frAthOLTjLbySGutnp-_Vw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: If Azure speech recognition suddenly starts failing with 'Connection failed (no connection to the remote host) / WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED' and your code did not change, check the network path first. The reporter traced it to network proxies / regional network issues and resolved it by provisioning a new secret key in a different region (Southeast Asia).

## The error

```text
Issue Azure-Samples/cognitive-services-speech-sdk#1911 (closed, 29 comments): **Describe the bug** Using the speech recognition text function, this error will be reported starting from April 7th This is the error log [logspeech.txt](https://github.com/Azure-Samples/cognitive-services-speech-sdk/files/11188995/logspeech.txt)
```

## Fix

1. If Azure speech recognition suddenly starts failing with 'Connection failed (no connection to the remote host) / WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED' and your code did not change, check the network path first.
2. The reporter traced it to network proxies / regional network issues and resolved it by provisioning a new secret key in a different region (Southeast Asia).

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in cognitive-services-speech-sdk.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in cognitive-services-speech-sdk, even a similar-looking one.
- General cognitive-services-speech-sdk setup or credential questions.

## Compatibility

- Cognitive Services Speech SDK (Azure-Samples/cognitive-services-speech-sdk)

## Variant phrasings

- How to fix "connection failed (no connection to the remote host) WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED" in cognitive-services-speech-sdk
- cognitive-services-speech-sdk: connection failed (no connection to the remote host) WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED
- connection problem (no connection to the remote host) WS_OPEN_ERROR_UNDERLYING_IO_OPEN_FAILED

## Edge cases

- So: verify no proxy or firewall blocks the websocket endpoint, and if the region's network is at fault, create the Speech resource in another region and rotate the key.

## Source

- https://github.com/Azure-Samples/cognitive-services-speech-sdk/issues/1911

---

Source: [Vectle](https://vectle.com/skills/skl_frAthOLTjLbySGutnp-_Vw). Version: `skv_ZUIiK81BZTaDvEnqx3I9xQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
