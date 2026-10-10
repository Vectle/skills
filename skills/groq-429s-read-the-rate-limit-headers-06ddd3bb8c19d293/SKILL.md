---
name: "groq-429s-read-the-rate-limit-headers-06ddd3bb8c19d293"
description: "Guide Groq 429s: read the rate-limit headers, don't just retry blindly: Every response carries x-ratelimit-* headers; retry-after appears ONLY on 429 responses. ## What to do Before blindly retrying a Groq 429: read the response headers first. Use this when you hit exactly this in Groq 429s. Not for different errors or different tools."
metadata:
  skill_id: "skl_2mbinMsdstsavd9J2DD2jA"
  title: "Groq 429s: read the rate-limit headers, don't just retry blindly"
  version: "skv_IkBSYONwTiN-BkmEpVG6Nw"
  updated: "2026-10-03T05:54:50.795173+00:00"
  canonical_url: "https://vectle.com/skills/skl_2mbinMsdstsavd9J2DD2jA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Every response carries x-ratelimit-* headers; retry-after appears ONLY on 429 responses. ## What to do Before blindly retrying a Groq 429: read the response headers first. x-ratelimit-limit-requests is your RPD cap, x-ratelimit-limit-tokens is TPM; the -remaining- and -reset- variants tell you how much headroom is left and when the window resets. retry-after is set only when you actually hit the limit, so treat it as the authoritative wait time.

## Fix
1. Check exact limits at console.groq.com/settings/limits and back off to that window instead of hammering.
   Expected: the value or setting is exactly right, nothing ambiguous.

## Details
Official docs (Rate Limits): documents how Groq enforces rate limits across six dimensions (RPM, RPD, TPM, TPD, plus ASH/ASD for audio), applied at the organization level, not per user. Some accounts also get separate input/output token caps (ITPM/OTPM). Gotchas agents hit: cached tokens don't count toward limits, so a high cache hit rate lowers effective pressure; org-level limits mean one noisy loop can starve the whole org; and if your account shows an ITPM/OTPM split on the limits page, a huge output can trip OTPM even when total TPM looks fine.

## When to use
You hit exactly this: Groq 429s: read the rate-limit headers, don't just retry blindly in Groq 429s.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Groq 429s.

---

Source: [Vectle](https://vectle.com/skills/skl_2mbinMsdstsavd9J2DD2jA). Version: `skv_IkBSYONwTiN-BkmEpVG6Nw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
