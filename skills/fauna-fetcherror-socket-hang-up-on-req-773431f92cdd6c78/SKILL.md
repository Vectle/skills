---
name: "fauna-fetcherror-socket-hang-up-on-req-773431f92cdd6c78"
description: "Fixes intermittent Fauna FetchError: socket hang up on requests to db.fauna.com from the Node driver. Use this when every few thousand requests one fails with no pattern on a long-lived server. Not for consistent connection failures or auth errors."
metadata:
  skill_id: "skl_4kM736rk-KtWdFHtjBM0rg"
  title: "Fauna FetchError: socket hang up on requests to db.fauna.com (intermittent)"
  version: "skv_t6zde4ZnpbLCh5YLVFQImQ"
  updated: "2026-10-03T04:37:47.500353+00:00"
  canonical_url: "https://vectle.com/skills/skl_4kM736rk-KtWdFHtjBM0rg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if the Fauna Node driver intermittently fails with `FetchError: request to https://db.fauna.com/ failed, reason: socket hang up` every few thousand requests, upgrade the driver to 4.1.1 or newer. It was a driver bug; the maintainer closed the thread saying the newest driver resolved it, and there is no config workaround worth chasing.

```text
FetchError: request to https://db.fauna.com/ failed, reason: socket hang up
```

## Steps

1. Upgrade the driver to at least 4.1.1.

2. Run your normal request volume.

   Expected: the intermittent hang-ups stop. Success check: thousands of requests complete without the FetchError.

## When to use this

- Intermittent socket hang up with no pattern, from a long-lived server (not a lambda thaw issue).
- Driver 4.0.3 or similar older version.

## When NOT to use this

- Every request fails; check network and auth.
- You are already on a current driver and still see it; report it fresh.

## Compatibility

- Fauna Node driver 4.1.1+ (thread closed April 2021).

## Variant phrasings

- "fauna socket hang up node driver"
- "faunadb-js intermittent FetchError"

## Root cause

A driver-side bug dropped connections intermittently under sustained request volume.

## Edge cases

- Retry logic can mask this but not fix it; upgrade instead.

Source: https://github.com/fauna/faunadb-js/issues/377

---

Source: [Vectle](https://vectle.com/skills/skl_4kM736rk-KtWdFHtjBM0rg). Version: `skv_t6zde4ZnpbLCh5YLVFQImQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
