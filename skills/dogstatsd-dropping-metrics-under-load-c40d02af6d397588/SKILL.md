---
name: "dogstatsd-dropping-metrics-under-load-c40d02af6d397588"
description: "DogStatsD runs over UDP, so a saturated socket buffer drops packets silently. Spotty custom metrics under load mean the buffer, not Datadog."
metadata:
  skill_id: "skl_T4LK6UQVNrtcMSuI3oun9g"
  title: "DogStatsD dropping metrics under load: socket buffer and sampling"
  version: "skv_JTCHmtrMltuiF2CEu1I90Q"
  updated: "2026-10-03T04:36:14.958904+00:00"
  canonical_url: "https://vectle.com/skills/skl_T4LK6UQVNrtcMSuI3oun9g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/developers/dogstatsd/\"]"
---

**TL;DR:** DogStatsD runs over UDP, so a saturated socket buffer drops packets silently. Spotty custom metrics under load mean the buffer, not Datadog. Aggregate more, emit less. Prefer distributions over histograms for latency: server-side aggregation handles the math.

## The fix

1. Bursty emission (10k increments in a loop, then nothing).

2. Many containers sharing one agent with small buffers.

3. Histograms with high cardinality: more series, more packets.

4. **Raise the socket buffer** (`SO_RCVBUF`) on the agent host if the OS default is small. This is the usual fix.

5. **Sample client-side.** DogStatsD supports sample rates; a 0.1 rate on a high-volume counter keeps the shape and drops 90 percent of packets.

6. **Aggregate more, emit less.** Counters and distributions exist so you do not emit a gauge per event.

7. **Prefer distributions over histograms** for latency: server-side aggregation handles the math.

8. If loss is unacceptable for a specific metric, send it via the API instead of UDP. Slower, reliable, and rate-limited, pick your tradeoff.

## When to use this

- This covers exactly what the title says: DogStatsD dropping metrics under load.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with DogStatsD; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 0.1 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_T4LK6UQVNrtcMSuI3oun9g). Version: `skv_JTCHmtrMltuiF2CEu1I90Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
