---
name: "infinite-rebuild-loop-using-compute-se-360de3c84c2ed633"
description: "Shows how to fix infinite rebuild loop using compute serve --watch. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_eaVwQWxb4TtufBWhsuLzhA"
  title: "infinite rebuild loop using compute serve --watch"
  version: "skv_W6TlPvWQg43CnDPBBgRbYQ"
  updated: "2026-10-03T04:46:40.325918+00:00"
  canonical_url: "https://vectle.com/skills/skl_eaVwQWxb4TtufBWhsuLzhA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/fastly/cli/issues/1332\"]"
---

## TL;DR

Upgrade to v15.2.0 or newer and the reported issue is resolved; the maintainer confirmed the fix shipped there. Fixed in the Fastly Compute release v15.2.0.

## Steps

1. Upgrade to v15.2.0 or newer and the reported issue is resolved; the maintainer confirmed the fix shipped there.

2. Fixed in the Fastly Compute release v15.2.0.

## When to use

You are seeing this: Viceroy version: viceroy 0.12.1 What happened Happens: While running fastly compute serve --watch we ended up with an infinite loop of rebuilding, it seemed that something on the specific Mac, that was used, was doing a chmod operation as soon as fastly... Use this skill when you run into "infinite rebuild loop using compute serve --watch".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: v15.2.0, viceroy 0.12.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

Viceroy version: viceroy 0.12.1 What happened Happens: While running fastly compute serve --watch we ended up with an infinite loop of rebuilding, it seemed that something on the specific Mac, that was used, was doing a chmod operation as soon as fastly compute serve was issued creating an endless loop.


---

Source: [Vectle](https://vectle.com/skills/skl_eaVwQWxb4TtufBWhsuLzhA). Version: `skv_W6TlPvWQg43CnDPBBgRbYQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
