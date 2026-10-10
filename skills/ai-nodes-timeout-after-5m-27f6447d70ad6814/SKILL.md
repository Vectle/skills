---
name: "ai-nodes-timeout-after-5m-27f6447d70ad6814"
description: "N8n: AI nodes timeout after 5m. The verified fix is Fix: Community patch by Piggeldi2013 worked as a stopgap; on 2.5.0+ set N8N_AI_TIMEOUT_MAX to a higher value instead. Use this when you hit the symptoms above in n8n; not for unrelated n8n errors or general setup questions."
metadata:
  skill_id: "skl_D1OoHQI6fx1vp82hpBK6pQ"
  title: "AI nodes timeout after 5m"
  version: "skv_zR5H0HXU1QBb11GUO5RphA"
  updated: "2026-10-03T04:42:13.846133+00:00"
  canonical_url: "https://vectle.com/skills/skl_D1OoHQI6fx1vp82hpBK6pQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Community patch by Piggeldi2013 worked as a stopgap; on 2.5.0+ set N8N_AI_TIMEOUT_MAX to a higher value instead.

## The error

```text
Issue n8n-io/n8n#11886 (closed, 51 comments): ### Bug Description When using AI nodes with local model, sometimes they take more than 5 mins to respond, which causes fetch to timeout (i looked through the code and past changes, and it seems to be set to 300 seconds aka 5 mins). Because of this, all AI nodes are basically unusuable for anyone with local models. Could this be an env variable so that we can configure it to be whatever we need it to be? This is the error that all AI nodes give when the model takes more than 5 mins to respond: { "name": "HeadersTimeoutError", "code": "UND_ERR_HEADERS_TIMEOUT", "message": "Headers Timeout Error
```

## Fix

1. Community patch by Piggeldi2013 worked as a stopgap; on 2.5.0+ set N8N_AI_TIMEOUT_MAX to a higher value instead.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in n8n.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in n8n, even a similar-looking one.
- General n8n setup or credential questions.

## Compatibility

- N8n (n8n-io/n8n)

## Variant phrasings

- How to fix "AI nodes timeout after 5m" in n8n
- n8n: AI nodes timeout after 5m

## Source

- https://github.com/n8n-io/n8n/issues/11886

---

Source: [Vectle](https://vectle.com/skills/skl_D1OoHQI6fx1vp82hpBK6pQ). Version: `skv_zR5H0HXU1QBb11GUO5RphA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
