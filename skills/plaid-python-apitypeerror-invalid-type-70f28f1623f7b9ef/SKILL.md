---
name: "plaid-python-apitypeerror-invalid-type-70f28f1623f7b9ef"
description: "Shows how to fix plaid-python ApiTypeError: Invalid type for variable 'category_id' (NoneType) on transactions_get. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_K807YgtBygzDCTm5pxwpNw"
  title: "plaid-python ApiTypeError: Invalid type for variable 'category_id' (NoneType) on transactions_get"
  version: "skv_k61BNPKVYEdgdZ0ZFS8brQ"
  updated: "2026-10-03T13:56:30.675191+00:00"
  canonical_url: "https://vectle.com/skills/skl_K807YgtBygzDCTm5pxwpNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "ApiTypeError: Invalid type for variable 'category_id'. Required value type is str and passed type was NoneType at ['received_data']['transac": a maintainer confirmed the category_id field was erroneously missing nullable in the spec and fixed it on Plaid's side, shipping the corrected SDK in 8.0.0b13. Fix: upgrade plaid-python to 8.0.0b13+.

```text
ApiTypeError: Invalid type for variable 'category_id'. Required value type is str and passed type was NoneType at ['received_data']['transactions'][14]['category_id']
```

## Steps

1. A maintainer confirmed the category_id field was erroneously missing `nullable` in the spec and fixed it on Plaid's side, shipping the corrected SDK in 8.0.0b13. Fix: upgrade plaid-python to 8.0.0b13+. Don't use `_check_return_type=False` as a workaround - it returns raw dicts that break `.to_dict()` with an AttributeError about `_composed_schemas`.

Expected: A maintainer confirmed the category_id field was erroneously missing nullable in the spec and fixed it on Plaid's side, shipping the corrected SDK in 8.0.0b13.

## When to use

You are seeing this: With plaid-python 8.0.0b12, client.transactions\_get raised ApiTypeError: Invalid type for variable 'category\_id'. Use this skill when you run into "plaid-python ApiTypeError: Invalid type for variable 'category_id' (NoneType) on transactions_get".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_K807YgtBygzDCTm5pxwpNw). Version: `skv_k61BNPKVYEdgdZ0ZFS8brQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
