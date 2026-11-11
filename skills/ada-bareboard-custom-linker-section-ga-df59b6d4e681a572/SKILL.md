---
name: "ada-bareboard-custom-linker-section-ga-df59b6d4e681a572"
description: "Ada bareboard custom linker section garbage collected: MSE not bumped, fix with KEEP()"
metadata:
  skill_id: "skl_2WScAjM1KgmXj_C2QNaiBg"
  title: "Ada bareboard custom linker section garbage collected: MSE not bumped, fix with KEEP()"
  version: "skv_NqfB_loVQ-PUKlqKnguJbw"
  updated: "2026-11-11T12:04:19.580155+00:00"
  canonical_url: "https://vectle.com/skills/skl_2WScAjM1KgmXj_C2QNaiBg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the section is really being dropped, not misplaced. Build with a map file (for example -Wl,-Map=map.txt in the linker switches) and look for the custom section in it. Success check: the output section is listed at size 0, or the input section appears under Discarded input sections, which proves garbage collection rather than an address problem.

Open the linker script (in the bareboard case a copy of ld_user/common-ROM.ld) and find the output section you added after .data, the one collecting the custom input section by name. Success check: the input section line is a plain wildcard match with no KEEP() around it, which matches the diagnosis.

Wrap that input section in KEEP() so the linker retains it even though nothing references it. Change the plain wildcard line for the section to the same line wrapped in KEEP, keeping the output section name, address, and any start/end symbols exactly as they were. Success check: the script diff is only the KEEP wrapper on that one line.

Rebuild from clean so the linker script change is actually picked up (a stale object or cached link can hide it). Success check: the build reruns the link step with the edited script.

Check the map file again. Success check: the custom output section now has its real size (4 bytes for a single 4-byte object), it is no longer in the discarded list, and the section end symbol has advanced by that size.

Verify on the board in gdb: print the end symbol again. Success check: MSE now reads 4 bytes higher than the run without the custom object (0x20000838 in the original STM32F429 Disco case instead of 0x20000834), and the custom object reads back its initialised value.

---

Source: [Vectle](https://vectle.com/skills/skl_2WScAjM1KgmXj_C2QNaiBg). Version: `skv_NqfB_loVQ-PUKlqKnguJbw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
