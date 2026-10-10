---
name: "error-failed-to-save-state-4734c378da4e2c70"
description: "Recovers from OpenTofu's 'Error: Failed to save state' when apply succeeds but the backend write fails. Use when tofu parks state in errored.tfstate and tells you not to re-run apply. Not for plan-time backend config errors."
metadata:
  skill_id: "skl_qKC5Z37eJ3aDU00P_n0rag"
  title: "Error: Failed to save state"
  version: "skv_CIMFFuO2Jf0g1_2dNlOqoA"
  updated: "2026-10-03T05:59:15.459337+00:00"
  canonical_url: "https://vectle.com/skills/skl_qKC5Z37eJ3aDU00P_n0rag"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: tofu applied your changes but couldn't write the new state to the backend. Your infrastructure changed; the state is parked in `errored.tfstate` in the working directory. Do NOT re-run apply (it forks the state). Fix the backend problem, then `tofu state push errored.tfstate`.

```text
Error: Failed to save state

Error saving state: ephemeral resource
"ephemeral.random_password.session_token" detected in the current state.
This is an error in OpenTofu
```

```text
Error: Failed to persist state to backend

The error shown above has prevented OpenTofu from writing the updated state
to the configured backend. To allow for recovery, the state has been
written to the file "errored.tfstate" in the current working directory.

Running "tofu apply" again at this point will create a forked state, making
it harder to recover.

To retry writing this state, use the following command:
    tofu state push errored.tfstate
```

## Steps

1. Stop. Do not re-run `tofu apply`. Confirm `errored.tfstate` exists in the working directory.
   Expected: `ls errored.tfstate` finds the file.
2. Read the FIRST error (above the persist message). That's the actual cause: backend credentials, network, a lineage mismatch, or an engine bug like an ephemeral resource leaking into state.
   Expected: you can name the cause.
3. Fix the cause: refresh expired backend credentials, restore network to the backend, or resolve the lineage mismatch by pulling (`tofu state pull`) and comparing which copy is authoritative.
   Expected: the underlying write path works again.
4. Push the parked state: `tofu state push errored.tfstate`.
   Expected: `tofu state pull` afterwards shows the new serial.
5. Delete `errored.tfstate` once the push succeeds, so a later run doesn't pick up a stale file.
   Expected: working directory clean.

## When this applies

- `tofu apply` reports success on resources, then fails with `Failed to save state` / `Failed to persist state to backend`.
- You see an `errored.tfstate` file after a run.

## When it doesn't apply

- `Error: Backend initialization required` is an init problem, not a save problem.
- `Error: Failed to acquire state lock` happens BEFORE apply, not after.

## Tool versions

All OpenTofu versions. The `errored.tfstate` recovery flow is built into every backend.

## Why it happens

State is written after the infrastructure changes are done, so a backend outage, permission failure, or state-format bug strands you: the real world moved, the backend didn't. tofu writes the state locally instead of dropping it, and refuses to let a second apply build on a backend that doesn't know about the first.

## Edge cases

- Lineage mismatches (`Lineage is not equal to one in workspace state`, often an HTTP 412) mean you're pushing a state file that doesn't belong to that workspace. Pull first, compare the `lineage` fields, and only use `push -force` once you've confirmed your file is the authoritative one.
- If the parked state itself is corrupt, push a known-good backup instead, then reconcile drift with plan.
- Backends with versioning (S3): you can also restore the previous good version from the bucket as a fallback.

---

Source: [Vectle](https://vectle.com/skills/skl_qKC5Z37eJ3aDU00P_n0rag). Version: `skv_CIMFFuO2Jf0g1_2dNlOqoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
