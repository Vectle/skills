---
name: "meltano-with-airflow-fails-sqlite-data-8cc5290944b60628"
description: "Fixes Airflow failing under Meltano 2.0 with 'sqlite database file doesn't exist, do you need to create the database with airflow db init'. Use this when upgrading Meltano 2.0 and Airflow's metadata DB setup breaks. Not for non-Meltano Airflow installs or for database corruption."
metadata:
  skill_id: "skl_169XMri2Fy2UjsM9VXEyGg"
  title: "Meltano with Airflow fails: sqlite database file doesn't exist, do you need to create the database with airflow db init"
  version: "skv_m11vDsByX5BtMSGiGAg4Xg"
  updated: "2026-10-03T04:36:22.641093+00:00"
  canonical_url: "https://vectle.com/skills/skl_169XMri2Fy2UjsM9VXEyGg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_ZAcw0G3p893W-Dk-WeEGiQ\",\"https://github.com/meltano/meltano/issues/6209\"]"
---

TL;DR: if Airflow fails under Meltano 2.0 saying the sqlite database file does not exist and asking about `airflow db init`, your config is still speaking Airflow 1.x. Switch to Airflow 2.3.2, set `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN` (the 2.x name; the old `AIRFLOW__CORE__SQL_ALCHEMY_CONN` is dead), use the `postgresql://` scheme with the l (`postgres://` is no longer accepted), and point at a fresh metadata database. The reporter confirmed this exact combination started cleanly.

```text
sqlite database file doesn't exist, do you need to create the database with airflow db init
```

## Steps

1. Set the Airflow 2.x database variable with the correct scheme:

```sh
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql://[db-host]/[db-name]"
```

   (Fill in your real host, database, and credentials.)
   Expected: the variable uses the 2.x name and the `postgresql://` scheme.

2. Create a fresh metadata database (do not reuse the stale sqlite file).

3. Delete or re-init the stale sqlite metadata file so the new connection is what Airflow actually uses.

4. Start Airflow.

   Expected: it connects to the metadata DB. Success check: the scheduler and webserver come up without the db-init error.

## When to use this

- Meltano 2.0 upgrade, Airflow fails with the missing-sqlite-db error.
- Config still references Airflow 1.x variable names or the `postgres://` scheme.

## When NOT to use this

- Plain Airflow installs without Meltano; the passthrough changes are Meltano-specific.
- The metadata DB is genuinely corrupted; restore it instead.

## Compatibility

- Meltano 2.0 with Airflow 2.3.2 (the confirmed working combination).

## Variant phrasings

- "Meltano Airflow db init sqlite missing"
- "Airflow 2 AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"
- "postgres:// vs postgresql:// Airflow"

## Root cause

Meltano 2.0 changed how Airflow config is passed through, and Airflow 2.x renamed the database env vars, so the old settings silently stopped pointing at a real metadata DB and Airflow fell back to a nonexistent sqlite file.

## Edge cases

- Keeping the stale sqlite file around can make Airflow pick it up again; delete it rather than leaving it.

---

Source: [Vectle](https://vectle.com/skills/skl_169XMri2Fy2UjsM9VXEyGg). Version: `skv_m11vDsByX5BtMSGiGAg4Xg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
