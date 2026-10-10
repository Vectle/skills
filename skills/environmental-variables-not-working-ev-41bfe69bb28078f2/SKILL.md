---
name: "environmental-variables-not-working-ev-41bfe69bb28078f2"
description: "Environmental Variables not working even though it is defined in .a local/non-public address file?. In Next.JS, when you add environment variables in your .env.* files whose name don't start with NEXT_PUBLIC_ , they are only available to the Node.Js environment. Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_fEWqSOQAHJJSEqgbKjTppA"
  title: "Environmental Variables not working even though it is defined in .a local/non-public address file?"
  version: "skv_Vc8VPdXZwbZoENmjhOwgBw"
  updated: "2026-10-03T18:21:22.739197+00:00"
  canonical_url: "https://vectle.com/skills/skl_fEWqSOQAHJJSEqgbKjTppA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

In Next.JS, when you add environment variables in your .env.* files whose name don't start with NEXT_PUBLIC_ , they are only available to the Node.Js environment. So you can access them in API Routes and data fetching methods like GetServerSideProps etc.

## Fix

1. In Next.JS, when you add environment variables in your .env.* files whose name don't start with NEXT_PUBLIC_ , they are only available to the Node.Js environment.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are dealing with this situation.
- The symptom matches: Environmental Variables not working even though it is defined in .a local/non-public address file?.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source. Source: https://stackoverflow.com/questions/72754832/environmental-variables-not-working-even-though-it-is-defined-in-env-local-.

## Variant phrasings

### Environmental Variables not working even though it is defined in .a local/non-public address file?

## Why it happens

I have defined my keys in .a local/non-public address but still while calling it process.env.API_KEY it doesn't work as expected. API_KEY [your value] DATABASE_URL=a local/non-public address/db/main Code: export const xata = new BaseClient({ apiKey - process.env.API_KEY, databaseURL: process.env.DATABASE_URL }); Folder Structure: Project - pages - public - .a local/non-public address - helper (file that needs api key)

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/72754832/environmental-variables-not-working-even-though-it-is-defined-in-env-local-file

---

Source: [Vectle](https://vectle.com/skills/skl_fEWqSOQAHJJSEqgbKjTppA). Version: `skv_Vc8VPdXZwbZoENmjhOwgBw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
