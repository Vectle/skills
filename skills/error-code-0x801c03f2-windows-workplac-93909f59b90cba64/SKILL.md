---
name: "error-code-0x801c03f2-windows-workplac-93909f59b90cba64"
description: "error code 0x801c03f2 windows workplace join failed bug"
metadata:
  skill_id: "skl_mIPTGns-dgTLP_ky-bdETg"
  title: "error code 0x801c03f2 windows workplace join failed bug"
  version: "skv_aXY1EbvXmkCdcVCi3hJjZQ"
  updated: "2026-11-21T01:54:16.06203+00:00"
  canonical_url: "https://vectle.com/skills/skl_mIPTGns-dgTLP_ky-bdETg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

On the affected machine, run the dsregcmd status command from an elevated prompt and save the device state and user state sections.

Note which user attempted the join and whether the device may already exist in the tenant under an old name, a previous owner, or a disabled state.

In the tenant device list, check the record found in step 2 and the per user device limit and registration settings that apply to that user.

Fix the record level blocker first, for example enabling or removing a stale duplicate record through your admin process, or freeing a device slot for that user.

Sign in as the intended user, retry adding the work or school account, then run the dsregcmd status command again.

---

Source: [Vectle](https://vectle.com/skills/skl_mIPTGns-dgTLP_ky-bdETg). Version: `skv_aXY1EbvXmkCdcVCi3hJjZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
