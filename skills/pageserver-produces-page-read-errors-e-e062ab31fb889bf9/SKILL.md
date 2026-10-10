---
name: "pageserver-produces-page-read-errors-e-e062ab31fb889bf9"
description: "Guide pageserver produces page read errors (`ECANCELED`) (presumably due to SIGTERM): [alexanderlaw (reporter)]: > But note my comment > > Tried 6.14.5 (latest LTS), which has this patch. Doesn't repro. > However, it also doesn't repro on 6.14.5 with this patch reverted. Use this when you hit exactly this in pageserver. Not for different errors or different tools."
metadata:
  skill_id: "skl_N7ux-jvT7MqzMwzz9HSaAQ"
  title: "pageserver produces page read errors (`ECANCELED`) (presumably due to SIGTERM)"
  version: "skv_WqurBWxfEdvuP6QthfsW_w"
  updated: "2026-10-03T14:00:53.849845+00:00"
  canonical_url: "https://vectle.com/skills/skl_N7ux-jvT7MqzMwzz9HSaAQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: [alexanderlaw (reporter)]: > But note my comment > > Tried 6.14.5 (latest LTS), which has this patch. Doesn't repro. > However, it also doesn't repro on 6.14.5 with this patch reverted. > Yes, it corresponds to my find: it looks like the issue was fixed in kernel version 6.13.8. UPD: Sorry, I hadn't looked at the link, thought you referred a commit made for 6.14.5.

## Fix
1. [alexanderlaw (reporter)]: > But note my comment > > Tried 6.14.5 (latest LTS), which has this patch.
   Expected: this specific failure stops.
2. Doesn't repro. > However, it also doesn't repro on 6.14.5 with this patch reverted. > Yes, it corresponds to my find: it looks like the issue was fixed in kernel version 6.13.8.
   Expected: this specific failure stops.
3. UPD: Sorry, I hadn't looked at the link, thought you referred a commit made for 6.14.5.
   Expected: this specific failure stops.
4. Context: GitHub issue neondatabase/neon#11446 (closed, 21 comments): When reproducing "could not ingest record" (YOUR_HOST.com/neondatabase/neon/issues/11427) (I ran 15 instances of test_pageserver_restarts_under_worload[release-pg17] in parallel), besides those errors, I also got another interesting one:.
   Expected: this specific failure stops.

## Details
[alexanderlaw (reporter)]: > But note my comment > > Tried 6.14.5 (latest LTS), which has this patch. Doesn't repro. > However, it also doesn't repro on 6.14.5 with this patch reverted. > Yes, it corresponds to my find: it looks like the issue was fixed in kernel version 6.13.8. UPD: Sorry, I hadn't looked at the link, thought you referred a commit made for 6.14.5. Context: GitHub issue neondatabase/neon#11446 (closed, 21 comments): When reproducing "could not ingest record" (YOUR_HOST.com/neondatabase/neon/issues/11427) (I ran 15 instances of test_pageserver_restarts_under_worload[release-pg17] in parallel), besides those errors, I also got another interesting one: `` ` 9 2025-04-02 15:42:11.256 INFO [utils.py:514] not allowed pageserver_1 error: 2025-04-02T12:41:43.352467Z ERROR page_service_conn_main{peer_addr=the loopback address:50098 application_name=2568761 compute_mode=primary}:process_query{tenant_id=868bb64929f843d98ee2463e3749566c timeline_id=576bfa03d129ba39d0d484b551825c3c}:handle_pagerequests:request:handle_get_pag

## When to use
You hit exactly this: pageserver produces page read errors (`ECANCELED`) (presumably due to SIGTERM) in pageserver.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
pageserver (versions mentioned here: 6.14.5, 6.13.8, 11.256).

---

Source: [Vectle](https://vectle.com/skills/skl_N7ux-jvT7MqzMwzz9HSaAQ). Version: `skv_WqurBWxfEdvuP6QthfsW_w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
