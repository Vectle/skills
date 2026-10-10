---
name: "buddy-debugging-a-failed-execution-rea-b0b0f598491bdc41"
description: "Buddy: debugging a failed execution - read failed action logs before retrying. the order is buddy executions failed for the failed action logs, then buddy executions show with the logs flag for all actions (the verbose flag surfaces errors from skipped actions), then failed with the analyze flag for error pattern analysis. Use when hitting this exact issue with Buddy. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_hkf9-NSX9qUMK4v7nhL_Sg"
  title: "Buddy: debugging a failed execution - read failed action logs before retrying"
  version: "skv_unjf5NIk1znN-iiGcBI3rg"
  updated: "2026-10-03T16:18:23.307553+00:00"
  canonical_url: "https://vectle.com/skills/skl_hkf9-NSX9qUMK4v7nhL_Sg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

The order is buddy executions failed for the failed action logs, then buddy executions show with the logs flag for all actions (the verbose flag surfaces errors from skipped actions), then failed with the analyze flag for error pattern analysis. URL execution IDs are hex hashes and the CLI resolves them automatically. For targeted debugging, use executions actions to find the specific action's hex ID, then action-logs to fetch just that one action, which is faster than pulling all logs sequentially.

## The error

```text
debugging a failed execution - read failed action logs before retrying
```

## Fix

1. The order is buddy executions failed for the failed action logs, then buddy executions show with the logs flag for all actions (the verbose flag surfaces errors from skipped actions), then failed with the analyze flag for error pattern analysis.
   Expected: You get the expected result; the problem is gone.
2. URL execution IDs are hex hashes and the CLI resolves them automatically.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Buddy.
- The symptom matches: debugging a failed execution - read failed action logs before retrying.

## When NOT to use

- A different error message from Buddy; the cause here is specific to this error.
- Unrelated Buddy issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Buddy. Source: https://github.com/jtsternberg/buddy-cli/blob/HEAD/claude-plugin/skills/troubleshooting-pipelines/SKILL.md.

## Variant phrasings

### debugging a failed execution - read failed action logs before retrying

## Why it happens

The fastest Buddy debugging loop reads the failed action's own logs first, then the full log, then analyzes the error pattern. Never guess before reading logs.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/jtsternberg/buddy-cli/blob/HEAD/claude-plugin/skills/troubleshooting-pipelines/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_hkf9-NSX9qUMK4v7nhL_Sg). Version: `skv_unjf5NIk1znN-iiGcBI3rg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
