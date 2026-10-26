---
name: "adyen-invalid-merchant-account-error-9-fb0e02e2100652b7"
description: "Fixes Adyen error 901 Invalid Merchant Account. Covers copying the case-sensitive merchant account name exactly from the Customer Area, matching it to the right environment, confirming the web service user is permitted for the account, and not confusing the 3DS MD value with merchantAccount. Not for 010 Not allowed or genuine credential problems."
metadata:
  skill_id: "skl_oIcL4yfUpe9p4ZyOhmL5uQ"
  title: "Adyen: Invalid Merchant Account (error 901)"
  version: "skv_i3L0hNFrWo08vXAeSMk2zw"
  updated: "2026-10-03T04:31:13.742047+00:00"
  canonical_url: "https://vectle.com/skills/skl_oIcL4yfUpe9p4ZyOhmL5uQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: Invalid Merchant Account (error 901)

**TL;DR:** The merchantAccount in your request does not exist in that environment, is spelled with the wrong casing, or your web service user is not allowed to use it. Copy the name exactly from the Customer Area, same environment as your endpoint, and check the credential's permissions.

```text
901 - Invalid Merchant Account
```

## Steps

1. **Copy the exact merchant account name.** In the Customer Area, open the merchant account and copy the name character for character. It is case-sensitive: `MyMerchant` and `mymerchant` are different accounts.
   - *Success check:* the string in your request matches the Customer Area letter for letter, including case.
2. **Match the environment.** A merchant account that exists in TEST does not exist in LIVE. Confirm the account exists in the environment your endpoint points to.
   - *Success check:* you can see the account in the Customer Area of that same environment.
3. **Check the web service user's permissions.** The credential making the call must be permitted for that merchant account. Open Developers > API credentials and verify.
   - *Success check:* the web service user lists the merchant account (or the company account) in its access.
4. **Confirm the company account is active.** An inactive company behind the merchant account produces the same error.
   - *Success check:* the company account shows active in the Customer Area.
5. **Dont pass the 3DS MD value as merchantAccount.** In 3DS flows the MD (merchant data) value is a different field; reusing it where merchantAccount belongs triggers 901.
   - *Success check:* merchantAccount holds the account name, MD holds the 3DS merchant data.

## When to use this

- /payments or /authorise fails with 901.
- It works in TEST but fails in LIVE (or the reverse) with the same code.

## When NOT to use this

- Error 931 (no merchant with the code). Similar area, different code path; still, check the account name first.
- 010 Not allowed. That is a roles problem on a valid account.

## Compatibility

All Adyen API products that take merchantAccount, TEST and LIVE.

## Why it happens

The usual story: a hand-typed account name with wrong casing, a TEST account name pasted into LIVE config, a web service user that was never granted access to the account, or MD/merchantAccount fields swapped in a 3DS integration.

## Edge cases

- After renaming or migrating accounts, old configs keep the stale name. Search your codebase for every place merchantAccount is set.
- Sub-merchant setups: make sure you are sending the processing merchant account, not the parent company name.


---

Source: [Vectle](https://vectle.com/skills/skl_oIcL4yfUpe9p4ZyOhmL5uQ). Version: `skv_i3L0hNFrWo08vXAeSMk2zw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
