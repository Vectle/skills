---
name: "how-to-get-the-azure-account-tenant-id-51102f1dc12839e7"
description: "Walks through get the azure account tenant Id?, step by step. Use it when you need to do exactly this. Not a troubleshooting guide, so skip it if you are here because of an error."
metadata:
  skill_id: "skl_jYigxRDnrJi3KnJrnpdfgg"
  title: "How to get the azure account tenant Id?"
  version: "skv_TAtd6_wE0h24j4HI3eQSpA"
  updated: "2026-10-04T07:36:29.847255+00:00"
  canonical_url: "https://vectle.com/skills/skl_jYigxRDnrJi3KnJrnpdfgg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/26384034\"]"
---

## TL;DR

[Kevin R. (top answer)] Time changes everything. I was looking to do the same recently and came up with this: Note added 02/17/2021 Stable Portal Page thanks Palec added 12/18/2017 As indicated by shadowbq, the DirectoryId and TenantId both equate to the GUID representing the ActiveDirectory Tenant.

## Steps

1. [Kevin R. (top answer)] Time changes everything. I was looking to do the same recently and came up with this: Note added 02/17/2021 Stable Portal Page thanks Palec added 12/18/2017 As indicated by shadowbq, the DirectoryId and TenantId both equate to the GUID representing the ActiveDirectory Tenant. Depending on context, either term may be used by Microsoft documentation and products, which can be confusing. Assumptions - You have access to the Azure Portal Solution The tenant ID is tied to ActiveDirectoy in Azure - Navigate to Dashboard - Navigate to ActiveDirectory - Navigate to Manage / Properties - Copy the "Directory ID" Azure ActiveDirectory Tenant ID:

## When to use

You are seeing this: Depending on context, either term may be used by Microsoft documentation and products, which can be confusing. Use this skill when you run into "How to get the azure account tenant Id?".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_jYigxRDnrJi3KnJrnpdfgg). Version: `skv_TAtd6_wE0h24j4HI3eQSpA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
