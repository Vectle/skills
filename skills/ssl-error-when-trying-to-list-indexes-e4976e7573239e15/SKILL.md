---
name: "ssl-error-when-trying-to-list-indexes-e4976e7573239e15"
description: "Python SDK: SSL Error when trying to .list_indexes(). The verified fix is Fix: Community-verified causes for the SSL error, no single maintainer fix (closed with workaround). Use this when you hit the symptoms above in python-sdk; not for unrelated python-sdk errors or general setup questions."
metadata:
  skill_id: "skl_M2xdq91cB7tLbQ9FR8ir4A"
  title: "SSL Error when trying to `.list_indexes()`"
  version: "skv_T7NAvpvAiUU33v6U5XDZfw"
  updated: "2026-10-03T04:34:11.245085+00:00"
  canonical_url: "https://vectle.com/skills/skl_M2xdq91cB7tLbQ9FR8ir4A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pinecone-io/python-sdk/issues/162\"]"
---

## TL;DR

Fix: Community-verified causes for the SSL error, no single maintainer fix (closed with workaround). (1) Typo in the environment name - confirm it in the Pinecone console (one reporter fixed us-east1-gcp -> us-east4-gcp). (2) Corporate firewall/proxy intercepting TLS: workarounds are `pip install pip-system-certs`, setting proxy env vars, or appending the corporate CA cert to certifi's cacert.pem.

## The error

```text
Issue pinecone-io/python-sdk#162 (closed, 8 comments): ### Is this a new bug in the Pinecone Python client?
- [X] I believe this is a new bug in the Pinecone Python Client
- [X] I have searched the existing issues, and I could not find an existing issue for this bug
```

## Fix

1. Community-verified causes for the SSL error, no single maintainer fix (closed with workaround).
2. (1) Typo in the environment name - confirm it in the Pinecone console (one reporter fixed us-east1-gcp -> us-east4-gcp).
3. (2) Corporate firewall/proxy intercepting TLS: workarounds are `pip install pip-system-certs`, setting proxy env vars, or appending the corporate CA cert to certifi's cacert.pem.
4. If behind a proxy, configure it per the Pinecone community proxy guide.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in python-sdk.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in python-sdk, even a similar-looking one.
- General python-sdk setup or credential questions.

## Compatibility

- Python SDK (pinecone-io/python-sdk)

## Variant phrasings

- How to fix "SSL Error when trying to .list_indexes()" in python-sdk
- python-sdk: SSL Error when trying to .list_indexes()
- SSL problem when trying to .list_indexes()

## Root cause

(1) Typo in the environment name - confirm it in the Pinecone console (one reporter fixed us-east1-gcp -> us-east4-gcp).

## Edge cases

- (2) Corporate firewall/proxy intercepting TLS: workarounds are `pip install pip-system-certs`, setting proxy env vars, or appending the corporate CA cert to certifi's cacert.pem.
- If behind a proxy, configure it per the Pinecone community proxy guide.

## Source

- https://github.com/pinecone-io/python-sdk/issues/162

---

Source: [Vectle](https://vectle.com/skills/skl_M2xdq91cB7tLbQ9FR8ir4A). Version: `skv_T7NAvpvAiUU33v6U5XDZfw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
