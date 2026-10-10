---
name: "how-to-find-which-group-membership-gra-3f0dee5a1a37c529"
description: "Traces which AD or Entra group gives a user access to an application. Covers token groups, app assignment, and nested group expansion. Use when access works but nobody knows why, or to audit access paths. Not for fixing denied access (check assignment first)."
metadata:
  skill_id: "skl_lmJUntrLoNfnOsrDlU4VHQ"
  title: "how to find which group membership grants app access"
  version: "skv_Y97F6kmY6Bn6l_-S611QHw"
  updated: "2026-10-04T14:03:02.185298+00:00"
  canonical_url: "https://vectle.com/skills/skl_lmJUntrLoNfnOsrDlU4VHQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR
Check the app's assignment in the IdP admin console first (Okta app assignments or Entra enterprise app users and groups). Then expand nested groups to confirm the membership path. For AD-native apps, check the user's tokenGroups to see the effective group list.

## The error
```text
(Audit or troubleshooting question; no error. "Why does this user have access?")
```

## Steps
1. In the IdP, open the app > Assignments (Okta) or Users and groups (Entra enterprise app). Expected: the granting group is listed. This answers the question in most cases.
2. If the assignment is a group, expand it: check the group's members and any nested groups. Expected: the membership chain user > nested group > assigned group is visible.
3. For AD-native apps (file shares, legacy SSO), check the user's effective groups: PowerShell `whoami /groups` as the user, or check the tokenGroups attribute. Expected: full group list including nested.
4. Watch for "Authenticated Users" or "Domain Users" assignments. Expected: noted if present. These grant access to everyone and explain mystery access instantly.
5. Document the path in the ticket: app > assigned group > nested groups > user. Expected: clear chain. This is what auditors want to see.

## When to use
- Auditing why a user has access
- Cleaning up access before offboarding
- Troubleshooting unexpected access

## When not to use
- Access denied errors (check assignment and licensing first)
- Real-time provisioning issues

## Compatibility
- Okta, Entra ID, and Active Directory; PowerShell ActiveDirectory module for AD checks

## Variants
### Access via multiple paths
Users often have access through two groups. Remove one and test before removing both.
### Dynamic groups in Entra
Membership is rule-based; check the rule, not a static member list.

## Why it happens
Access flows through assignments, and assignments usually point at groups, which nest. Nobody memorizes the nesting, so the path has to be traced each time.

## Edge cases
- Group nesting loops are prevented by AD, but deep nesting (5+ levels) is common in old domains.
- Privileged groups: finding Domain Admins nested inside an app group is a finding, not just an answer.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_H16D_D7jshVUuCRiwdgbaA


---

Source: [Vectle](https://vectle.com/skills/skl_lmJUntrLoNfnOsrDlU4VHQ). Version: `skv_Y97F6kmY6Bn6l_-S611QHw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
