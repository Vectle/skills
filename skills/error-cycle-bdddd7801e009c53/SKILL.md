---
name: "error-cycle-bdddd7801e009c53"
description: "Fixes terraform's \"Error: Cycle\" circular dependency failure. Use when plan or validate refuses to run because resources or modules reference each other in a loop. Shows how to read the cycle chain and break it by splitting resources, using data sources, or passing shared values. Not for self-referencing depends_on or cycles inside expression logic."
metadata:
  skill_id: "skl_A2KBshZshpa-0i7shKLGug"
  title: "Error: Cycle"
  version: "skv_Qo5nRFsl-Es0tOgsSnxgXw"
  updated: "2026-10-03T06:08:55.902161+00:00"
  canonical_url: "https://vectle.com/skills/skl_A2KBshZshpa-0i7shKLGug"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/zoya1945/terraform-project-zoya-h-/blob/HEAD/terraform-qa/17-troubleshooting/common-issues.md\"]"
---

# Fix terraform "Error: Cycle" (circular dependency)

**TL;DR:** Two or more resources depend on each other in a circle, so terraform cannot pick an order to create them. Read the cycle chain in the error, find the reference that closes the loop, and break it: split the cross-referencing bits into separate resources (the classic is splitting security group rules out of security groups), use a data source, or pass a plain value instead of a computed attribute.

## The error

```text
Error: Cycle: aws_security_group.web, aws_security_group.db
```

## Steps

1. Read the chain. `Error: Cycle: A, B` means A references B and B references A. Find both references in your config.
2. For the classic security-group pair, move the rules out of the groups:

   ```hcl
   resource "aws_security_group" "web" {
     name   = "web-sg"
     vpc_id = var.vpc_id
   }

   resource "aws_security_group" "db" {
     name   = "db-sg"
     vpc_id = var.vpc_id
   }

   resource "aws_security_group_rule" "web_to_db" {
     type                     = "ingress"
     from_port                = 3306
     to_port                  = 3306
     protocol                 = "tcp"
     security_group_id        = aws_security_group.db.id
     source_security_group_id = aws_security_group.web.id
   }
   ```

3. For module cycles (`module.a` needs `module.b`'s output and vice versa), pass a shared plain value into both instead of chaining outputs, or move the shared resource up to the root module.
4. Run `terraform validate`. Expected: `Success! The configuration is valid.`

## When this applies

- `plan` or `validate` fails with `Error: Cycle:` followed by a chain of resources or modules.
- You see it after wiring two resources to reference each other's attributes.

## When it does NOT apply

- Errors about a resource depending on itself through `depends_on`. That is a self-reference, a different (simpler) fix: remove the redundant `depends_on`.
- `Error: Cycle` inside a `for` expression or local value. Same principle, but the loop is in expression logic, not resource ordering.

## Tool and version compatibility

- Terraform CLI 0.12+ through 1.x. Graph behavior unchanged across versions.

## Why it happens

Terraform builds a dependency graph and creates resources in topological order. A cycle makes ordering impossible, so it refuses to plan at all rather than guess. References create edges automatically; the cycle is always a real circle in your references, never a terraform bug.

## Edge cases and pitfalls

- `terraform graph | dot -Tpng > graph.png` draws the dependency graph so you can see the loop visually.
- Data sources can break cycles only when the data is knowable without the resource existing. A data source that reads the resource you are creating re-creates the cycle.
- Avoid `depends_on` between whole modules. It creates coarse edges that invite cycles; prefer passing specific values.
- Sometimes the cycle is fake: two resources reference each other but only one reference is load-bearing. Deleting the unnecessary one fixes it in one line.

---

Source: [Vectle](https://vectle.com/skills/skl_A2KBshZshpa-0i7shKLGug). Version: `skv_Qo5nRFsl-Es0tOgsSnxgXw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
