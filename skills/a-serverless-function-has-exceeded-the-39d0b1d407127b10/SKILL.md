---
name: "a-serverless-function-has-exceeded-the-39d0b1d407127b10"
description: "Your Vercel deploy fails with \"A Serverless Function has exceeded the unzipped maximum size of 250 MB\". This shows how to find what is bloating the bundle (huge deps like ace-builds or elizaos packages, stray data dirs pulled in by file tracing) and shrink it: serverExternalPackages, outputFileTracingExcludes, moving dev-only deps out of dependencies. Use when a Vercel deploy errors on function size. Not for build-time size errors or other platforms."
metadata:
  skill_id: "skl_FD7NhQE0oiGg3MKWlTBA0g"
  title: "A Serverless Function has exceeded the unzipped maximum size of 250 MB"
  version: "skv_UEdS98lnwLl-Qc3BR4SP9Q"
  updated: "2026-10-03T05:33:20.187482+00:00"
  canonical_url: "https://vectle.com/skills/skl_FD7NhQE0oiGg3MKWlTBA0g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/BabylonSocial/babylon/pull/1254\"]"
---

# A Serverless Function has exceeded the unzipped maximum size of 250 MB (Vercel)

TL;DR: one of your serverless functions bundles more than 250 MB unzipped and Vercel refuses to deploy it. The usual culprits are a giant dependency being bundled (50+ MB packages), dev-only packages in `dependencies`, or file tracing dragging in data directories. Fix it by externalizing the heavy package with `serverExternalPackages`, excluding unneeded paths with `outputFileTracingExcludes`, and moving dev-only libs to `devDependencies`.

```text
Error: A Serverless Function has exceeded the unzipped maximum size of 250 MB.
```

## 1. Find what is bloating the function

Look at the deploy log: Vercel prints the offending function path. Then check the three usual suspects:

- `package.json` `dependencies`: anything huge that only runs in dev or tests (playwright, testing libs, CLI tools)
- Heavy runtime imports: editor libs (ace-builds ~57 MB), AI agent frameworks (@elizaos/* ~91 MB), chromium bundles
- `outputFileTracingIncludes` globs that pull whole data directories into the bundle

Expected: you identify one or two packages or globs responsible for most of the weight.

## 2. Externalize heavy packages

In `next.config.ts`, keep big ESM packages out of the webpack bundle so they resolve at runtime instead:

```ts
export default {
  serverExternalPackages: ['@elizaos/core', '@elizaos/plugin-sql'],
}
```

This uses native `import()` at runtime, which also avoids `ERR_REQUIRE_ESM` breakage that a manual webpack externals callback can cause.

Expected: the function bundle drops by roughly the size of the externalized packages.

## 3. Trim file tracing

Exclude what the function never reads at runtime:

```ts
export default {
  outputFileTracingExcludes: {
    '*': ['./desktop/**', './data/raw/**', 'node_modules/@playwright/**'],
  },
}
```

One real case went from a 627 MB standalone bundle to 78 MB by excluding an Electron subproject the web app never imported.

Expected: redeploy passes the 250 MB check; the function still serves 200s.

## 4. Move dev-only deps out of dependencies

`@playwright/test`, `cheerio` used only by scripts, type-only tooling: these belong in `devDependencies`. Vercel's tracer walks the prod `node_modules` tree, so anything in `dependencies` is bundle candidate.

Expected: `npm install` still resolves cleanly; the tracer has less tree to walk.

## 5. Client-only the browser libs

If a heavy lib (code editor, charting) is only used in the browser, import it dynamically with `ssr: false` so it never enters server bundles:

```tsx
const CodeEditor = dynamic(() => import('./code-editor'), { ssr: false });
```

Expected: the lib disappears from serverless function bundles entirely.

## When this applies

- Vercel deploy fails with the exact 250 MB error above
- You recently added a big dependency or a broad `outputFileTracingIncludes` glob
- Next.js App Router or Pages Router on Vercel

## When it does not apply

- `Build exceeded maximum duration`: build time, not bundle size
- Edge Function 1 MB limit: separate, smaller limit with its own fixes
- Static export (`output: 'export'`) has no serverless functions at all

## Compatibility

Vercel serverless functions, all plans (the 250 MB unzipped cap applies to every plan). Next.js 13+ with `serverExternalPackages` (preferred over manual webpack externals for ESM packages). `outputFileTracingExcludes` works in next.config.js/mjs/ts.

## Why it happens

Vercel packages each API route/page into a serverless function by tracing its imports. Anything the tracer can reach, including a giant dependency, a dev tool left in `dependencies`, or a data directory matched by a glob, gets zipped into the function. Past 250 MB unzipped, the deploy is rejected.

## Edge cases

- The error names no function: check the full deploy log, the path is printed a few lines above the error.
- Externalizing breaks with `ERR_REQUIRE_ESM`: do not use a manual webpack externals callback with a `commonjs` prefix for ESM-only packages; `serverExternalPackages` handles them correctly.
- `.next/cache` (hundreds of MB) getting traced: add it to `outputFileTracingExcludes`.
- Dynamic `fs.readFileSync` on computed paths makes the tracer conservatively pull in whole parent directories; narrow with `excludeFiles` in vercel.json for the affected functions.

---

Source: [Vectle](https://vectle.com/skills/skl_FD7NhQE0oiGg3MKWlTBA0g). Version: `skv_UEdS98lnwLl-Qc3BR4SP9Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
