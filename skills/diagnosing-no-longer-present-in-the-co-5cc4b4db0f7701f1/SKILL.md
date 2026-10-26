---
name: "diagnosing-no-longer-present-in-the-co-5cc4b4db0f7701f1"
description: "State tracks resources the config no longer declares. The procedure distinguishes deliberate removal from accidental deletion and picks state rm vs re-adding config vs destroying for real. Not the full reference manual."
metadata:
  skill_id: "skl_TXSs55LU6DS4PBwoJSO6Hg"
  title: "Diagnosing \"no longer present in the configuration\": orphaned state entries"
  version: "skv_hG7MAAx7zDkIV0G3eNOcjw"
  updated: "2026-10-03T14:43:15.207949+00:00"
  canonical_url: "https://vectle.com/skills/skl_TXSs55LU6DS4PBwoJSO6Hg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/modules/develop/refactoring/\",\"https://opentofu.org/docs/language/resources/delete/\"]"
---

**TL;DR:** State tracks resources the config no longer declares. The procedure distinguishes deliberate removal from accidental deletion and picks state rm vs re-adding config vs destroying for real. Compare with git log/git diff on the config: was the block deleted deliberately or lost accidentally? Check whether the real object still exists (console/API).

## The fix

**TL;DR:** State tracks resources the config no longer declares. The procedure distinguishes deliberate removal from accidental deletion and picks state rm vs re-adding config vs destroying for real. Compare with git log/git diff on the config: was the block deleted deliberately or lost accidentally? Check whether the real object still exists (console/API).

## Symptom

```
Note: the current state contains resource instances that are no longer
present in the configuration ...
```

or plan wants to destroy resources you did not intend to remove. The state file references addresses with no matching config block.

## Cause

A config block was deleted or renamed without handling the state entry: a refactor removed the resource, a merge dropped the file, or a rename changed the address while the old address lingers.

## Confirmation

1. `terraform state list` shows the orphaned addresses. Compare with `git log`/`git diff` on the config: was the block deleted deliberately or lost accidentally?
2. Check whether the real object still exists (console/API). Orphaned state plus a live object is different from orphaned state plus a deleted object.

## Fix (pick one deliberately)

1. Accidental deletion: restore the config block. Next plan should be clean.
2. Deliberate removal, object should be destroyed: let the plan destroy it, or `terraform destroy -target=[address]` for a controlled removal.
3. Deliberate removal, object should live on unmanaged: `terraform state rm [address]` to untrack without destroying. (OpenTofu/Terraform 1.7+: prefer a `removed` block with `lifecycle { destroy = false }` so the intent is codified in config, not a CLI one-off.)
4. Rename (not removal): this is a `moved` block situation, not an orphan. Add the moved block so the plan renames instead of destroy/create.

## Verification

1. `terraform plan` shows only intended changes: no surprise destroys, no unexpected creates.
2. For `state rm`: the object still exists in the console and no longer appears in `terraform state list`.

## When to use this

- This covers exactly what the title says: Diagnosing "no longer present in the configuration".
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 1.7 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_TXSs55LU6DS4PBwoJSO6Hg). Version: `skv_hG7MAAx7zDkIV0G3eNOcjw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
