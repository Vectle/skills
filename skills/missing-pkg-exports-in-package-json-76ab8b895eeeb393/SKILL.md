---
name: "missing-pkg-exports-in-package-json-76ab8b895eeeb393"
description: "Shows how to fix missing `pkg.exports` in package.json. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_xE8_SNG4vs_6bbgGp5xAhg"
  title: "Missing `pkg.exports` in package.json"
  version: "skv_GJLC1ez5wiHo3y3nBNbrZg"
  updated: "2026-10-03T22:18:57.684063+00:00"
  canonical_url: "https://vectle.com/skills/skl_xE8_SNG4vs_6bbgGp5xAhg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "SyntaxError: Named export 'PostHogProvider' not found": maintainer hpouillot: use the dedicated @posthog/react package (same code, proper ESM exports) instead of posthog-js/react, docs at posthog.com/docs/libraries/react were updated to reflect this, and the issue was closed.

```text
SyntaxError: Named export 'PostHogProvider' not found
```

## Steps

1. Maintainer hpouillot: use the dedicated `@posthog/react` package (same code, proper ESM exports) instead of `posthog-js/react`, docs at posthog.com/docs/libraries/react were updated to reflect this, and the issue was closed.
2. Community workarounds that also worked: `pnpm patch` to add an `exports` map to posthog-js' package.json, or `ssr: { noExternal: ['posthog-js'] }` in vite.config.ts.

2. Success check: the symptom above is gone and the original operation completes.

3. - You hit this exact symptom in posthog-js.
- You want the verified fix without digging through the thread.

4. - A different error in posthog-js, even a similar-looking one.
- General posthog-js setup or credential questions.

5. - How to fix "missing pkg.exports in package.json" in posthog-js
- posthog-js: missing pkg.exports in package.json

## When to use

You are seeing this: ``text posthog-js can't be used in ESM/SSR Node projects (Remix/Vite): package.json lacks the exports map, so import { PostHogProvider } from 'posthog-js/react' fails with SyntaxError: Named export 'PostHogProvider' not found, the ESM file is treated as... Use this skill when you run into "Missing `pkg.exports` in package.json".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Variants

Other phrasings of the same problem that show up in reports:

### posthog-js can't be used in ESM/SSR Node projects (Remix/Vite): package.json lacks the exports map, so import { PostHogP

```text
`posthog-js` can't be used in ESM/SSR Node projects (Remix/Vite): package.json lacks the `exports` map, so `import { PostHogProvider } from 'posthog-js/react'` fails with `SyntaxError: Named export 'PostHogProvider' not found`, the ESM file is treated as CommonJS.
```

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/PostHog/posthog-js/issues/908


---

Source: [Vectle](https://vectle.com/skills/skl_xE8_SNG4vs_6bbgGp5xAhg). Version: `skv_GJLC1ez5wiHo3y3nBNbrZg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
