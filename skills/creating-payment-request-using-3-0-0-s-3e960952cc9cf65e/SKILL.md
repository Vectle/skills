---
name: "creating-payment-request-using-3-0-0-s-3e960952cc9cf65e"
description: "Shows how to fix creating Payment Request Using 3.0.0 SDK. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_lDu1GUMAxHHqxPrHx8tzdQ"
  title: "Creating Payment Request Using 3.0.0 SDK"
  version: "skv_y6lL5flrYr8HCc-IlRLusg"
  updated: "2026-10-03T14:02:21.849156+00:00"
  canonical_url: "https://vectle.com/skills/skl_lDu1GUMAxHHqxPrHx8tzdQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error_code [1] => message ) [container:protected": creating Payment Request Using 3.0.0 SDK What was going on Issue xendit/xendit-php#209 (closed, 7 comments): Hello I tried creating Payment Request using the new sdk. i am using the example code from the docs and the output is this. `` Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error\_code [1] => message ) [container:protected] => Array ( [error\_code] => [message] => )) `` is this normal? because i 

```text
Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error_code [1] => message ) [container:protected] => Array ( [error_code] => [message] => ))
```

## Steps

1. Creating Payment Request Using 3.0.0 SDK

2. What was going on
Issue xendit/xendit-php#209 (closed, 7 comments): Hello I tried creating Payment Request using the new sdk. i am using the example code from the docs and the output is this.

``` Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error_code [1] => message ) [container:protected] => Array ( [error_code] => [message] => )) ```

3. is this normal? because i can see my post request on the xendit dashboard log api page.

4. The fix
[adityarx (contributor)]: The createPaymentRequest failure was because the SDK expected a 200 status but Xendit returns 201. Fixed in v3.1.0; the reporter confirmed it works after upgrading. Note: Over-The-Counter payment channels in test mode need manual activation via Xendit support.

## When to use

You are seeing this: Note: Over-The-Counter payment channels in test mode need manual activation via Xendit support. Use this skill when you run into "Creating Payment Request Using 3.0.0 SDK".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: Using 3.0.0, v3.1.0. If you are on something much newer or older, the details may have shifted.

## Variants

Other phrasings of the same problem that show up in reports:

### `` Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error\_code [1] => messag

```text
``` Xendit\PaymentRequest\Error Object( [openAPINullablesSetToNull:protected] => Array ( [0] => error_code [1] => message ) [container:protected] => Array ( [error_code] => [message] => )) ```
```

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Note: Over-The-Counter payment channels in test mode need manual activation via Xendit support.


---

Source: [Vectle](https://vectle.com/skills/skl_lDu1GUMAxHHqxPrHx8tzdQ). Version: `skv_y6lL5flrYr8HCc-IlRLusg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
