---
name: "diagnosing-a-stale-terraform-state-loc-7a9cd6d03500192b"
description: "When the lock holder is gone but the lock remains, force-unlock is safe only after confirmation. This is the full procedure: identify the holder, prove it dead, unlock, verify. Not for different error messages."
metadata:
  skill_id: "skl_aB7l3GtY3GfRjhrWR82jRg"
  title: "Diagnosing a stale Terraform state lock: \"Error acquiring the state lock\" from a dead process"
  version: "skv_oKexPZRpjXolMp36hvmAZg"
  updated: "2026-10-03T14:15:20.721547+00:00"
  canonical_url: "https://vectle.com/skills/skl_aB7l3GtY3GfRjhrWR82jRg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/state/locking/\"]"
---

**TL;DR:** When the lock holder is gone but the lock remains, force-unlock is safe only after confirmation. This is the full procedure: identify the holder, prove it dead, unlock, verify. Cause The lock was never released because the holder died without cleanup: SIGKILLed CI job, OOM-killed runner, closed laptop lid mid-apply. Read the Lock Info ID.

## The error

```text
Error: Error acquiring the state lock
```

# Diagnosing a stale Terraform state lock

## Symptom

`Error: Error acquiring the state lock`, and the Lock Info `Who`/`Created` point at a process that should be finished: a CI job that ended, a laptop that rebooted, a terminal that was closed.

## Cause

The lock was never released because the holder died without cleanup: SIGKILLed CI job, OOM-killed runner, closed laptop lid mid-apply. The lock record in DynamoDB (or the S3 lockfile) outlives the process.

## Confirmation

1. Read the Lock Info ID. Note the exact lock ID string.
2. Prove the holder is dead: check the CI job status for that run ID, `ps` on the machine named in `Who`, or the runner's job history. A finished/failed job with no running terraform process means stale.
3. Check whether the dead run half-applied: you cannot know yet, and that is fine. Do not touch state until the lock is cleared and you can plan.

## Fix

1. `terraform force-unlock [lock-id]` with the exact ID from the error. It asks for confirmation; this is the one prompt you answer deliberately.
2. Immediately run `terraform plan` (not apply). Read the whole plan.

## Verification

1. The plan tells you what the dead run did: creates/updates that already happened show as no-change or as drift to reconcile; unfinished work shows as pending changes.
2. If the plan is clean or only shows expected changes, the state is consistent. Proceed normally.
3) If the plan shows half-created resources or confusing diffs, reconcile before applying: import what exists, remove what is broken, then apply.
4. Fix the root cause: CI jobs that get SIGKILLed need graceful shutdown or lock timeouts; runners need enough memory to not OOM mid-apply.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Diagnosing a stale Terraform state lock.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Diagnosing behavior.

## Edge cases

- 3) If the plan shows half-created resources or confusing diffs, reconcile before applying: import what exists, remove what is broken, then apply.

---

Source: [Vectle](https://vectle.com/skills/skl_aB7l3GtY3GfRjhrWR82jRg). Version: `skv_oKexPZRpjXolMp36hvmAZg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
