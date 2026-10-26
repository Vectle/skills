---
name: "phantombuster-phantom-not-working-is-o-a1ec61001be482ee"
description: "Fix for PhantomBuster Phantom \"not working\" is often just spent execution time or full slots: PhantomBuster - Docs (PhantomBuster help center): the free trial gives 2 hours of execution time total and 5 Phantom slots for 14 days; the ongoing free plan gives 30 minutes per month and 1 slot. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_hbsqtV0VKcoVHo_sSZBFLA"
  title: "PhantomBuster Phantom \"not working\" is often just spent execution time or full slots"
  version: "skv_NgkhmYcOxwcrMErF4O2Z2Q"
  updated: "2026-10-03T13:56:02.602936+00:00"
  canonical_url: "https://vectle.com/skills/skl_hbsqtV0VKcoVHo_sSZBFLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://support.phantombuster.com/hc/en-us/articles/26283273736466-How-to-Make-the-Most-of-Your-PhantomBuster-Free-Trial\"]"
---

TL;DR: PhantomBuster - Docs (PhantomBuster help center): the free trial gives 2 hours of execution time total and 5 Phantom slots for 14 days; the ongoing free plan gives 30 minutes per month and 1 slot, with result files capped at 10 rows. ## The fix When Phantoms stop launching or sit idle, check plan limits before debugging anything else: 1.

```text
PhantomBuster Phantom "not working" is often just spent execution time or full slots
```

## Fix
1. PhantomBuster - Docs (PhantomBuster help center): the free trial gives 2 hours of execution time total and 5 Phantom slots for 14 days; the ongoing free plan gives 30 minutes per month and 1 slot, with result files capped at 10 rows. ## The fix When Phantoms stop launching or sit idle, check plan limits before debugging anything else: 1.
   Expected: this specific failure stops.

## Details
Open the PhantomBuster dashboard and look at the usage meters: remaining monthly execution time and active slots. 2. If execution time is burned through, everything halts until the plan resets; either wait or upgrade the plan. 3. If all slots are busy with other automations, the new Phantom is queued, not broken. Stagger launches throughout the day instead of firing everything at once. 4. Keep inputs clean: a Phantom chewing through 1,000 junk profiles burns execution time that should go to real leads. Clean inputs plus staggered scheduling usually buys back a lot of headroom. Thread: docs:phantombuster-free-trial-limits

## When to use
You hit exactly this: PhantomBuster Phantom "not working" is often just spent execution time or full slots.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title.

## Root cause
Constantly hitting the ceiling means you have outgrown the plan, not that the tool is flaky.

---

Source: [Vectle](https://vectle.com/skills/skl_hbsqtV0VKcoVHo_sSZBFLA). Version: `skv_NgkhmYcOxwcrMErF4O2Z2Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
