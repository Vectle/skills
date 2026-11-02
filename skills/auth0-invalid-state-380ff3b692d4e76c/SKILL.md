---
name: "auth0-invalid-state-380ff3b692d4e76c"
description: "auth0 invalid state"
metadata:
  skill_id: "skl_6CTNyTB_JXd5wqelGesgXA"
  title: "auth0 invalid state"
  version: "skv_2mbK1wEqm-nDqFP_-cK2NQ"
  updated: "2026-11-02T16:11:23.165489+00:00"
  canonical_url: "https://vectle.com/skills/skl_6CTNyTB_JXd5wqelGesgXA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Start login through the SDK (loginWithRedirect, or the equivalent in your framework SDK) instead of building an /authorize URL by hand. A hand-built link sends a state Auth0 returns faithfully, but the SDK never stored it, so its callback check compares against nothing and fails. Expected: the stored transaction and the returned state come from the same flow.

Handle the callback exactly once. The SDK deletes the stored state after it validates it, so a second parse or callback handling (a React StrictMode double effect, a remounted callback component, a page refresh on the callback URL, or a user revisiting a bookmarked callback link) reads an empty store and reports invalid state. Guard the handler so it runs a single time. Expected: refreshing or re-entering the callback no longer appears in your error logs as new failures.

Keep the origin identical from login start to callback: same scheme, same host, same port. The SDK stores state in browser storage, which is scoped per origin, so starting on the https origin and landing on the http origin (or a different subdomain than the one configured) makes the stored value invisible. Expected: the redirect URI in the Auth0 application settings matches the real callback origin character for character.

Exclude the callback URL from page caching and service worker precaching. A cached callback response can replay a stale state or run the handler against an already-consumed transaction. Expected: the callback route is served fresh and its query parameters are the ones from this login.

If you genuinely manage state yourself (a server-side flow), store the exact value you sent in the session at authorize time and compare it to the value on the callback before exchanging the code; log both (truncated) when they differ so you can see whether the returned one is stale, from another tab, or missing entirely. Expected: mismatches stop being guesswork.

---

Source: [Vectle](https://vectle.com/skills/skl_6CTNyTB_JXd5wqelGesgXA). Version: `skv_2mbK1wEqm-nDqFP_-cK2NQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
