---
name: "meltano-add-fails-in-git-submodule-upd-4aacd5054694086a"
description: "Try removing the system gettext package (or otherwise getting it off the PATH for the subprocess) rather than debugging git itself. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_avcXh1auEPaZbDSx80cQmQ"
  title: "Meltano add fails in git submodule update: remove conflicting gettext"
  version: "skv_BxHpxlQE6M3FcIyNde54yQ"
  updated: "2026-10-03T04:35:03.581871+00:00"
  canonical_url: "https://vectle.com/skills/skl_avcXh1auEPaZbDSx80cQmQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/meltano/meltano/issues/9701\"]"
---

## TL;DR

Try removing the system gettext package (or otherwise getting it off the PATH for the subprocess) rather than debugging git itself. When an agent hits tool-subprocess failures that do not reproduce with the same command run manually, compare the subprocess environment's PATH against the interactive shell before assuming the tool is at fault. The host system had gettext 0.21 but the Meltano/uv subprocess environment was injecting a gettext 0.22.5 whose gettext.

## Fix

If meltano add fails in git submodule update with a gettext.sh usage error, the host's gettext installation is conflicting with the one the Meltano subprocess sees. Try removing the system gettext package (or otherwise getting it off the PATH for the subprocess) rather than debugging git itself. When an agent hits tool-subprocess failures that do not reproduce with the same command run manually, compare the subprocess environment's PATH against the interactive shell before assuming the tool is at fault.

Context: GitHub issue meltano/meltano#9701 (closed, 11 comments): meltano add failed during git submodule update with GNU gettext shell script function library version 0.22.5 / Usage: . gettext.sh. The host system had gettext 0.21 but the Meltano/uv subprocess environment was injecting a gettext 0.22.5 whose gettext.sh was incompatible with what git's scripts expected. Manual git clone and submodule updates worked fine outside Meltano. The maintainer's fix: uninstall gettext entirely from the environment, which resolved the conflict and let meltano add complete.

## Matched source
Source: Published skill
Original query: "Meltano add fails in git submodule update: remove conflicting gettext"
Key terms: conflicting, fails, gettext, meltano, remove, submodule, update

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_avcXh1auEPaZbDSx80cQmQ). Version: `skv_BxHpxlQE6M3FcIyNde54yQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
