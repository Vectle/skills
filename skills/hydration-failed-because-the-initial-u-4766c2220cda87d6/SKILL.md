---
name: "hydration-failed-because-the-initial-u-4766c2220cda87d6"
description: "Wrap the non-deterministic render in useEffect so the first client render matches the server HTML. Success looks like the console warning disappearing on reload. Applies to: Next.js 13+ (app or pages router), React 18+."
metadata:
  skill_id: "skl_ytzzhIPMi-zYXSaseQ5otQ"
  title: "Hydration failed because the initial UI does not match what was rendered on the server"
  version: "skv_J5eBCDWoTRRCGOTvKQhg0w"
  updated: "2026-10-03T05:35:38.675089+00:00"
  canonical_url: "https://vectle.com/skills/skl_ytzzhIPMi-zYXSaseQ5otQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://nextjs.org/docs/messages/react-hydration-error\"]"
---

## TL;DR
Wrap the non-deterministic render in useEffect so the first client render matches the server HTML. Success looks like the console warning disappearing on reload.

## The exact error
```text
Hydration failed because the initial UI does not match what was rendered on the server
```

## Steps to fix
1. Find the element the warning points at (the console names the mismatching tag)
2. Move browser-only values like Date.now, Math.random, or window.innerWidth into a useEffect or a mounted flag
3. Only if the difference is cosmetic and unavoidable, add suppressHydrationWarning to that element
4. Rebuild and reload; the warning should be gone

## When this applies
- Next.js app or pages router with SSR
- React prints the hydration mismatch warning in the console

## When this does NOT apply
- Pure client-side React apps with no SSR
- Errors that crash the build instead of warning at runtime

## Tool + versions
Next.js 13+ (app or pages router), React 18+

## Why it happens
The HTML the server sent and the HTML React renders on the client for the first pass disagree. The usual cause is rendering something that only exists in the browser during SSR.

## Edge cases
- Third-party widgets that inject their own markup
- React StrictMode double-invoking render in dev
- Browser extensions rewriting the DOM before React hydrates

## Where this came from
Resolved from a real public thread: https://nextjs.org/docs/messages/react-hydration-error (docs:react-hydration-error).

---

Source: [Vectle](https://vectle.com/skills/skl_ytzzhIPMi-zYXSaseQ5otQ). Version: `skv_J5eBCDWoTRRCGOTvKQhg0w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
