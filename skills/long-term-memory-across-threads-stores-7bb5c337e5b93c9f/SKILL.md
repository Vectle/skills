---
name: "long-term-memory-across-threads-stores-7bb5c337e5b93c9f"
description: "Checkpoints remember within a thread. For memory across threads and users, use a store: the BaseStore interface with namespaced key-value memory that tools and middleware can read and write. Not the full reference manual."
metadata:
  skill_id: "skl_LD498gFjRlqUgY2jXZE_tA"
  title: "Long-term memory across threads: stores, not just checkpoints"
  version: "skv_SnVFUtYQK9t3OUUOWqdAgA"
  updated: "2026-10-03T13:53:16.716348+00:00"
  canonical_url: "https://vectle.com/skills/skl_LD498gFjRlqUgY2jXZE_tA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Checkpoints remember within a thread. For memory across threads and users, use a store: the BaseStore interface with namespaced key-value memory that tools and middleware can read and write.

## The fix

1. Short-term memory: checkpoints, per thread_id. The conversation.

2. Long-term memory: stores, across threads. Facts about the user, preferences, learned state.

3. Namespace deliberately: `(user_id, "preferences")` style namespaces keep users' memories separate. A flat namespace leaks one user's facts into another's.

4. Write memories from tools (after a successful lookup or when the user states a preference), read them in before_model middleware or in the tool itself. Do not dump the whole store into every prompt; retrieve the relevant slice.

5. Decide what is worth remembering. Long-term memory without a write policy becomes a junk drawer that poisons prompts. The docs' long-term memory guide covers the patterns; start with explicit user facts and preferences.

6. Stores are separate from checkpointers. Back them up and secure them independently; they hold user data across sessions.

## When to use this

- This covers exactly what the title says: Long-term memory across threads.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Long-term; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Long-term behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_LD498gFjRlqUgY2jXZE_tA). Version: `skv_SnVFUtYQK9t3OUUOWqdAgA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
