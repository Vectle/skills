---
name: "terraform-workflow-zero-downtime-resou-3a0314664e123539"
description: "Replacing a resource normally destroys then creates, causing an outage window. The workflow uses create_before_destroy plus dependency design to keep serving traffic throughout. Not the full reference manual."
metadata:
  skill_id: "skl_wZUpeFiR__15vhz_GSzEAQ"
  title: "Terraform workflow: zero-downtime resource replacement"
  version: "skv_WHRTHC2AIueVP_-U3JXPsw"
  updated: "2026-10-03T05:58:48.132551+00:00"
  canonical_url: "https://vectle.com/skills/skl_wZUpeFiR__15vhz_GSzEAQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developer.hashicorp.com/terraform/docs/language/meta-arguments/lifecycle\"]"
---

**TL;DR:** Replacing a resource normally destroys then creates, causing an outage window. The workflow uses create_before_destroy plus dependency design to keep serving traffic throughout. Add create_before_destroy = true to the resource's lifecycle block. Check the plan: it must show create then destroy in that order.

## When

Replacing load balancers, instance groups, DNS records, or anything in the serving path where a destroy-then-create gap means downtime.

## Steps

1. Add `create_before_destroy = true` to the resource's lifecycle block. Terraform now creates the replacement before destroying the old one.
2. Check the plan: it must show create then destroy in that order. If the provider cannot support it for this resource type, the plan will tell you; not all resources can be replaced this way.
3. Design for it: the replacement must be able to coexist with the old one briefly. That means no unique-name conflicts (use name_prefix or generated names, not fixed names), and dependencies must tolerate two instances existing at once.
4. Apply and watch: confirm the new resource is healthy (passing health checks, serving traffic) before the old one is destroyed. Terraform orders this automatically, but verify.
5. For data resources that cannot coexist (single static IP, single DNS name), the pattern shifts: create the new infra alongside, switch the pointer (DNS, target group), then destroy the old. Two applies, explicit cutover.

## Rules for agents

1. `create_before_destroy` on a resource with a fixed unique name fails: the create collides with the existing object. Name conflicts are the number one reason this pattern breaks; use generated names.
2. Dependencies of the replaced resource also get the ordering. Check the plan for cascading replacements you did not intend.
3. Test the replacement in non-prod first, including the traffic cutover. "It planned fine" is not "it serves traffic fine".
4. After replacement, confirm the old resource is actually gone and the new one is the one serving. Leftover old resources are silent cost and confusion.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Terraform behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_wZUpeFiR__15vhz_GSzEAQ). Version: `skv_WHRTHC2AIueVP_-U3JXPsw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
