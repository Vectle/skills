---
name: "clerk-user-webhooks-handle-created-upd-3a260d93f72f827c"
description: "Clerk user sync: user.created, user.updated, and user.deleted are one sync unit. Covers subscribing to all three, routing to one sync function, and the created-only handler trap. Not for organization events or session webhooks."
metadata:
  skill_id: "skl_f9feGngyxR50OAhd0NnfgQ"
  title: "Clerk user webhooks: handle created, updated, and deleted, never only created"
  version: "skv_CO9cCzhCJNwaZUMOchdfnQ"
  updated: "2026-10-03T05:06:56.783104+00:00"
  canonical_url: "https://vectle.com/skills/skl_f9feGngyxR50OAhd0NnfgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://clerk.com/docs/guides/development/webhooks/syncing\",\"https://clerk.com/docs/guides/development/webhooks/debugging\",\"https://clerk.com/docs/guides/development/webhooks/overview\"]"
---

TL;DR: user.created, user.updated, user.deleted. Clerk emits all three; your app needs all three. This is the single most common webhook failure pattern: a created-only handler that works on demo day and rots immediately. Users change emails and your copy lies, users delete accounts and your copy keeps billing them. Subscribe to all three, route them to one sync function with a switch on evt.type, and use the Clerk user id as your external key in all three paths.

Steps:

1. In the Clerk Dashboard webhook endpoint settings, subscribe to all three user events. Check this in code review whenever the subscription list changes. Success: all three are subscribed.
2. Route them to one sync function with a switch on evt.type: created and updated both call your upsert path (they share logic; the only difference is whether the row is expected to exist), deleted calls your delete/anonymize path. Success: one function handles the trio.
3. Use the Clerk user id as your external key in all three paths. Never re-derive identity from email, because email changes arrive as updated. Success: identity is stable across email changes.
4. Test all three with replays from the Dashboard. A test plan that only creates users is a test plan for half the system. Success: create, update, and delete replays all process.

When to use: syncing Clerk users to your own database.

When not to use: organization or membership sync (same pattern, different events), session webhooks, or polling the Clerk API.

Compatibility: Clerk webhooks, any backend.

Variants:
- clerk user webhooks all three events
- clerk user.deleted handler
- clerk sync users created updated deleted

Root cause: the trio is one unit and teams implement one third of it. Every user.updated you ignored is a support ticket waiting; every user.deleted you ignored is a billing or compliance problem waiting.

Edge cases:
- Checklist: one shared upsert for created and updated. If you find yourself writing them separately, merge them.
- The trio pattern repeats for organizations and memberships. If you sync orgs, apply the same rule there.
- Subscribe to the events explicitly per endpoint. A new endpoint that forgets user.deleted is the same bug in a new place.

---

Source: [Vectle](https://vectle.com/skills/skl_f9feGngyxR50OAhd0NnfgQ). Version: `skv_CO9cCzhCJNwaZUMOchdfnQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
