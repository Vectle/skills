---
name: "diagnosing-a-moved-block-misfire-plan-4718772c2c3323fb"
description: "A moved block that does not match leaves the plan showing destroy plus create. The procedure checks address matching, module boundaries, and the common from/to mistakes."
metadata:
  skill_id: "skl_XIYn4cHfsweGSTw9YsL_Aw"
  title: "Diagnosing a moved block misfire: plan still wants destroy/create"
  version: "skv_ytIerA1wYhFbuOoquFfHew"
  updated: "2026-10-03T14:45:51.541449+00:00"
  canonical_url: "https://vectle.com/skills/skl_XIYn4cHfsweGSTw9YsL_Aw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** A moved block that does not match leaves the plan showing destroy plus create. The procedure checks address matching, module boundaries, and the common from/to mistakes. Check the to address against the actual config. Check boundaries: moved blocks cannot move into or out of a for_each/count instance change cleanly in all cases, and cannot cross from a resource to a different resource type.

## The fix

**TL;DR:** A moved block that does not match leaves the plan showing destroy plus create. The procedure checks address matching, module boundaries, and the common from/to mistakes. Check the to address against the actual config. Check boundaries: moved blocks cannot move into or out of a for_each/count instance change cleanly in all cases, and cannot cross from a resource to a different resource type.

## Symptom

You added `moved { from = ... to = ... }` but the plan still shows destroy of the old address and create of the new one.

## Cause

The moved block did not match: the `from` address does not exist in state, the `to` address is wrong, or the move crosses a boundary moved blocks cannot express.

## Confirmation

1. `terraform state list | grep` for the `from` address. If it is not in state, there is nothing to move; the plan is correct and your `from` is wrong.
2. Check the `to` address against the actual config. Typos in resource names or module paths are the most common misfire.
3. Check boundaries: moved blocks cannot move into or out of a `for_each`/`count` instance change cleanly in all cases, and cannot cross from a resource to a different resource type.

## Fix

1. Correct the `from`/`to` addresses and re-plan. The plan should flip from destroy/create to a no-op move (shown as a move in the plan output).
2. If the move is genuinely inexpressible with moved blocks, do it with `terraform state mv` (same effect, imperative), then codify with a moved block afterwards for the record.
3. Never "fix" a misfired move by letting the destroy/create happen unless you have verified the resource is safe to recreate (stateless, no data).

## Verification

1. The plan shows the move (Terraform reports moved objects explicitly), with no destroy and no create for that resource.
2. After apply, `terraform state list` shows only the new address.
3. Keep the moved block in config as history. Removing it later is safe once every collaborator has applied past the move.

## When to use this

- This covers exactly what the title says: Diagnosing a moved block misfire.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Diagnosing behavior.

## Edge cases

- Never "fix" a misfired move by letting the destroy/create happen unless you have verified the resource is safe to recreate (stateless, no data).

---

Source: [Vectle](https://vectle.com/skills/skl_XIYn4cHfsweGSTw9YsL_Aw). Version: `skv_ytIerA1wYhFbuOoquFfHew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
