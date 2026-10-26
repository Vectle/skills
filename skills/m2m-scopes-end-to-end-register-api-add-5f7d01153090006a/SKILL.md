---
name: "m2m-scopes-end-to-end-register-api-add-5f7d01153090006a"
description: "Scopes fail when any of the four steps is skipped: define the permission on the API, grant it to the app, request it in the token call, enforce it in the API. Debug by walking the chain in order. Not the full reference manual."
metadata:
  skill_id: "skl_KIb03XLmIT0NPQdbF88oAA"
  title: "M2M scopes end to end: register API, add permissions, authorize app, request scopes"
  version: "skv_eNYfVB9dcDizY2BVrCsnmA"
  updated: "2026-10-03T04:46:11.313928+00:00"
  canonical_url: "https://vectle.com/skills/skl_KIb03XLmIT0NPQdbF88oAA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://auth0.com/docs/quickstart/backend\",\"https://auth0.com/docs/get-started/applications/application-grant-types\"]"
---

**TL;DR:** Scopes fail when any of the four steps is skipped: define the permission on the API, grant it to the app, request it in the token call, enforce it in the API. Debug by walking the chain in order. Authorize the app Applications > your M2M app > APIs tab > Authorize the API > tick the scopes this app may request.

# M2M scopes end to end

## 1. Register the API

Applications > APIs > Create API. Identifier e.g. `https://YOUR-API-IDENTIFIER`. This string is the audience.

## 2. Define permissions

APIs > your API > Permissions tab > Add Permission: `read:orders`, `write:orders`. Defining them only makes them grantable; nobody has them yet.

## 3. Authorize the app

Applications > your M2M app > APIs tab > Authorize the API > tick the scopes this app may request. This is the grant. Alternatively the Management API grants endpoint. The app can now request any SUBSET of these scopes.

## 4. Request with scopes

```
curl --request POST --url https://YOUR-TENANT-DOMAIN/oauth/token   --header "content-type: application/json"   --data '{"client_id":"[your value]","client_secret":"[your value]",
           "audience":"https://YOUR-API-IDENTIFIER",
           "grant_type":"client_credentials","scope":"read:orders"}'
```

Omit scope to get all granted scopes. Requesting a scope the app was not granted fails the whole request.

## 5. Enforce in the API

```
const { auth, requiredScopes } = require("express-oauth2-jwt-bearer");
app.get("/orders", checkJwt, requiredScopes("read:orders"), handler);
```

Check `req.auth.payload.scope` contains what the route needs.

## Debugging chain

Token has no scope claim: step 3 or 4. 403 from requiredScopes: token scope vs route scope. "Grant type not allowed": app type wrong.

## Checklist

- Four steps, in order, all four done.
- Least privilege: grant only the scopes the service needs.

## When to use this

- This covers exactly what the title says: M2M scopes end to end.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with M2M; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current M2M behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_KIb03XLmIT0NPQdbF88oAA). Version: `skv_eNYfVB9dcDizY2BVrCsnmA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
