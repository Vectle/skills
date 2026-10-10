---
name: "posthog-was-already-loaded-elsewhere-554ee06ff6d6e739"
description: "Posthog Js: posthog was already loaded elsewhere\". The verified fix is Fix: Recommended best practice from the maintainer: own the initialization yourself, call `posthog.init(key, opts)` once and pass your client via `the PostHogProvider `client` prop` instead of letting the provider init from `apiKey`/`options`. Use this when you hit the symptoms above in posthog-js; not for unrelated posthog-js errors or general setup questions."
metadata:
  skill_id: "skl_gB0wir1kEXpTiuxjdbkzbw"
  title: "posthog was already loaded elsewhere\""
  version: "skv_7p9-oKG1LJ35liD05Xl_vg"
  updated: "2026-10-03T05:02:29.682997+00:00"
  canonical_url: "https://vectle.com/skills/skl_gB0wir1kEXpTiuxjdbkzbw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Recommended best practice from the maintainer: own the initialization yourself, call `posthog.init(key, opts)` once and pass your client via `the PostHogProvider `client` prop` instead of letting the provider init from `apiKey`/`options`.

## The error

```text
Console warning `[PostHog.js] was already loaded elsewhere. This may cause issues.` appears in production with `PostHogProvider` from `posthog-js/react`, even when the provider is used exactly once. Reported against Gatsby, Next.js, and Vite apps.
```

## Fix

1. Recommended best practice from the maintainer: own the initialization yourself, call `posthog.init(key, opts)` once and pass your client via `the PostHogProvider `client` prop` instead of letting the provider init from `apiKey`/`options`.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in posthog-js.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in posthog-js, even a similar-looking one.
- General posthog-js setup or credential questions.

## Compatibility

- Posthog Js (PostHog/posthog-js)

## Variant phrasings

- How to fix "posthog was already loaded elsewhere"" in posthog-js
- posthog-js: posthog was already loaded elsewhere"

## Source

- https://github.com/PostHog/posthog-js/issues/723

---

Source: [Vectle](https://vectle.com/skills/skl_gB0wir1kEXpTiuxjdbkzbw). Version: `skv_7p9-oKG1LJ35liD05Xl_vg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
