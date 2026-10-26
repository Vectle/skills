---
name: "rangeerror-map-maximum-size-exceeded-w-8fa58d94d09c4118"
description: "Fixes 'RangeError: Map maximum size exceeded' when uploading large files to an Apify Actor key-value store with Actor.setValue(). Pass the data as a ReadableStream instead of a fully materialized Buffer or string; the reporter confirmed this works for almost any file size. Use when setValue throws on files over roughly 9 MB. Not for dataset or request-queue limits."
metadata:
  skill_id: "skl_K00HKulQo8CIfQMZiyGTHA"
  title: "RangeError: Map maximum size exceeded when uploading large file to Apify key-value store"
  version: "skv__LnoMhMmuBA_aN3y00yqog"
  updated: "2026-10-03T05:33:55.990514+00:00"
  canonical_url: "https://vectle.com/skills/skl_K00HKulQo8CIfQMZiyGTHA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr__7MxyYvptVhbwxuoVacimg\",\"https://github.com/apify/crawlee/issues/1732\"]"
---

TL;DR: if `Actor.setValue()` throws `RangeError: Map maximum size exceeded` on a large file, do not pass a Buffer or string. Convert the file into a ReadableStream and hand that to `setValue()` instead. The reporter confirmed this works for almost any file size.

The error, verbatim:

```text
RangeError: Map maximum size exceeded
```

## Steps

1. Confirm the pattern: small files save fine, files over roughly 9 MB throw. If small files also fail, this is not your problem.

2. Replace the materialized payload with a stream:

```js
const stream = fs.createReadStream('archive.zip');
await Actor.setValue('my-file', stream, { contentType: 'application/zip' });
```

   Expected: `setValue` accepts the stream without throwing.

3. Success check: the upload completes and the key reads back the full file. Building the archive itself was never the slow part; the crash happened while saving, so a fast archive build plus this crash is the signature.

## When to use this

- `Actor.setValue()` throws `RangeError: Map maximum size exceeded` on large payloads (seen above ~9 MB).
- You are writing to an Apify Actor key-value store.

## When NOT to use this

- Dataset pushes or request-queue limits; different storage, different errors.
- Small payloads failing; look at serialization or auth instead.

## Compatibility

- crawlee 3.1.3 / apify 3.1.1, Actor key-value store `setValue`. The crash is size-dependent, not version-dependent beyond that.

## Variant phrasings

- apify setValue large file RangeError
- crawlee key value store Map maximum size exceeded
- upload zip to apify kv store fails over 9mb

## Root cause

The store materializes the whole payload in a Map-backed structure before writing, and V8's Map size limit trips on large buffers. A ReadableStream never materializes the full payload in one structure, so the limit is never hit.

## Edge cases

- Content type still matters; pass it explicitly so the stored key is readable as the right type.
- If you need progress reporting, wrap the stream; `setValue` itself gives you no progress callback either way.

Source: https://github.com/apify/crawlee/issues/1732

---

Source: [Vectle](https://vectle.com/skills/skl_K00HKulQo8CIfQMZiyGTHA). Version: `skv__LnoMhMmuBA_aN3y00yqog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
