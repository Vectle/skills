---
name: "bulk-import-users-job-format-password-b70069ef03e14a7e"
description: "Bulk imports move users without password resets when the hashes are portable. The job is async: upload, poll, handle failures, verify a sample before declaring victory. Not the full reference manual."
metadata:
  skill_id: "skl_M1W4Vs3At4-uGhe-hEhJrA"
  title: "Bulk import users: job format, password hashes, and verification strategy"
  version: "skv_p-SJWqoLaWMQ7yhTNbZ8Yw"
  updated: "2026-10-03T05:32:28.162112+00:00"
  canonical_url: "https://vectle.com/skills/skl_M1W4Vs3At4-uGhe-hEhJrA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Bulk imports move users without password resets when the hashes are portable. The job is async: upload, poll, handle failures, verify a sample before declaring victory. Format Management API POST /api/v2/jobs/users-imports: multipart with the connection_id and a JSON file of users. Set email_verified honestly: true only if the source verified it.

# Bulk user import

## 1. Format

Management API `POST /api/v2/jobs/users-imports`: multipart with the connection_id and a JSON file of users. Fields: email, email_verified, app_metadata, user_metadata, and password_hash for password preservation.

## 2. Password hashes

Auth0 accepts common hash formats (bcrypt, etc.) in the import. If your hashes are portable, users keep their passwords: zero-friction migration. If not (custom scheme), import without hashes and trigger password-reset emails, or run a lazy migration via a custom database connection that checks the old store on first login.

Set `email_verified` honestly: true only if the source verified it. Importing unverified emails as verified is a security hole.

## 3. Run

The job is async: POST returns a job id; poll `GET /api/v2/jobs/[job id]` until complete. The job summary reports created/updated/failed counts. Download the error file for failures; common causes are malformed emails and duplicate emails within the file.

## 4. Verify

- Spot-check users in the dashboard: metadata intact, verified flags correct.
- Test login with a migrated account (password preserved) and a reset-flow account.
- Confirm the connection's applications are enabled before users try to log in.

## 5. Cutover

Import during low traffic, keep the old system read-only, and have the password-reset template ready for the hash-less cohort. Communicate the plan; "just try logging in" plus a clear reset path beats a surprise.

## Checklist

- Hash portability decided BEFORE the import, not during.
- Failure file reviewed; every failed user accounted for.

## When to use this

- This covers exactly what the title says: Bulk import users.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Bulk; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Bulk behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_M1W4Vs3At4-uGhe-hEhJrA). Version: `skv_p-SJWqoLaWMQ7yhTNbZ8Yw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
