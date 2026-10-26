---
name: "airwallex-redirecttocheckout-produces-a8cbacc3777d353b"
description: "Shows how to fix airwallex redirectToCheckout produces \"undefined\" error on hosted payment page. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Wv0n7gCFBkphHOxjLKVkvA"
  title: "Airwallex redirectToCheckout produces \"undefined\" error on hosted payment page"
  version: "skv_54BX870-UX6vmGyt8y5aQQ"
  updated: "2026-10-03T13:59:34.021298+00:00"
  canonical_url: "https://vectle.com/skills/skl_Wv0n7gCFBkphHOxjLKVkvA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_wtOsz6FWknwUshYbChK14A\",\"https://github.com/airwallex/airwallex-payment-demo/issues/76\"]"
---

## TL;DR

So if you land on a blank page at the hosted checkout URL with /undefined in it, log the values you pass in before the call: ``js Airwallex.redirectToCheckout({ env: 'demo', intent\_id: data.id, // make sure this isnt undefined currency: 'AUD', // plus the client secret from your payment intent, // which also must not be undefined }); `` Fix the data plumbing and the checkout page loads normally.

## Steps

1. The undefined in the URL means your intent id (or the client secret) was undefined when redirectToCheckout ran. A maintainer asked the reporter to double check the id and the client secret coming back from their own data object, and the reporter confirmed that was exactly it: while fighting the library import they had overlooked their own data structure and were passing undefined values in.

2. So if you land on a blank page at the hosted checkout URL with /undefined in it, log the values you pass in before the call:

```js
Airwallex.redirectToCheckout({
 env: 'demo',
 intent_id: data.id, // make sure this isnt undefined
 currency: 'AUD',
 // plus the client secret from your payment intent,
 // which also must not be undefined
});
```

3. Fix the data plumbing and the checkout page loads normally.

## When to use

You are seeing this: Calling Airwallex.redirectToCheckout with an env, intent id, client secret and currency opened a blank hosted payment page. Use this skill when you run into "Airwallex redirectToCheckout produces "undefined" error on hosted payment page".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_Wv0n7gCFBkphHOxjLKVkvA). Version: `skv_54BX870-UX6vmGyt8y5aQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
