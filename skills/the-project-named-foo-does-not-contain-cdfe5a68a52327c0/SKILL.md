---
name: "the-project-named-foo-does-not-contain-cdfe5a68a52327c0"
description: "Shows how to fix the project named \"Foo does not contain a scheme named \"Bar\" bitrise.io. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_vG-o27M0PU6JOYZzv6wosQ"
  title: "The project named \"Foo does not contain a scheme named \"Bar\" bitrise.io"
  version: "skv_5nEYe_lMquCLVHJD8t1inw"
  updated: "2026-10-04T06:28:53.915526+00:00"
  canonical_url: "https://vectle.com/skills/skl_vG-o27M0PU6JOYZzv6wosQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Based on the Bryan Mussial answer The root cause is that the default behavior of Schemes is to keep schemes 'private' until they are specifically marked as shared.

## Steps

1. Based on the Bryan Mussial answer The root cause is that the default behavior of Schemes is to keep schemes 'private' until they are specifically marked as shared. In the case of a command-line initiated build, the Xcode UI never runs and the xcoderun tool doesn't have its own cache of Schemes to work with. To your schema be visible for command-line build you must mark it as a shared scheme. From the menu bar, select Product &gt; Scheme &gt; Manage Schemes Ensure the 'Shared' box is checked for that scheme A new .xcscheme file has been created in your project at WorkspaceName.xcworkspace/xcshareddata/xcschemes. Commit this file to your repository

## When to use

You are seeing this: To your schema be visible for command-line build you must mark it as a shared scheme. Use this skill when you run into "The project named "Foo does not contain a scheme named "Bar" bitrise.io".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_vG-o27M0PU6JOYZzv6wosQ). Version: `skv_5nEYe_lMquCLVHJD8t1inw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
