---
name: "jenkins-shell-step-keep-the-build-gree-d982c38d1d48605b"
description: "Use it deliberately per command, not as a blanket set +e, so real failures still fail the build. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_Rs9bCQU1f5Cwb2QZnJdA8w"
  title: "Jenkins shell step: keep the build green when a command exits nonzero"
  version: "skv_JsA6a-g5YPzXwoWLYcTgNg"
  updated: "2026-10-03T05:07:52.291904+00:00"
  canonical_url: "https://vectle.com/skills/skl_Rs9bCQU1f5Cwb2QZnJdA8w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use it deliberately per command, not as a blanket set +e, so real failures still fail the build. The asker wants the build to survive that. The accepted answer gives the shell idiom for controlling step failure explicitly.

## Fix

Suffix the command with || true to let the step continue past the failure, or || exit 0 to stop the script there while still reporting success. For the opposite behavior, do nothing: Jenkins fails the step on the first nonzero exit by default. The same idiom works inside sh steps in Declarative pipelines. Use it deliberately per command, not as a blanket set +e, so real failures still fail the build.

Context: Stack Overflow #14392349 (accepted answer, 181 votes): an execute-shell step runs git commit, which exits nonzero when there is nothing to commit, and Jenkins marks the whole build failed. The asker wants the build to survive that. The accepted answer gives the shell idiom for controlling step failure explicitly.

## Matched source
Source: Published skill
Original query: "Jenkins shell step: keep the build green when a command exits nonzero"
Key terms: build, command, exits, green, jenkins, keep, nonzero, shell, step

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_Rs9bCQU1f5Cwb2QZnJdA8w). Version: `skv_JsA6a-g5YPzXwoWLYcTgNg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
