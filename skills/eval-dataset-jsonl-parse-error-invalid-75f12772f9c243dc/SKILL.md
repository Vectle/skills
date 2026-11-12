---
name: "eval-dataset-jsonl-parse-error-invalid-75f12772f9c243dc"
description: "eval dataset JSONL parse error invalid line fails run"
metadata:
  skill_id: "skl_uBBdczpv1iWiAvB04Lr-IA"
  title: "eval dataset JSONL parse error invalid line fails run"
  version: "skv_yyAe9UOtQRgLgYphM0d2yg"
  updated: "2026-11-12T01:54:53.398967+00:00"
  canonical_url: "https://vectle.com/skills/skl_uBBdczpv1iWiAvB04Lr-IA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Rerun the eval command and copy the exact line number and position from the parse error.

Print only that line and the two lines around it, without opening the whole file in an editor that rewraps lines.

Validate each line independently with a JSON parser in a short script or command that reports the first failing line number.

Fix that line in place: escape internal double quotes, remove the trailing comma, close any unclosed brace or bracket, and delete a trailing blank line at end of file if the loader treats it as a record.

Check the record keys on the fixed line against a known good line from the same file, especially the prompt, input, and expected fields the harness requires.

Rerun the full eval.

---

Source: [Vectle](https://vectle.com/skills/skl_uBBdczpv1iWiAvB04Lr-IA). Version: `skv_yyAe9UOtQRgLgYphM0d2yg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
