"""Anonymous consumer of the released Vectle distribution representation.

The server owns signatures, selection, names and rendering. The consumer checks
the complete ordered digest locally and presents the original signed claims to
the server for live admission validation. It never invents or decodes tokens.
"""
from datetime import datetime, timezone
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ORIGIN = "https://vectle.com"
CATALOG = ORIGIN + "/exports/skills/v1/catalog"
VALIDATE = ORIGIN + "/exports/skills/v1/validate"
LEGACY_SOURCE = ORIGIN + "/sitemap-skills.xml"
REVISIONS = {"schema_version": 1, "artifact_format_revision": 2,
             "distribution_policy_revision": "public-service-distribution-1",
             "name_map_revision": "908987d1727ea4291c77a097eebae5fee5ada14bc5afcf1e0db40a98bc12981b"}
SNAPSHOT_FIELDS = tuple(REVISIONS) + ("snapshot_id", "generation", "generated_at", "expires_at",
                                    "page_size", "expected_entry_count")
ID = re.compile(r"skl_[A-Za-z0-9_-]{22}\Z")
VERSION = re.compile(r"skv_[A-Za-z0-9_-]{22}\Z")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
HEX = re.compile(r"[0-9a-f]{64}\Z")
TOKEN = re.compile(r"[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\Z")
JSON_LIMIT = 2 * 1024 * 1024
ARTIFACT_LIMIT = 256 * 1024
EMPTY_DIGEST = hashlib.sha256(b"vectle-skill-export-chain-v1").hexdigest()


class ExportFailure(ValueError):
    def __init__(self, code, message=None):
        super().__init__(message or code)
        self.code = code


def require(condition, message):
    if not condition:
        raise ExportFailure("invalid_export", message)


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def advance(before, entry):
    return sha256((before + "\n" + canonical({key: value for key, value in entry.items() if key != "claim"})).encode())


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def decode(body):
    require(len(body) <= JSON_LIMIT, "Oversized JSON response")
    value = json.loads(body, object_pairs_hook=unique_object,
                       parse_constant=lambda _value: require(False, "Nonfinite JSON value"))
    require(isinstance(value, dict), "Expected a JSON object")
    return value


def instant(value):
    require(isinstance(value, str), "Missing timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ExportFailure("invalid_export", "Invalid timestamp") from error
    require(parsed.tzinfo is not None, "Timestamp needs timezone")
    return parsed.timestamp()


def token(value, limit=16384):
    require(isinstance(value, str) and len(value) <= limit and TOKEN.fullmatch(value), "Invalid opaque token")


def integer(value, minimum=0, maximum=None):
    return type(value) is int and value >= minimum and (maximum is None or value <= maximum)


def request(url, body=None, limit=JSON_LIMIT):
    """Five bounded attempts, no redirects, credentials or content mutations.

    The only POST is the public metadata-only admission check. A whole physical
    response, including reading its bytes, shares a 30-second monotonic bound.
    """
    parsed = urllib.parse.urlsplit(url)
    require(parsed.scheme == "https" and parsed.netloc == "vectle.com"
            and parsed.path.startswith("/exports/skills/v1/"), "Unexpected export origin")

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None

    opener = urllib.request.build_opener(NoRedirect)
    data = None if body is None else canonical(body).encode()
    require(data is None or len(data) <= JSON_LIMIT, "Oversized validation request")
    for attempt in range(5):
        started = time.monotonic()
        try:
            headers = {"User-Agent": "Vectle-public-skills-mirror/2.0"}
            if data is not None:
                headers["Content-Type"] = "application/json"
            req = urllib.request.Request(url, data=data, headers=headers)
            with opener.open(req, timeout=30) as response:
                chunks, size = [], 0
                while True:
                    if response.isclosed():
                        break
                    remaining = 30 - (time.monotonic() - started)
                    if remaining <= 0:
                        raise TimeoutError("Export response deadline")
                    # urllib's socket timeout is per read; shrink it to the
                    # remaining aggregate budget so a slow body cannot run on.
                    response.fp.raw._sock.settimeout(remaining)
                    chunk = response.read1(min(65536, limit + 1 - size))
                    if not chunk:
                        break
                    chunks.append(chunk)
                    size += len(chunk)
                    require(size <= limit, "Response exceeds size limit")
                require(time.monotonic() - started <= 30, "Export response deadline")
                return b"".join(chunks)
        except urllib.error.HTTPError as error:
            if error.code not in (408, 429, 500, 502, 503, 504):
                try:
                    code = decode(error.read(JSON_LIMIT + 1))["error"]["code"]
                except (ValueError, KeyError, TypeError):
                    code = "http_" + str(error.code)
                raise ExportFailure(code) from error
            if attempt == 4:
                raise ExportFailure("retry_exhausted") from error
            try:
                retry_after = int(error.headers.get("Retry-After", "0"))
            except ValueError:
                retry_after = 0
            delay = min(120, max(2 ** attempt, retry_after))
        except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
            if attempt == 4:
                raise ExportFailure("retry_exhausted") from error
            delay = min(120, 2 ** attempt)
        time.sleep(delay)


def check_snapshot(page, now):
    require(all(page.get(key) == value for key, value in REVISIONS.items()), "Unsupported export revision")
    require(isinstance(page.get("snapshot_id"), str) and re.fullmatch(r"[A-Za-z0-9_-]{32}", page["snapshot_id"]), "Invalid snapshot identity")
    require(isinstance(page.get("generation"), str) and re.fullmatch(r"[0-9]+", page["generation"]), "Invalid generation")
    generated, expiry = instant(page.get("generated_at")), instant(page.get("expires_at"))
    require(abs(expiry - generated - 21600) < 0.002 and expiry > now, "Expired or invalid snapshot lifetime")
    require(integer(page.get("page_size"), 1, 250) and integer(page.get("expected_entry_count")), "Invalid page/count")
    return {key: page[key] for key in SNAPSHOT_FIELDS}


def check_entry(entry):
    require(isinstance(entry, dict), "Invalid entry")
    required = {"skill_id", "version_id", "installation_name", "title", "description", "attribution", "published_at",
                "version_sequence", "canonical_url", "exact_version_url", "artifact_url", "source_snapshot_digest",
                "public_input_digest", "artifact_sha256", "claim"}
    require(set(entry) == required, "Unknown or incomplete entry fields")
    skill, version, name = entry["skill_id"], entry["version_id"], entry["installation_name"]
    require(isinstance(skill, str) and ID.fullmatch(skill) and isinstance(version, str) and VERSION.fullmatch(version), "Invalid public identity")
    require(isinstance(name, str) and len(name) <= 64 and NAME.fullmatch(name), "Invalid installation name")
    require(all(isinstance(entry[key], str) and entry[key].strip() for key in ("title", "description")), "Missing title/description")
    author = entry["attribution"]
    require(isinstance(author, dict) and set(author) == {"label", "client"}
            and isinstance(author["label"], str) and author["label"].strip()
            and (author["client"] is None or isinstance(author["client"], str)), "Invalid public attribution")
    require(isinstance(entry["version_sequence"], str) and re.fullmatch(r"[0-9]+", entry["version_sequence"]), "Invalid version sequence")
    instant(entry["published_at"])
    require(entry["canonical_url"] == ORIGIN + "/skills/" + skill
            and entry["exact_version_url"] == ORIGIN + "/skills/" + skill + "/versions/" + version
            and entry["artifact_url"] == ORIGIN + "/exports/skills/v1/artifacts/" + skill + "/" + version + "/SKILL.md", "Unexpected citation/artifact URL")
    require(all(isinstance(entry[key], str) and HEX.fullmatch(entry[key]) for key in
                ("source_snapshot_digest", "public_input_digest", "artifact_sha256")), "Invalid digest")
    token(entry["claim"], 32768)


def catalog(fetch=request, now=None):
    now = now or time.time
    for scan in range(3):
        entries, names, cursors, snapshot = [], set(), set(), None
        chain, url = EMPTY_DIGEST, CATALOG + "?limit=250"
        try:
            while True:
                page = decode(fetch(url))
                selected = check_snapshot(page, now())
                require(snapshot is None or selected == snapshot, "Mixed catalog snapshots")
                snapshot = selected
                batch = page.get("entries")
                require(isinstance(batch, list) and len(batch) <= snapshot["page_size"], "Invalid catalog page")
                require(type(page.get("complete")) is bool, "Missing completeness flag")
                for entry in batch:
                    check_entry(entry)
                    require(not entries or entry["skill_id"] > entries[-1]["skill_id"], "Duplicate or unordered skill ID")
                    require(entry["installation_name"] not in names, "Duplicate installation name")
                    names.add(entry["installation_name"])
                    entries.append(entry)
                    chain = advance(chain, entry)
                if len(entries) and len(entries) % 2500 == 0:
                    print(f"Validated catalog metadata: {len(entries)}/{snapshot['expected_entry_count']}", flush=True)
                require(page.get("selected_entry_count") == len(entries)
                        and page.get("manifest_digest") == chain
                        and len(entries) <= snapshot["expected_entry_count"], "Catalog count/digest mismatch")
                if page["complete"]:
                    require(page.get("next_cursor") is None and len(entries) == snapshot["expected_entry_count"], "Incomplete terminal catalog")
                    token(page.get("terminal_certificate"))
                    return {"snapshot": snapshot, "entries": entries, "digest": chain,
                            "terminal_certificate": page["terminal_certificate"], "scans": scan + 1}
                require(batch and page.get("terminal_certificate") is None
                        and len(entries) < snapshot["expected_entry_count"], "Invalid incomplete page")
                cursor = page.get("next_cursor")
                token(cursor)
                require(cursor not in cursors, "Repeated catalog cursor")
                cursors.add(cursor)
                url = CATALOG + "?" + urllib.parse.urlencode({"cursor": cursor})
        except ExportFailure as error:
            if error.code != "EXPORT_SNAPSHOT_CHANGED" or scan == 2:
                raise
            print(f"Catalog generation changed; restarting metadata scan {scan + 2}/3", flush=True)
    raise ExportFailure("scan_exhausted")


def validate(selected, fetch=request, now=None):
    now = now or time.time
    entries = selected["entries"]
    for attempt in range(3):
        cursor, generation, chain, index = None, None, EMPTY_DIGEST, 0
        try:
            while True:
                # Claims vary in size. Stay within both the 250-entry and 2MiB
                # request bounds rather than assuming a fixed byte cost.
                claims = []
                body = {"terminal_certificate": selected["terminal_certificate"], "claims": claims}
                if cursor is not None:
                    body["cursor"] = cursor
                for entry in entries[index:index + 250]:
                    claims.append(entry["claim"])
                    if len(canonical(body).encode()) > JSON_LIMIT:
                        claims.pop()
                        break
                require(claims or index == len(entries), "Validation claim exceeds request limit")
                for entry in entries[index:index + len(claims)]:
                    chain = advance(chain, entry)
                index += len(claims)
                result = decode(fetch(VALIDATE, body=body))
                require(result.get("snapshot_id") == selected["snapshot"]["snapshot_id"], "Foreign validation snapshot")
                current = result.get("generation")
                require(isinstance(current, str) and re.fullmatch(r"[0-9]+", current), "Invalid validation generation")
                require(int(current) >= int(selected["snapshot"]["generation"]), "Obsolete validation generation")
                require(generation is None or generation == current, "Mixed validation generations")
                generation = current
                require(type(result.get("complete")) is bool and result["complete"] == (index == len(entries))
                        and result.get("selected_entry_count") == index and result.get("manifest_digest") == chain,
                        "Validation count/digest mismatch")
                if result["complete"]:
                    require(result.get("next_cursor") is None and chain == selected["digest"], "Invalid final validation")
                    token(result.get("validation_receipt"))
                    started, expiry = instant(result.get("validated_at")), instant(result.get("expires_at"))
                    require(abs(expiry - started - 300) < 0.002 and started <= now() + 5 and expiry > now(), "Expired validation receipt")
                    return result
                require(result.get("validation_receipt") is None and result.get("validated_at") is None
                        and result.get("expires_at") is None, "Premature validation receipt")
                following = result.get("next_cursor")
                token(following)
                require(following != cursor, "Repeated validation cursor")
                cursor = following
        except ExportFailure as error:
            if error.code != "EXPORT_SNAPSHOT_CHANGED" or attempt == 2:
                raise
            print(f"Admission generation changed; restarting validation pass {attempt + 2}/3", flush=True)
    raise ExportFailure("validation_exhausted")


def artifact(entry, certificate, fetch=request):
    url = entry["artifact_url"] + "?" + urllib.parse.urlencode({"claim": entry["claim"], "certificate": certificate})
    body = fetch(url, limit=ARTIFACT_LIMIT)
    require(len(body) <= ARTIFACT_LIMIT and sha256(body) == entry["artifact_sha256"], "Artifact checksum mismatch")
    text = body.decode("utf-8")
    require(text.startswith("---\n") and "\n---\n\n" in text[4:], "Invalid Agent Skills frontmatter")
    header = text[4:].split("\n---\n\n", 1)[0]
    values, metadata, in_metadata = {}, {}, False
    for line in header.splitlines():
        if line == "metadata:":
            require(not in_metadata, "Duplicate metadata")
            in_metadata = True
            continue
        parts = line.split(": ", 1)
        require(len(parts) == 2, "Invalid frontmatter scalar")
        key, value = parts
        target = metadata if in_metadata else values
        require((in_metadata and key.startswith("  ")) or (not in_metadata and not key.startswith(" ")), "Invalid frontmatter indentation")
        key = key.strip()
        require(key not in target, "Duplicate frontmatter field")
        target[key] = json.loads(value)
        require(isinstance(target[key], str), "Frontmatter metadata must be strings")
    require(values == {"name": entry["installation_name"], "description": entry["description"][:1024]}, "Artifact name/description mismatch")
    expected = {"skill_id": entry["skill_id"], "title": entry["title"], "version": entry["version_id"],
                "updated": entry["published_at"], "canonical_url": entry["canonical_url"],
                "author": entry["attribution"]["label"], "terms": ORIGIN + "/terms", "artifact_format_revision": "2"}
    require(all(metadata.get(key) == value for key, value in expected.items()), "Artifact provenance mismatch")
    require(json.loads(metadata.get("public_attribution", "null")) == entry["attribution"]
            and isinstance(json.loads(metadata.get("original_notices_and_references", "null")), list), "Missing original public provenance")
    return body
