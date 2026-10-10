---
name: "the-runner-has-received-a-shutdown-sig-e17b31757c73fc01"
description: "What The runner has received a shutdown signal means in a GitHub Actions log, and how to tell a preempted runner from an OOM kill or a timeout. Use when the log ends with this line and exit 143 with no test failures."
metadata:
  skill_id: "skl_zkaDpzudMZijOnmHCocSrg"
  title: "The runner has received a shutdown signal"
  version: "skv_x5dnE6momeokWs3Mit7GyQ"
  updated: "2026-10-03T05:59:53.355231+00:00"
  canonical_url: "https://vectle.com/skills/skl_zkaDpzudMZijOnmHCocSrg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Keep jobs short, set timeout-minutes, and retry transient runner kills automatically. The runner process received SIGTERM from outside the job: the host reclaimed the machine. Your code is almost never at fault; the job had no chance to fail cleanly, so the absence of test failures is the signature.

```text
The runner has received a shutdown signal.
```

## The fix

1. Check the job log around the line: if it ends with exit code 143 and no test failures, the runner was killed externally.

2. Rule out your own causes: a concurrency group with cancel-in-progress (expected cancel, not a kill), an expired timeout-minutes (different message), and a process in the job sending SIGTERM to its own process group.

3. Retry the failed job - a preempted runner almost always passes on retry:
   ```bash
   gh run rerun [run-id] --failed
   ```
   Expected: The rerun completes; the kill does not repeat at the same point.

4. For jobs that sustain high CPU for 15+ minutes on GitHub-hosted runners, split the work into smaller matrix legs with per-leg timeout-minutes so one eviction costs minutes, not the whole job.

5. On self-hosted runners, check the host: preemptible or spot VMs are reclaimed at will. Use on-demand hosts for long jobs or accept retries as normal.

## When this applies

- the log ends with The runner has received a shutdown signal and exit 143
- a long job dies at different points on different runs
- self-hosted runners on preemptible VMs

## When it does NOT apply

- the log shows test failures before the line - the shutdown may be a consequence, not the cause
- the message appears with a concurrency cancel - that is a deliberate cancel, handle it with cancel-in-progress semantics

## Compatibility

GitHub-hosted and self-hosted runners; exit 143 is SIGTERM on Linux.

## Variants of this error

### `##[error]The runner has received a shutdown signal.`
Same message with the runner's error prefix.

### `exiting (rc=143); halting VM`
How the same kill reads in self-hosted runner logs.

## Why it happens

The runner process received SIGTERM from outside the job: host eviction on preemptible machines, autoscaler scale-in, the runner service stopping, or (on GitHub-hosted) the host reclaiming an overloaded machine. The job had no chance to fail cleanly, so there is no test output - the absence of failures is the signature.

## Edge cases and pitfalls

- A memory-eating test can look identical (the OOM killer sends SIGKILL, not SIGTERM, and usually logs differently) - check memory graphs if the kill always happens at the same point.
- Jobs killed this way usually pass on retry; if a specific job dies every run at the same point, suspect the workload, not the host.

---

Source: [Vectle](https://vectle.com/skills/skl_zkaDpzudMZijOnmHCocSrg). Version: `skv_x5dnE6momeokWs3Mit7GyQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
