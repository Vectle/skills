---
name: "issue-with-configuring-hugging-face-cr-325516cb95fb2442"
description: "N8n: issue with configuring Hugging Face credentials for local n8n. The verified fix is Fixed via PR #18047 after the langchain upgrade merged - member janober confirmed 'Fix got released with n8n@1.107.0'. Use this when you hit the symptoms above in n8n; not for unrelated n8n errors or general setup questions."
metadata:
  skill_id: "skl_RRoqR9YrJpzCSEXPz_oebQ"
  title: "Issue with configuring Hugging Face credentials for local n8n"
  version: "skv_UHgyWcK_90ZqhXz0DbWsCA"
  updated: "2026-10-03T04:39:17.667099+00:00"
  canonical_url: "https://vectle.com/skills/skl_RRoqR9YrJpzCSEXPz_oebQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/n8n-io/n8n/issues/15246\"]"
---

## TL;DR

Fixed via PR #18047 after the langchain upgrade merged - member janober confirmed 'Fix got released with n8n@1.107.0'. Upgrade to 1.107.0+ and re-save the Hugging Face credential.

## The error

```text
Issue n8n-io/n8n#15246 (closed, 38 comments): ### Bug Description Hi there, I’m trying to use a Hugging Face model in n8n, but I’m unable to set up the credentials successfully. I obtained my Hugging Face token (which begins with hf_) and pasted it into the API Key field under Hugging Face credentials in n8n. However, when I save it, I receive the error message: “Couldn’t connect with these settings. More details.” Even after clicking the “Retry” button, the same error persists. I found that others have encountered the same issue when using n8n locally. However, I’m not sure if it’s caused by running n8n on YOUR_HOST. I’ve tried updating
```

## Fix

1. Fixed via PR #18047 after the langchain upgrade merged - member janober confirmed 'Fix got released with n8n@1.107.0'.
2. Upgrade to 1.107.0+ and re-save the Hugging Face credential.

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

- How to fix "issue with configuring Hugging Face credentials for local n8n" in n8n
- n8n: issue with configuring Hugging Face credentials for local n8n

## Root cause

Hugging Face credential test failing on local n8n: root cause per contributor schrothbn was that HuggingFace updated their API/SDK and the bundled LangChain version lagged behind.

## Source

- https://github.com/n8n-io/n8n/issues/15246

---

Source: [Vectle](https://vectle.com/skills/skl_RRoqR9YrJpzCSEXPz_oebQ). Version: `skv_UHgyWcK_90ZqhXz0DbWsCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
