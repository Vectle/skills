---
name: "deno-deploy-unexpected-non-whitespace-a618f2df656eb81a"
description: "Fixes Deno Deploy Fresh apps failing with 'Unexpected non-whitespace character after JSON at position 3' plus a 508 when server code fetches the app's own API. Use this when local dev works but Deploy fails. Not for genuine JSON errors."
metadata:
  skill_id: "skl_Fvpbar7eQ880e6jrq49C4Q"
  title: "Deno Deploy: 'Unexpected non-whitespace character after JSON at position 3' when fetching own API (508 loop)"
  version: "skv_bfSOzpRUWPlom-bKwRXQew"
  updated: "2026-10-03T05:40:50.235268+00:00"
  canonical_url: "https://vectle.com/skills/skl_Fvpbar7eQ880e6jrq49C4Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if a Fresh app works locally but on Deno Deploy a server-side fetch to the app's own API route fails with `SyntaxError: Unexpected non-whitespace character after JSON at position 3` and the logs show `Response status: 508`, the JSON error is a red herring. Deno Deploy returns 508 when it detects a request loop: a deployment making an HTTP request to itself. Do not fetch your own deployment over HTTP from server-side code; import the route handler and call it directly (the reporter invoked `trialRequest.POST(fakeRequest)` with a stubbed request). Alternatively, move the fetch to a frontend island so the request comes from the browser.

```text
SyntaxError: Unexpected non-whitespace character after JSON at position 3
Response status: 508
```

## Steps

1. Replace the self-fetch with a direct handler call:

```js
import { trialRequest } from './routes/api/members/securedApi/trial.js';
const res = await trialRequest.POST(fakeRequest);
```

2. Redeploy.

   Expected: no more 508. Success check: the page renders with the API data.

## When to use this

- Fresh on Deno Deploy, server code fetches the deployment's own routes.
- Local dev works fine.

## When NOT to use this

- The JSON is genuinely malformed; validate the payload.
- No self-fetch involved; the 508 has another cause.

## Compatibility

- Deno Deploy with Fresh.

## Variant phrasings

- "deno deploy 508 request loop"
- "deno deploy fetch own api fails"

## Root cause

Deno Deploy blocks recursive requests where a deployment fetches itself, returning 508; the error body is not JSON, hence the parse error.

## Edge cases

- Frontend islands are the other sanctioned path since the request then comes from the browser.

---

Source: [Vectle](https://vectle.com/skills/skl_Fvpbar7eQ880e6jrq49C4Q). Version: `skv_bfSOzpRUWPlom-bKwRXQew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
