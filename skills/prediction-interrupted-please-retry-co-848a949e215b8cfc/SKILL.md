---
name: "prediction-interrupted-please-retry-co-848a949e215b8cfc"
description: "Fixes 'Prediction interrupted; please retry (code: PA)' on Replicate when passing a file object by uploading the file to a URL (a signed S3 URL works for private files) and passing the URL instead. Use when replicate.run fails on local file inputs around 20 MB or larger. Not for other prediction error codes."
metadata:
  skill_id: "skl_VWY0vYIwpe4qYkxsEd3Qow"
  title: "Prediction interrupted; please retry (code: PA) when passing a file object as input"
  version: "skv_w7lW3rbr_zgAVAvg0nt4vw"
  updated: "2026-10-03T04:11:25.759827+00:00"
  canonical_url: "https://vectle.com/skills/skl_VWY0vYIwpe4qYkxsEd3Qow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upload the file to a URL, a signed S3 URL works for private files, and pass the URL as the model input instead of the file object. Client libraries base64-encode file objects into the request body and the API caps request size; files around 20 MB or larger trip the limit. The Replicate website does exactly this internally.

## The error

```text
Prediction interrupted; please retry (code: PA)
```

Seen when calling `replicate.run` with a local file object, while the same model works from the Replicate website.

## Fix it

1. Upload the file somewhere reachable. For private files, generate a signed S3 URL.
   Success check: the URL is fetchable (curl it) without authentication errors.

2. Pass the URL as the input instead of the file object:
   ```python
   output = replicate.run(
       "model/name:version",
       input={"image": "https://your-signed-url/file.png"}
   )
   ```
   Success check: the prediction starts instead of interrupting immediately.

3. For files well under 20 MB, the file object path keeps working; only switch to URLs for large files.
   Success check: small files still succeed inline.

## When this applies

- `replicate.run` with a local file object fails with `(code: PA)`.
- The file is around 20 MB or larger.
- The same model and inputs work from the Replicate website.

## When it does not apply

- A different error code; PA specifically means the interrupted-on-input path.
- Small files failing too; that points at the model or input schema, not size.
- You already pass URLs and still get PA.

## Compatibility

- Replicate Python and JS clients (any recent version); the website is unaffected.
- Signed S3 URLs, presigned GCS URLs, or any public HTTPS URL.

## Variant phrasings

- Prediction interrupted please retry code PA
- replicate.run file object prediction interrupted
- Replicate file input too large code PA

## Why it happens

Client libraries send file objects inline as base64-encoded data in the request body, and the Replicate API enforces a request size limit. Files around 20 MB or larger exceed it, so the prediction is interrupted before it starts. The website uploads to a URL first, which is why the same model works there.

## Edge cases

- Signed URLs expire; generate a fresh one per run for long-lived jobs.
- If the model needs multiple files, upload each and pass a list of URLs.


---

Source: [Vectle](https://vectle.com/skills/skl_VWY0vYIwpe4qYkxsEd3Qow). Version: `skv_w7lW3rbr_zgAVAvg0nt4vw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
