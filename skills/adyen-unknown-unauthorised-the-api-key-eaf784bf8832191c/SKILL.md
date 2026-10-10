---
name: "adyen-unknown-unauthorised-the-api-key-eaf784bf8832191c"
description: "Resolves Adyen API 401/403 responses with errorCode 000 Unknown Unauthorised. Covers matching the API key to the right environment (TEST keys on test endpoints, LIVE keys on live), generating a fresh key in the Customer Area, and confirming the web service user carries the required roles. Not for error 010 Not allowed, which is a roles problem on an otherwise valid key."
metadata:
  skill_id: "skl_B3Ujhukb4xm7N-OCY5o6-w"
  title: "Adyen: Unknown Unauthorised - The API key or Auth credentials are incorrect"
  version: "skv_r8dF1zYUTJbeCcA3I-TxYA"
  updated: "2026-10-03T04:28:07.197507+00:00"
  canonical_url: "https://vectle.com/skills/skl_B3Ujhukb4xm7N-OCY5o6-w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Unknown Unauthorised - The API key or Auth credentials are incorrect

**TL;DR:** Your API key is wrong, or it belongs to the other environment. Generate a fresh key in the Customer Area for the environment you are actually calling: TEST keys only work against the test endpoints, LIVE keys only against live. Paste it exactly, no extra whitespace.

```text
000 - Unknown: Unauthorised: The API key or Auth credentials are incorrect.
```

## Steps

1. **Check which environment your URL points at.** Test endpoints look like `https://checkout-test.adyen.com`; live ones like `https://checkout-live-...adyen.com`. The key must come from the Customer Area of the same environment.
   - *Success check:* the env in the URL matches the env of the Customer Area where the key was created.
2. **Generate a fresh API key.** In the Customer Area go to Developers > API credentials, open your web service user, and generate a new API key. Copy it straight into your config, no typing it by hand.
   - *Success check:* the full key is stored without leading or trailing spaces or newlines.
3. **Confirm the credential has the roles it needs.** Open the web service user and check the roles, e.g. the Checkout webservice role for Checkout API calls. A valid key with no roles still gets rejected.
   - *Success check:* required roles are listed on the API credential.
4. **Retry one minimal request.** Send a simple call and confirm you get past auth before debugging anything else.
   - *Success check:* HTTP 200/201 instead of 401/403.

## When to use this

- Every Adyen API call returns 401/403 with the Unauthorised message and errorCode 000.
- It worked before and broke after someone rotated credentials or you switched environments.

## When NOT to use this

- Error 010 "Not allowed". That means the key is fine but the credential lacks roles, which is a different fix.
- One endpoint works and another does not. Check the endpoint URL, not the key.

## Compatibility

All Adyen API products (Checkout, Payments, Management, webhooks config). TEST and LIVE environments each have their own keys.

## Why it happens

Almost always one of three things: the key was copied with a stray space or got truncated, a TEST key is being sent to a LIVE endpoint (or the reverse), or the credential was deleted or regenerated in the Customer Area and the app still holds the old one.

## Edge cases

- Basic auth (ws user + password) vs API key are different credentials. Dont mix them up; the Checkout API expects the API key.
- If you use IP allowlisting on the credential, calls from a new IP get rejected the same way. Check that too.


---

Source: [Vectle](https://vectle.com/skills/skl_B3Ujhukb4xm7N-OCY5o6-w). Version: `skv_r8dF1zYUTJbeCcA3I-TxYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
