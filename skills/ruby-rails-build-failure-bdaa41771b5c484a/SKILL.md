---
name: "ruby-rails-build-failure-bdaa41771b5c484a"
description: "Nixpacks: ruby rails build failure. The verified fix is Fix: Community-resolved: the failure comes from files in the build directory with restrictive permissions (e.g. Use this when you hit the symptoms above in nixpacks; not for unrelated nixpacks errors or general setup questions."
metadata:
  skill_id: "skl_0uEMxyDiXBc240jfH5gO5A"
  title: "Ruby rails build failure"
  version: "skv_HW0LYlOjBOhkITyKHRQ0CA"
  updated: "2026-10-03T05:06:41.532753+00:00"
  canonical_url: "https://vectle.com/skills/skl_0uEMxyDiXBc240jfH5gO5A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Community-resolved: the failure comes from files in the build directory with restrictive permissions (e.g.

## The error

```text
nixpacks build fails with `Error: Writing app. Caused by: Permission denied (os error 13)` while copying app files, e.g. on macOS with Docker Desktop, especially for Ruby/Rails and Node projects.
```

## Fix

1. Community-resolved: the failure comes from files in the build directory with restrictive permissions (e.g.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in nixpacks.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in nixpacks, even a similar-looking one.
- General nixpacks setup or credential questions.

## Compatibility

- Nixpacks (railwayapp/nixpacks)

## Variant phrasings

- How to fix "ruby rails build failure" in nixpacks
- nixpacks: ruby rails build failure
- ruby rails build problem

## Edge cases

- Maintainer iloveitaly noted it's still hard to tell *which* file causes it, especially on macOS without strace.

## Source

- https://github.com/railwayapp/nixpacks/issues/700

---

Source: [Vectle](https://vectle.com/skills/skl_0uEMxyDiXBc240jfH5gO5A). Version: `skv_HW0LYlOjBOhkITyKHRQ0CA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
