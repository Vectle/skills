---
name: "pscale-unknown-flag-org-put-org-on-the-79076f8cf71da35f"
description: "Fixes pscale failing with unknown flag: --org. Use when targeting a non-default organization and the CLI rejects the flag placement. Moves --org after the subcommand (pscale database list --org my-org) instead of before it. Not for auth errors or genuinely unknown flags."
metadata:
  skill_id: "skl_d3EBQmjV2yZf3zBC_6YLYw"
  title: "pscale: unknown flag: --org (put --org on the subcommand)"
  version: "skv_eYEPFagFjnE05P1FOPI0Xw"
  updated: "2026-10-03T06:00:38.627995+00:00"
  canonical_url: "https://vectle.com/skills/skl_d3EBQmjV2yZf3zBC_6YLYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# pscale: unknown flag: --org (put --org on the subcommand)

TL;DR: pscale parses flags per subcommand, so a global-looking `pscale --org my-org database list` is rejected: --org is not a root flag. Put it after the subcommand instead: `pscale database list --org my-org`. The same applies to other subcommand flags that look global.

```text
unknown flag: --org
```

## Steps

1. Rewrite the command with the flag after the subcommand: `pscale database list --org my-org`.

2. Rerun. Expected: the command executes against that org instead of the flag error.

3. If you script it, set the org once per command or export the default org so scripts do not need the flag at all.

4. For other `unknown flag` errors, run `pscale [subcommand] --help` to see which flags that subcommand actually accepts.

## When this applies

- the exact `unknown flag: --org` error
- scripts that worked with an older CLI layout and broke after an update
- any pscale flag rejected at the root but accepted on the subcommand

## When it doesn't

- auth failures — those happen after the flags parse
- flags that truly do not exist on the subcommand either (check --help)
- shell quoting issues around the org name

## Compatibility

pscale CLI; per-subcommand flag parsing. Verified against the official PlanetScale CLI docs.

## Variant phrasings

- pscale unknown flag org
- pscale --org flag placement
- planetscale cli org flag error

## Root cause

pscale uses per-command flag sets rather than global flags, so the parser only knows --org in the context of commands that declare it. Root-level placement fails parsing before anything else runs.

## Edge cases

- the default org can be set so most commands skip the flag entirely
- in scripts, prefer the explicit flag over env defaults for readability
- copy-pasted commands from docs for a different subcommand often carry misplaced flags

---

Source: [Vectle](https://vectle.com/skills/skl_d3EBQmjV2yZf3zBC_6YLYw). Version: `skv_eYEPFagFjnE05P1FOPI0Xw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
