---
name: "chargebee-can-t-resolve-http-after-upg-ae371501eaa9759d"
description: "Fixes the chargebee Node SDK failing with 'Can't resolve http' after upgrading to Next.js 15. Use this when the build breaks on browser/edge bundling of Node core modules. Not for other missing modules."
metadata:
  skill_id: "skl_0mSVHiCI-jStaerBsmoeXQ"
  title: "chargebee: Can't resolve 'http' after upgrading to Next.js 15 (fixed in v3.12.0)"
  version: "skv_r_pW9BXfADtrW7R28D76_Q"
  updated: "2026-10-03T05:06:57.935681+00:00"
  canonical_url: "https://vectle.com/skills/skl_0mSVHiCI-jStaerBsmoeXQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_jWN6i5HSYbrRmG_ZdZerMw\",\"https://github.com/chargebee/chargebee-node/issues/68\"]"
---

TL;DR: if upgrading from Next.js 14 to 15 breaks the build with `Module not found: Can't resolve 'http'` from the chargebee package, the SDK imported Node.js core modules (http, https) in code that gets bundled for the browser/edge runtime. Upgrade to chargebee v3.12.0 or newer (the fix landed first in 3.12.0-beta.1); the reporter confirmed the beta fixed the build on Cloudflare Pages edge runtime and the stable release closed the issue. The chargebee team shipped it as a non-breaking change.

```text
Module not found: Can't resolve 'http'
```

## Steps

1. Upgrade:

```sh
npm install chargebee@^3.12.0
```

2. Rebuild.

   Expected: the build completes. Success check: no more http resolve errors on Next 15 / edge.

## When to use this

- Next.js 15 (upgraded or fresh) with the chargebee package.

## When NOT to use this

- Other modules fail to resolve; check your imports.
- You are on 3.12.0+ and still see it; report it.

## Compatibility

- chargebee v3.12.0+ with Next.js 15 / edge runtimes.

## Variant phrasings

- "chargebee Can't resolve http nextjs 15"
- "chargebee node core modules browser"

## Root cause

Node core imports leaked into browser-bundled code paths.

## Edge cases

- None; the SDK fix is the whole story.

Source: https://github.com/chargebee/chargebee-node/issues/68

---

Source: [Vectle](https://vectle.com/skills/skl_0mSVHiCI-jStaerBsmoeXQ). Version: `skv_r_pW9BXfADtrW7R28D76_Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
