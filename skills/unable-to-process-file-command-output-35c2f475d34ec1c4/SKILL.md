---
name: "unable-to-process-file-command-output-35c2f475d34ec1c4"
description: "Fixes 'Unable to process file command 'output' successfully' when writing step outputs. Use when $GITHUB_OUTPUT writes fail with Invalid format. Not for $GITHUB_ENV issues."
metadata:
  skill_id: "skl_9FIiJRezotJcR_vd7VTPhQ"
  title: "Unable to process file command 'output' successfully in GitHub Actions"
  version: "skv_dHKrNNhWV9URe-2woHaS_g"
  updated: "2026-10-03T05:33:44.821151+00:00"
  canonical_url: "https://vectle.com/skills/skl_9FIiJRezotJcR_vd7VTPhQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Write multi-line values with the heredoc form (name<<EOF on its own lines) instead of echo "name=$value"; every line appended to $GITHUB_OUTPUT must be name=value on a single line. The runner parses $GITHUB_OUTPUT line by line, so a value containing newlines looks like several malformed entries and the step fails.

```text
Unable to process file command 'output' successfully
```

## The fix

1. Find the line that writes the multi-line value, e.g. echo "report=$REPORT" >> "$GITHUB_OUTPUT".
   Expected: You see the plain key [your value] write.

2. Replace it with the heredoc form, delimiter alone on its line:
   ```bash
   echo "report<[EOF"]> "$GITHUB_OUTPUT"
   echo "$REPORT" >> "$GITHUB_OUTPUT"
   echo "EOF" >> "$GITHUB_OUTPUT"
   ```
   Expected: The step completes; downstream steps read the full multi-line value.

3. Use a delimiter that cannot appear in the value (e.g. REPORT_EOF) if the value might contain EOF.
   Expected: No more Invalid format or Matching delimiter not found errors.

## When this applies

- a step fails with Unable to process file command 'output' successfully plus Invalid format '...'
- you write command output, JSON, or markdown into $GITHUB_OUTPUT

## When it does NOT apply

- the error names file command 'env' instead (same idea, but the file is $GITHUB_ENV)
- the value is single-line (then look for a missing key [your value] instead)

## Compatibility

GitHub Actions runners on all OSes. Applies to $GITHUB_OUTPUT and, by analogy, $GITHUB_ENV.

## Variants of this error

### `##[error]Invalid format '...'`
The detail line naming the offending line. Same fix.

### `##[error]Invalid value. Matching delimiter not found 'EOF'`
The delimiter collided with file content or was not alone on its line. Pick a unique delimiter and ensure a trailing newline before it.

## Why it happens

$GITHUB_OUTPUT replaced the old ::set-output command with a plain file protocol: one name=value per line, or a heredoc block. Anything else in the file is a parse error, and the runner fails the step rather than guessing.

## Edge cases and pitfalls

- If the value is produced by cat file >> $GITHUB_OUTPUT, make sure the file ends with a newline or the closing delimiter glues onto the last line.
- Values containing the delimiter string terminate the block early; generate a random delimiter for untrusted content.
- Composite actions have the same rule; the error looks identical.

---

Source: [Vectle](https://vectle.com/skills/skl_9FIiJRezotJcR_vd7VTPhQ). Version: `skv_dHKrNNhWV9URe-2woHaS_g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
