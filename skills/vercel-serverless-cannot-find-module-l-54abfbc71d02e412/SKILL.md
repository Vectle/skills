---
name: "vercel-serverless-cannot-find-module-l-54abfbc71d02e412"
description: "Libsql Client Ts: vercel Serverless Cannot find module '@libsql/linux-x64-gnu'. The verified fix is Fix: Next.js/Vercel: use the documented extra bundler config for Next.js ('Using the library with Next.js' in the README; not needed on newer Next with vercel/next.js#55266) - 0.3.5-pre.2 resolved it for the reporter on both Vercel runtimes. Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_z7PI3ZbxF64hpM1rnqeY9A"
  title: "Vercel Serverless Cannot find module '@libsql/linux-x64-gnu'"
  version: "skv_CcIFUbJFZfp4eQpHc_Yycg"
  updated: "2026-10-03T04:41:03.771993+00:00"
  canonical_url: "https://vectle.com/skills/skl_z7PI3ZbxF64hpM1rnqeY9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Next.js/Vercel: use the documented extra bundler config for Next.js ('Using the library with Next.js' in the README; not needed on newer Next with vercel/next.js#(55266) - 0.3.5-pre.2 resolved it for the reporter on both Vercel runtimes.

## The error

```text
Issue tursodatabase/libsql-client-ts#84 (closed, 7 comments): After upgrading to @libsql/client@0.3.3-pre.2 it started giving me this error in the Vercel logs --- @libsql/client@0.3.2 works fine.
```

## Fix

1. Next.js/Vercel: use the documented extra bundler config for Next.js ('Using the library with Next.js' in the README; not needed on newer Next with vercel/next.js#(55266) - 0.3.5-pre.2 resolved it for the reporter on both Vercel runtimes.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in libsql-client-ts.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in libsql-client-ts, even a similar-looking one.
- General libsql-client-ts setup or credential questions.

## Compatibility

- Libsql Client Ts (tursodatabase/libsql-client-ts)

## Variant phrasings

- How to fix "vercel Serverless Cannot find module '@libsql/linux-x64-gnu'" in libsql-client-ts
- libsql-client-ts: vercel Serverless Cannot find module '@libsql/linux-x64-gnu'

## Edge cases

- AWS Lambda / other serverless: import `@libsql/client/web` instead - same API without the optional native dependency, so no `@libsql/linux-x64-gnu` module is ever required.

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/84

---

Source: [Vectle](https://vectle.com/skills/skl_z7PI3ZbxF64hpM1rnqeY9A). Version: `skv_CcIFUbJFZfp4eQpHc_Yycg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
