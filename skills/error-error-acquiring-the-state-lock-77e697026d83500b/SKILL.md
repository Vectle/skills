---
name: "error-error-acquiring-the-state-lock-77e697026d83500b"
description: "Fixes terraform's \"Error acquiring the state lock\" failure. Use when terraform plan or apply refuses to run because a previous run crashed, was cancelled, or is still holding the state lock. Explains how to identify the dead lock holder and release it safely with terraform force-unlock. Not for first-time backend setup errors, provider install failures, or locks held by a live running apply."
metadata:
  skill_id: "skl_rv1NBjnbTu6XLbx_K7I9LQ"
  title: "Error: Error acquiring the state lock"
  version: "skv_lzVi3zhDpLqIjJ1c2CNY8A"
  updated: "2026-10-03T06:01:56.090134+00:00"
  canonical_url: "https://vectle.com/skills/skl_rv1NBjnbTu6XLbx_K7I9LQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix terraform "Error: Error acquiring the state lock"

**TL;DR:** A previous terraform run crashed, was cancelled, or is still holding the state lock. Copy the Lock ID out of the error output, confirm nobody (and no CI job) is actually running terraform against this state right now, then run `terraform force-unlock [lock-id]`. Your next plan or apply will take the lock cleanly.

## The error

```text
Error: Error acquiring the state lock

Lock Info:
  ID:        a1b2c3d4-0000-0000-0000-000000000000
  Who:       runner@ci-agent-7
  Created:   2026-10-02 21:40:00 +0000 UTC
  Operation: OperationTypeApply
```

## Steps

1. Find the lock holder. Read the `Who` and `Created` fields in the error. Check your CI dashboard and ask the team whether anyone is mid-apply. Expected: you can identify a dead or finished run holding the lock.
2. If a real run is still active, wait for it. Killing it or unlocking under it can corrupt state. Expected: the active run finishes and the error goes away on its own.
3. If the holder is dead (cancelled CI job, killed terminal, crashed process), release the lock:

   ```bash
   terraform force-unlock a1b2c3d4-0000-0000-0000-000000000000
   ```

   Terraform prompts for confirmation. Type `yes`. Expected output: `Terraform state has been successfully unlocked!`
4. Re-run your command: `terraform plan`. Expected: the plan runs with no lock error.

## When this applies

- Plan or apply fails with `Error acquiring the state lock` and the Lock Info points at a run you know is dead (cancelled CI job, closed laptop, killed process).
- You use a remote backend with locking (S3 + DynamoDB, GCS, Azure Blob lease, Terraform Cloud).

## When it does NOT apply

- The lock holder is a live, running apply. Wait for it instead.
- You see the error on a *local* backend because two terminals are running terraform at once. Close one instead of force-unlocking.

## Tool and version compatibility

- Terraform CLI 0.12+ through 1.x (lock format stable across versions).
- Any backend that supports locking: S3, GCS, AzureRM, Terraform Cloud/Enterprise.

## Why it happens

Terraform takes an exclusive lock on state before every plan/apply so two writers cannot interleave changes. If the process dies while holding it (CI timeout, Ctrl-C, closed laptop), the lock record is never released. The lock is just a record; the state itself is usually fine.

## Edge cases and pitfalls

- `force-unlock` while a real apply runs can corrupt state. This is the one dangerous move here. Verify first.
- With the S3 backend, the native lockfile (use_lockfile) and the older DynamoDB table both exist in the wild; `force-unlock` handles either, but needs the same backend config as the run that locked it.
- Local backend locks appear as `.terraform.tfstate.lock.info`; deleting that file by hand is the local equivalent, but prefer `force-unlock`.
- If locks keep appearing, your CI is cancelling jobs mid-apply. Fix the timeout, not the symptom.

---

Source: [Vectle](https://vectle.com/skills/skl_rv1NBjnbTu6XLbx_K7I9LQ). Version: `skv_lzVi3zhDpLqIjJ1c2CNY8A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
