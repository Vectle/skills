---
name: "ai-foundry-401-on-the-ai-plane-usually-4f1b1d62ca323e74"
description: "Fix for AI Foundry 401 on the AI plane usually means the Azure AI User role is missing: If the AI-plane API returns 401, check RBAC before anything else: the calling identity needs the Azure AI User role on the project. Re-issuing tokens will not help without the role assignment. Use this when you hit exactly this in AI Foundry. Not for different errors or different tools."
metadata:
  skill_id: "skl_1imLEXHlOvs5IDVuiYb4uw"
  title: "AI Foundry 401 on the AI plane usually means the Azure AI User role is missing"
  version: "skv_QhxvMD0yPo6ccEizSA7jww"
  updated: "2026-10-03T05:08:42.869835+00:00"
  canonical_url: "https://vectle.com/skills/skl_1imLEXHlOvs5IDVuiYb4uw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If the AI-plane API returns 401, check RBAC before anything else: the calling identity needs the Azure AI User role on the project. Re-issuing tokens will not help without the role assignment. For file uploads that fail when you bring your own storage, check the storage account network rules: defaultAction=Deny blocks the upload path, so allow the Foundry service through or scope an exception.

```text
AI Foundry 401 on the AI plane usually means the Azure AI User role is missing
```

## Fix
1. If the AI-plane API returns 401, check RBAC before anything else: the calling identity needs the Azure AI User role on the project.
   Expected: the identity carries the role on the project.
2. For file uploads that fail when you bring your own storage, check the storage account network rules: defaultAction=Deny blocks the upload path, so allow the Foundry service through or scope an exception.
   Expected: this specific failure stops.
3. In APIM metadata, staticModels and modelDiscovery are mutually exclusive, so pick one routing style.
   Expected: this specific failure stops.

## Details
Re-issuing tokens will not help without the role assignment.

## When to use
You hit exactly this: AI Foundry 401 on the AI plane usually means the Azure AI User role is missing in AI Foundry.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
AI Foundry.

## Root cause
Also, when an Assistants API deployment fails, the model name must match the catalog model id exactly; a close-but-different name is treated as missing.

---

Source: [Vectle](https://vectle.com/skills/skl_1imLEXHlOvs5IDVuiYb4uw). Version: `skv_QhxvMD0yPo6ccEizSA7jww`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
