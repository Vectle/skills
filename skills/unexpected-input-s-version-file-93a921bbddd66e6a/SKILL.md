---
name: "unexpected-input-s-version-file-93a921bbddd66e6a"
description: "Why GitHub Actions logs Unexpected input(s) warnings for an action input you passed, and how to fix the typo without breaking the workflow. Use when the step log shows Unexpected input(s) warnings or an action seems to ignore a with: value."
metadata:
  skill_id: "skl_IpJNZ_FG7OpnnYQAYeMZHw"
  title: "Unexpected input(s) 'version-file'"
  version: "skv_tSi2Mhj2C9UfPJGTWHMeKg"
  updated: "2026-10-03T05:55:48.3415+00:00"
  canonical_url: "https://vectle.com/skills/skl_IpJNZ_FG7OpnnYQAYeMZHw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Check the action's action.yml for the real input name (often version vs version-file, or kebab-case vs snake_case after a major bump) and rename the key. The runner drops the unknown input and carries on, so the step runs without whatever that input was meant to do. The warning is the only trace.

```text
Unexpected input(s) 'version-file', valid inputs are ['version', 'mirror', 'use-cache', 'cache-key', 'cache-size-limit', 'use-tool-cache']
```

## The fix

1. Open the pinned action's action.yml at the exact ref you use and read its inputs: section. The valid list in the warning is the same list.

2. Fix the key name in your workflow, for example:
   ```yaml
   # before
   - uses: mlugg/setup-zig@v1
     with:
       version-file: build.zig.zon   # does not exist, silently ignored
   # after
   - uses: mlugg/setup-zig@v1
     with:
       version: 0.13.0               # or remove the key if the default is what you want
   ```

3. If the action changed input names across a major version (for example repo-token to repo_token in actions/first-interaction v3), rename every key and re-read the required inputs - a renamed required input also errors as Input required and not supplied.

4. Rerun and confirm the warning is gone from the step log.

## When this applies

- the step log shows Unexpected input(s) warnings
- an action seems to ignore a with: value you set
- after bumping an action across a major version

## When it does NOT apply

- the input IS declared but the step errors - that is a different bug in the value, not the name

## Compatibility

All runners; warning text is stable across runner versions.

## Variants of this error

### `##[warning]Unexpected input(s) 'targets', valid inputs are ['toolchain', 'target', ...]`
The plural-substring form, for example targets vs target.

### `Unexpected input(s) 'repo-token', 'issue-message', valid inputs are ['issue_message', ...]`
The form after actions/first-interaction v1 to v3 renamed its inputs to snake_case.

## Why it happens

The runner validates with: keys against the action's declared inputs before running it. Undeclared keys are not an error by design (for forward compatibility), so they are logged as warnings and dropped. The step then behaves as if you never passed the value, which is why the failure shows up far from the typo.

## Edge cases and pitfalls

- actionlint does not always catch this for actions pinned by commit SHA, so the runner log is the only instrument in that case.
- Defaults can hide the bug: if the real input defaults to what you wanted, the workflow works by accident and the warning is the only trace.

---

Source: [Vectle](https://vectle.com/skills/skl_IpJNZ_FG7OpnnYQAYeMZHw). Version: `skv_tSi2Mhj2C9UfPJGTWHMeKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
