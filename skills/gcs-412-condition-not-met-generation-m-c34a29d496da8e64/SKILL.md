---
name: "gcs-412-condition-not-met-generation-m-c34a29d496da8e64"
description: "Google Cloud Storage writes rejected with 412 Precondition Failed on if-generation-match. Covers reading the current generation, the retry loop, and why removing the precondition is the wrong fix. Not for 403 permission errors or 404 not-found on the object."
metadata:
  skill_id: "skl_T0BnAL14-IZu8RdjLa4mYA"
  title: "GCS 412 condition not met: generation-match preconditions explained"
  version: "skv_JQeJSAR-_fSkUjU0N_yZBg"
  updated: "2026-10-03T04:38:36.64809+00:00"
  canonical_url: "https://vectle.com/skills/skl_T0BnAL14-IZu8RdjLa4mYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: 412 means your if-generation-match precondition failed: the object changed (or appeared/disappeared) between your read and write, and GCS rejected the write to protect you from clobbering. Re-read the object, get the new generation, re-apply your change, and retry. Do not retry the same bytes with the same stale generation, that fails forever. This is optimistic concurrency working as designed, not an error to fix by removing the precondition.

The error, verbatim:

```text
412 Precondition Failed, "condition not met".
```

Steps:

1. Read the object and its current generation. Success: you have the fresh generation number.
2. Compute the new content against that generation. Success: your change applies to current state.
3. Write with if-generation-match set to the generation from step 1. Success: 200 and the returned generation increments by one.
4. On 412, go back to step 1. Bound the retries; infinite retry loops on hot objects starve. Success: the write lands or you stop after N attempts with a clear signal.

When to use: GCS writes rejected with 412 on generation-match preconditions.

When not to use: 403s (permissions), 404s (wrong object name), or a write path that never sets preconditions (nothing to fail).

Compatibility: Google Cloud Storage JSON API and XML API, any client that supports generation preconditions.

Variants:
- gcs 412 precondition failed
- if_generation_match condition not met
- gcs optimistic concurrency 412

Common patterns:
- if-generation-match=0 with an existing object: "only write if absent" failed because it is present. You wanted create-or-fail semantics and the object is already there.
- if-generation-match=[N] after a read: another writer beat you. Re-read, get the new generation, re-apply, retry.

Root cause: the write carried a stale generation. Either someone else wrote first, or the object was created or deleted since you read it. The rejection is the system working, it stopped a lost update.

Edge cases:
- Agent trap: catching 412 and retrying the SAME bytes with the SAME stale generation fails forever. You must re-read first.
- Removing the precondition "fixes" the 412 and reintroduces the lost-update race it was preventing. Dont do that.
- Verify: after a successful write the returned generation increments by one from your read; concurrent writers see 412s, not silent overwrites.

---

Source: [Vectle](https://vectle.com/skills/skl_T0BnAL14-IZu8RdjLa4mYA). Version: `skv_JQeJSAR-_fSkUjU0N_yZBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
