---
name: "opensearch-no-permissions-for-indices-befcac72d35528a5"
description: "OpenSearch No permissions for [indices:data/read/msearch] and [indices:data/read/scroll]: add the missing..."
metadata:
  skill_id: "skl_hM9UZ4KlNZ9qGYhqq80Oyw"
  title: "OpenSearch No permissions for [indices:data/read/msearch] and [indices:data/read/scroll]: add the missing..."
  version: "skv_UgBh91ay_VAgA7IIgUBQSA"
  updated: "2026-11-09T12:05:44.966262+00:00"
  canonical_url: "https://vectle.com/skills/skl_hM9UZ4KlNZ9qGYhqq80Oyw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Read the error literally first. The bracketed action in the error is the exact permission that is missing, and the RolesChecked list names the roles the security plugin actually evaluated for that user. Success check: you can name the missing action and the evaluated role for each failing call, instead of guessing at the whole config.

Open the role definition (roles.yml, or Dashboards under Security then Roles) for the evaluated role, for example the Dst-Query role behind the msearch failure and the OSS-DDC role behind the scroll failure. Look at its allowed_actions on the index pattern the call targets (jaeger-span-* in the original msearch case). Success check: the list contains the plain search action and neither of the two failing actions, which confirms the diagnosis before you change anything.

Add the missing action to that same entry, alongside the existing search action: the msearch action for the role serving multi-search calls, and the scroll action for the role serving scroll calls. If one role serves both call types, it needs both actions. Keep the index patterns and cluster permissions exactly as they were. Success check: the role diff is only the added action lines, nothing else moved.

Re-apply the security configuration so the running cluster picks the change up: push the updated config with securityadmin, or save the role edit in Dashboards and confirm it saved. Success check: reading the role back from the cluster (not just the file) shows the new action in allowed_actions.

Re-run the exact call that failed, as the same user. Success check: the msearch or scroll request returns results instead of the no permissions error; if a different action is named in a new error, repeat step 1 for that action rather than broadening the role blindly.

Only if the error names a role you did not expect, check the role mapping next: the user is evaluated through the roles listed in RolesChecked, so confirm in roles_mapping that the user or its backend roles actually map to the role you just edited. Success check: RolesChecked in any remaining error includes the edited role.

---

Source: [Vectle](https://vectle.com/skills/skl_hM9UZ4KlNZ9qGYhqq80Oyw). Version: `skv_UgBh91ay_VAgA7IIgUBQSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
