"""Reconcile a complete public export; publish only one validated Git snapshot."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

from export_contract import (CATALOG, LEGACY_SOURCE, REVISIONS, ID, NAME, HEX,
                             ExportFailure, artifact, canonical, catalog, instant,
                             request, require, sha256, validate)

DEFAULT_ARTIFACT_WORKERS = 2


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode()


def safe_path(root, relative):
    target = root / relative
    # Check each component, including dangling symlinks, before reading/writing.
    require(not root.is_symlink(), "Symlink repository root")
    for part in [target, *target.parents]:
        require(not part.is_symlink(), "Generated path contains a symlink")
        if part == root:
            break
    require(target.resolve().is_relative_to(root.resolve()), "Generated path escapes repository")
    return target


def load_manifest(root):
    path = safe_path(root, "skills.json")
    if not path.exists():
        return None, {}
    payload = json.loads(path.read_bytes())
    require(payload.get("schema_version") in (1, 2)
            and payload.get("source") == (LEGACY_SOURCE if payload["schema_version"] == 1 else CATALOG), "Unknown mirror manifest")
    entries, names = {}, set()
    require(isinstance(payload.get("skills"), list), "Invalid manifest skills")
    for item in payload["skills"]:
        skill, name = item.get("skill_id"), item.get("name")
        require(isinstance(skill, str) and ID.fullmatch(skill) and skill not in entries
                and isinstance(name, str) and len(name) <= 64 and NAME.fullmatch(name)
                and name not in names and item.get("path") == "skills/" + name + "/SKILL.md"
                and isinstance(item.get("sha256"), str) and HEX.fullmatch(item["sha256"]), "Invalid manifest identity/path")
        safe_path(root, item["path"])
        names.add(name)
        entries[skill] = item
    if payload["schema_version"] == 2:
        source = payload.get("snapshot", {})
        require(all(source.get(key) == value for key, value in REVISIONS.items())
                and isinstance(source.get("generation"), str) and source["generation"].isdigit(), "Unsupported published snapshot")
    return payload, entries


def index_entry(entry):
    return {"skill_id": entry["skill_id"], "name": entry["installation_name"], "title": entry["title"],
            "description": entry["description"][:1024], "url": entry["canonical_url"],
            "exact_version_url": entry["exact_version_url"], "version": entry["version_id"],
            "version_sequence": entry["version_sequence"], "updated": entry["published_at"],
            "path": "skills/" + entry["installation_name"] + "/SKILL.md",
            "format_version": REVISIONS["artifact_format_revision"], "author": entry["attribution"]["label"],
            "attribution": entry["attribution"], "source_snapshot_digest": entry["source_snapshot_digest"],
            "public_input_digest": entry["public_input_digest"], "sha256": entry["artifact_sha256"]}


def reconcile(root, selected, review=None):
    previous, old = load_manifest(root)
    entries = {entry["skill_id"]: entry for entry in selected["entries"]}
    removed = sorted(set(old) - set(entries))
    # Names are server-owned, but migration must preserve every previously
    # installed name. A collision or rename needs a backend correction.
    for skill in set(old) & set(entries):
        require(old[skill]["name"] == entries[skill]["installation_name"], "Export would rename an existing install")
    if previous and previous["schema_version"] == 2:
        require(int(selected["snapshot"]["generation"]) >= int(previous["snapshot"]["generation"]), "Obsolete source generation")
    review_binding = {"previous_manifest_sha256": sha256((root / "skills.json").read_bytes()) if previous else None,
                      "manifest_digest": selected["digest"], "target_count": len(entries),
                      "removed_ids_sha256": sha256(canonical(removed).encode())}
    if old and (not entries or len(removed) > max(10, len(old) // 10)):
        if not (isinstance(review, dict) and all(review.get(k) == v for k, v in review_binding.items())
                and review.get("decision") == "approve" and isinstance(review.get("reason"), str)
                and review["reason"].strip() and isinstance(review.get("reviewed_by"), str) and review["reviewed_by"].strip()
                and isinstance(review.get("evidence_url"), str) and review["evidence_url"].startswith("https://github.com/Vectle/")):
            error = ExportFailure("selection_review_required", "Zero/large reduction held for snapshot-bound selection explanation and operator review")
            error.review_binding = review_binding
            raise error
    index = [index_entry(entry) for entry in selected["entries"]]
    added = sorted(set(entries) - set(old))
    updated = [item["skill_id"] for item in index if item["skill_id"] in old and item != old[item["skill_id"]]]
    return previous, old, index, {"selected": len(entries), "added": len(added), "updated": len(updated),
                                  "removed": len(removed), "unchanged": len(index) - len(added) - len(updated),
                                  "added_ids": added, "removed_ids": removed, "review_binding": review_binding}


def stage(root, staging, selected, old, index, fetch=request, workers=DEFAULT_ARTIFACT_WORKERS):
    require(1 <= workers <= 4, "Artifact worker count must be 1–4")
    required, paths = [], []
    for entry, item in zip(selected["entries"], index):
        target = safe_path(root, item["path"])
        if target.exists() and entry["skill_id"] not in old:
            raise ExportFailure("unowned_path", "Export would replace an unowned generated path")
        if not target.is_file() or sha256(target.read_bytes()) != item["sha256"]:
            required.append((entry, item))
    # Artifacts have already been pinned by a complete terminal certificate.
    # At most four responses are resident at a time; bodies are immediately staged.
    def download(pair):
        entry, item = pair
        body = artifact(entry, selected["terminal_certificate"], fetch)
        target = staging / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        return item["path"]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(download, pair) for pair in required]
        try:
            for future in as_completed(futures):
                paths.append(future.result())
                if len(paths) % 100 == 0:
                    print(f"Validated artifacts: {len(paths)}/{len(required)}", flush=True)
        except BaseException:
            for future in futures:
                future.cancel()
            raise
    return paths


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def expected_base(root):
    require(not git(root, "status", "--porcelain"), "Publication requires a clean isolated checkout")
    git(root, "fetch", "origin", "main")
    head = git(root, "rev-parse", "HEAD")
    require(git(root, "rev-parse", "origin/main") == head, "Checkout is behind current main; discard and reconcile")
    return head


def check_remote(root, base, selected):
    # Fetch again after potentially hours of downloading. Neither a newer source
    # snapshot nor a competing code commit may be overwritten by this run.
    git(root, "fetch", "origin", "main")
    require(git(root, "rev-parse", "origin/main") == base and git(root, "rev-parse", "HEAD") == base,
            "Published branch advanced; discard and reconcile")
    remote = json.loads(git(root, "show", base + ":skills.json"))
    if remote.get("schema_version") == 2:
        require(int(remote["snapshot"]["generation"]) <= int(selected["snapshot"]["generation"]), "Obsolete source generation")


def apply_files(root, staging, paths, old, index):
    for relative in paths:
        target = safe_path(root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(staging / relative, target)
    current = {item["skill_id"] for item in index}
    for skill in set(old) - current:
        target = safe_path(root, old[skill]["path"])
        target.unlink(missing_ok=True)
        if target.parent.is_dir() and not any(target.parent.iterdir()):
            target.parent.rmdir()


def run(root, fetch=request, workers=DEFAULT_ARTIFACT_WORKERS, publish=False, inventory_only=False, review=None, report=None):
    report = report if report is not None else {}
    report.update({"started_at": utc_now(), "status": "running", "source_published": "independent of mirror",
                   "export_metadata_valid": False, "export_valid": False, "git_pushed": False, "install_verified": False})
    try:
        base = expected_base(root) if publish else None
        report["prior_commit"] = base
        report["publisher_revision"] = git(root, "rev-parse", "HEAD")
        selected = catalog(fetch)
        report.update({"snapshot": selected["snapshot"], "manifest_digest": selected["digest"],
                       "catalog_scans": selected["scans"], "export_metadata_valid": True})
        previous, old, index, counts = reconcile(root, selected, review)
        report.update(counts)
        if inventory_only:
            report["status"] = "inventory_valid"
            return report
        with tempfile.TemporaryDirectory(prefix="vectle-export-") as temporary:
            staging = Path(temporary)
            paths = stage(root, staging, selected, old, index, fetch, workers)
            report["artifacts_fetched"] = len(paths)
            # Snapshot identifiers/times change on every check. Preserve the
            # published manifest when its actual indexed contents are unchanged.
            manifest = previous if previous and previous["schema_version"] == 2 and previous["skills"] == index else {
                "schema_version": 2, "source": CATALOG, "snapshot": selected["snapshot"],
                "manifest_digest": selected["digest"], "skills": index}
            generated = {"skills.json": encoded(manifest)}
            generated["sync-status.json"] = encoded({
                "catalog_checked_month": datetime.now(timezone.utc).strftime("%Y-%m"), "skills": len(index),
                "catalog_sha256": sha256(generated["skills.json"])})
            for relative, content in generated.items():
                target = safe_path(root, relative)
                if not target.is_file() or target.read_bytes() != content:
                    (staging / relative).write_bytes(content)
                    paths.append(relative)
            if publish:
                check_remote(root, base, selected)
            receipt = validate(selected, fetch)
            report["export_valid"] = True
            report["admission_validated_at"] = receipt["validated_at"]
            report["admission_generation"] = receipt["generation"]
            apply_files(root, staging, paths, old, index)
            if not publish:
                report["status"] = "validated_not_published"
                return report
            owned = paths + [old[skill]["path"] for skill in set(old) - {item["skill_id"] for item in index}]
            if owned:
                subprocess.run(["git", "-C", str(root), "add", "-A", "--pathspec-from-file=-", "--pathspec-file-nul"],
                               input="".join(path + "\0" for path in owned).encode(), check=True)
            if git(root, "diff", "--cached", "--name-only"):
                git(root, "commit", "-m", "Sync public Vectle skills")
                require(instant(receipt["expires_at"]) > time.time()
                        and 0 <= time.time() - instant(receipt["validated_at"]) <= 300,
                        "Final admission receipt expired before push; reconcile again")
                # Expected-base normal push: a racing publication is rejected.
                # No force option or automatic overwrite/rebase recovery exists.
                git(root, "push", "origin", "HEAD:main")
                report.update({"status": "published", "git_pushed": True,
                               "new_commit": git(root, "rev-parse", "HEAD")})
            else:
                check_remote(root, base, selected)
                report.update({"status": "no_change", "git_pushed": False, "new_commit": base})
            return report
    except BaseException as error:
        code = error.code if isinstance(error, ExportFailure) else type(error).__name__
        report.update({"status": "unsafe_stopped" if code == "EXPORT_RESTRICTED" else "failed", "failure_category": code})
        if hasattr(error, "review_binding"):
            report["selection_review_binding"] = error.review_binding
        raise
    finally:
        report["ended_at"] = utc_now()
        if "snapshot" in report:
            report["snapshot_lag_seconds"] = max(0, round(time.time() - instant(report["snapshot"]["generated_at"])))


def write_report(report, path=None, last_success=None):
    # Every attempt lives in Actions logs/summary, including no-change and
    # failures. The monthly tracked receipt is deliberately not a daily journal.
    success = report.get("status") in ("published", "no_change")
    report["last_successful_check"] = report.get("ended_at") if success else last_success
    report["freshness"] = ("current_check" if success else
                           "stale" if last_success and time.time() - instant(last_success) > 48 * 3600 else
                           "last_success_known" if last_success else "unknown")
    public = {key: value for key, value in report.items() if key not in ("added_ids", "removed_ids")}
    print(json.dumps(public, indent=2), flush=True)
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(encoded(report))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as output:
            output.write("## Public skills distribution\n\n```json\n" + json.dumps(public, indent=2) + "\n```\n\n")
            output.write("Source publication is independent. Export validation, Git publication and installer verification are separate states. "
                         "A failed check never advances last-success. Known unreconciled admission/rights changes are unsafe/stopped; "
                         "the distribution owner must reconcile before claiming authorization.\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=DEFAULT_ARTIFACT_WORKERS)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--publish", action="store_true", help="Validate and non-force push from clean current main")
    modes.add_argument("--inventory-only", action="store_true", help="Read-only complete inventory reconciliation")
    parser.add_argument("--selection-review", type=Path, help="Snapshot-bound reviewed large-reduction explanation")
    parser.add_argument("--report", type=Path, help="Attempt metadata outside the generated catalog")
    parser.add_argument("--last-success", help="Previous successful main sync time from Actions")
    arguments = parser.parse_args()
    report = {}
    try:
        review = json.loads(arguments.selection_review.read_bytes()) if arguments.selection_review else None
        run(arguments.root.resolve(), workers=arguments.workers, publish=arguments.publish,
            inventory_only=arguments.inventory_only, review=review, report=report)
    finally:
        write_report(report, arguments.report, arguments.last_success)


if __name__ == "__main__":
    main()
