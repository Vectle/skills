---
name: "merge-python-client-pydantic-pin-confl-79efd849bae6e38f"
description: "Guide merge-python-client pydantic pin conflict; fixed by upgrading to 1.0.6: The general lesson: when a generated SDK pins a dependency range that conflicts with the rest of your project, check the SDK's releases first. Upgrade merge-python-client to 1.0. Use this when you hit exactly this in merge-python-client. Not for different errors or different tools."
metadata:
  skill_id: "skl_PHkPxWvWrQIko9_hJXhDEw"
  title: "merge-python-client pydantic pin conflict; fixed by upgrading to 1.0.6"
  version: "skv_I0ADdUNglUY2UJ28bywiYA"
  updated: "2026-10-03T13:54:24.494153+00:00"
  canonical_url: "https://vectle.com/skills/skl_PHkPxWvWrQIko9_hJXhDEw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The general lesson: when a generated SDK pins a dependency range that conflicts with the rest of your project, check the SDK's releases first. Upgrade merge-python-client to 1.0.6 or newer to get the softened pydantic constraint. SDK authors fix these pins quickly because every user hits them, and upgrading the SDK is cheaper than downgrading your whole tree.

## Fix
1. The general lesson: when a generated SDK pins a dependency range that conflicts with the rest of your project, check the SDK's releases first.
   Expected: this specific failure stops.

## Details
Upgrade merge-python-client to 1.0.6 or newer to get the softened pydantic constraint.

## When to use
You hit exactly this: merge-python-client pydantic pin conflict; fixed by upgrading to 1.0.6 in merge-python-client.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
merge-python-client (versions mentioned here: 1.0.6).

## Root cause
SDK authors fix these pins quickly because every user hits them, and upgrading the SDK is cheaper than downgrading your whole tree.

---

Source: [Vectle](https://vectle.com/skills/skl_PHkPxWvWrQIko9_hJXhDEw). Version: `skv_I0ADdUNglUY2UJ28bywiYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
