---
name: "loops-contact-not-receiving-email-chec-7f9cfeb5e8bc7239"
description: "Loops: contact not receiving email - check suppression and variable fallbacks first. first, check whether the contact is suppressed: a suppressed contact silently receives nothing, and suppression is the most common reason a contact stops getting mail. Use when hitting this exact issue with Loops. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_ypPoBDlA2iiv_EtHsHBRCw"
  title: "Loops: contact not receiving email - check suppression and variable fallbacks first"
  version: "skv_VDOjpALSrJof4gSnNN3F3w"
  updated: "2026-10-03T14:41:55.750698+00:00"
  canonical_url: "https://vectle.com/skills/skl_ypPoBDlA2iiv_EtHsHBRCw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

First, check whether the contact is suppressed: a suppressed contact silently receives nothing, and suppression is the most common reason a contact stops getting mail.

## Fix

1. First, check whether the contact is suppressed: a suppressed contact silently receives nothing, and suppression is the most common reason a contact stops getting mail.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this Loops feature.
- The symptom matches: contact not receiving email - check suppression and variable fallbacks first.

## When NOT to use

- Unrelated Loops issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Loops. Source: https://github.com/tinkerers-labs/fetchbean-skills/blob/HEAD/skills/fetchbean-loops/SKILL.md.

## Variant phrasings

### contact not receiving email - check suppression and variable fallbacks first

## Why it happens

Two silent failure modes in Loops make emails vanish with no error. Both are cheap to check before debugging anything else.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/tinkerers-labs/fetchbean-skills/blob/HEAD/skills/fetchbean-loops/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_ypPoBDlA2iiv_EtHsHBRCw). Version: `skv_VDOjpALSrJof4gSnNN3F3w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
