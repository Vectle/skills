---
name: "fix-pxc-operator-reconcile-loop-error-ff724e3761596f1e"
description: "Fix PXC operator reconcile loop: Error 4006 CREATE USER failed for a view definer account"
metadata:
  skill_id: "skl_uL2vn4yWMDOG-b6BiK1TdA"
  title: "Fix PXC operator reconcile loop: Error 4006 CREATE USER failed for a view definer account"
  version: "skv_oE4gbaOMeVI4yphIrgS0NA"
  updated: "2026-10-29T10:57:41.79533+00:00"
  canonical_url: "https://vectle.com/skills/skl_uL2vn4yWMDOG-b6BiK1TdA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the loop signature in the operator log. Look for the grant check reporting the ALL grant as not present, followed by the Error 4006 line above, repeating every few seconds (the reported case looped about 300 times in 30 minutes). Success check: the same pair of lines repeats on every reconcile instead of appearing once.

Check what the custom user actually holds. Run SHOW GRANTS for the user named in spec.users. Success check: the output is an explicit privilege list per schema with no ALL PRIVILEGES line, even though spec.users requests grants [ALL].

Apply the workaround grant from an account that has the GRANT OPTION on those schemas. For each database listed for that user in spec.users, run: GRANT ALL ON app_db1.* TO the custom user account (repeat per schema, for example app_db2). Success check: SHOW GRANTS now returns ALL PRIVILEGES for each schema.

Watch the next reconcile cycles. Success check: the operator stops re-running the upsert, the repeated CREATE DATABASE IF NOT EXISTS statements stop, wsrep_local_cert_failures stops climbing, and application transactions stop failing at COMMIT with deadlock errors.

Make the fix durable. Either keep the account grants aligned with the ALL entry in spec.users, or trim the spec grants down to the explicit list the account already holds so the grant comparison stays false. Success check: a later operator restart or upgrade does not restart the loop.

---

Source: [Vectle](https://vectle.com/skills/skl_uL2vn4yWMDOG-b6BiK1TdA). Version: `skv_oE4gbaOMeVI4yphIrgS0NA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
