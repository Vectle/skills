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

[Sync public skills](https://github.com/Vectle/skills/actions/workflows/sync.yml) runs daily at **07:37 UTC**, and can be run manually from Actions. Scheduled and push-triggered runs use two artifact workers. Manual dispatch defaults to two and offers one through four; the command-line `--workers` option has the same default and bounds. GitHub may delay scheduled runs. A small [`sync-status.json`](sync-status.json) receipt records each month's successful catalog check, keeping the repository active even during quiet periods so GitHub's 60-day schedule-inactivity rule does not disable the sync. See [GitHub's schedule behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

The publisher reads the supported [`/exports/skills/v1/catalog`](https://vectle.com/exports/skills/v1/catalog) representation. The backend owns eligibility, stable installation names and exact immutable-version `SKILL.md` bytes. Search ranking and sitemap inclusion do not define distribution. The publisher accepts schema 1, artifact format 2, policy `public-service-distribution-1` and the frozen compatibility name-map revision. An incompatible revision stops publication until its consumer has been reviewed.

Every metadata page must belong to one snapshot, with unique ordered IDs and install names, the expected total and the exact rolling digest. Only the signed terminal certificate permits artifact fetching. The publisher downloads changed, missing or locally corrupt artifacts with two workers by default, checks exact SHA-256 and Agent Skills provenance/frontmatter, and stages them outside the repository. It copies the server's bytes without reconstructing the authored body. A title edit keeps its installation name. Format 2 preserves original public attribution and notices; it deliberately replaces format 1's artifact hashes while preserving install paths.

Immediately before publication, the publisher submits the complete ordered signed claims to the metadata-only admission validator. This rechecks current eligibility and original rights inputs even for unchanged local files. An ordinary newer skill version does not invalidate the pinned dated snapshot. A new restriction stops adoption. Catalog enumeration and final admission validation each restart at most three times on generation drift. Each request has a 30-second aggregate deadline, five attempts, a 2 MiB JSON/256 KiB artifact limit and bounded Retry-After/backoff of at most 120 seconds. The whole job is limited to 300 minutes; expired snapshots or exhausted retries fail honestly.

Publication uses one non-force Git commit/push containing files and index. The branch must still equal the expected starting commit, its published source generation cannot be newer, and the final receipt must be less than five minutes old when pushing. Concurrent branch advancement or push rejection stops the run. A fresh rerun reconciles current main; it never force-pushes or restores old generated files. Failed/interrupted reads, malformed/incomplete pages and checksum mismatches leave the remote valid catalog intact. Only paths owned by the previous validated manifest may be removed. Hand-maintained neighboring files are retained.

No-change checks do not rewrite the catalog or artifacts. The monthly `sync-status.json` receipt keeps a quiet schedule active. Every attempt records bounded operational metadata in its Actions logs and job summary: source snapshot/time/revisions, publisher revision, prior/new commit, selected/added/updated/removed/unchanged counts, outcome, lag and failure category. Successful no-change checks count as successful checks. Failures never advance last-success. These records distinguish source publication, validated export, Git push and installer verification; the daily publisher does not claim a real installer check.

The operating objective is a successful current-generation check within 24 hours and an actionable stale status after 48 hours. These are operating objectives; GitHub does not guarantee scheduling. Failed runs use existing repository Actions notifications. The distribution owner checks the latest successful **main sync** and failed-run summary, then follows the recovery steps below. Review actual workload, lag and failures after the first 14 days before adjusting cadence. GitHub failure never delays canonical skill publication.

### Maintenance and recovery

Python 3.10+ and its standard library are sufficient:

```sh
python3 -m unittest discover -s tests -v
# Read-only complete-set reconciliation; report is outside generated output.
python3 scripts/sync.py --inventory-only --report /tmp/vectle-inventory.json
# Validate/stage the complete snapshot into this isolated checkout, without push.
python3 scripts/sync.py --report /tmp/vectle-attempt.json
# Actions uses --publish only from a clean checkout equal to current origin/main.
```

Edit the publisher and README rather than generated skills. A new export schema/format/policy must be coordinated with the API owner before adoption. No Vectle account credentials, database access or content-write permissions enter the publisher; only GitHub's repository-scoped workflow token publishes to this repository.

- **Partial export, timeout, expiry, corruption or failed push:** preserve the failed run. Correct the cause and rerun from a fresh current-main checkout. A newer complete snapshot supersedes the interrupted one. Do not retry a rejected local commit by force-pushing.
- **Cancelled initial adoption:** [run 40191681894](https://github.com/Vectle/skills/actions/runs/40191681894) validated metadata for 21,397 entries; its last artifact progress checkpoint was 1,200 before operator cancellation on October 25, 2026. It did not publish a new mirror. Cancellation during broad service variability does not establish that the publisher caused that variability. A fresh run restarts staging; temporary runner artifacts are not a persisted checkpoint. Two workers reduce concurrent reads, but do not guarantee completion within the existing 300-minute job or six-hour snapshot lifetime. Fast and degraded portions of that run had materially different throughput; expired or unfinished runs must continue to fail without publication.
- **Zero or large reduction:** the existing `max(10, floor(previous_count/10))` removal guard remains; every zero-entry replacement also stops. Investigate the complete old/current/export membership difference with the API/distribution owner. Record the selection explanation and operator review in [the owning issue](https://github.com/Vectle/vectle/issues/843). Supply a JSON file using `--selection-review` only after that review, containing the exact `selection_review_binding` emitted by the held attempt plus `decision: "approve"`, nonempty `reason`, `reviewed_by` and the supporting `evidence_url`. The previous manifest hash, target count, removed-ID hash and terminal manifest digest must all match. Never weaken the guard to recover an outage.
- **Known rights/admission restriction:** `EXPORT_RESTRICTED` marks the attempt **unsafe/stopped**. Escalate to the existing distribution owner and reconcile current admission. Do not describe the old copy as currently authorized. A successful complete reconciliation removes excluded generated paths from the current tree; Git history and installed third-party copies cannot be promised erased.
- **Stale check:** a failed run reports the prior successful main check and marks it stale after 48 hours. Inspect Actions even if the schedule stops firing; `sync-status.json` is a monthly keepalive, not a daily freshness claim. Use manual dispatch after correcting the cause. No new personal reminder or service dashboard is required.
- **Rollback:** restore the prior compatible publisher/export implementation, retaining a consumer-compatible schema, then reconcile against **current admission**. Never restore stale generated content blindly after a rights change. Preserve failed evidence and link the recovery run/commit.

For initial adoption, reconcile all old and new public IDs and stable names, classify additions/removals, and verify the complete count/digest. Source-published, export-valid, Git-pushed and install-verified remain separate until the integration owner records actual export → GitHub → supported installer listing and selected exact installation evidence in [#843](https://github.com/Vectle/vectle/issues/843). No new registry, content license or skill publication gate is introduced.

## Content rights

This repository is Vectle's public service distribution mirror, not a training dataset. Contributors retain ownership. Content remains subject to [Vectle's terms](https://vectle.com/terms) and any rights or licenses stated by its contributors. Mirroring does not relicense contributions under MIT, CC-BY, or another blanket license, or grant model training, fine-tuning, benchmarking, model evaluation, or dataset-creation rights. Preserve source links, contributor attribution and any notices when using guidance. Skills are community material; verify technical guidance against your own environment and its cited upstream sources.
