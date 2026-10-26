---
name: "diagnosing-secrets-leaked-into-terrafo-69cff3c036437da5"
description: "State files contain secret values in plaintext and plans echo them. The procedure finds where secrets entered, rotates them, and stops the leak at the variable and output level. Not the full reference manual."
metadata:
  skill_id: "skl_J72RR5wd1CWFZGY2IIMsuQ"
  title: "Diagnosing secrets leaked into Terraform state and plan output"
  version: "skv_70ptRU6v1IMi8UZPK6nN3Q"
  updated: "2026-10-03T14:19:34.990522+00:00"
  canonical_url: "https://vectle.com/skills/skl_J72RR5wd1CWFZGY2IIMsuQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developer.hashicorp.com/terraform/docs/language/values/variables\",\"https://opentofu.org/docs/language/state/encryption/\"]"
---

**TL;DR:** State files contain secret values in plaintext and plans echo them. The procedure finds where secrets entered, rotates them, and stops the leak at the variable and output level. Check exposure: who can read the state backend? Rotate the secret first.

## Symptom

A secret (password, token, private key) appears in plaintext in the state file, in plan output, or in a CI log. It may have been there for a long time.

## Cause

A non-sensitive variable or output carried the value: variables default to non-sensitive, and any value flowing through them lands in state and plan logs in cleartext.

## Confirmation

1. `terraform state pull | grep -c` for the secret pattern (careful: this puts the secret in your shell history; use a script or pipe, not the literal secret on the command line).
2. Trace the flow: which variable, local, or output carried it? `terraform console` is not needed; the config shows the path.
3. Check exposure: who can read the state backend? Who can read CI logs containing plans? The blast radius is everyone with that access, for the whole time the secret was there.

## Fix

1. Rotate the secret first. It is compromised; scrubbing the file without rotation achieves nothing.
2. Mark the variable `sensitive = true` and the output `sensitive = true`. This redacts them from plan output and console.
3. For state history: backend versioning keeps old copies with the old secret. Rotate, then consider the old versions burned; you cannot unsee them, but rotation makes them useless.
4. OpenTofu users: enable state encryption so future state is encrypted client-side.

## Verification

1. New `terraform plan` output no longer shows the value (shows `(sensitive value)`).
2. `terraform state pull` on a fresh state still contains the value by design (Terraform needs it to manage the resource); the protection is access control plus rotation, not absence. Verify backend access is scoped to the operators who need it.
3. CI logs: confirm plan output is redacted in the log viewer, not just in your terminal.

## When to use this

- This covers exactly what the title says: Diagnosing secrets leaked into Terraform state and plan output.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_J72RR5wd1CWFZGY2IIMsuQ). Version: `skv_70ptRU6v1IMi8UZPK6nN3Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
