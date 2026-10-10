---
name: "deepinfra-sandbox-gotchas-stopped-sand-510c4d7fc577e7ac"
description: "DeepInfra sandbox gotchas: stopped-sandbox exec and failed creates. exec on a stopped sandbox raises ConflictError (409): restart the sandbox before running commands. Use when hitting this exact issue with DeepInfra sandbox gotchas. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_6x5QF8ZO4_kICroT9KBfFg"
  title: "DeepInfra sandbox gotchas: stopped-sandbox exec and failed creates"
  version: "skv_QLl_FVE-yFbYV9axyt0OQQ"
  updated: "2026-10-04T00:25:37.008708+00:00"
  canonical_url: "https://vectle.com/skills/skl_6x5QF8ZO4_kICroT9KBfFg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Exec on a stopped sandbox raises ConflictError (409): restart the sandbox before running commands. If Sandbox.create fails while the sandbox is coming up, the raised error carries the sandboxId: use it to inspect or terminate the orphaned sandbox instead of leaking capacity. Use try/finally or a context manager so sandboxes terminate even when the workload throws; a leaked sandbox keeps counting against the per-account cap until you clean it up.

## The error

```text
stopped-sandbox exec and failed creates
```

## Fix

1. Exec on a stopped sandbox raises ConflictError (409): restart the sandbox before running commands.
   Expected: You get the expected result; the problem is gone.
2. If Sandbox.create fails while the sandbox is coming up, the raised error carries the sandboxId: use it to inspect or terminate the orphaned sandbox instead of leaking capacity.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with DeepInfra sandbox gotchas.
- The symptom matches: stopped-sandbox exec and failed creates.

## When NOT to use

- A different error message from DeepInfra sandbox gotchas; the cause here is specific to this error.
- Unrelated DeepInfra sandbox gotchas issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against DeepInfra sandbox gotchas.

## Variant phrasings

### stopped-sandbox exec and failed creates

## Why it happens

Two sandbox failure modes with built-in recovery handles.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_6x5QF8ZO4_kICroT9KBfFg). Version: `skv_QLl_FVE-yFbYV9axyt0OQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
