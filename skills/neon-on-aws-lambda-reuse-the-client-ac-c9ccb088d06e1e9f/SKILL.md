---
name: "neon-on-aws-lambda-reuse-the-client-ac-c9ccb088d06e1e9f"
description: "AWS Lambda functions hitting Neon's max_connections with too many clients already. Covers creating the Postgres client at module scope, using the pooled connection string, and recovering from dead clients. Not for VPC networking issues or Neon compute sizing."
metadata:
  skill_id: "skl_DQ6FSzWPDu6zAIzH-KlFFg"
  title: "Neon on AWS Lambda: reuse the client across invocations, pool the string"
  version: "skv_tn9h_3tvIMvwjHJqfUgWMg"
  updated: "2026-10-03T04:36:33.719211+00:00"
  canonical_url: "https://vectle.com/skills/skl_DQ6FSzWPDu6zAIzH-KlFFg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Creating a fresh Postgres client on every Lambda invocation multiplies connections by concurrency and eats the whole max_connections budget on a small Neon compute. Declare the client (or pool) at module scope outside the handler so warm invocations reuse it, point it at the pooled connection string (the -pooler hostname), and drop the cached client on connection errors so the next invocation reconnects.

What it looks like:

```text
"too many clients already" exactly when traffic is highest.
```

Steps:

1. Move client creation to module scope, outside the handler, connecting lazily on first use. Success: warm invocations reuse one client.
2. Point it at the pooled connection string, the -pooler hostname, so PgBouncer absorbs per-invocation churn. Success: the connection string in use is the pooled one.
3. On connection errors, drop the cached client so the next invocation reconnects fresh. A dead client must not poison the warm container. Success: a failed connection recovers on the next invoke without a deploy.

```js
const { Client } = require('pg');
let client;
async function getClient() {
  if (!client) {
    client = new Client({ connectionString: process.env.DATABASE_URL });
    await client.connect();
  }
  return client;
}
exports.handler = async () => {
  const c = await getClient();
  const { rows } = await c.query('SELECT * FROM users');
  return { statusCode: 200, body: JSON.stringify(rows) };
};
```

When to use: Lambda plus Neon (or any Postgres) showing connection exhaustion under concurrency.

When not to use: VPC networking failures (Lambda needs NAT to reach Neon), or a Neon compute that is simply undersized for the workload.

Compatibility: AWS Lambda (Node pg client shown, same pattern in any runtime), Neon pooled endpoints.

Variants:
- lambda postgres too many clients
- neon max_connections lambda
- reuse postgres client lambda

Root cause: the naive Lambda pattern connects inside the handler on every invocation. With 100 concurrent invocations you hold 100 Postgres connections, and on a small Neon compute that is the whole budget gone, so the function fails exactly when traffic is highest.

Edge cases:
- Checklist: client created once per execution environment, not per invocation. DATABASE_URL is the pooled string. On connection errors, drop the cached client.
- If you use provisioned concurrency or VPC, recheck: each provisioned instance holds its own client, and VPC Lambda needs NAT to reach Neon.

---

Source: [Vectle](https://vectle.com/skills/skl_DQ6FSzWPDu6zAIzH-KlFFg). Version: `skv_tn9h_3tvIMvwjHJqfUgWMg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
