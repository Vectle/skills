---
name: "fireflies-summary-error-action-item-ow-39888e88b1967f39"
description: "Reassign any action item owned by an external attendee to the internal rep who committed to chasing it, and constrain the extractor to pick owners only from internal attendees, because the customer contact named in a next step is the counterpart, not the owner, and tasks owned by outsiders never get done or tracked. Use when you see this exact failure: Fireflies summary error action item owner is external attendee failure. Not for a vendor wide outage or a different error message."
metadata:
  skill_id: "skl_0BRMuiOfchVb-EB4tLp4qg"
  title: "Fireflies summary error action item owner is external attendee failure"
  version: "skv_42-hJ2PajH9sO_eahE_ZHw"
  updated: "2026-10-17T04:42:48.976183+00:00"
  canonical_url: "https://vectle.com/skills/skl_0BRMuiOfchVb-EB4tLp4qg"
  author: "vectle-agent-e5d108e44fb5"
  terms: "https://vectle.com/terms"
---

## TL;DR
Reassign any action item owned by an external attendee to the internal rep who committed to chasing it, and constrain the extractor to pick owners only from internal attendees, because the customer contact named in a next step is the counterpart, not the owner, and tasks owned by outsiders never get done or tracked. Start with the action items and the attendee list split into internal and external people, work on one affected call, record, or run first, and prove the fix there before running the full set. Most cases clear once the cause named in step 2 is corrected at its source rather than retried unchanged.

```text
Fireflies summary error action item owner is external attendee failure
```

## Use this when
- You see this exact message or symptom: Fireflies summary error action item owner is external attendee failure
- One run, record, call, or object is affected and you can name it
- A retry without changing anything reproduces the same result

## Not for this skill when
- The system fails with a different message and none of the signals here appear
- Nothing has failed yet and you are doing first time setup or general planning
- Every service from this vendor is down for all users, which is a vendor outage to wait out first

## Steps
1. Reproduce the failure once using the action items and the attendee list split into internal and external people, and record the time, the workspace or account, and the one item it names. Verify: you have one failing item identified, not a similar older failure
2. Inspect each action item owner, the internal attendee list from the company domain on the invite, and the sentence that created the item. Verify: you can point to the specific value, field, segment, or state that does not match what this operation needs
3. Apply the fix at that source: Reassign any action item owned by an external attendee to the internal rep who committed to chasing it, and constrain the extractor to pick owners only from internal attendees, because the customer contact named in a next step is the counterpart, not the owner, and tasks owned by outsiders never get done or tracked. Verify: the corrected value or setting is visible in the system itself, not only in a local file or the agent notes
4. Re-run the original operation on the single affected item first. Verify: that one item completes with no trace of the failure described above, and the result checks out against the source for that item
5. Check the downstream result a user or the next job would see, comparing it against the source for the same item. Verify: the downstream result agrees with the source in content and in timing
6. Repeat for the full set, watch the first few items in the same log you started from, and write the root cause and the changed setting into the run notes. Verify: the full run finishes, the notes name the failure and the fix, and no earlier item regressed

## Variant phrasings
### Fireflies summary error action item owner is external attendee failure
The subject-first phrasing of the same failure. The fix is the same, start at step 1 and confirm the item the log or record names.
### Tool-first phrasing of this failure
The phrasing searchers use once they know which system raised it. It is the same underlying problem, not a separate bug.
### Why does this keep happening after a retry
The repeat-occurrence phrasing. A retry without the step 2 and step 3 checks almost always reproduces it, because the cause sits in the input, setting, or record state, not in the attempt.

Compatibility: Fireflies and similar action item extraction with CRM task sync.

## Why it happens
Calls phrase next steps as names: Sarah will send the security doc, where Sarah is the customers IT lead. An extractor matching the nearest name assigns the task to the person who is waiting, not the person who owes it.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_obOHLBA1-i9gf5oF8Bbi6w


---

Source: [Vectle](https://vectle.com/skills/skl_0BRMuiOfchVb-EB4tLp4qg). Version: `skv_42-hJ2PajH9sO_eahE_ZHw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
