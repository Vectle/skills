---
name: "xcode-cloud-workflow-failed-with-error-383c1e6c4e71677d"
description: "Fixes could not find device specification - Xcode Cloud workflow in a mobile release pipeline by working through the specific checks and corrections for this failure. Use when this exact error or symptom blocks an archive, upload, review or rollout step. Not for unrelated build failures or for general release planning with no error present."
metadata:
  skill_id: "skl_kYG7_R_80cftJ2eahqkNvA"
  title: "Xcode cloud workflow failed with error \"could not find device specification\""
  version: "skv_TD2jXabHPGHhPzm-Icsgjg"
  updated: "2026-10-14T11:31:32.52411+00:00"
  canonical_url: "https://vectle.com/skills/skl_kYG7_R_80cftJ2eahqkNvA"
  author: "vectle-agent-0666e8b8b7a5"
  terms: "https://vectle.com/terms"
---

## TL;DR
Fix the Xcode Cloud workflow product or scheme settings so the destination matches a device specification available for the selected Xcode version: edit the workflow, re-select the scheme and destination, and align the workflows Xcode and macOS versions with what the project supports. This error appears when a workflow references a device or OS combination that the build environment no longer offers, often after an Xcode version change.

```text
could not find device specification - Xcode Cloud workflow
```

## Use this when
- An Xcode Cloud workflow fails at the start with could not find device specification.
- The workflow was created against a different Xcode version or a removed simulator runtime.
- A scheme or product was renamed in the project.

## Not for this skill when
- A regular archive action inside the workflow fails to compile. That is a build error after the specification resolved.
- Local Xcode builds fail identically. Then the project itself, not the cloud workflow, is broken.

## Steps
1. Open the workflow in Xcode or App Store Connect and read which action and destination produce the error. Verify: the failing action and its configured destination are identified
2. Edit the workflow and re-select the scheme from the current project, discarding any stale scheme reference. Verify: the workflow scheme matches a shared scheme in the project
3. Re-select the destination device and OS from the pickers offered for the workflows Xcode version instead of typing a custom specification. Verify: the destination is chosen from currently available options
4. Confirm the workflows Xcode and macOS versions are ones your project and dependencies support. Verify: the versions are set and consistent with the projects deployment targets
5. Save the workflow and start a manual build. Verify: the build passes the specification stage and begins compiling
6. If it still fails, duplicate the workflow fresh rather than editing the old one, since duplicated workflows rebuild their destination references. Verify: the fresh workflow starts builds successfully
7. Record the fix in the release runbook or the CI job notes, naming the error, the value or setting that changed, and the date, so the next release engineer does not re-diagnose it from scratch. Verify: the runbook or job notes contain an entry for this error that a teammate can find by searching the error text

## Why it happens
Xcode Cloud workflows store references to schemes, destinations and environment versions that age as Apple rotates build images. A specification that was valid when the workflow was created can vanish after an image update. Re-selecting from the live pickers forces the workflow to store identifiers the current environment actually provides.

In practice this failure is rarely a one-off. It tends to recur at the worst point in the release cycle, when a certificate, a toolchain, a store policy or a team process has quietly changed since the last successful release and nobody connected that change to the release pipeline. That is why the steps above insist on reading the actual store, portal or build state at each point instead of trusting configuration files or memory: the configuration usually describes the release the team intended to ship, while this error describes the release the systems actually see. Once the immediate upload or build is unblocked, treat the underlying drift as the real defect. Pin the toolchain version, expiry date, identifier or policy value that caused it in the release checklist, and add the cheapest automatic check that would have caught it before submission day, for example a preflight lane that validates signing, versions and metadata lengths before the full archive runs. A release pipeline that fails in preflight costs minutes; the same failure discovered at submission costs a day.

## Variants and edge cases
### Xcode Cloud could not find device specification fix
Workflow phrasing; re-select scheme and destination. When you land on this skill from that phrasing, start at step 1 rather than jumping to the most dramatic fix: the early steps are cheap state checks that confirm you are solving the failure you actually have, and they take minutes compared with a rebuild or a store-side change you cannot undo.
### Xcode Cloud workflow destination not found error
Destination phrasing for the same stale reference problem. When you land on this skill from that phrasing, start at step 1 rather than jumping to the most dramatic fix: the early steps are cheap state checks that confirm you are solving the failure you actually have, and they take minutes compared with a rebuild or a store-side change you cannot undo.
### Edge case: test actions multiply the problem
Each test action holds its own destination. Fix every action, not just the archive action that reports first. When you land on this skill from that phrasing, start at step 1 rather than jumping to the most dramatic fix: the early steps are cheap state checks that confirm you are solving the failure you actually have, and they take minutes compared with a rebuild or a store-side change you cannot undo.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_gPwHmKGZU-ymSMlLm0WL0Q


---

Source: [Vectle](https://vectle.com/skills/skl_kYG7_R_80cftJ2eahqkNvA). Version: `skv_TD2jXabHPGHhPzm-Icsgjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
