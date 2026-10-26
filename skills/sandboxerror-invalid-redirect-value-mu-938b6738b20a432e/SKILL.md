---
name: "sandboxerror-invalid-redirect-value-mu-938b6738b20a432e"
description: "Fixes the E2B SandboxError \"Invalid redirect value, must be one of follow or manual\" on Vercel Edge by upgrading the E2B JS SDK to v1.2.3 or newer, where the RPC layer uses redirect: \"follow\". Use when E2B sandbox calls fail inside Vercel Edge functions but the same code works on Node. Not for redirect errors from your own fetch calls or other SDKs."
metadata:
  skill_id: "skl_4zGdy5IPtJERkBcoJPUXWw"
  title: "SandboxError \"Invalid redirect value, must be one of follow or manual\" running E2B on Vercel Edge"
  version: "skv_Z9UfwIfZ7m7DpVsg9xDIFA"
  updated: "2026-10-03T04:05:41.078847+00:00"
  canonical_url: "https://vectle.com/skills/skl_4zGdy5IPtJERkBcoJPUXWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_Es7XVl1G_7VfBmGLsvf9lQ\",\"https://github.com/e2b-dev/E2B/issues/531\"]"
---

## TL;DR

Upgrade the E2B JS SDK to v1.2.3 or newer with `npm i e2b@^1.2.3`. Versions before 1.2.3 pass a redirect mode the Vercel Edge runtime does not implement, so every sandbox call throws. If you cannot upgrade, move the E2B calls to a standard Node runtime instead of an Edge function.

## The error

```text
SandboxError: 2: [unknown] Invalid redirect value, must be one of "follow" or "manual"
```

## Fix it

1. Confirm your installed E2B SDK version:
   ```bash
   npm ls e2b
   ```
   Success check: the reported version is below 1.2.3, confirming you are affected.

2. Upgrade the SDK:
   ```bash
   npm i e2b@^1.2.3
   ```
   Success check: install completes with no peer-dependency errors.

3. Redeploy the Edge function and trigger a sandbox call.
   Success check: the call succeeds and no SandboxError appears in the logs.

4. If you cannot upgrade (pinned version), move E2B calls out of the Edge function into a Node runtime route or serverless function.
   Success check: the identical code that failed on Edge now runs.

## When this applies

- E2B JS SDK below v1.2.3 running inside a Vercel Edge function or any Edge runtime.
- The same code works on Node.js locally or on a Node serverless function.

## When it does not apply

- You are already on e2b@1.2.3 or newer and still see the error; the cause is different.
- The redirect error comes from your own fetch calls, not the E2B SDK.
- You are not using an Edge runtime at all.

## Compatibility

- E2B JS SDK: affected below v1.2.3, fixed in v1.2.3 and up.
- Vercel Edge Runtime (any version). Node.js 18+ is unaffected.

## Variant phrasings

- `SandboxError: Invalid redirect value`
- E2B Edge function redirect error
- e2b on Vercel Edge: "must be one of follow or manual"

## Why it happens

The E2B JS SDK's RPC layer (connect-es) sent `redirect: "error"` on requests to E2B endpoints. The Vercel Edge runtime only implements `redirect: "follow"` and `redirect: "manual"`, so the runtime rejected the value and the SDK surfaced it as a SandboxError. The E2B team fixed Edge support in v1.2.3 by using `redirect: "follow"`.

## Edge cases

- If your lockfile pins e2b below 1.2.3 transitively, bump the direct dependency and remove the stale lockfile entry before reinstalling.
- Edge middleware hits the same issue; the fix is identical.
- Source: https://github.com/e2b-dev/E2B/issues/531


---

Source: [Vectle](https://vectle.com/skills/skl_4zGdy5IPtJERkBcoJPUXWw). Version: `skv_Z9UfwIfZ7m7DpVsg9xDIFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
