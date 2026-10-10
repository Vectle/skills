---
name: "terraform-error-cycle-means-your-depen-b63b9fcc555f9ce3"
description: "Terraform plan fails with Error Cycle listing resources in a dependency loop. Covers reading the cycle list and the three standard ways to break it. Not for provider errors, state locks, or apply-time failures."
metadata:
  skill_id: "skl_zxU1n_roSxO1D53ZQgnyKw"
  title: "Terraform: \"Error: Cycle:\" means your dependency graph has a loop"
  version: "skv_Rv7q3_BLAvlUJkSepyi4-Q"
  updated: "2026-10-03T04:47:09.9819+00:00"
  canonical_url: "https://vectle.com/skills/skl_zxU1n_roSxO1D53ZQgnyKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Terraform built the dependency graph and found a loop: A needs B's value, B needs A's value, so nothing can be ordered and planning stops. Read the cycle list (it names the exact resources), draw the arrows to find which reference is incidental, and break it by removing the incidental reference, splitting the shared value into a third resource, or reading the existing side with a data source.

The error, verbatim:

```text
Error: Cycle: aws_instance.a, aws_instance.b
```

Steps:

1. Read the cycle list. It names the exact resources. Draw the arrows: which attribute of A references B, and which attribute of B references A? Success: you can name both references.
2. Find the incidental reference. The usual suspect: two resources referencing each other's computed attributes, where one direction is real (security group needs the instance's subnet) and the other is incidental (instance tags reference the security group name). Success: you know which edge to cut.
3. Break it with one of: (a) remove the incidental reference, hardcode or variable-ize it; (b) split one resource so the shared value lives in a third resource both depend on; (c) use a data source to read the already-existing side instead of referencing the managed resource. Success: plan proceeds past graph building.

When to use: terraform plan or apply fails with Error: Cycle.

When not to use: provider errors, state locks, apply-time failures, or cycles reported by other tools.

Compatibility: Terraform and OpenTofu, any provider.

Variants:
- terraform error cycle dependency
- terraform cycle aws_instance
- break terraform dependency cycle

Rules for agents:

1. depends_on never fixes a cycle. It adds edges to the graph; the graph already has too many.
2. Cycles through modules are the same problem one level up: module A output feeds module B input feeds module A input. Restructure so data flows one way.
3. A cycle that appears after a refactor means the refactor moved a reference across a boundary. git diff the refactor and look for the new edge.
4. terraform graph | dot renders the graph visually for big configs where the text list is hard to follow. The cycle is usually obvious in the picture.

Root cause: real config loops, not tool bugs. Two resources genuinely need each other's computed values, which is unorderable by definition. One of the two references is almost always incidental.

Edge cases: longer chains work the same way, just with more arrows to draw. Start from the cycle list order.

---

Source: [Vectle](https://vectle.com/skills/skl_zxU1n_roSxO1D53ZQgnyKw). Version: `skv_Rv7q3_BLAvlUJkSepyi4-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
