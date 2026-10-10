# Vectle skills

Public engineering guidance from [Vectle](https://vectle.com), mirrored automatically for agent skill discovery and installation. Vectle remains the canonical source; every skill links to its source page and preserves its immutable version ID and public contributor attribution.

## Browse and install

Browse [the live catalog](https://vectle.com/skills) or the generated [`skills.json`](skills.json) index. Skills use stable installation-name directories under `skills/`; names include a short source-ID digest so identical titles remain distinct. Directory names and frontmatter follow the [Agent Skills specification](https://agentskills.io/specification).

```sh
npx skills add Vectle/skills --list
npx skills add Vectle/skills --skill <name-from-skills.json>
```

See the [installer documentation](https://github.com/vercel-labs/skills#readme). Select the guidance you need; this repository can contain thousands of skills.

## Automatic sync

[Sync public skills](https://github.com/Vectle/skills/actions/workflows/sync.yml) runs daily at **07:37 UTC**, and can be run manually from Actions. GitHub may delay scheduled runs. A small [`sync-status.json`](sync-status.json) receipt records each month's successful catalog check, keeping the repository active even during quiet periods so GitHub's 60-day schedule-inactivity rule does not disable the sync. See [GitHub's schedule behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

The sync reads the existing public `sitemap-skills.xml` discovery export, then anonymously reads new or changed skills through `GET /api/v1/skills/{skill_id}`. Sitemap dates plus local content hashes avoid repeatedly fetching unchanged bodies. Discovery is refreshed daily by Vectle, so newly published guidance can take up to two daily cycles to reach this mirror. Synthetic fixtures and search-excluded entries stay out of the repository.

Only successful, current public skill reads are published. Empty, malformed, failed or substantially reduced discovery exports fail without changing the mirror. Every required read must succeed before any generated files change. Entries no longer in the discovery export are removed only from manifest-owned paths. No-change runs do not create commits, apart from the monthly successful-check receipt. No Vectle credentials, database access, API writes, or external AI services are needed. GitHub's built-in token can write only to this repository.

For local maintenance (Python 3.10+; standard library only):

```sh
python3 -m unittest discover -s tests -v
python3 scripts/sync.py
```

Edit the sync and README, rather than generated skill files. A title edit keeps the original installation name stable. Update the workflow with a pull request; its tests run before live syncing. Failed runs are visible in Actions and retain the last successfully published catalog. For a genuine removal exceeding 10% of the catalog, inspect the source export and deliberately update the guard after review; never bypass it for an outage.

## Content rights

This repository is Vectle's public service distribution mirror, not a training dataset. Contributors retain ownership. Content remains subject to [Vectle's terms](https://vectle.com/terms) and any rights or licenses stated by its contributors. Mirroring does not relicense contributions under MIT, CC-BY, or another blanket license, or grant model training, fine-tuning, benchmarking, model evaluation, or dataset-creation rights. Preserve source links, contributor attribution and any notices when using guidance. Skills are community material; verify technical guidance against your own environment and its cited upstream sources.
