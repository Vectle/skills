---
name: "jenkins-unstash-fails-on-stashed-symli-b39a98ce04d69dd6"
description: "If your stashes legitimately contain symlinks, set the documented escape hatches on the agent JVM: -Dhudson.FilePath.ALLOW_REENTRY_PATH_TRAVERSAL=true and -Dhudson.FilePath.ALLOW_UNTAR_SYMLINK_RESOLUTION=true, added to the agent launch command or the agent JVM options. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_5W5bZJT9C-3prC0rk8z6Rw"
  title: "Jenkins unstash fails on stashed symlinks after the path traversal fix"
  version: "skv_UhMPRMhk4JfoKqAnKYUozA"
  updated: "2026-10-03T05:08:23.918094+00:00"
  canonical_url: "https://vectle.com/skills/skl_5W5bZJT9C-3prC0rk8z6Rw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/jenkinsci/jenkins/issues/26563\"]"
---

## TL;DR

If your stashes legitimately contain symlinks, set the documented escape hatches on the agent JVM: -Dhudson.FilePath.ALLOW_REENTRY_PATH_TRAVERSAL=true and -Dhudson.FilePath.ALLOW_UNTAR_SYMLINK_RESOLUTION=true, added to the agent launch command or the agent JVM options. Maintainer daniel-beck confirmed this works around the failure, and since the security fix targets traversal on the controller, the agent-side opt-out does not weaken security for typical setups.

## Fix

The block comes from the core path-traversal guard in FilePath operations. If your stashes legitimately contain symlinks, set the documented escape hatches on the agent JVM: -Dhudson.FilePath.ALLOW_REENTRY_PATH_TRAVERSAL=true and -Dhudson.FilePath.ALLOW_UNTAR_SYMLINK_RESOLUTION=true, added to the agent launch command or the agent JVM options. Maintainer daniel-beck confirmed this works around the failure, and since the security fix targets traversal on the controller, the agent-side opt-out does not weaken security for typical setups. Longer term, prefer fixing the stash contents (keep symlinks inside the workspace) over leaving the hatches open forever.

Context: GitHub issue jenkinsci/jenkins#26563 (closed, 13 comments): a pipeline stashes a directory containing symlinks, and the unstash step can no longer restore them. The cause is a Jenkins core security fix that blocks path traversal during untar operations, which also catches legitimate symlinks inside stashes.

## Matched source
Source: Published skill
Original query: "Jenkins unstash fails on stashed symlinks after the path traversal fix"
Key terms: after, fails, jenkins, path, stashed, symlinks, traversal, unstash

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_5W5bZJT9C-3prC0rk8z6Rw). Version: `skv_UhMPRMhk4JfoKqAnKYUozA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
