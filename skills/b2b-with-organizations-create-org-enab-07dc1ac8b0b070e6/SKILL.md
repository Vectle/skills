---
name: "b2b-with-organizations-create-org-enab-07dc1ac8b0b070e6"
description: "Organizations give each customer an isolated login context. The setup order matters: org first, then connections on the org, then members, then the app passes the organization on every login. Not the full reference manual."
metadata:
  skill_id: "skl_6mLHRfKSkI5toWrMI2Rinw"
  title: "B2B with Organizations: create org, enable connections, invite members, login hints"
  version: "skv_De4gsqpXSSivNKCIgR9IxQ"
  updated: "2026-10-03T04:41:37.171856+00:00"
  canonical_url: "https://vectle.com/skills/skl_6mLHRfKSkI5toWrMI2Rinw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Organizations give each customer an isolated login context. The setup order matters: org first, then connections on the org, then members, then the app passes the organization on every login. Create the organization Dashboard > Organizations > Create. Use the id in code; names can change.

# Organizations B2B setup

## 1. Create the organization

Dashboard > Organizations > Create. You get an org_id (`org_xxx`) and a name. Use the id in code; names can change.

## 2. Enable connections on the org

Organizations > your org > Connections > Enable Connection. Org logins ONLY offer org-enabled connections; app-level enablement is not enough. Options:

- One database connection per org (isolated user pools), or
- A shared database connection with org membership controlling access, or
- Enterprise connections per customer (their IdP).

Just-in-time membership: on the org connection settings, turn on JIT so users logging in through that connection auto-join the org. This removes most invitation toil.

## 3. Add members

Invite via email (Organizations > Members > Invite) or assign directly. Invitations expire in 7 days and are bound to the invited email. For bulk onboarding prefer JIT.

## 4. Log in with the org context

Every authorize call must pass the organization:

```
authorizationParams: { organization: "org_xxx" }
```

Without it, the user logs in outside the org context: no org roles, no org claims, and org-required apps fail. Silent auth calls need it too.

For multi-tenant callback URLs, use the `{organization_name}` placeholder in Allowed Callback URLs on domains you control.

## 5. Tokens

The access token carries an `org_id` claim. Org roles land in the token when RBAC is on and the login had org context. Your API should check `org_id` against the tenant being accessed.

## Checklist

- Connection enabled on the org, not just the app.
- organization passed on login, silent auth, and invite acceptance.
- API authorizes on org_id, not just user identity.

## When to use this

- This covers exactly what the title says: B2B with Organizations.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with B2B; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current B2B behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_6mLHRfKSkI5toWrMI2Rinw). Version: `skv_De4gsqpXSSivNKCIgR9IxQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
