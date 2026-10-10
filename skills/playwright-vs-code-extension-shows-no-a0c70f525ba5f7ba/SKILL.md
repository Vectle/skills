---
name: "playwright-vs-code-extension-shows-no-a0c70f525ba5f7ba"
description: "Shows how to fix playwright VS Code extension shows 'no tests have been found' and connect ETIMEDOUT on the IPv6 loopback. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_E9_kdFcGu1cYw-I1Ijr0JA"
  title: "Playwright VS Code extension shows 'no tests have been found' and connect ETIMEDOUT on the IPv6 loopback"
  version: "skv_FcIaviO5ZYS4N2EQTq0poA"
  updated: "2026-10-03T05:04:10.568369+00:00"
  canonical_url: "https://vectle.com/skills/skl_E9_kdFcGu1cYw-I1Ijr0JA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The Node-side fix shipped in v24.14.0. Multiple users confirmed that upgrading Node.js to v24.15.0 resolves both the ETIMEDOUT error and the missing tests. If you see this combo of symptoms, upgrade Node to v24.15.0 or later.

## When to use

You are seeing this: The extension talks to its language server over the IPv6 loopback, and a Node.js DNS regression broke that path: the c-ares fallback detection did not recognize the loopback address as a loopback DNS server on Windows, so the connection timed out and the... Use this skill when you run into "Playwright VS Code extension shows 'no tests have been found' and connect ETIMEDOUT on the IPv6 loopback".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: v24.14.0, v24.15.0. If you are on something much newer or older, the details may have shifted.

## Steps

1. The extension talks to its language server over the IPv6 loopback, and a Node.js DNS regression broke that path: the c-ares fallback detection did not recognize the loopback address as a loopback DNS server on Windows, so the connection timed out and the extension reported no tests. The Node-side fix shipped in v24.14.0. Multiple users confirmed that upgrading Node.js to v24.15.0 resolves both the ETIMEDOUT error and the missing tests. If you see this combo of symptoms, upgrade Node to v24.15.0 or later.


---

Source: [Vectle](https://vectle.com/skills/skl_E9_kdFcGu1cYw-I1Ijr0JA). Version: `skv_FcIaviO5ZYS4N2EQTq0poA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
