---
name: "loops-event-sent-but-workflow-did-not-3b502bc2027c1344"
description: "Loops: event sent but workflow did not fire - check the event pattern. Also confirm the contact match rule: when both email and userId are present, Loops looks for a contact with either value and updates the other. Use when hitting this exact issue with Loops. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_csfKR6hTmPRa4Mt9kJcXlQ"
  title: "Loops: event sent but workflow did not fire - check the event pattern"
  version: "skv_PQ9g7QDqksyxOG08XRhWSQ"
  updated: "2026-10-03T14:40:29.712103+00:00"
  canonical_url: "https://vectle.com/skills/skl_csfKR6hTmPRa4Mt9kJcXlQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tinkerers-labs/fetchbean-skills/blob/HEAD/skills/fetchbean-loops/SKILL.md\"]"
---

## TL;DR

Also confirm the contact match rule: when both email and userId are present, Loops looks for a contact with either value and updates the other. Check the event pattern exists before sending the event.

## Fix

1. Also confirm the contact match rule: when both email and userId are present, Loops looks for a contact with either value and updates the other.
   Expected: You see the expected output instead of the problem.

## When to use

- You are setting up or using this Loops feature.
- The symptom matches: event sent but workflow did not fire - check the event pattern.

## When NOT to use

- Unrelated Loops issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Loops. Source: https://github.com/tinkerers-labs/fetchbean-skills/blob/HEAD/skills/fetchbean-loops/SKILL.md.

## Variant phrasings

### event sent but workflow did not fire - check the event pattern

## Why it happens

sendEvent returns success but nothing happens downstream. The event pattern the workflow listens for is the usual gap.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/tinkerers-labs/fetchbean-skills/blob/HEAD/skills/fetchbean-loops/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_csfKR6hTmPRa4Mt9kJcXlQ). Version: `skv_PQ9g7QDqksyxOG08XRhWSQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
