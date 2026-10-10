"""Mirror Vectle's public discovery catalog using only anonymous read endpoints."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ORIGIN = "https://vectle.com"
SITEMAP = ORIGIN + "/sitemap-skills.xml"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
ID = re.compile(r"skl_[A-Za-z0-9_-]{22}\Z")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def current_month():
    return datetime.now(timezone.utc).strftime("%Y-%m")


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("Missing publication timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamp must include timezone")
    return value


def request(url):
    """Bounded, read-only retries; never follow a redirect away from Vectle."""
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(NoRedirect)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Vectle-public-skills-mirror/1.0"})
            with opener.open(req, timeout=30) as response:
                body = response.read(8 * 1024 * 1024 + 1)
                if len(body) > 8 * 1024 * 1024:
                    raise ValueError("Response exceeds export size limit")
                return body
        except urllib.error.HTTPError as error:
            if error.code not in (408, 429, 500, 502, 503, 504) or attempt == 4:
                raise
            delay = min(120, max(2 ** attempt, int(error.headers.get("Retry-After", "0"))))
        except (urllib.error.URLError, TimeoutError):
            if attempt == 4:
                raise
            delay = 2 ** attempt
        time.sleep(delay)


def discover(xml):
    if b"<!DOCTYPE" in xml.upper() or b"<!ENTITY" in xml.upper():
        raise ValueError("Unsupported XML declarations")
    root = ET.fromstring(xml)
    if root.tag != NS + "urlset":
        raise ValueError("Expected the complete skills urlset")
    entries = {}
    for child in root:
        loc = child.findtext(NS + "loc", "")
        skill_id = loc.removeprefix(ORIGIN + "/skills/")
        if child.tag != NS + "url" or not ID.fullmatch(skill_id):
            raise ValueError("Unexpected public skill URL")
        if skill_id in entries:
            raise ValueError("Duplicate sitemap skill ID")
        entries[skill_id] = timestamp(child.findtext(NS + "lastmod"))
    if not entries or len(entries) > 49000:
        raise ValueError("Empty or oversized discovery export")
    return entries


def read_skill(skill_id, fetch=request):
    payload = json.loads(fetch(ORIGIN + "/api/v1/skills/" + skill_id))
    data = payload["data"]
    skill, version = data["skill"], data["version"]
    if (payload.get("operation") != "read_skill" or data.get("is_current") is not True
            or skill["skill_id"] != skill_id or version["skill_id"] != skill_id
            or skill["current_version_id"] != version["version_id"]
            or not re.fullmatch(r"skv_[A-Za-z0-9_-]{22}", version["version_id"])):
        raise ValueError("Skill public current-version read did not match")
    for field in ("title", "description", "markdown"):
        if not isinstance(version[field], str) or not version[field].strip():
            raise ValueError("Invalid skill content")
    if not isinstance(version["author"].get("label"), str):
        raise ValueError("Missing public author attribution")
    timestamp(version["created_at"])
    return version


def skill_name(title, skill_id):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:38].rstrip("-") or "skill"
    # Stable ID suffix distinguishes identical titles and case-sensitive source IDs.
    return slug + "-" + hashlib.sha256(skill_id.encode()).hexdigest()[:16]


def render(version, name):
    skill_id = version["skill_id"]
    metadata = {
        "name": name,
        "description": version["description"][:1024],
        "skill_id": skill_id,
        "title": version["title"],
        "version": version["version_id"],
        "updated": version["created_at"],
        "canonical_url": ORIGIN + "/skills/" + skill_id,
        "author": version["author"]["label"],
        "terms": ORIGIN + "/terms",
    }
    # JSON-quoted scalars are YAML-safe, including newlines and hostile metadata.
    header = "\n".join(key + ": " + json.dumps(value, ensure_ascii=True) for key, value in metadata.items())
    attribution = ("\n\n---\n\nSource: [Vectle](" + metadata["canonical_url"]
                   + "). Version: `" + version["version_id"]
                   + "`. Original contributor attribution is preserved in the frontmatter. "
                   "Content remains subject to [Vectle’s terms](https://vectle.com/terms) "
                   "and its contributors’ rights; this mirror does not grant a new content license.\n")
    return "---\n" + header + "\n---\n\n" + version["markdown"] + attribution


def load_index(root):
    path = root / "skills.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text())
    if payload["schema_version"] != 1 or payload["source"] != SITEMAP:
        raise ValueError("Unknown mirror manifest")
    entries = {}
    for item in payload["skills"]:
        skill_id = item["skill_id"]
        if (not ID.fullmatch(skill_id) or skill_id in entries
                or not NAME.fullmatch(item["name"]) or len(item["name"]) > 64
                or item["path"] != "skills/" + skill_id + "/SKILL.md"):
            raise ValueError("Invalid mirror manifest path or name")
        entries[skill_id] = item
    return entries


def sync(root, fetch=request, workers=4):
    entries = discover(fetch(SITEMAP))
    old = load_index(root)
    removed = set(old) - set(entries)
    if old and len(removed) > max(10, len(old) // 10):
        raise ValueError("Discovery lost over 10% of the mirror; inspect the export before pruning")
    changed = [skill_id for skill_id, modified in entries.items()
               if skill_id not in old or old[skill_id]["discovery_updated"] != modified
               or not (root / old[skill_id]["path"]).is_file()
               or hashlib.sha256((root / old[skill_id]["path"]).read_bytes()).hexdigest()
               != old[skill_id]["sha256"]]
    versions = {}
    # No generated files change until EVERY required public read succeeds.
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {pool.submit(read_skill, skill_id, fetch): skill_id for skill_id in changed}
        try:
            for future in as_completed(pending):
                skill_id = pending[future]
                versions[skill_id] = future.result()
                if len(versions) % 100 == 0:
                    print(f"Validated {len(versions)}/{len(changed)} public skill reads", flush=True)
        except Exception:
            for future in pending:
                future.cancel()
            raise
    index, files = [], {}
    for skill_id in sorted(entries):
        if skill_id not in versions:
            index.append(old[skill_id])
            continue
        version = versions[skill_id]
        name = old[skill_id]["name"] if skill_id in old else skill_name(version["title"], skill_id)
        path = "skills/" + skill_id + "/SKILL.md"
        body = render(version, name).encode()
        files[path] = body
        index.append({"skill_id": skill_id, "name": name, "title": version["title"],
                      "description": version["description"][:1024], "url": ORIGIN + "/skills/" + skill_id,
                      "version": version["version_id"], "updated": version["created_at"],
                      "discovery_updated": entries[skill_id], "path": path,
                      "author": version["author"]["label"], "sha256": hashlib.sha256(body).hexdigest()})
    manifest = {"schema_version": 1, "source": SITEMAP, "skills": index}
    files["skills.json"] = (json.dumps(manifest, indent=2, ensure_ascii=True) + "\n").encode()
    # Monthly successful-check receipt keeps GitHub's 60-day inactivity timer alive.
    status = {"catalog_checked_month": current_month(), "skills": len(index),
              "catalog_sha256": hashlib.sha256(files["skills.json"]).hexdigest()}
    files["sync-status.json"] = (json.dumps(status, indent=2) + "\n").encode()
    for path, content in files.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + ".tmp")
        temporary.write_bytes(content)
        temporary.replace(target)
    # Only remove files previously owned by the validated manifest.
    for skill_id in removed:
        target = root / old[skill_id]["path"]
        target.unlink(missing_ok=True)
        if target.parent.is_dir() and not any(target.parent.iterdir()):
            target.parent.rmdir()
    print(f"Catalog: {len(index)} skills; fetched: {len(changed)}; removed from discovery: {len(removed)}", flush=True)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=4)
    arguments = parser.parse_args()
    sync(arguments.root.resolve(), workers=arguments.workers)
