---
name: "debug-a-failed-galaxy-job-red-dataset-6da1f301caa89573"
description: "Diagnoses failed Galaxy jobs (red datasets) by reading the job's own Tool Standard Output and Standard Error before changing anything. Use when a history dataset turns red or a tool run or workflow step fails. Not for green-but-wrong results or Galaxy platform outages."
metadata:
  skill_id: "skl_KjuPCn5va6A8U2TkDx0PLQ"
  title: "Debug a failed Galaxy job (red dataset): read the job logs before changing anything"
  version: "skv_4y8dT8bI0HYkYfVUHgpgFg"
  updated: "2026-10-03T04:23:51.510483+00:00"
  canonical_url: "https://vectle.com/skills/skl_KjuPCn5va6A8U2TkDx0PLQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Debug a failed Galaxy job (red dataset)

## TL;DR

Read the job's own logs before changing anything: click the red dataset, use the bug icon and the view-details Job Information section to read Tool Standard Output and Standard Error. The failure class is visible there in under a minute; do not change parameters or reinstall until you have.

Use this when a history dataset turns red, a tool run or workflow step fails,
or a rerun produces the same red output. Do not change parameters or
reinstall anything until you have read the job's own logs — Galaxy records
the tool's stdout and stderr for every job.

**When not to use this skill:** the dataset is green but the results look wrong (science problem, not a job failure); Galaxy itself is down or the job never started (platform problem); you need to write a new tool wrapper rather than debug a failed run. — Galaxy records
the tool's stdout and stderr for every job, and the failure class is visible
there in under a minute.

## 1. Get the actual error (the 30-second procedure)

1. Click the red dataset to expand it — the summary sometimes already shows
   the error message.
2. Click the **bug icon** to see the tool's reported error message.
3. Click the ⓘ (view details) icon, scroll to the **Job Information** section,
   and read **Tool Standard Output** and **Tool Standard Error**. These are
   the tool's own stdout/stderr from the failed run — ground truth, not a
   Galaxy interpretation.

Everything below keys off what those two logs contain.

## 2. Classify FIRST from the logs

### Gray dataset that never runs — not a failure

A gray dataset is **queued**, waiting for cluster capacity. On public servers
this is normal, and worse during training events. Nothing is broken; wait,
or run a smaller test job. Do not "fix" this by rerunning repeatedly.

### stderr contains `Killed` — out of memory

The signature, from the job's stderr:

```
command.sh: line 120: 2997 Killed blastn -query '...' -subject '...' \
  -num_threads "${GALAXY_SLOTS:-8}" ...
```

The scheduler killed the process for exceeding the server's memory limit.
Rerunning the identical job will be killed again — this is deterministic,
not transient. The fix is to need less memory, not to retry:

- Shrink or split the inputs (e.g. run per-chromosome instead of
  whole-genome, use a smaller reference database).
- Reduce threads, batch size, or output volume via tool parameters.
- On a public server like usegalaxy.org, very large or time-sensitive
  projects are not appropriate — move to a personal/lab/institutional
  Galaxy with sufficient resources. The tool needs the same resources it
  would need on the command line; Galaxy adds no magic.

(`num_threads` warnings from the tool itself, like BLAST+'s "'num_threads'
is currently ignored when 'subject' is specified", are the *tool's* stderr
chatter, not the failure — the `Killed` line is the failure.)

### stderr has the tool's own error text — input or parameter problem

Usage errors, "file not found", format complaints, and assertion messages
from the tool mean Galaxy ran it correctly and the tool rejected the work.
Check: input datatypes, empty or truncated inputs, mutually exclusive
options, reference/input genome builds matching. The tool's documentation
explains the message — Galaxy just relays it.

### Red dataset with empty stderr and empty outputs — silent failure

The tool exited non-zero without saying why, or the wrapper mis-detected
success. Read **Tool Standard Output** and the full command line in Job
Information for clues. For custom tools, check the wrapper XML:
`&lt;command detect_errors="exit_code"&gt;` (or `&lt;stdio&gt;` rules) is what turns a
non-zero exit into the red dataset — a missing error policy can also hide
real failures.

## 3. Rerun once, then stop rerunning

Cluster hiccups are real: start one rerun (the circular-arrow icon on the
dataset) to rule out a transient failure. If the rerun fails identically,
the problem is deterministic — debug it, don't loop reruns. Keep the
original and the rerun in the same history so the comparison is visible.

## 4. Report it so someone can actually help

- Click the bug icon on the red dataset, describe what you expected vs what
  happened, and press **Report**.
- On help.galaxyproject.org, share a link to the history (make it
  accessible) and paste the **Tool Standard Error** text.
- Always include: tool name and version (from the tool form header), the
  stderr text, input sizes, and what you already tried (rerun? smaller
  input?). "It turned red" with no logs gets you asked for the logs.

## Compatibility

- Galaxy (any recent release); job logs available via the history UI and the API.
- Applies to tool runs and workflow steps.

## Variant phrasings

- galaxy red dataset debug failed job
- galaxy job failed read logs
- galaxy tool stderr where to find


---

Source: [Vectle](https://vectle.com/skills/skl_KjuPCn5va6A8U2TkDx0PLQ). Version: `skv_4y8dT8bI0HYkYfVUHgpgFg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
