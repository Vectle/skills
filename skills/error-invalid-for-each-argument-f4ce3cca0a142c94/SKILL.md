---
name: "error-invalid-for-each-argument-f4ce3cca0a142c94"
description: "Fixes OpenTofu's 'Error: Invalid for_each argument' by giving for_each plan-time-known keys. Use when plan or validate rejects a for_each over unknown values, null, or a wrong-typed collection. Not for count errors or dynamic block issues."
metadata:
  skill_id: "skl_Y74taZs2y8GG_6Rb0_MTmg"
  title: "Error: Invalid for_each argument"
  version: "skv_QsoaOLCTwt5Neb2tYE7evg"
  updated: "2026-10-03T14:39:39.696846+00:00"
  canonical_url: "https://vectle.com/skills/skl_Y74taZs2y8GG_6Rb0_MTmg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/zachreborn/terraform-modules/blob/HEAD/.github/specs/issue-320-aws-backup-organization-for-each-type.md\"]"
---

TL;DR: `for_each` needs a map or a set of strings whose KEYS are known at plan time. You're giving it something else: a value that's unknown until apply, a wrong-typed collection, or null. Key the collection on static values you control, and keep the computed stuff in the values.

```text
Error: Invalid for_each argument
  on .../modules/services/aws_backup/main.tf line 276, in module "organization_backup_plan":
  276:   for_each = var.enable_organization_backup ? [true] : []
The given "for_each" argument value is unsuitable: the "for_each" argument
must be a map, or set of strings, and you have provided a value of type
list of bool.
```

## Steps

1. Read what the error complains about: a TYPE (`list of bool`), UNKNOWN values (`known only after apply`), or NULL.
   Expected: you know which of the three you're dealing with.
2. Fix by case:
   - Unknown keys: re-key the map on a static logical name you supply, and carry the computed ID as a VALUE, not a key. Keys become instance addresses, so they must be plannable.
   - Wrong type: convert, e.g. `for_each = toset(var.names)` or build a real map. Since OpenTofu 1.10 the type is enforced statically, so `? [true] : []` fails even when disabled.
   - Null: guard it, e.g. `for_each = var.branches != null ? var.branches : {}`.
   Expected: `tofu validate` passes.
3. Re-run `tofu plan`.
   Expected: no for_each error.

## When this applies

- `tofu plan` or `tofu validate` fails with `Error: Invalid for_each argument`.
- You just added a `for_each`, changed its expression, or upgraded to OpenTofu 1.10+.

## When it doesn't apply

- `Error: Invalid count argument` is the count twin; same idea, different meta-argument.
- `Error: Missing resource instance key` means a reference forgot `[each.key]`; the for_each itself is fine.

## Tool versions

All OpenTofu versions. Note: 1.10+ enforces the for_each TYPE statically, so expressions that used to slip through when empty (like `[true] : []`) now fail.

## Why it happens

`for_each` keys become part of resource instance addresses (`aws_x.y["key"]`), and addresses must be decided at plan time. An unknown key would mean planning an instance you can't name yet, so tofu refuses.

## Edge cases

- Sensitive values as KEYS are rejected too: keys land in addresses, and addresses can't be sensitive. Keep secrets in values and index by `each.key`.
- The escape hatch is a targeted apply: create the upstream resource first (`tofu apply -target=...`), then run the full apply. Restructuring the keys is the real fix; targeting is the bandage.
- Splitting one apply into two (create accounts, then register them) is sometimes the honest answer when the key genuinely can't be known upfront.

---

Source: [Vectle](https://vectle.com/skills/skl_Y74taZs2y8GG_6Rb0_MTmg). Version: `skv_QsoaOLCTwt5Neb2tYE7evg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
