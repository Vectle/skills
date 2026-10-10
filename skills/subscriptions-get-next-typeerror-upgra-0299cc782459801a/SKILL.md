---
name: "subscriptions-get-next-typeerror-upgra-0299cc782459801a"
description: "Shows how to fix subscriptions.get_next() TypeError: upgrade mollie-api-python to 3.6.0. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_HORdcX_xMbBfRBQ8NAXKPA"
  title: "subscriptions.get_next() TypeError: upgrade mollie-api-python to 3.6.0"
  version: "skv_SLIWIeg6wg_hLkmBoLca4w"
  updated: "2026-10-03T14:04:10.702593+00:00"
  canonical_url: "https://vectle.com/skills/skl_HORdcX_xMbBfRBQ8NAXKPA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade mollie-api-python to 3.6.0 or later, where this was fixed (PR 323 reworked the resource path handling so the parent context is no longer needed). A working proof of concept landed in PR 323, and the maintainer confirmed the issue was resolved in release 3.6.0.

## Steps

1. If subscriptions.get_next() throws TypeError: __init__() missing 1 required positional argument: 'customer', you are on a version with the nested pagination bug: the next page rebuilds the resource without the parent Customer context. Upgrade mollie-api-python to 3.6.0 or later, where this was fixed (PR 323 reworked the resource path handling so the parent context is no longer needed). The maintainer confirmed the fix in the 3.6.0 release. Note this bug class affected all nested list resources (refunds, chargebacks, captures, shipments, mandates), so if you paginate any of those, the same upgrade applies.

Expected: The maintainer confirmed the fix in the 3.6.0 release.

## When to use

You are seeing this: Calling get_next() on a subscription list raised TypeError: __init__() missing 1 required positional argument: customer. Use this skill when you run into "subscriptions.get_next() TypeError: upgrade mollie-api-python to 3.6.0".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 3.6.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

A maintainer explained the root cause: subscriptions are nested CustomerSubscription objects, and the generic ObjectList pagination path rebuilt the next page without the parent Customer

## Edge cases

- Note this bug class affected all nested list resources (refunds, chargebacks, captures, shipments, mandates), so if you paginate any of those, the same upgrade applies.


---

Source: [Vectle](https://vectle.com/skills/skl_HORdcX_xMbBfRBQ8NAXKPA). Version: `skv_SLIWIeg6wg_hLkmBoLca4w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
