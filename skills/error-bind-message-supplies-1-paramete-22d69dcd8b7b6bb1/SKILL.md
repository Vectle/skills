---
name: "error-bind-message-supplies-1-paramete-22d69dcd8b7b6bb1"
description: "Serverless: error: bind message supplies 1 parameters, but prepared statement \"\" requires 0. The verified fix is Fix: [jawj (maintainer)]: Fixed in driver 0.4.23. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl_MpobzEgRlo9NlVb6WCN-Ig"
  title: "Error: bind message supplies 1 parameters, but prepared statement \"\" requires 0"
  version: "skv_Xi-RniRyxmLoUL_5pqpMSA"
  updated: "2026-10-03T05:08:29.668728+00:00"
  canonical_url: "https://vectle.com/skills/skl_MpobzEgRlo9NlVb6WCN-Ig"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: [jawj (maintainer)]: Fixed in driver 0.4.23.

## The error

```text
Adding one or more parameters to the query cause the error: `NeonDbError: db error: ERROR: bind message supplies 1 parameters, but prepared statement "" requires 0` when `neonConfig.poolQueryViaFetch = true`
```

## Fix

1. [jawj (maintainer)]: Fixed in driver 0.4.23.

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

- How to fix "error: bind message supplies 1 parameters, but prepared statement "" requires 0" in serverless
- serverless: error: bind message supplies 1 parameters, but prepared statement "" requires 0
- problem: bind message supplies 1 parameters, but prepared statement "" requires 0

## Source

- https://github.com/neondatabase/serverless/issues/28

---

Source: [Vectle](https://vectle.com/skills/skl_MpobzEgRlo9NlVb6WCN-Ig). Version: `skv_Xi-RniRyxmLoUL_5pqpMSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
