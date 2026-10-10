---
name: "sentry-next-js-three-runtimes-three-in-c5e69b1a551eaf95"
description: "Next.js runs in three runtimes, so Sentry needs three init files plus a wrapped next.config. This skill covers the wizard output, what each file does, and the tunnelRoute fix for adblockers. Not the full reference manual."
metadata:
  skill_id: "skl_UqNeXXoWhzXmlAJoGK0zyw"
  title: "Sentry Next.js: three runtimes, three init files, one wrapped config"
  version: "skv_8gDY0POxKythjrOTvJxVjg"
  updated: "2026-10-03T04:46:47.129367+00:00"
  canonical_url: "https://vectle.com/skills/skl_UqNeXXoWhzXmlAJoGK0zyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Next.js runs in three runtimes, so Sentry needs three init files plus a wrapped next.config. This skill covers the wizard output, what each file does, and the tunnelRoute fix for adblockers. Keep that shape.

## Use the wizard

```
npx @sentry/wizard@latest -i nextjs
```

It creates separate init files because Next.js runs your code in three environments:

- Client: `instrumentation-client.ts` (browser)
- Server: `sentry.server.config.ts` (Node.js)
- Edge: `sentry.edge.config.ts` (edge runtime)

And `instrumentation.ts` registers them:

```ts
import * as Sentry from "@sentry/nextjs";

export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./sentry.server.config");
  }
  if (process.env.NEXT_RUNTIME === "edge") {
    await import("./sentry.edge.config");
  }
}

export const onRequestError = Sentry.captureRequestError;
```

## The wrapped next.config

```ts
import { withSentryConfig } from "@sentry/nextjs/config";

export default withSentryConfig(nextConfig, {
  org: "[your org slug]",
  project: "[your project slug]",
  authToken value process.env.SENTRY_AUTH_TOKEN, // secret, CI only, never client-exposed
  tunnelRoute: "/sentry-tunnel", // routes events through your server, dodges adblockers
  silent: !process.env.CI,
});
```

`org` and `project` here are for build-time source map uploads, which is why they sit next to the auth token. This is also where the classic mixup happens: the DSN goes in the three init files, the AUTH TOKEN goes here. Swapping them breaks both.

## Sample rates per environment

The wizard generates `tracesSampleRate: process.env.NODE_ENV === "development" ? 1.0 : 0.1`. Keep that shape. Setting 1.0 unconditionally is the fastest way to burn a month of span quota in a week.

## Don't forget global-error.tsx

The wizard adds `app/global-error.tsx` to catch React rendering errors in App Router. If you hand-rolled the setup and rendering crashes are missing from Sentry, that file is what you forgot.

## When to use this

- This covers exactly what the title says: Sentry Next.js.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 1.0, 0.1 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_UqNeXXoWhzXmlAJoGK0zyw). Version: `skv_8gDY0POxKythjrOTvJxVjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
