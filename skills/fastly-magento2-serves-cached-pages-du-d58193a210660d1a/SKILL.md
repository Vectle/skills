---
name: "fastly-magento2-serves-cached-pages-du-d58193a210660d1a"
description: "Fixes Fastly Magento2 serving cached pages during maintenance mode for whitelisted IPs. Use this when admin IPs still get stale content. Not for non-Fastly Magento setups."
metadata:
  skill_id: "skl_265ulKmC_k7HleTeUpMsbQ"
  title: "Fastly Magento2 serves cached pages during maintenance mode for whitelisted IPs"
  version: "skv_uxrNX9db9460mVkyp5tzEg"
  updated: "2026-10-03T05:08:44.141334+00:00"
  canonical_url: "https://vectle.com/skills/skl_265ulKmC_k7HleTeUpMsbQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if with Fastly caching a Magento 2 store, enabling maintenance mode does not stop Fastly from serving cached pages (even whitelisted admin IPs get stale content), the fix landed in the extension via PR #256: Fastly's Magento2 module now handles maintenance mode natively so whitelisted admin IPs bypass the cache during maintenance. Upgrade fastly/magento2 to a version containing the #256 fix. Workaround if you cannot upgrade: a hand-rolled config with an Edge ACL (`maint_allowlist`) for the bypass IPs plus an Edge Dictionary flag (`allow_super_users_during_maint`), checked in a custom VCL snippet during maintenance mode; it works but prefer the upgrade.

## Steps

1. Upgrade fastly/magento2 past the #256 fix.

2. Enable maintenance mode and test from a whitelisted IP.

   Expected: fresh admin pages, cached pages for everyone else. Success check: no stale content for whitelisted IPs.

## When to use this

- Fastly + Magento 2, maintenance mode still serves cache.

## When NOT to use this

- Non-Fastly caching; check that layer's maintenance handling.
- You are upgraded and still see it; report it.

## Compatibility

- fastly/magento2 with the PR #256 fix.

## Variant phrasings

- "fastly magento2 maintenance mode cache"
- "fastly serves cached pages maintenance"

## Root cause

The module did not natively handle maintenance-mode cache bypass.

## Edge cases

- The VCL workaround is community-documented; prefer the supported upgrade.

---

Source: [Vectle](https://vectle.com/skills/skl_265ulKmC_k7HleTeUpMsbQ). Version: `skv_uxrNX9db9460mVkyp5tzEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
