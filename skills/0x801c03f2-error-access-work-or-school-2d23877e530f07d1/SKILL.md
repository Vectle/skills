---
name: "0x801c03f2-error-access-work-or-school-2d23877e530f07d1"
description: "0x801c03f2 error access work or school device registration fails how to fix"
metadata:
  skill_id: "skl_gsyGPqTePmkwZpySc302hA"
  title: "0x801c03f2 error access work or school device registration fails how to fix"
  version: "skv_AUAuJF-Y037ofq2ttsHndw"
  updated: "2026-11-11T13:53:56.3689+00:00"
  canonical_url: "https://vectle.com/skills/skl_gsyGPqTePmkwZpySc302hA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open an elevated command prompt, run the dsregcmd status command, and read the Device State section first.

Read the User State and SSO State sections and note any errors named there, especially a missing Ngc key or a Workplace Join failure.

In the Entra admin center, check the device registration settings for the user: whether users may join or register devices, and the maximum number of devices per user.

If dsregcmd shows a stale or partial join, run the dsregcmd leave command as administrator, restart the device, and confirm the status is clean before retrying.

Retry Settings, Accounts, Access work or school, Connect, signing in with the work account, on an open network first if the office network filters Microsoft endpoints.

---

Source: [Vectle](https://vectle.com/skills/skl_gsyGPqTePmkwZpySc302hA). Version: `skv_AUAuJF-Y037ofq2ttsHndw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
