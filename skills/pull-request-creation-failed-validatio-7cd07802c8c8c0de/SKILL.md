---
name: "pull-request-creation-failed-validatio-7cd07802c8c8c0de"
description: "pull request creation failed. validation failed: title can't be blank"
metadata:
  skill_id: "skl_PgRiOf1u_LZrsa2vj4nh5Q"
  title: "pull request creation failed. validation failed: title can't be blank"
  version: "skv_AXZu-xUO3qVZ3qTaLhBN-Q"
  updated: "2026-11-02T16:06:51.92775+00:00"
  canonical_url: "https://vectle.com/skills/skl_PgRiOf1u_LZrsa2vj4nh5Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Create the PR with the title and body passed explicitly: `gh pr create --title "Fix the login redirect" --body "What changed and why"`. Expected: gh prints the new pull request URL instead of the validation error.

If your script builds the title from a variable, print it before creating: an unset or empty variable is the usual cause, because `--title "$TITLE"` with an empty TITLE sends a blank title that looks identical in the command line. Expected: the variable expands to a non-empty string.

If you use --fill, check the commit it reads with `git log -1 --pretty=%s`. An empty or whitespace-only commit subject becomes an empty title. Either amend the commit message or drop --fill and pass --title yourself. Expected: the subject line is a real sentence.

If you use the editor flow (-e or the interactive prompt), the first line of the file is the title. A leading blank line or a file that starts with the body makes the title blank. Put the title on line one. Expected: the saved file starts with the title text.

After a failed interactive create, gh offers to recover the input. Re-run with the --recover flag it printed, fix the title line, and submit again instead of retyping the body. Expected: the recovered draft opens with your previous input.

Confirm before you submit in scripts with `gh pr create --dry-run` plus your flags. Expected: the printed details show the exact non-empty title that will be sent.

---

Source: [Vectle](https://vectle.com/skills/skl_PgRiOf1u_LZrsa2vj4nh5Q). Version: `skv_AXZu-xUO3qVZ3qTaLhBN-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
