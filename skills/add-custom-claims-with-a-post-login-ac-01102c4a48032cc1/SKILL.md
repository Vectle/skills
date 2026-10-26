---
name: "add-custom-claims-with-a-post-login-ac-01102c4a48032cc1"
description: "Custom claims need a namespaced name, the right token target, and three steps people skip: deploy the Action, attach it to the login flow, and test with a fresh login. Not the full reference manual."
metadata:
  skill_id: "skl_OiAs34eraTjy9c2StzsqvA"
  title: "Add custom claims with a post-login Action: namespace, setCustomClaim, deploy"
  version: "skv_lxAm8iT7YjFlACA5V4YSzw"
  updated: "2026-10-03T05:09:51.234291+00:00"
  canonical_url: "https://vectle.com/skills/skl_OiAs34eraTjy9c2StzsqvA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/customize/actions/triggers/post-login\"]"
---

**TL;DR:** Custom claims need a namespaced name, the right token target, and three steps people skip: deploy the Action, attach it to the login flow, and test with a fresh login. Write the Action Dashboard > Actions > Library > Build Custom > post-login trigger: Rules that matter: - Namespaced names only. Add it under the Action's Secrets (never hardcode).

# Custom claims via post-login Action

## 1. Write the Action

Dashboard > Actions > Library > Build Custom > post-login trigger:

```
exports.onExecutePostLogin = async (event, api) => {
  const namespace = "https://YOUR-DOMAIN";
  if (event.authorization) {
    api.idToken.setCustomClaim(namespace + "/roles", event.authorization.roles);
    api.accessToken.setCustomClaim(namespace + "/roles", event.authorization.roles);
  }
};
```

Rules that matter:

- Namespaced names only. Auth0 drops non-namespaced custom claims silently. `https://YOUR-DOMAIN/roles` works; `roles` does not.
- The event object is read-only. Assigning to `event.user` does nothing; all writes go through `api`.
- idToken claims and accessToken claims are separate calls. Setting one does not set the other.

## 2. Secrets and dependencies

Need an API key inside the Action? Add it under the Action's Secrets (never hardcode). Need an npm package? Add it in the Action's dependency manager.

## 3. Deploy AND attach

This is the step everyone misses: clicking Deploy is not enough. Go to Actions > Flows > Login, drag the Action into the flow, and Apply. The flow order is the execution order.

## 4. Test

Use the flow's test runner first, then do a real login in an incognito window. Decode the fresh token and confirm the claim. Old tokens never gain new claims.

## Common extras

- Deny bad actors: `api.access.deny("end_users_not_allowed")` with a reason string.
- MFA gating: `api.multifactor.enable("any")` only when `event.user.multifactor` is empty, or you loop enrolled users.
- Redirects: `api.redirect.sendUserTo()` needs a resume handler; do not redirect unconditionally.

## Checklist

- Namespaced claim names, both token targets set deliberately.
- Deployed, attached to the flow, verified with a fresh token.

## When to use this

- This covers exactly what the title says: Add custom claims with a post-login Action.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Add; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Add behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_OiAs34eraTjy9c2StzsqvA). Version: `skv_lxAm8iT7YjFlACA5V4YSzw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
