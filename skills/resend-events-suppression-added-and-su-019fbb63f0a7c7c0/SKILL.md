---
name: "resend-events-suppression-added-and-su-019fbb63f0a7c7c0"
description: "Resend suppression.added and suppression.removed webhook events: addresses entering or leaving the suppression list after hard bounces, spam complaints, or manual changes. Covers honoring suppression across all systems and the re-adding trap. Not for bounce event handling itself."
metadata:
  skill_id: "skl_UX0qhaPFe5RpZFzt_5T8oQ"
  title: "Resend events: suppression.added and suppression.removed"
  version: "skv_Z8Jfv-ZKT5OnQvp2uDD9HA"
  updated: "2026-10-03T05:08:56.801154+00:00"
  canonical_url: "https://vectle.com/skills/skl_UX0qhaPFe5RpZFzt_5T8oQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://resend.com/docs/webhooks/event-types\",\"https://raw.githubusercontent.com/resend/resend-skills/HEAD/skills/resend/references/webhooks.md\"]"
---

TL;DR: suppression.added fires whenever an email address is added to your suppression list: automatically after a hard bounce or spam complaint, or manually through the dashboard or API. On receipt, stop mailing that address from every system you operate, not just Resend. Record the reason alongside the address: a complaint is a consent signal, a bounce is a data-quality signal. On suppression.removed, confirm the removal was intentional and authorized.

Steps:

1. On suppression.added: stop mailing that address from every system you operate, not just Resend. The cause (bounce or complaint) applies to the address itself. Success: no system still mails it.
2. Record the reason alongside the address. A complaint-driven suppression is a consent signal; a bounce-driven one is a data-quality signal. They need different follow-ups. Success: the reason is stored with the entry.
3. On suppression.removed: confirm the removal was intentional and authorized. An address should only come off suppression because the underlying problem was fixed. Success: the removal has a reason attached.

When to use: handling Resend suppression lifecycle events, or auditing who you must not mail.

When not to use: processing the bounce or complaint events themselves (different events), or building the initial suppression list.

Compatibility: Resend webhooks and suppression lists.

Variants:
- resend suppression list webhook
- suppression.added handler
- resend do not mail list

Root cause of suppression failures: partial compliance. Honoring suppression in Resend while another tool keeps mailing the same address still gets you the complaint, the bounce, and the reputation hit.

Edge cases:
- The trap: re-adding suppressed addresses casually, or letting a list import resurrect them. Suppression is a compliance and reputation control; every removal should be a deliberate decision with a reason attached.

---

Source: [Vectle](https://vectle.com/skills/skl_UX0qhaPFe5RpZFzt_5T8oQ). Version: `skv_Z8Jfv-ZKT5OnQvp2uDD9HA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
