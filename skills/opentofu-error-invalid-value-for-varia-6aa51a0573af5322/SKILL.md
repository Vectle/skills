---
name: "opentofu-error-invalid-value-for-varia-6aa51a0573af5322"
description: "Diagnoses OpenTofu and Terraform 'Error: Invalid value for variable' plan failures: read the failing validation rule from the diagnostic, trace which precedence layer supplied the bad value (TF_VAR_ env vars lose to .tfvars files), and fix the value or the rule. Use when tofu plan or apply stops on a variable validation error. Not for type-constraint errors, precondition failures, or invalid references inside validation blocks."
metadata:
  skill_id: "skl_bewx0zzn7BUyJd5eV6ZQBA"
  title: "opentofu Error: Invalid value for variable"
  version: "skv_g-rP-qYXVG363gke-c-rYg"
  updated: "2026-10-03T14:05:04.638545+00:00"
  canonical_url: "https://vectle.com/skills/skl_bewx0zzn7BUyJd5eV6ZQBA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/platformrelay/opentofu-workshop/blob/HEAD/labs/day-1/06-variables.solution.md\",\"https://opentofu.org/docs/language/values/variables/#custom-validation-rules\"]"
---

## TL;DR

This error means a `validation` block on one of your input variables rejected the value you passed. Read the lines under the error: they name the variable, show the value it got, and print the rule's custom error message. Fix the value so it satisfies the rule, then plan again. The value usually comes from the wrong precedence layer (a `TF_VAR_` env var losing to a `.tfvars` file, or a stale default), not from a typo in the rule.

### Verbatim error

```text
Error: Invalid value for variable

  on main.tf line 16:
  16: variable "service" {
    |----------------
    | var.environment is "prod"
    | var.service.replicas is 1

A prod service needs at least 2 replicas (got 1).

This was checked by the validation rule at main.tf:27,3-13.
```

## When this applies

- You ran `tofu plan` or `tofu apply` and got `Error: Invalid value for variable`.
- The diagnostic names a variable and prints a custom rule message (the text after the value lines).
- You pass variables via `-var`, `TF_VAR_` env vars, `.tfvars` files, or module inputs.

## When this does NOT apply

- `Error: Incorrect attribute value type`: that is a type-constraint failure, not a validation rule. Fix the value's type instead.
- `Error: Invalid reference in variable validation` (pre-1.9 engines): the rule itself references another variable, which old engines forbid. Upgrade OpenTofu instead.
- Errors inside `lifecycle` `precondition` blocks: those say `precondition failed`, a different diagnostic with different fixes.

## Fix

### 1. Read which variable and which rule fired

The diagnostic names the variable and the exact validation rule location (e.g. `main.tf:27,3-13`). The custom error message below the value lines tells you the constraint in plain language.

Expected output: you can point at one variable and one rule.

### 2. Find where the rejected value came from

Variable values resolve in this precedence order (later wins): environment variables (`TF_VAR_name`), `terraform.tfvars`, `*.auto.tfvars` (alphabetical), `-var` and `-var-file` flags on the command line. Check each layer:

```bash
tofu plan -var='environment=prod' -var='service={name="checkout",tier="standard",replicas=2}'
```

Expected output: the plan proceeds once the winning layer carries a valid value. A common surprise: a `TF_VAR_` env var silently loses to a `.tfvars` file.

### 3. Satisfy the rule or fix the rule

Either change the value to meet the constraint (e.g. raise `replicas` to 2 for a prod service), or, if the rule is wrong, edit the `validation` block's `condition`. Since OpenTofu 1.9, validation rules may reference other variables, so also check the cross-referenced variable's value.

Expected output: `tofu plan` runs clean, or reports a different, later error.

### 4. Confirm with a clean plan

```bash
tofu plan -no-color 2>&1 | head -20
```

Expected output: no `Invalid value for variable` diagnostic; the plan shows proposed changes or `No changes`.

## Variant phrasings

### tofu plan fails on variable validation
Same diagnostic; follow the same steps. `terraform plan` behaves identically since OpenTofu shares the validation semantics.

### Invalid value for variable in a module call
The diagnostic points at the module block line (e.g. `in module "bucket_name"`). The fix is the same, but you get one diagnostic per call site passing the bad value: fix the value once at the source.

## Why it happens

`validation` blocks are assertions the module author writes on input variables. OpenTofu evaluates them before planning any resources, so a failing rule stops the run early with this diagnostic. The value that fails is rarely the one you think you passed: precedence layers (env var vs tfvars vs CLI flag) mean a stale or broader-scoped value can win silently.

## Edge cases

- A `null` value fails validation unless the rule explicitly allows it; check `nullable` handling in the rule condition.
- Cross-variable validation (1.9+) prints all referenced variables' values; fix any of them to satisfy the combined condition.
- One bad value passed into several module call sites produces one diagnostic per site; fix the source value once.
- `tofu validate` catches some of these without provider credentials, useful in CI.

## Tool compatibility

OpenTofu 1.x and Terraform 0.13+ (validation blocks); cross-variable references require OpenTofu 1.9+ / Terraform 1.9+.

---

Source: [Vectle](https://vectle.com/skills/skl_bewx0zzn7BUyJd5eV6ZQBA). Version: `skv_g-rP-qYXVG363gke-c-rYg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
