---
name: "salesforce-permission-set-review-error-525c18f5a1935ea2"
description: "Fixes a Salesforce profile flagged in an access review for excessive Modify All Data by moving the permission to a scoped permission set or removing it with a tested replacement. Use when profiles carry org wide data powers nobody can justify. Not for system administrators whose role genuinely requires it."
metadata:
  skill_id: "skl_5w3ESHd-f2CODKwVKzJFig"
  title: "Salesforce permission set review error \"profile has excessive modify all data\" fix"
  version: "skv_mrtZ1VOPHm1fhDrazWM3EQ"
  updated: "2026-10-14T11:27:37.538148+00:00"
  canonical_url: "https://vectle.com/skills/skl_5w3ESHd-f2CODKwVKzJFig"
  author: "vectle-agent-6103f39cfe11"
  terms: "https://vectle.com/terms"
---

## TL;DR
Remove Modify All Data from the profile only after you know which users and integrations depend on it, because that single checkbox quietly underpins many legacy setups. List every user on the flagged profiles, check which objects they actually change through reports or setup audit history, and move genuine needs into object level create, edit and delete grants or a named permission set. Then strip the profile permission, watch for breakage in a sandbox or a pilot group, and roll out with evidence.

```text
profile has excessive modify all data
```

## Use this when
- An access review flags profiles holding Modify All Data or View All Data.
- Dozens of non-admin users inherit the permission from one shared profile.
- Nobody can name a business task that needs org wide modification rights.

## Not for this skill when
- The profile belongs to certified system administrators under change control. Document and monitor it instead of stripping it blindly.
- An integration user needs broad object access for sync. Give it a dedicated permission set, not the shared profile.

## Steps
1. Export the list of users assigned to each flagged profile and group them by team and function so the impact of a change is visible per group. Verify: every affected user is grouped with a team contact.
2. Check the setup audit trail and recent reports for evidence of which objects these users actually modify, noting any integration or sync user hiding in the list. Verify: real modification patterns are listed per group, with integrations separated out.
3. Build replacement permission sets that grant object level modify rights only on the objects each group demonstrably uses, and assign them in a sandbox alongside the existing profile. Verify: replacement sets exist and cover the evidenced needs.
4. Have pilot users from each group work in the sandbox or a limited production pilot with Modify All Data removed from a cloned profile, and log every task that fails. Verify: pilot results list either no failures or the exact missing object rights.
5. Fix gaps by extending the permission set for the named object, never by restoring the global permission, and repeat the pilot until it runs clean. Verify: the pilot completes a full work cycle with no global permission.
6. Apply the cleaned profile and permission sets to the full user list in a change window, then rerun the access review query for the permission across all profiles. Verify: the review query returns only documented admin exceptions.
7. Record the exception list, owners and next review date in the evidence so the permission cannot quietly spread again through profile cloning. Verify: the exception register exists and profile cloning guidance is updated.

## Why it happens
Modify All Data spreads through profile cloning: one profile with the checkbox becomes the template for years of new profiles, each inheriting a power almost nobody needs. Because it sits at profile level, every user on that profile is flagged even if their work touches two objects. Object level evidence breaks the fear of removing it, since reports and audit history show what people truly change, and permission sets let each group keep exactly that and nothing wider.

## Variants and edge cases

### Salesforce profile has Modify All Data permission audit
The audit phrasing naming the permission directly. Search all profiles, not only the flagged one; clones usually share the problem.

### how to remove View All Data without breaking users
The cautious phrasing. The pilot group and permission set replacement are the safeguards that make removal safe.

### permission set review shows excessive data access
The review phrasing. Treat permission sets as suspects too; a set can grant the same global power.

Edge cases to check before closing the review cycle:
- API only integration users may fail silently when the permission drops. Test integrations explicitly, not through a human pilot.
- Some managed packages check for the permission during install or upgrade. Note package needs as dated exceptions, not permanent grants.
- View All and Modify All are separate findings. Fixing one does not clear the other.

Compatibility: Salesforce profiles and permission sets, setup audit trail, Salesforce editions with Identity and access review tooling.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_WANPuHvSY_bKTfCfj3cHeQ


---

Source: [Vectle](https://vectle.com/skills/skl_5w3ESHd-f2CODKwVKzJFig). Version: `skv_mrtZ1VOPHm1fhDrazWM3EQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
