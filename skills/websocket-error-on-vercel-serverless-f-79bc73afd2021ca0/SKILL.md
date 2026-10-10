---
name: "websocket-error-on-vercel-serverless-f-79bc73afd2021ca0"
description: "Serverless: websocket error on Vercel Serverless Function. The verified fix is Fix: [jawj (maintainer)]: On Vercel's non-Edge serverless functions the WebSocket transport may fail to open; in that environment just use ordinary node-postgres (`pg`) instead of the serverless driver. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl___TVCCNjybydk6dyYYK6Yg"
  title: "Websocket error on Vercel Serverless Function"
  version: "skv_vyNM5uKJhRl9I-dnwNpUxg"
  updated: "2026-10-03T05:38:06.90776+00:00"
  canonical_url: "https://vectle.com/skills/skl___TVCCNjybydk6dyYYK6Yg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: [jawj (maintainer)]: On Vercel's non-Edge serverless functions the WebSocket transport may fail to open; in that environment just use ordinary node-postgres (`pg`) instead of the serverless driver. On Edge functions the driver works (no need to set webSocketConstructor there).

## The error

```text
I'm getting the following error when using this on vercel
```

## Fix

1. [jawj (maintainer)]: On Vercel's non-Edge serverless functions the WebSocket transport may fail to open; in that environment just use ordinary node-postgres (`pg`) instead of the serverless driver.
2. On Edge functions the driver works (no need to set webSocketConstructor there).

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in serverless.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in serverless, even a similar-looking one.
- General serverless setup or credential questions.

## Compatibility

- Serverless (neondatabase/serverless)

## Variant phrasings

- How to fix "websocket error on Vercel Serverless Function" in serverless
- serverless: websocket error on Vercel Serverless Function
- websocket problem on Vercel Serverless Function

## Source

- https://github.com/neondatabase/serverless/issues/15

---

Source: [Vectle](https://vectle.com/skills/skl___TVCCNjybydk6dyYYK6Yg). Version: `skv_vyNM5uKJhRl9I-dnwNpUxg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
