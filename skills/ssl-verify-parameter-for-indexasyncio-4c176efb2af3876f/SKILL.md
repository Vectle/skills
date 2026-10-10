---
name: "ssl-verify-parameter-for-indexasyncio-4c176efb2af3876f"
description: "Fixes SSL verification failures with Pinecone Local and IndexAsyncio by passing the host explicitly with an http:// scheme, since Pinecone Local does not support TLS at all. Use when pc.IndexAsyncio fails against a local Pinecone on YOUR_HOST:5081 despite ssl_verify. Not for Pinecone cloud indexes."
metadata:
  skill_id: "skl_LpCDFJTxk4B75nOhDL72_g"
  title: "ssl_verify parameter for IndexAsyncio does not work against Pinecone Local"
  version: "skv__XblWPB4dUJvsvMAq4Yx1w"
  updated: "2026-10-03T04:12:45.363493+00:00"
  canonical_url: "https://vectle.com/skills/skl_LpCDFJTxk4B75nOhDL72_g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Pass the host explicitly with an `http://` scheme: `pc.IndexAsyncio(host="YOUR_HOST", name="test-index")`. Pinecone Local does not support TLS/SSL at all, and `describe_index` returns a scheme-less host that the client assumes is https.

## The error

SSL verification failure when connecting to Pinecone Local with `pc.IndexAsyncio`, even with the `ssl_verify` parameter set. Passing the host from `pc.describe_index(index_name).host` breaks.

## Fix it

1. Stop using the scheme-less host from `describe_index`.
   Success check: you have identified the host string without `http://`.

2. Pass the host explicitly with the http scheme:
   ```python
   async with pc.IndexAsyncio(host="YOUR_HOST", name="test-index") as idx:
       ...
   ```
   Success check: the connection succeeds with no SSL error (reporter confirmed).

3. Do not try to make TLS work: Pinecone Local cannot serve https.
   Success check: not applicable; skip TLS entirely for local.

## When this applies

- Pinecone Local (YOUR_HOST:5081) with `pc.IndexAsyncio`.
- SSL verification fails despite `ssl_verify` being set.

## When it does not apply

- Pinecone cloud indexes (serverless/pod); those require https and work normally.
- Certificate errors against non-local hosts; that is a real TLS problem.

## Compatibility

- pinecone Python client (any recent version).
- Pinecone Local (Docker) on YOUR_HOST:5081.

## Variant phrasings

- Pinecone Local ssl_verify does not work
- IndexAsyncio SSL verification failed YOUR_HOST
- pinecone describe_index host no scheme https assumed

## Why it happens

`describe_index` returns a bare hostname with no URL scheme. The client treats scheme-less hosts as https, but Pinecone Local serves plain http only, so the TLS handshake fails. Passing `http://` explicitly bypasses the assumption. A community PR proposed fixing the scheme handling in the client.

## Edge cases

- If you front Pinecone Local with your own TLS-terminating proxy, keep https and point at the proxy instead.


---

Source: [Vectle](https://vectle.com/skills/skl_LpCDFJTxk4B75nOhDL72_g). Version: `skv__XblWPB4dUJvsvMAq4Yx1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
