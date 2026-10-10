---
name: "error-test-assertion-failed-ddb899f0f90765bb"
description: "Explains OpenTofu's 'Error: Test assertion failed' from tofu test: how to read the actual-vs-expected output and decide whether the config or the assertion is wrong. Use when a .tftest.hcl run block fails its assert. Not for engine errors or syntax errors inside test runs."
metadata:
  skill_id: "skl_7sSWOYDaziqjtCPnPBdyCw"
  title: "Error: Test assertion failed"
  version: "skv_qQlUDGe6aASjPFheQUwv3Q"
  updated: "2026-10-03T05:31:03.719359+00:00"
  canonical_url: "https://vectle.com/skills/skl_7sSWOYDaziqjtCPnPBdyCw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: One of the `assert` blocks in your `.tftest.hcl` file evaluated to false. This is not a tofu bug: the error shows you the exact condition, the actual value, and the expected value. Read the `is` lines, decide whether the config or the assertion is wrong, fix that side, and re-run.

```text
tests/integration.tftest.hcl... fail
  run "localstack_apply"... fail

Error: Test assertion failed

  on tests/integration.tftest.hcl line 5, in run "localstack_apply":
   5:     condition     = can(regex("^s3-${var.expected_project}-d-web-[a-f0-9]{4}$", output.bucket_name))
    ├────────────────
    │ output.bucket_name is "s3-crmapp-d-web-3641"
    │ var.expected_project is "orders"

expected project orders in bucket name, got s3-crmapp-d-web-3641.

Failure! 0 passed, 1 failed.
```

## Steps

1. Find the `condition` line and the `│ ... is ...` lines. The `is` lines are ground truth: what tofu actually saw.
   Expected: you can point at the actual value and the expected value.
2. Decide which side is wrong. If the config produced the wrong value, fix the config. If your expectation was stale (for example you overrode a variable just for the test run), fix the assertion.
   Expected: you know which file to edit.
3. Re-run just that file: `tofu test -filter=tests/integration.tftest.hcl`.
   Expected: `Success! 1 passed, 0 failed.`

## When this applies

- `tofu test` prints `fail` on a run block, followed by `Error: Test assertion failed`.

## When it doesn't apply

- `Error: Missing required argument` or other engine errors inside a test run mean the config itself is broken, not the assertion.
- A run that errors during apply (not during assert) is an infrastructure problem, not a failed expectation.

## Tool versions

OpenTofu 1.6 and later, which ship the native test framework (`.tftest.hcl` files, `assert` blocks).

## Why it happens

`assert` blocks are postconditions on a plan or apply: tofu evaluates each condition after the run, and a false condition fails the run by design. The verbose output (actual values, diffs) exists precisely so you can tell a wrong config apart from a wrong expectation.

## Edge cases

- `-filter` selects test FILES, not individual run blocks. You can't run a single `run` block in isolation.
- A failed apply run still gets cleaned up by tofu; you don't need to destroy test leftovers by hand.
- For tests that are supposed to fail (invalid input should be rejected), use `expect_failures` instead of watching asserts fail.

---

Source: [Vectle](https://vectle.com/skills/skl_7sSWOYDaziqjtCPnPBdyCw). Version: `skv_qQlUDGe6aASjPFheQUwv3Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
