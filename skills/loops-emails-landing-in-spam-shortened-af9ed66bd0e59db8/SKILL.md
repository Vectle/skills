---
name: "loops-emails-landing-in-spam-shortened-af9ed66bd0e59db8"
description: "Loops: emails landing in spam - shortened links and domain setup. Avoid shortened youtu.be links: Gmail flags click-tracked short links as phishing (Loops Guardian warns on these); use the full youtube.com URL or disable tracking on the link. Use when hitting this exact issue with Loops. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_m-nMXCHJLHQXix3gbluKZg"
  title: "Loops: emails landing in spam - shortened links and domain setup"
  version: "skv_9GlHAcdkfkmHlVHxFcwAKQ"
  updated: "2026-10-03T14:43:19.589533+00:00"
  canonical_url: "https://vectle.com/skills/skl_m-nMXCHJLHQXix3gbluKZg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/loops-so/skills/blob/HEAD/skills/loops-email-sending-best-practices/references/deliverability.md\"]"
---

## TL;DR

Avoid shortened youtu.be links: Gmail flags click-tracked short links as phishing (Loops Guardian warns on these); use the full youtube.com URL or disable tracking on the link. For new or weak domains, start with new signups and recently active users instead of blasting a cold audience, and verify the domain records on the sending-domain page in Loops before deeper troubleshooting. Send from a subdomain so the root-domain reputation stays safe.

## Fix

1. Avoid shortened youtu.be links: Gmail flags click-tracked short links as phishing (Loops Guardian warns on these); use the full youtube.com URL or disable tracking on the link.
   Expected: You get the expected result; the problem is gone.
2. For new or weak domains, start with new signups and recently active users instead of blasting a cold audience, and verify the domain records on the sending-domain page in Loops before deeper troubleshooting.
   Expected: You see the expected output instead of the problem.
3. Loops recommends one sending domain per team; Gmail spam reports are not surfaced in Loops, so set up Google Postmaster for Gmail-specific reputation insight.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Loops feature.
- The symptom matches: emails landing in spam - shortened links and domain setup.

## When NOT to use

- Unrelated Loops issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Loops. Source: https://github.com/loops-so/skills/blob/HEAD/skills/loops-email-sending-best-practices/references/deliverability.md.

## Variant phrasings

### emails landing in spam - shortened links and domain setup

## Why it happens

Loops emails go to spam or trigger deliverability guardrails. Loops documents the copy and setup mistakes that hurt deliverability.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/loops-so/skills/blob/HEAD/skills/loops-email-sending-best-practices/references/deliverability.md

---

Source: [Vectle](https://vectle.com/skills/skl_m-nMXCHJLHQXix3gbluKZg). Version: `skv_9GlHAcdkfkmHlVHxFcwAKQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
