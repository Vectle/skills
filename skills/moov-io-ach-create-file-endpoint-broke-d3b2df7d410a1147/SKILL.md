---
name: "moov-io-ach-create-file-endpoint-broke-d3b2df7d410a1147"
description: "Fixes moov-io/ach create-file endpoint being unreachable for raw NACHA text from Java clients due to the OpenAPI generator's one-body-schema limit. Use this when the generated client only exposes the JSON path. Not for JSON-body creation issues."
metadata:
  skill_id: "skl_BYbAbJvYpKIbTrknzySA7w"
  title: "moov-io/ach: create file endpoint broken for Java clients (cant send raw NACHA text)"
  version: "skv_kG_3KYwKkDw43bgO3Xi8Ag"
  updated: "2026-10-03T04:45:46.025078+00:00"
  canonical_url: "https://vectle.com/skills/skl_BYbAbJvYpKIbTrknzySA7w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr__Ydk13U0cq7947dCLdsauw\",\"https://github.com/moov-io/ach/issues/1650\"]"
---

TL;DR: if your Java app cannot send raw NACHA text through moov-io/ach's `POST /files/[fileID]` because the OpenAPI-generated client only exposes the JSON body schema (a long-standing openapi-generator limitation of one body schema per endpoint), use the dedicated raw-text endpoint added in PR #1653 (`POST /files/[fileID]/new`). The generator produces a method that takes a plain string body for it. The reporter confirmed this works for them.

## Steps

1. Use the dedicated endpoint for raw NACHA text:

```
POST /files/[fileID]/new
```

   with the raw NACHA text as the string body.

   Expected: the file is created from the raw text. Success check: the file reads back correctly.

2. Keep using the shared endpoint for JSON bodies; both paths now exist.

## When to use this

- Generated Java client cannot reach the raw-text code path on the shared endpoint.
- You need both JSON and raw-text creation.

## When NOT to use this

- JSON-body creation fails; that path is separate.
- You hand-write the HTTP calls; just send the raw text to the shared endpoint (the server now ignores Content-Type and tries both parsings).

## Compatibility

- moov-io/ach with PR #1653.

## Variant phrasings

- "moov ach java raw NACHA"
- "moov-io ach create file raw text endpoint"

## Root cause

The generator can only emit one body schema per endpoint, so the raw-text variant was unreachable from generated clients even after the server learned to parse both.

## Edge cases

- Hand-written clients do not need the new endpoint; the server-side Content-Type-agnostic parsing covers them.

---

Source: [Vectle](https://vectle.com/skills/skl_BYbAbJvYpKIbTrknzySA7w). Version: `skv_kG_3KYwKkDw43bgO3Xi8Ag`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
