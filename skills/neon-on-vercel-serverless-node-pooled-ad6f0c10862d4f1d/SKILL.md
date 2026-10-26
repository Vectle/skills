---
name: "neon-on-vercel-serverless-node-pooled-ad6f0c10862d4f1d"
description: "Guide Neon on Vercel Serverless (Node): pooled connection string for the app: # Neon on Vercel Serverless (Node): use the pooled string ## The trap Vercel Serverless Functions scale to many concurrent invocations, and each one that opens a direct Postgres connection consumes. Use this when you hit exactly this in Neon on Vercel Serverless (Node). Not for different errors or different tools."
metadata:
  skill_id: "skl_oQd_7neB-X-czy9nMJ3q_w"
  title: "Neon on Vercel Serverless (Node): pooled connection string for the app"
  version: "skv_lhw-4K9P5C2DQzKxkm9XPQ"
  updated: "2026-10-03T06:09:03.134418+00:00"
  canonical_url: "https://vectle.com/skills/skl_oQd_7neB-X-czy9nMJ3q_w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://neon.com/docs/connect/connect-from-any-app\",\"https://neon.com/docs/connect/connection-pooling\"]"
---

TL;DR: # Neon on Vercel Serverless (Node): use the pooled string ## The trap Vercel Serverless Functions scale to many concurrent invocations, and each one that opens a direct Postgres connection consumes one of the compute's `max_connections` slots (104 on a 0.25 CU compute, 419 on 1 CU, with 7 reserved for the Neon superuser).

# Neon on Vercel Serverless (Node): use the pooled string

## The trap
Vercel Serverless Functions scale to many concurrent invocations, and each one that opens a direct Postgres connection consumes one of the compute's `max_connections` slots (104 on a 0.25 CU compute, 419 on 1 CU, with 7 reserved for the Neon superuser). A traffic spike turns into "too many clients already".

## The rule
Neon's Console shows the pooled connection string by default for a reason: it adds `-pooler` to the hostname and routes through PgBouncer, which multiplexes thousands of client connections onto a small pool of real Postgres connections (up to 10,000 concurrent clients).

1. In the Neon Console, open Connect to your branch and copy the pooled connection string (hostname contains `-pooler`).
2. Set it as `DATABASE_URL` in your Vercel project.
3. Keep the direct (non-pooler) string somewhere separate for migrations and admin work, never for request traffic.

## What breaks on pooled (and how to spot it)
PgBouncer runs in transaction mode, so anything needing a persistent session fails: `SET`/`RESET`, `LISTEN`/`NOTIFY`, `PREPARE`, session advisory locks. If a query works locally on a direct connection and fails on Vercel with odd session errors, check which string you deployed.

## Checklist
- `DATABASE_URL` on Vercel = pooled string (`-pooler` in hostname).
- Direct string reserved for migrations, seeds, and admin.
- If you outgrow even the pooler, that is what read replicas are for, not bigger connection counts in app code.

## When to use
You hit exactly this: Neon on Vercel Serverless (Node): pooled connection string for the app in Neon on Vercel Serverless (Node).

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Neon on Vercel Serverless (Node) (versions mentioned here: 0.25).

---

Source: [Vectle](https://vectle.com/skills/skl_oQd_7neB-X-czy9nMJ3q_w). Version: `skv_lhw-4K9P5C2DQzKxkm9XPQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
