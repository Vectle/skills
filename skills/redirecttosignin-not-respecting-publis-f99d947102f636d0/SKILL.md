---
name: "redirecttosignin-not-respecting-publis-f99d947102f636d0"
description: "Shows how to fix redirectToSignIn not respecting publishableKey passed to authMiddleware. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_KKg7gbSkBxY_xZ9_2Tlckg"
  title: "RedirectToSignIn not respecting publishableKey passed to authMiddleware"
  version: "skv_NL07r-a9Y44W8ZqdbeEJOQ"
  updated: "2026-10-03T22:29:50.496544+00:00"
  canonical_url: "https://vectle.com/skills/skl_KKg7gbSkBxY_xZ9_2Tlckg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Passing publishableKey explicitly to authMiddleware (custom env var naming) works, but calling redirectToSignIn inside afterAuth throws 'Missing publishableKey'.

## Steps

1. Maintainer brkalow: addressed in recent versions - keys passed to clerkMiddleware() are now respected by the auth methods called inside the middleware handler; see the dynamic-keys docs. Workaround used in the thread: inject the key into process.env.CLERK_PUBLISHABLE_KEY before the middleware runs.

## When to use

You are seeing this: Passing publishableKey explicitly to authMiddleware (custom env var naming) works, but calling redirectToSignIn inside afterAuth throws 'Missing publishableKey'. Use this skill when you run into "RedirectToSignIn not respecting publishableKey passed to authMiddleware".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_KKg7gbSkBxY_xZ9_2Tlckg). Version: `skv_NL07r-a9Y44W8ZqdbeEJOQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
