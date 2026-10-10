---
name: "replit-agent-diagnose-before-fixing-lo-bbfa2855189ee3ad"
description: "Replit Agent rewrites working code because the prompt let it. Use when hitting this exact issue with Replit Agent. Not for unrelated errors."
metadata:
  skill_id: "skl_ZWKY-B95j328wUCBkhtvWg"
  title: "Replit Agent: diagnose before fixing, lock working files every prompt"
  version: "skv_IuhC9xNSYh_lQEWRKseTsQ"
  updated: "2026-10-04T08:39:21.86015+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZWKY-B95j328wUCBkhtvWg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Two prompts fix most of it. Diagnose before fixing. Replit Agent rewrites working code because the prompt let it.

[real practitioner pattern]: Replit Agent rewrites working code because the prompt let it. Two prompts fix most of it. 1. Diagnose before fixing. Give expected vs actual, the FULL error (no paraphrasing), the last known working checkpoint, and what changed since. Instruct it to trace the root cause, report the diagnosis, and WAIT. Only confirm, then the minimal fix. Do NOT let it refactor unrelated code, install packages, or change architecture along the way. 2. Lock what works on every follow-up. Around ten messages in, your original rules have fallen out of its working memory. Every prompt restates: the original goal, decisions already made, the locked files and behaviors, and exactly one requested change. Then ask which files it modified and confirm the locked ones are untouched. Rule of thumb: one kind of change per prompt. Vague prompts get speculative fixes that treat symptoms and quietly rewrite three files.

Context: Web, PocketStudio on Medium (Sep 2026): how to stop Replit Agent and Lovable from nuking working code, 5 copy-paste prompts. The key patterns: diagnose before you fix (give expected vs actual, the full error, last known working checkpoint, what changed; the agent must report the diagnosis and WAIT before touching code). Lock what works on every follow-up: around ten messages in, the original rules fall out of working memory, so every prompt restates the goal, decisions to keep, locked files/behaviors, and exactly one requested change. One kind of change per prompt: never mix spacing fixes with data-layer restructures.

## When to use

- You hit this exact issue with Replit Agent.
- The symptom matches: diagnose before fixing, lock working files every prompt.

## When NOT to use

- A different error or symptom from Replit Agent; the cause here is specific to this one.

## Compatibility

Reported against Replit Agent.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_ZWKY-B95j328wUCBkhtvWg). Version: `skv_IuhC9xNSYh_lQEWRKseTsQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
