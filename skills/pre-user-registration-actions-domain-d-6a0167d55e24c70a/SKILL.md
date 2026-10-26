---
name: "pre-user-registration-actions-domain-d-6a0167d55e24c70a"
description: "The pre-user-registration trigger is where signup policy lives: block bad domains, stamp metadata, or deny the signup entirely before the user record is created. Not the full reference manual."
metadata:
  skill_id: "skl__KuUJNC-6CldNyOlno5ToA"
  title: "Pre-user-registration Actions: domain denylist, metadata, and deny signup"
  version: "skv_sAviUz9a262MIDETSLSvJw"
  updated: "2026-10-03T04:34:35.936052+00:00"
  canonical_url: "https://vectle.com/skills/skl__KuUJNC-6CldNyOlno5ToA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/customize/actions/triggers/pre-user-registration\"]"
---

**TL;DR:** The pre-user-registration trigger is where signup policy lives: block bad domains, stamp metadata, or deny the signup entirely before the user record is created. Not the full reference manual. Deploy and attach Deploy the Action, then attach it in Actions > Flows > Pre User Registration. Test with the flow runner using a blocked and an allowed email.

## The fix

**TL;DR:** The pre-user-registration trigger is where signup policy lives: block bad domains, stamp metadata, or deny the signup entirely before the user record is created. Deploy and attach Deploy the Action, then attach it in Actions > Flows > Pre User Registration. Test with the flow runner using a blocked and an allowed email.

# Pre-user-registration Action

## 1. Create it

Actions > Library > Build Custom > pre-user-registration trigger:

```
exports.onExecutePreUserRegistration = async (event, api) => {
  const blocked = ["tempmail.example", "mailinator.example"];
  const domain = event.user.email.split("@")[1].toLowerCase();
  if (blocked.includes(domain)) {
    api.validation.error("email", "Please sign up with a work email.");
  }
  api.user.setUserMetadata("signup_source", "web");
  api.user.setAppMetadata("tier", "trial");
};
```

## What you can do here

- `api.validation.error(field, message)`: reject the signup with a field-level error shown on Universal Login.
- `api.user.setUserMetadata` / `setAppMetadata`: stamp data on the user before creation. user_metadata is user-editable; app_metadata is admin-only. Put entitlements in app_metadata.
- Read `event.user.email`, `event.connection`, `event.request` for context.

## What you cannot do

- No access tokens exist yet; do not try to set token claims here (that is post-login).
- Heavy network calls slow every signup; keep it fast or move enrichment to post-registration async.

## 2. Deploy and attach

Deploy the Action, then attach it in Actions > Flows > Pre User Registration. Test with the flow runner using a blocked and an allowed email.

## 3. Pair with post-login

Signup policy (this trigger) and login-time enforcement (post-login) are different moments. A domain denylist here plus an app_metadata tier check at login covers both new and existing users.

## Checklist

- Deny messages are human-readable; they render on the signup page.
- Metadata names are consistent with what post-login Actions and your API expect.

## When to use this

- This covers exactly what the title says: Pre-user-registration Actions.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pre-user-registration; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pre-user-registration behavior.

---

Source: [Vectle](https://vectle.com/skills/skl__KuUJNC-6CldNyOlno5ToA). Version: `skv_sAviUz9a262MIDETSLSvJw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
